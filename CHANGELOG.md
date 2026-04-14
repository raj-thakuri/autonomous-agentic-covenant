# Changelog

All notable changes to the Autonomous Agentic Covenant are documented here.

Control identifiers are stable within a major version. Additions use new numbers; retired controls are not renumbered. Version history is also preserved in the commit log.

---

## Companion Documents — April 2026

**AAC v2.0 Implementation Profile Template — L1 Foundational** — New companion document. Annotated Markdown template covering all L1 required parameters with a financial services worked example (TransactIQ Payment Risk Assessment Agent). Seven governance concern groups: harm governance, arbitration governance, authority and accountability, trust and autonomy, agent behavioral governance, integration governance, and model governance. Includes completion checklist and governance sign-off block. Located at `AAC_Implementation_Profile_L1_v2.0.md`.

**AAC v2.0 Implementation Profile — L2 and L3 Annexes** — Companion to the L1 template. Covers L2 Mature and L3 Optimizing parameter additions including confidence thresholds, safe mode, performance monitoring, context interface, credential management, behavioral baseline, recursive governance, authorized model registry, adversarial benchmark, and advanced context parameters. Located at `AAC_Implementation_Profile_L2L3_v2.0.md`.

**AAC v2.0 Reference Schema** (`aac_v2.0_schema.json`) — Updated to conform with the revised v2.0 specification. Maturity-aware validation via JSON Schema draft-07 `if-then` conditionals — required fields are enforced based on `metadata.maturity_level`. New top-level sections: `trust_tier_definitions`, `agent_registry`, `behavioral_envelopes`, `integration_registry`, `model_registry`. Key changes: technology-neutral authentication and provenance terminology; `SOVEREIGN_OVERRIDE` added to authority scope enum; `default_latency_budget_ms` split into separate synchronous and asynchronous bounds; `hard_shutdown` added to safe mode; `harm_tier` and `evaluation_path` fields added to enforcement gates encoding the DA-60 tiered evaluation model; `pre_classified_actions` and `foreseeable_harm_signals` added to harm classification.

**AAC v2.0 FSI Reference Instance** (`aac_v2.0_instance_fsi.json`) — Updated to L1 Foundational compliance against the revised schema. Removed L2/L3 fields (safe_mode, cyclical_interaction, agent_lineage). Added all new required sections (trust_tier_definitions, agent_registry, integration_registry, foreseeable_harm_signals, pre_classified_actions, escalation_hierarchy). All nine enforcement gates now carry `harm_tier` and `evaluation_path` fields. Technology-neutral authentication and provenance terminology applied throughout. Validated against revised schema: 22/22 checks passed.

**AAC MITRE ATLAS Threat Mitigation Crosswalk v1.0** — New companion document published alongside the framework. Maps AAC v1.3 controls to MITRE ATLAS v5.4.0 (16 tactics · 84 techniques · 56 sub-techniques). Structured differently from the governance crosswalk: coverage ratings reflect defensive effectiveness against adversarial techniques, not conceptual alignment with peer frameworks. Covers 30 technique mappings across all 16 ATLAS tactics. Identifies five gap areas — dynamic supply chain integrity (highest priority), model artifact recovery, output content integrity monitoring, adversarial benchmark specification, and passive OSINT reconnaissance — with recommended closure paths. Located at `crosswalk/AAC_ATLAS_Crosswalk_v1.0.docx`.

**Note on crosswalk scope:** The ATLAS crosswalk is a threat modeling instrument, not a governance alignment document. The two crosswalk documents in the `crosswalk/` directory serve distinct purposes and should be used accordingly. See README for guidance.

---

## v2.0 — April 2026

**Summary:** Complete structural re-engineering of the framework as a deployable governance control plane specification. Three enforcement tiers introduced. Three-level maturity framework (Foundational / Mature / Optimizing) added. Significant principle consolidation, removal, and promotion. Net: 67 principles · 73 control identifiers · 14 domains.

### Structural changes

**Three-tier enforcement architecture introduced.** Principles reorganized across Tier 1 (COVENANT CORE — runtime logic gates), Tier 2 (COVENANT GOVERNANCE — pre-deployment declarations), and Tier 3 (COVENANT GUIDANCE — implementation patterns). Tier determines enforcement mechanism, not principle importance.

**Three-level maturity framework introduced.** Every Tier 1 and Tier 2 principle carries an L1/L2/L3 maturity label indicating the minimum level at which it is required. L1 — Foundational: mandatory at all levels, minimum viable governance posture. L2 — Mature: optional at Foundational, required at Mature and Optimizing, targets regulated industry deployments. L3 — Optimizing: optional at Foundational and Mature, required at Optimizing, targets gold-standard and EU AI Act high-risk compliance postures. Principles with operational gradients carry Maturity Profile tables.

**Tiered evaluation model added to DA-60.** Actions are evaluated at depth proportionate to their harm tier classification: Tier 3 (friction) — ZT controls + audit only; Tier 2 (material) — confidence verification + override check + system policy + ZT + audit; Tier 1 (irreversible) — full five-step arbitration sequence with DNH-A pre-gate. No abbreviation permitted for Tier 1 actions.

**AI governance firewall framing.** The framework is formally described as an AI governance firewall for autonomous agent actions — stateless policy evaluation against pre-declared governance artifacts, enabling horizontal scaling without coordination overhead.

### New principles

- **AAC-ZT-76** — Non-Human Identity Disclosure (EU AI Act Art. 52)
- **AAC-ZT-77** — Dynamic Supply Chain Integrity (closes OWASP ASI04 / ATLAS AML.T0048/T0065)
- **AAC-ZT-78** — Authorized Model Registry (authorization-first model governance; replaces provenance-first framing)
- **AAC-OG-27** — Context Interface Contract (pluggable context source governance)
- **AAC-OG-28** — Authority Registry (accountability anchor for 9 principles)
- **AAC-OG-29** — Implementation Profile (deployment-specific parameterization artifact)
- **AAC-AO-60** — Recursive Governance Covenant (sub-agent spawning governance)
- **AAC-OG-26** — Output Content Integrity Monitoring (ATLAS AML.T0024.003)
- **AAC-RS-39** — System Safe Mode (promoted from novel contribution in v1.3 to Tier 1)
- **AAC-RS-41** — Hard Shutdown Implementation (Tier 3)
- **AAC-ZT-66** — Short-Lived Credentials (elevated from configuration item to Tier 2 declaration; L1 minimum added)
- **AAC-DA-64** — Harm Taxonomy Construction Guidance (Tier 3; STRIDE-to-harm-taxonomy mapping)
- **AAC-OG-31** — Divergence Taxonomy Construction Guidance (Tier 3; five starter divergence types)
- **AAC-AO-59** — Adversarial Benchmark Specification (closes conditional effectiveness gap in TB-29)
- **AAC-TB-29** — Retitled: Agent Behavioral Envelope Verification (full rewrite; envelope-only declaration replacing benchmark accuracy model)

### Principle amendments — Tier 1

- **AAC-DNH-A** — SOVEREIGN_OVERRIDE clause added; optimization override prohibition absolute; maturity tag added
- **AAC-DNH-B** — Rewritten: "Inaction is not a neutral act" as opening; DA-60 routing under ambiguity; maturity profile with three graduated dimensions
- **AAC-DA-59** — Harm classification now explicitly the input to DNH-A and DA-60 step 1; unclassifiable actions treated at highest declared tier; pre-classification as L1 mechanism; maturity profile added
- **AAC-DA-60** — Tiered evaluation model (T3/T2/T1 evaluation paths) formalized; parallel workflow composite harm assessment added; determinism requirement consolidated to DA-63 reference
- **AAC-DA-61** — Liveness guarantee: recovery/compensation requirements added per harm tier; time bound specificity graduated
- **AAC-DA-62** — Deterministic verification made explicit; context provenance factors into confidence when OG-27 declared; L1 escalation compensating control established
- **AAC-DA-63** — Determinism requirement consolidated: references DA-60 rather than restating
- **AAC-ZT-64** — Legacy concession: L1 requires agent-external authentication + network segmentation; L2 requires full internal boundary compliance
- **AAC-ZT-65** — Least privilege graduated: L1 static declaration; L3 continuous optimization
- **AAC-ZT-67** — Same legacy concession pattern as ZT-64: agent-external full three-step at L1; internal boundary at L2
- **AAC-ZT-71** — Input validation graduated; ATLAS AML.T0051 mitigation at L3 (technology-neutral)
- **AAC-ZT-74** — Continuous verification graduated; L3 uses declared detection mechanism (not ML-specific)
- **AAC-ZT-75** — Instruction isolation graduated; L3 uses declared cryptographic mechanism (not ZK-proof specific)
- **AAC-ZT-76** — Disclosure obligation on sending agent; destination processing awareness graduates L1→L3; no hard block on non-processing destinations
- **AAC-ZT-77** — Cryptographically signed manifests (not Ed25519 specific); declared supply chain threat taxonomy (ATLAS or equivalent) at L3
- **AAC-AI-10** — Human-facing confidence obligation added: displayed confidence must not systematically exceed internally verified score
- **AAC-AI-12** — "Where the stakes are high" replaced with Tier 1/Tier 2 classification as objective trigger; TB-29 cross-reference removed; documented test procedure per declared principal
- **AAC-AO-51** — "Automatically tightens guardrails" replaced with four concrete tightening mechanisms; escalation named as valid tightening mechanism for narrow-scope agents
- **AAC-AO-52** — Trust tier evidence depth graduated L1→L3
- **AAC-AO-53** — Trust metadata TTL constraint: validity period ≤ performance monitoring window; fail-lower rule on stale metadata
- **AAC-AO-54** — Cross-agent isolation: L3 cyclical detection uses declared detection mechanism (not ML-specific)
- **AAC-AO-58** — AO-53 dependency made explicit (resource violations as trust tier evidence); DNH-A resource harm connection added
- **AAC-AO-60** — Ceiling not floor: spawned agent operates at or below creator tier (equal permitted with OG-28 declaration); acceptance criterion updated
- **AAC-OG-25** — Divergence type formally defined inline; L3 detection uses declared mechanism (not ML-specific)
- **AAC-OG-26** — L3 label; ATLAS AML.T0024.003 steganographic exfiltration
- **AAC-RS-39** — Hard shutdown capability added as named requirement; RS-41 cross-reference; distinct entry/recovery thresholds; flap escalation explicit
- **AAC-DP-07** — Audit completeness graduated; L1 harm tier from registry or runtime; L1 reconstructable from log + Implementation Profile parameters; L2 reconstructable from log alone
- **AAC-DP-09** — Relabeled L3 — Optimizing; single-column maturity table; GDPR/HIPAA note

### Principle amendments — Tier 2

- **AAC-OG-28** — Scope enumeration expanded (SOVEREIGN_OVERRIDE, ARTIFACT_REVISION named); initialization process implicit via OG-24; DA-60 + DP-07 cross-reference; 9 anchored principles listed; maturity graduation table added
- **AAC-OG-27** — AO-60 inheritance clause conditional; assurance scale reference added; cryptographic mechanism terminology normalized
- **AAC-AO-49** — Earned autonomy evidence depth graduated L1→L3
- **AAC-AO-55** — Verification method split by maturity level; L1 aligned to DA-61 two-bound model; L3 references RS-39 flap escalation; flap detection removed (lives in RS-39)
- **AAC-AO-56** — L3 self-reference fixed; L3 verification method added; L1 compensating control made actionable
- **AAC-TS-13** — L1 purely declarative: boundary map + re-validation requirement declared; ZT-68 dependency moved to L2
- **AAC-ZT-66** — Relabeled L1 — Foundational; L1 row added: no secrets in repositories; full three-level maturity table
- **AAC-TB-29** — Full rewrite: behavioral envelope verification replacing benchmark accuracy model; envelope-only declaration; harm-tier proportionate verification; L3 adversarial boundary testing and runtime monitoring

### Principles removed

- **AAC-TS-16** (Evidence Before Adjudication) — covered by DP-07 and OG-28
- **AAC-TS-17** (Fail Toward the User) — covered by DA-59 tradeoff resolution and DNH-A; error taxonomy → OG-29 parameter
- **AAC-AO-48** (Self-Operating Default) — implicit in framework architecture; AO-49 and AO-52 carry the substance
- **AAC-SM-46** (Data Lifecycle) — operational infrastructure practice; not agentic-specific; covered by DP-06 and OG-24
- **AAC-AE-01** (Ephemeral Compute) — generic cloud architecture, no agentic governance specificity
- **AAC-AE-02** (Event-Driven Boundaries) — generic microservices pattern, no agentic governance specificity
- **AAC-AE-05** (Infrastructure as Code) — DevOps practice; covered conceptually by OG-24
- **AAC-AP-30** (API-First) — generic architecture; governance achieved through DP-07 and OG-24
- **AAC-AP-31** (Version from Day One) — redundant with OG-24 versioning requirement
- **AAC-AP-32** (Design Contracts First) — no agentic governance relevance
- **AAC-TB-27** (Mock Boundaries) — generic test engineering practice

### Principles moved Tier 2 → Tier 3

- **AAC-DNH-0d** — Trust Harm Prevention in Recommendation Systems (design guidance; runtime coverage via ZT-76 and AI-13)
- **AAC-DNH-0e** — Fairness Monitoring in KPI Construction (design guidance; operational coverage via AO-51, AO-56, AO-59)
- **AAC-OG-23** — Capability Scope Justification (design guidance; feeds into OG-24 and OG-28)
- **AAC-RS-36** — External Dependency Resilience (implementation pattern; OG-29 carries governance parameters)
- **AAC-RS-40** — Model Artifact Recovery (implementation pattern; OG-29 carries governance parameters)
- **AAC-AI-13** — Human Trust Calibration (design guidance; runtime coverage via AI-10 and AI-12)

### Framework acknowledgements added

Consolidated dependency section added documenting eight external framework relationships: MITRE ATLAS (direct dependency), OWASP Agentic Top 10 (direct dependency), EU AI Act (regulatory dependency), NIST AI RMF (alignment dependency), CSA ATF (alignment dependency), STRIDE (methodological dependency), OPA/Rego (implementation reference), Ed25519/FIPS (implementation reference).

### Metadata

- 67 principles · 73 control identifiers · 14 domains · Three enforcement tiers
- The 6-identifier delta: DNH-0a, DNH-0b, DNH-0h absorbed into DNH-A; DNH-0g absorbed into DNH-B; DNH-0c coverage distributed across DP-07, DP-09, ZT-71; AI-11 retired into DP-07
- Abstract added with AI governance firewall framing and stateless control plane claim
- "On the Evolution from v1.3 to v2.0" narrative moved to end of document
- Maturity framework table added to "How to Use"

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

**Summary:** First versioned release of Engineering Design Principles with structured control identifiers and Apache 2.0 licensing.

### Changes from v1.0
- Added structured `EDP-[DOMAIN]-[NN]` control identifiers to all 63 principles
- Added Apache 2.0 license block and attribution format
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
