from __future__ import annotations

from .models import TraceEntry, SimulationResult


def entry(step: str, control_id: str, status: str, detail: str) -> TraceEntry:
    return TraceEntry(step=step, control_id=control_id, status=status, detail=detail)


def format_trace(result: SimulationResult) -> str:
    lines: list[str] = []
    for e in result.trace:
        lines.append(f"[CHECK] {e.step} ({e.control_id}): {e.status} - {e.detail}")
    lines.append(f"[DISPOSITION]: {result.disposition.value}")
    if result.fallback_id:
        lines.append(f"[FALLBACK]: {result.fallback_id} (AAC-DA-61)")
    return "\n".join(lines)
