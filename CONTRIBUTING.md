# Contributing to the Autonomous Agentic Covenant

Thank you for your interest in contributing. The AAC is a practitioner-authored framework designed to evolve with the field — contributions from implementers, architects, and security practitioners are welcome.

This document describes a lightweight process that keeps the framework coherent without unnecessary bureaucracy.

---

## Before You Contribute

The AAC is a governance framework, not a software project. A few things that follow from that:

**Control identifiers are stable.** `AAC-ZT-64` will always mean what it means in v1.3. Retired controls are not renumbered. If your change requires renumbering existing controls, it needs to be flagged as a breaking change.

**The framework should stay lean.** The AAC has been deliberately pruned. A new principle needs to earn its place by being non-obvious, non-redundant with existing controls, relevant to autonomous systems specifically, and impactful enough that its violation causes meaningful harm. Generic software engineering advice doesn't belong here — it belongs in an implementation profile.

**External validation helps.** If your proposed addition maps to CSA ATF, OWASP Agentic Top 10, NIST AI RMF, or another recognized framework, say so. It strengthens the case and makes the crosswalk update easier.

---

## Types of Contributions

### Substantive changes — open an Issue first

For anything that changes framework content — new principles, modifications to existing principles, proposed retirements — please open a GitHub Issue before writing prose or submitting a PR.

Your issue doesn't need to be long. A good issue answers:
- What are you proposing?
- What problem does it solve that existing controls don't cover?
- Does it create any redundancy or tension with existing principles?
- Any external framework reference that validates the need?

This gives the community a chance to weigh in before you invest time writing, and gives the author a chance to flag if the gap is already addressed or planned.

A brief discussion period (around a week) before merging gives practitioners who've built on the framework time to surface conflicts.

### Editorial fixes — PR directly

Typos, broken cross-references, stale external links, and formatting issues don't need an issue. Submit a PR with a clear description of what you fixed.

### Implementation profiles and examples — welcome

If you've completed an implementation profile for a specific deployment context (healthcare, financial services, government, etc.) and want to share it as a reference example, open an issue or PR. These go in `profiles/examples/` and are clearly marked as community contributions, not official profiles.

### Tooling — Apache 2.0

If you're contributing code — CI/CD policy gate scripts, schema validators, test harnesses, anything executable — note that code contributions are licensed under Apache 2.0, separate from the CC BY 4.0 framework documents. Please confirm this in your PR.

---

## What Won't Be Accepted

To set expectations clearly:

- Principles that are implementation-specific and better suited to a profile than the core framework
- Principles without a clear agentic governance rationale (if it applies equally to any software system, it doesn't belong here)
- Changes that renumber existing controls without a compelling reason — stability matters
- Additions that duplicate existing controls without meaningfully extending them

None of this is meant to be discouraging. If you're unsure whether something fits, open an issue and ask — that's exactly what issues are for.

---

## Versioning

- **Patch (1.3.x):** Editorial fixes, cross-reference corrections, broken links
- **Minor (1.x):** New principles, principle changes, retirements, crosswalk updates
- **Major (x.0):** Structural changes — domain reorganization, identifier scheme changes, or breaking changes to existing control text

Each release gets a git tag, a GitHub Release with updated artifacts, and a CHANGELOG entry.

---

## Credit

Contributors whose proposals are accepted are credited in the CHANGELOG. Substantial contributions — a new domain, a significant restructuring, a well-researched external validation — will be recognized in the release notes.

---

## Questions

Not sure if your idea fits? Open an issue with the `question` label. No proposal is too early-stage for a conversation.
