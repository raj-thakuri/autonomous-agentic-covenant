from __future__ import annotations

import json

from .models import LintResult, MaturityReport, SimulationResult
from .tracer import format_trace


def format_lint(result: LintResult, *, as_json: bool = False) -> str:
    if as_json:
        return json.dumps(result.model_dump(), indent=2)

    if result.valid:
        return "PASS: schema valid, artifact current"

    lines = [f"FAIL: {len(result.errors)} error(s)"]
    for i, err in enumerate(result.errors, 1):
        lines.append(f"  [{i}] {err}")
    return "\n".join(lines)


def format_profile(report: MaturityReport, *, as_json: bool = False) -> str:
    if as_json:
        return json.dumps(report.model_dump(), indent=2)

    status = "COMPLIANT" if report.compliant else "NON-COMPLIANT"
    lines = [
        f"Maturity Grade: {report.declared_level.value} ({status})",
        "",
        "Populated Controls:",
    ]
    if report.populated_controls:
        for ctrl in report.populated_controls:
            lines.append(f"  [PASS] {ctrl}")
    else:
        lines.append("  (none)")

    lines.append("")
    lines.append("Missing Required:")
    if report.missing_required:
        for ctrl in report.missing_required:
            lines.append(f"  [FAIL] {ctrl}")
    else:
        lines.append("  (none)")

    return "\n".join(lines)


def format_simulation(result: SimulationResult, *, as_json: bool = False) -> str:
    if as_json:
        return json.dumps(result.model_dump(), indent=2)
    return format_trace(result)
