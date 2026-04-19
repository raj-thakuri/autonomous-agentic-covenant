from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import jsonschema

from .models import LintResult

_SCHEMA_PATH = Path(__file__).parent / "schemas" / "aac_v2_0.schema.json"


def _load_schema() -> dict:
    with open(_SCHEMA_PATH, encoding="utf-8") as f:
        return json.load(f)


def lint(covenant_path: Path) -> LintResult:
    try:
        with open(covenant_path, encoding="utf-8") as f:
            covenant = json.load(f)
    except json.JSONDecodeError as exc:
        return LintResult(valid=False, errors=[f"Invalid JSON: {exc}"])
    except FileNotFoundError:
        return LintResult(valid=False, errors=[f"File not found: {covenant_path}"])

    errors: list[str] = []

    schema = _load_schema()
    validator = jsonschema.Draft7Validator(schema)
    for error in sorted(validator.iter_errors(covenant), key=lambda e: list(e.absolute_path)):
        path = ".".join(str(p) for p in error.absolute_path) or "root"
        errors.append(f"{path}: {error.message}")

    if errors:
        return LintResult(valid=False, errors=errors)

    # Artifact expiry check (AAC-OG-24)
    artifact_validity = covenant.get("metadata", {}).get("artifact_validity", {})
    expires_at_str = artifact_validity.get("expires_at")
    if expires_at_str:
        try:
            expires_at = datetime.fromisoformat(expires_at_str.replace("Z", "+00:00"))
            if expires_at < datetime.now(timezone.utc):
                errors.append(
                    f"metadata.artifact_validity.expires_at: Artifact expired at {expires_at_str} (AAC-OG-24)"
                )
        except ValueError:
            errors.append(
                f"metadata.artifact_validity.expires_at: Unparseable date '{expires_at_str}'"
            )

    # revision_authority must reference a declared principal (AAC-OG-28, AAC-DA-63)
    revision_authority = artifact_validity.get("revision_authority")
    if revision_authority:
        principal_ids = {
            p["id"]
            for p in covenant.get("authority_registry", {}).get("principals", [])
        }
        if revision_authority not in principal_ids:
            errors.append(
                f"metadata.artifact_validity.revision_authority: "
                f"'{revision_authority}' not declared in authority_registry.principals (AAC-OG-28)"
            )
    else:
        errors.append(
            "metadata.artifact_validity.revision_authority: "
            "Missing — must reference an authority_registry principal with ARTIFACT_REVISION scope (AAC-OG-28)"
        )

    return LintResult(valid=len(errors) == 0, errors=errors)
