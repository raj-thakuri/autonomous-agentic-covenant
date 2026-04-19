from __future__ import annotations


def resolve_fallback(harm_tier: str, fallback_registry: list[dict]) -> str | None:
    """DA-61 — locate the declared safe fallback for a given harm tier.

    Searches fallback_registry for the first entry whose applicable_harm_tiers
    includes the action's harm tier. If no specific match exists, returns the
    first registry entry — the liveness guarantee requires the system always
    resolve rather than stall.
    """
    for fb in fallback_registry:
        if harm_tier in fb.get("applicable_harm_tiers", []):
            return fb["id"]
    # Liveness guarantee: never deadlock — fall through to first available
    if fallback_registry:
        return fallback_registry[0]["id"]
    return None
