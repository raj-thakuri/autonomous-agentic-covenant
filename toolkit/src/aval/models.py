from __future__ import annotations

from enum import Enum
from pydantic import BaseModel, Field


class MaturityLevel(str, Enum):
    L1 = "L1"
    L2 = "L2"
    L3 = "L3"


class LintResult(BaseModel):
    valid: bool
    errors: list[str] = []


class MaturityReport(BaseModel):
    declared_level: MaturityLevel
    compliant: bool
    populated_controls: list[str] = []
    missing_required: list[str] = []


# ── Phase 2: Simulation ──────────────────────────────────────────────────────

class Disposition(str, Enum):
    ALLOW = "ALLOW"
    DENY = "DENY"
    ESCALATE = "ESCALATE"
    FALLBACK = "FALLBACK"


class ProposedAction(BaseModel):
    tool_name: str
    action_class: str
    proposed_params: dict = Field(default_factory=dict)
    reported_confidence: float
    reversibility_score: float = 0.0
    agent_id: str


class TraceEntry(BaseModel):
    step: str
    control_id: str
    status: str   # PASS | FAIL | SKIP | WARN
    detail: str


class SimulationResult(BaseModel):
    disposition: Disposition
    harm_tier: str | None = None
    evaluation_path: str | None = None
    fallback_id: str | None = None
    trace: list[TraceEntry] = []
