from __future__ import annotations


def verify(reported: float, required: float | None) -> tuple[bool, str]:
    """DA-62 — deterministic confidence threshold check.

    Identical inputs always produce identical outputs (AAC-DA-77 acceptance criterion).
    """
    if required is None:
        return True, "No confidence_min declared for this gate — check skipped"
    if reported >= required:
        return True, f"reported_confidence {reported} >= required {required}"
    return False, f"reported_confidence {reported} < required {required}"
