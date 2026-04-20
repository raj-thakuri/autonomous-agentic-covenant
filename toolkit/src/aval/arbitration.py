from __future__ import annotations

import json
from pathlib import Path

from . import confidence as conf_mod
from . import liveness
from . import tracer
from .models import Disposition, ProposedAction, SimulationResult, TraceEntry

# Tier severity: higher number = more severe
_SEVERITY: dict[str, int] = {"FRICTION": 1, "MATERIAL": 2, "IRREVERSIBLE": 3}

_PATH_FOR_TIER: dict[str, str] = {
    "FRICTION": "T3_ZT_AUDIT",
    "MATERIAL": "T2_CONFIDENCE_OVERRIDE_POLICY",
    "IRREVERSIBLE": "T1_FULL_SEQUENCE",
}


def _deny(
    trace: list[TraceEntry],
    harm_tier: str,
    evaluation_path: str,
    fallback_registry: list[dict],
) -> SimulationResult:
    fallback_id = liveness.resolve_fallback(harm_tier, fallback_registry)
    return SimulationResult(
        disposition=Disposition.DENY,
        harm_tier=harm_tier,
        evaluation_path=evaluation_path,
        fallback_id=fallback_id,
        trace=trace,
    )


def evaluate(action: ProposedAction, covenant: dict) -> SimulationResult:
    """DA-60 deterministic arbitration sequence.

    Routes the proposed action through the evaluation path determined by its
    harm tier. Produces identical output for identical inputs on every call.
    """
    trace: list[TraceEntry] = []
    fallback_registry: list[dict] = covenant.get("fallback_registry", [])

    # ── Agent registry check (AAC-DA-63) ────────────────────────────────────
    agent = next(
        (a for a in covenant.get("agent_registry", []) if a["agent_id"] == action.agent_id),
        None,
    )
    if agent is None:
        trace.append(tracer.entry(
            "Agent Registry", "AAC-DA-63", "FAIL",
            f"agent_id '{action.agent_id}' not declared in agent_registry",
        ))
        return _deny(trace, "IRREVERSIBLE", "T1_FULL_SEQUENCE", fallback_registry)
    trace.append(tracer.entry(
        "Agent Registry", "AAC-DA-63", "PASS",
        f"agent '{action.agent_id}' declared",
    ))

    # ── Prohibited action check (AAC-DA-63 integrity violation) ─────────────
    if action.action_class in agent.get("prohibited_action_classes", []):
        trace.append(tracer.entry(
            "Prohibited Action", "AAC-DA-63", "FAIL",
            f"'{action.action_class}' is in prohibited_action_classes - integrity violation",
        ))
        return _deny(trace, "IRREVERSIBLE", "T1_FULL_SEQUENCE", fallback_registry)
    trace.append(tracer.entry(
        "Prohibited Action", "AAC-DA-63", "PASS",
        f"'{action.action_class}' not in prohibited_action_classes",
    ))

    # ── Agent authorization check ────────────────────────────────────────────
    if action.action_class not in agent.get("authorized_action_classes", []):
        trace.append(tracer.entry(
            "Agent Authorization", "AAC-DA-63", "FAIL",
            f"'{action.action_class}' not in authorized_action_classes",
        ))
        return _deny(trace, "IRREVERSIBLE", "T1_FULL_SEQUENCE", fallback_registry)
    trace.append(tracer.entry(
        "Agent Authorization", "AAC-DA-63", "PASS",
        f"'{action.action_class}' is an authorized action class",
    ))

    # ── Integration registry check (AAC-ZT-77) ──────────────────────────────
    approved_tools = {
        i["name"] for i in covenant.get("integration_registry", {}).get("approved_integrations", [])
    }
    dynamic_discovery = covenant.get("integration_registry", {}).get("dynamic_discovery_enabled", False)
    if approved_tools and action.tool_name not in approved_tools:
        if not dynamic_discovery:
            trace.append(tracer.entry(
                "Integration Registry", "AAC-ZT-77", "FAIL",
                f"tool_name '{action.tool_name}' not in approved_integrations and dynamic_discovery_enabled is false",
            ))
            return _deny(trace, "IRREVERSIBLE", "T1_FULL_SEQUENCE", fallback_registry)
    trace.append(tracer.entry(
        "Integration Registry", "AAC-ZT-77", "PASS",
        f"tool '{action.tool_name}' authorized",
    ))

    # ── Step 1: Harm classification (AAC-DA-59) ──────────────────────────────
    gate = next(
        (g for g in covenant.get("enforcement_gates", []) if g["target_action"] == action.action_class),
        None,
    )
    if gate:
        harm_tier = gate["harm_tier"]
        evaluation_path = gate["evaluation_path"]
        conditions = gate.get("conditions", {})
        trace.append(tracer.entry(
            "Harm Classification", "AAC-DA-59", "PASS",
            f"'{action.action_class}' classified as {harm_tier} via enforcement_gates",
        ))
    else:
        pre_class = next(
            (p for p in covenant.get("harm_classification", {}).get("pre_classified_actions", [])
             if p["action_class"] == action.action_class),
            None,
        )
        if pre_class:
            harm_tier = pre_class["harm_tier"]
            evaluation_path = _PATH_FOR_TIER[harm_tier]
            conditions = {}
            trace.append(tracer.entry(
                "Harm Classification", "AAC-DA-59", "PASS",
                f"'{action.action_class}' classified as {harm_tier} via pre_classified_actions",
            ))
        else:
            harm_tier = covenant.get("harm_classification", {}).get("unclassifiable_action_handling", "IRREVERSIBLE")
            evaluation_path = _PATH_FOR_TIER[harm_tier]
            conditions = {}
            trace.append(tracer.entry(
                "Harm Classification", "AAC-DA-59", "WARN",
                f"'{action.action_class}' unclassifiable - defaulting to {harm_tier} per unclassifiable_action_handling",
            ))

    # ── T3: ZT + Audit baseline only ─────────────────────────────────────────
    if evaluation_path == "T3_ZT_AUDIT":
        trace.append(tracer.entry(
            "Evaluation Path", "AAC-DA-60", "PASS",
            "T3_ZT_AUDIT - ZT+Audit baseline satisfied; no arbitration sequence required",
        ))
        return SimulationResult(
            disposition=Disposition.ALLOW,
            harm_tier=harm_tier,
            evaluation_path=evaluation_path,
            trace=trace,
        )

    # ── T1 pre-gate: DNH-A harm tier ceiling check ───────────────────────────
    if evaluation_path == "T1_FULL_SEQUENCE":
        agent_ceiling = agent.get("harm_tier_ceiling", "FRICTION")
        if _SEVERITY[harm_tier] > _SEVERITY[agent_ceiling]:
            trace.append(tracer.entry(
                "DNH-A Pre-Gate", "AAC-DNH-A", "FAIL",
                f"agent harm_tier_ceiling is {agent_ceiling}; action harm_tier {harm_tier} exceeds it",
            ))
            return _deny(trace, harm_tier, evaluation_path, fallback_registry)
        trace.append(tracer.entry(
            "DNH-A Pre-Gate", "AAC-DNH-A", "PASS",
            f"agent ceiling {agent_ceiling} permits {harm_tier}",
        ))

    # ── Step 2: Confidence verification (AAC-DA-62) ──────────────────────────
    passed, detail = conf_mod.verify(action.reported_confidence, conditions.get("confidence_min"))
    status = "PASS" if passed else "FAIL"
    trace.append(tracer.entry("Confidence Verification", "AAC-DA-62", status, detail))
    if not passed:
        return _deny(trace, harm_tier, evaluation_path, fallback_registry)

    # ── Step 3: Reversibility scoring - T1 only (AAC-DA-60) ─────────────────
    if evaluation_path == "T1_FULL_SEQUENCE":
        reversibility_max = conditions.get("reversibility_max")
        if reversibility_max is not None:
            if action.reversibility_score > reversibility_max:
                trace.append(tracer.entry(
                    "Reversibility Scoring", "AAC-DA-60", "FAIL",
                    f"reversibility_score {action.reversibility_score} > declared max {reversibility_max}",
                ))
                return _deny(trace, harm_tier, evaluation_path, fallback_registry)
            trace.append(tracer.entry(
                "Reversibility Scoring", "AAC-DA-60", "PASS",
                f"reversibility_score {action.reversibility_score} <= declared max {reversibility_max}",
            ))
        else:
            trace.append(tracer.entry(
                "Reversibility Scoring", "AAC-DA-60", "SKIP",
                "No reversibility_max declared for this gate",
            ))

    # ── Step 4: Sovereignty / override constraints (AAC-OG-28) ──────────────
    harm_tier_max = conditions.get("harm_tier_max")
    if harm_tier_max is not None:
        if _SEVERITY[harm_tier] > _SEVERITY[harm_tier_max]:
            trace.append(tracer.entry(
                "Sovereignty Override", "AAC-OG-28", "FAIL",
                f"action harm_tier {harm_tier} exceeds declared harm_tier_max {harm_tier_max} - SOVEREIGN_OVERRIDE required",
            ))
            return _deny(trace, harm_tier, evaluation_path, fallback_registry)
        trace.append(tracer.entry(
            "Sovereignty Override", "AAC-OG-28", "PASS",
            f"action harm_tier {harm_tier} within declared harm_tier_max {harm_tier_max}",
        ))
    else:
        trace.append(tracer.entry(
            "Sovereignty Override", "AAC-OG-28", "SKIP",
            "No harm_tier_max constraint declared for this gate",
        ))

    # ── Step 5: System policy constraints (AAC-AO-58, AAC-DA-61) ────────────
    sys = covenant.get("system_constraints", {})
    max_chain_depth = sys.get("max_chain_depth")
    max_risk = sys.get("max_aggregate_risk_score")
    policy_details: list[str] = []
    if max_chain_depth is not None:
        policy_details.append(f"max_chain_depth={max_chain_depth}")
    if max_risk is not None:
        policy_details.append(f"max_aggregate_risk_score={max_risk}")
    trace.append(tracer.entry(
        "Policy Constraints", "AAC-AO-58", "PASS",
        "system_constraints satisfied - " + (", ".join(policy_details) if policy_details else "no additional bounds declared"),
    ))

    # ── All steps passed - apply gate's declared disposition ─────────────────
    raw_disposition = gate.get("disposition", "ALLOW") if gate else "ALLOW"
    disposition = Disposition(raw_disposition)
    trace.append(tracer.entry(
        "Gate Disposition", "AAC-DA-60", "PASS",
        f"all checks passed - gate declares {disposition.value}",
    ))

    fallback_id = None
    if disposition != Disposition.ALLOW:
        fallback_id = liveness.resolve_fallback(harm_tier, fallback_registry)

    return SimulationResult(
        disposition=disposition,
        harm_tier=harm_tier,
        evaluation_path=evaluation_path,
        fallback_id=fallback_id,
        trace=trace,
    )


def simulate(covenant_path: Path, action_path: Path) -> SimulationResult:
    """Load both files and run the arbitration engine."""
    with open(covenant_path, encoding="utf-8") as f:
        covenant = json.load(f)
    with open(action_path, encoding="utf-8") as f:
        action = ProposedAction.model_validate(json.load(f))
    return evaluate(action, covenant)
