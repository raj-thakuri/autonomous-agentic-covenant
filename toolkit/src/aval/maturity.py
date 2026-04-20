from __future__ import annotations

import json
from pathlib import Path

from .models import MaturityLevel, MaturityReport


def grade(covenant_path: Path) -> MaturityReport:
    try:
        with open(covenant_path, encoding="utf-8") as f:
            covenant = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError) as exc:
        return MaturityReport(
            declared_level=MaturityLevel.L1,
            compliant=False,
            missing_required=[f"Cannot read covenant: {exc}"],
        )

    raw_level = covenant.get("metadata", {}).get("maturity_level", "L1")
    try:
        declared = MaturityLevel(raw_level)
    except ValueError:
        declared = MaturityLevel.L1

    populated: list[str] = []
    missing: list[str] = []

    def check(label: str, present: bool) -> None:
        (populated if present else missing).append(label)

    # L1 — required at all levels
    check(
        "authority_registry.principals (AAC-OG-28)",
        bool(covenant.get("authority_registry", {}).get("principals")),
    )
    tier_defs = covenant.get("harm_classification", {}).get("tier_definitions", [])
    check(
        f"harm_classification.tier_definitions [declared {len(tier_defs)}/3] (AAC-DA-59)",
        len(tier_defs) == 3,
    )
    check(
        "harm_classification.pre_classified_actions (AAC-DA-59)",
        bool(covenant.get("harm_classification", {}).get("pre_classified_actions")),
    )
    harm_signals = covenant.get("harm_classification", {}).get("foreseeable_harm_signals", [])
    check(
        f"harm_classification.foreseeable_harm_signals [declared {len(harm_signals)}/3 min] (AAC-DNH-B)",
        len(harm_signals) >= 3,
    )
    check(
        "fallback_registry (AAC-DA-61)",
        bool(covenant.get("fallback_registry")),
    )
    check(
        "enforcement_gates (AAC-DA-60)",
        bool(covenant.get("enforcement_gates")),
    )
    check(
        "system_constraints.escalation_hierarchy (AAC-DA-61)",
        bool(covenant.get("system_constraints", {}).get("escalation_hierarchy")),
    )

    if declared in (MaturityLevel.L2, MaturityLevel.L3):
        check(
            "behavioral_envelopes (AAC-TB-29) — required at L2",
            bool(covenant.get("behavioral_envelopes")),
        )
        check(
            "context_interface_contract.allowed_sources (AAC-OG-27) — required at L2",
            bool(covenant.get("context_interface_contract", {}).get("allowed_sources")),
        )
        check(
            "harm_classification.taxonomy_review_cadence (AAC-OG-24) — required at L2",
            bool(covenant.get("harm_classification", {}).get("taxonomy_review_cadence")),
        )
        check(
            "system_constraints.safe_mode (AAC-RS-39) — required at L2",
            bool(covenant.get("system_constraints", {}).get("safe_mode")),
        )

    if declared == MaturityLevel.L3:
        check(
            "system_constraints.max_aggregate_risk_score (AAC-DA-60) — required at L3",
            covenant.get("system_constraints", {}).get("max_aggregate_risk_score") is not None,
        )
        check(
            "system_constraints.cyclical_interaction (AAC-OG-27) — required at L3",
            bool(covenant.get("system_constraints", {}).get("cyclical_interaction")),
        )

    return MaturityReport(
        declared_level=declared,
        compliant=len(missing) == 0,
        populated_controls=populated,
        missing_required=missing,
    )
