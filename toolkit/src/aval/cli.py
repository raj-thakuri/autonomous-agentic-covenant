from __future__ import annotations

from pathlib import Path

import typer

from . import arbitration, maturity, validator
from .output import format_lint, format_profile, format_simulation

app = typer.Typer(name="aval", help="AAC Validator & Logic-checker (AAC v2.0)")


@app.command()
def lint(
    path: Path = typer.Argument(..., help="Path to covenant.json"),
    json_output: bool = typer.Option(False, "--json", help="Machine-readable JSON output"),
) -> None:
    """Validate syntax and schema compliance of a covenant.json (AAC-OG-24, AAC-OG-29)."""
    result = validator.lint(path)
    typer.echo(format_lint(result, as_json=json_output))
    raise typer.Exit(0 if result.valid else 1)


@app.command()
def profile(
    path: Path = typer.Argument(..., help="Path to covenant.json"),
    json_output: bool = typer.Option(False, "--json", help="Machine-readable JSON output"),
) -> None:
    """Output a Maturity Grade (L1/L2/L3) based on populated AAC controls."""
    report = maturity.grade(path)
    typer.echo(format_profile(report, as_json=json_output))
    raise typer.Exit(0 if report.compliant else 1)


@app.command()
def simulate(
    covenant: Path = typer.Option(..., "--covenant", help="Path to covenant.json"),
    action: Path = typer.Option(..., "--action", help="Path to proposed_action.json"),
    json_output: bool = typer.Option(False, "--json", help="Machine-readable JSON output"),
) -> None:
    """Run the DA-60 deterministic arbitration sequence for a proposed action (AAC-DA-60)."""
    result = arbitration.simulate(covenant, action)
    typer.echo(format_simulation(result, as_json=json_output))
    raise typer.Exit(0 if result.disposition.value == "ALLOW" else 1)
