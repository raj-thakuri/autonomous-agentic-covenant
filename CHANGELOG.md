# Changelog

All notable changes to the Autonomous Agentic Covenant are documented here.

Control identifiers are stable within a major version. Additions use new numbers; retired controls are not renumbered. Version history is also preserved in the commit log.

---

## Updated License  — April 2026

Updated license to **Apache 2.0** for enterprise/standardization alignment.

---

## Companion Documents — April 2026

**AAC MITRE ATLAS Threat Mitigation Crosswalk v1.0** — New companion document published alongside the framework. Maps AAC v1.3 controls to MITRE ATLAS v5.4.0 (16 tactics · 84 techniques · 56 sub-techniques). Structured differently from the governance crosswalk: coverage ratings reflect defensive effectiveness against adversarial techniques, not conceptual alignment with peer frameworks. Covers 30 technique mappings across all 16 ATLAS tactics. Located at `crosswalk/AAC_ATLAS_Crosswalk_v1.0.docx`.

**Note on crosswalk scope:** The ATLAS crosswalk is a threat modeling instrument, not a governance alignment document. The two crosswalk documents in the `crosswalk/` directory serve distinct purposes and should be used accordingly. See README for guidance.

---

## v1.3 — April 2026

**Summary:** Scope reframed from platform engineering to autonomous and AI-driven systems. DA-60 scoped to high-risk actions to prevent arbitration bottleneck. DNH directives tightened for universal applicability. AI-11 consolidated into DP-07. ZT-75 trimmed to remove overlap with ZT-71.

### Breaking changes
- None. All v1.2 control identifiers remain valid in v1.3.

### Principle changes
- **AAC-DA-60** — Scoped arbitration requirement from "every agent action" to "every high-risk action." This resolves a latency and bottleneck concern where applying the full five-step arbitration sequence to low-stakes operations (reads, recommendations, informational queries) would be prohibitively expensive. High-risk is defined by the deploying system's harm tier classification per AAC-DA-59. Principle title updated accordingly.
- **AAC-ZT-75** — Trimmed to remove the schema validation clause (already owned by AAC-ZT-71) and the stale AAC-ZT-60 cross-reference. The principle now focuses exclusively on instruction/data separation — its unique contribution.
- **AAC-AI-11 (Log Decisions, Not Just Outcomes)** — Retired. Intent fully consolidated into AAC-DP-07, which now explicitly requires decision ownership chain capture. A closing sentence added to DP-07 preserves the conceptual framing: *"An outcome log records what happened; a decision log records why. This principle requires the latter."*
- **AAC-DNH-0** — "platform" replaced with "system" throughout DNH directives for universal applicability.
- **AAC-DNH-0b** — "adequately protect" now anchored to "defined risk tier," giving the adequacy criterion a testable reference point.
- **AAC-DNH-0c** — Simplified to "private information" with illustrative enumeration retained as examples rather than exhaustive definition.
- **AAC-DNH-0d** — "Automated recommendations must reflect genuine conditions" strengthened to "must reflect traceable conditions" — making the audit requirement explicit.
- **AAC-DNH-0g** — "If inference clearly shows" replaced with "If available evidence clearly indicates" — removing ambiguity between model inference, logical inference, and sensor inference.
- **AAC-RS-39** — Added clarifying sentence: *"This is not a failure mode."* Safe Mode is a designed operating posture, not a crash state.
- **AAC-SM-46** — Retention figures (90 days / 1 year / 7 years) prefaced with "Example —" to signal they are illustrative rather than prescriptive.
- **AAC-LL-40** — "transactional platform" updated to "autonomous systems."

### Metadata changes
- Version updated to 1.3 throughout
- Cover count corrected: 69 principles + 9 foundational directives (DNH-0 root counted as a directive)
- Governance statement updated: "platform engineering work" → "autonomous and AI-driven systems"
- How to Use example ID updated: AAC-ZT-53 → AAC-ZT-64
- AAC-TS-13 cross-reference corrected: AAC-ZT-62 → AAC-ZT-64

---

## v1.2 — April 2026

**Summary:** Major restructuring pass. Renamed from Engineering Design Principles. New domains added (DA, expanded AO). Significant pruning and consolidation. OB prefix renamed to OG.

### Renames and restructuring
- **Framework renamed** from *Engineering Design Principles* to *The Autonomous Agentic Covenant (AAC)*
- **Control ID prefix** changed from `EDP-` to `AAC-`
- **OB domain** renamed to Operational Governance; prefix updated from `AAC-OB-` to `AAC-OG-`
- **Domain reorder:** AE · TB · AP · LL moved to follow DNH as an engineering cluster, signalling co-equal status with governance domains
- **GD domain (Growth & Discoverability)** removed — principles assessed as product marketing rather than agentic governance
- **UX domain** removed; UX-17 (trust calibration) absorbed into AI-13; UX-18 (single resolution path) absorbed into AE-06

### New controls
- **AAC-DA-59** — Harm Classification and Tradeoff Resolution (novel contribution)
- **AAC-DA-60** — Deterministic Arbitration Layer
- **AAC-DA-61** — Liveness Guarantee (novel contribution)
- **AAC-DA-62** — Confidence Enforcement at Arbitration Layer
- **AAC-DA-63** — Centralized Enforcement Boundary (novel contribution)
- **AAC-AO-52** — Agent Trust Tiers Explicit and Enforced
- **AAC-AO-53** — Dynamic Trust Adjustment
- **AAC-AO-54** — Cross-Agent Isolation
- **AAC-AO-55** — Governed Escalation Hierarchy
- **AAC-AO-56** — Governed Feedback and Learning Loop
- **AAC-AO-58** — Resource Constraint and Consumption Governance
- **AAC-OG-25** — Policy Enforcement Integrity (novel contribution)
- **AAC-RS-39** — System Safe Mode (novel contribution)
- **AAC-AI-13** — Human Trust Calibration
- **AAC-TS-13** — Trust Is Bounded by Verified Provenance (split from prior TS-13)
- **AAC-TS-14** — Trust Is Graduated, Not Granted (split from prior TS-13)
- **AAC-AE-06** — Single Resolution Path, Explicit Failure States
- **AAC-DP-09** — Least Disclosure
- **AAC-ZT-75** — Prompt and Instruction Isolation

### Consolidations
- **AAC-AE-01 + AE-04** merged → AE-01 (Ephemeral Compute, Persistent State)
- **AAC-RS-36 + RS-37** merged → RS-36 (External Dependency Resilience)
- **AAC-SM-44 + SM-45** merged → SM-44 (Liminal State Resolution)
- **AAC-ZT-68 + ZT-69** merged → ZT-68 (Authenticated Propagation)

### Retired controls
- AAC-AE-03 (Design for Full Scale) — generic software wisdom, not agentic-specific
- AAC-AE-04 (Stateless Compute) — merged into AE-01
- AAC-AP-33 (Webhook-Ready) — moved to implementation profile
- AAC-LL-39 (Sub-200ms target) — prescriptive metric, moved to implementation profile
- AAC-AI-09 (Automation as Operator) — philosophical framing, not a governable principle
- AAC-TS-15 (Symmetric Accountability) — too platform-specific after agentic reframe
- AAC-AO-50 (Agent Coordination) — covered by AE-02 and AO-48
- AAC-AO-52 original (One Human/Dashboards) — absorbed into AO-51
- AAC-ZT-70 (Row-Level Access) — moved to implementation profile
- AAC-RS-37 (Retry with Backoff) — merged into RS-36

### Metadata
- 69 principles + 9 foundational directives · 11 domains · 78 control identifiers

---

## v1.1 — April 2026

**Summary:** First versioned release of Engineering Design Principles with structured control identifiers and CC BY 4.0 licensing.

### Changes from v1.0
- Added structured `EDP-[DOMAIN]-[NN]` control identifiers to all 63 principles
- Added CC BY 4.0 license block and attribution format
- Added How to Use section with control ID format explanation
- Domain index table added
- Cover page and footer added with version and license information
- 63 principles + 8 foundational directives · 12 domains · 71 control identifiers

---

## v1.0 — March 2026

**Summary:** Initial framework as *Engineering Design Principles — A Universal Framework for Platform Design & Development.*

- 63 principles across 12 domains
- Unnumbered — no stable control identifiers
- No formal license
- Marketplace platform context throughout

---

*The Autonomous Agentic Covenant is a living framework. Proposals for additions, modifications, or retirements are welcome via GitHub Issues. See [CONTRIBUTING.md](governance/CONTRIBUTING.md) for the proposal process.*
