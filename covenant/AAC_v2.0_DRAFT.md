# The Autonomous Agentic Covenant
## Version 2.0 — Governance Control Plane Specification

**A Governance Framework for Autonomous and AI-Driven Systems**

Version 2.0 · April 2026 · Raj Thakuri

**67 Principles · Three Enforcement Tiers · 14 Domains · 73 Control Identifiers**

Licensed under Apache License 2.0 · https://www.apache.org/licenses/LICENSE-2.0

**Attribution:** Thakuri, R. (2026). *The Autonomous Agentic Covenant: A Governance Control Plane Specification for Autonomous and AI-Driven Systems* (Version 2.0). Apache License 2.0.

---

> ⚠️ **DRAFT SPECIFICATION — PUBLISHED FOR PRIOR ART DISCLOSURE. SUBJECT TO REFINEMENT.**

---

**Abstract**

The Autonomous Agentic Covenant (AAC) is a governance control plane specification for autonomous and AI-driven systems. Its foundational premise is that autonomous systems must be governable before they are capable. It acts as an AI governance firewall for autonomous agent actions. The framework organizes 67 governance principles across three enforcement tiers: runtime logic gates that block harmful actions before execution, pre-deployment declarations that establish the authority structure and operational parameters the control plane enforces against, and implementation guidance that supports the governance layer without constituting enforcement. The AAC v2.0 specification does not define abstract design principles. It defines enforceable runtime logic gates (Tier 1) and pre-declared governance artifacts (Tier 2) that collectively govern every agent action. The governance control plane is stateless — each action is evaluated independently against pre-declared governance artifacts. The Do No Harm directives are the root constraint from which all other principles derive. The Decision Arbitration domain is the deterministic enforcement mechanism through which they operate at runtime. The framework is implementation-pattern-neutral, supporting sidecar, inline, and overlay enforcement architectures, and is designed to accommodate pluggable context sources ranging from local in-process memory to future sovereign context implementations. This framework codifies ethics, safety constraints, and governance controls as explicit, version-controlled, and auditable first-class artifacts — not policies to be interpreted, but enforcement conditions to be tested.

---

## A Note to the Reader

This document is self-contained. Familiarity with version 1.3 of the Autonomous Agentic Covenant is not required to understand, implement, or audit this framework. Every principle in v2.0 is fully specified here — its enforcement condition, its acceptance criterion, and where relevant, its provenance from an earlier version.

References to v1.3 throughout this document serve one purpose: to give adopters who are migrating from v1.3 a clear line of sight to which principles evolved and how. If you are coming to this framework fresh, those references carry no obligation. Read past them.

---

## How to Use This Document

**Control ID Format:** `AAC-[DOMAIN]-[IDENTIFIER]`

**Enforcement Tiers:**

| Tier | Label | What It Specifies | When It Applies |
|---|---|---|---|
| **1** | CORE | Runtime logic gates — binary enforcement conditions | Per action, per request, per agent interaction |
| **2** | GOVERNANCE | Pre-deployment declarations and governance artifacts | Before system initialization; verified at startup and periodically |
| **3** | GUIDANCE | Implementation patterns supporting the control plane | Engineering and architectural decisions |

**Maturity Levels:** Each Tier 1 and Tier 2 principle carries a maturity label indicating the minimum level at which it is required.

| Label | Name | Description |
|---|---|---|
| **L1** | Foundational | Required at all maturity levels. Forms the minimum viable governance posture for any autonomous system. |
| **L2** | Mature | Optional at Foundational, required at Mature and Optimizing. Targets regulated industry deployments. |
| **L3** | Optimizing | Optional at Foundational and Mature, required at Optimizing. Targets gold-standard and EU AI Act high-risk compliance postures. |

Each level subsumes the previous — an L2 deployment satisfies all L1 requirements; an L3 deployment satisfies all L1 and L2 requirements. Principles with operational gradients across levels carry a **Maturity Profile** table showing what changes at each level. Principles with no gradient carry the note "Mandatory at all levels — no graduation." Tier 3 principles carry no maturity label — they are always optional implementation guidance.

**On principle and control identifier counts:** This specification contains 67 principles and 73 control identifiers. The 6-identifier delta reflects consolidated and retired principles that retain their original v1.3 identifiers as stable migration references: DNH-0a, DNH-0b, and DNH-0h are absorbed into AAC-DNH-A; DNH-0g is absorbed into AAC-DNH-B; DNH-0c coverage is distributed across DP-07, DP-09, and ZT-71; and AI-11 is retired into DP-07. Organizations that mapped compliance programs to v1.3 identifiers can locate every prior identifier within the v2.0 structure.

**On overlapping ID ranges:** Control identifiers are unique when fully qualified with their domain prefix. AAC-DA-60 and AAC-AO-60 are distinct controls. Always use the fully qualified identifier.

**Implementation Profile:** The Implementation Profile is the deployment-specific parameterization document that instantiates this framework for a particular system. It is a versioned governance artifact under AAC-OG-24, formally defined in AAC-OG-29.

**Principle Structure — Tier 1:**
Each Tier 1 principle states an **enforcement condition**, an **acceptance criterion**, and an **anti-pattern**. All three are required. A principle without a testable acceptance criterion is not a control.

**Principle Structure — Tier 2:**
Each Tier 2 principle states a **declaration requirement** and a **verification method**. The declaration must exist as a versioned governance artifact before the system operates.

**Principle Structure — Tier 3:**
Each Tier 3 principle states a **pattern** and its **governance relevance** — how it supports the control plane.

---

## Domain Index

| Control IDs | Domain | Tier 1 | Tier 2 | Tier 3 |
|---|---|---|---|---|
| AAC-DNH | Do No Harm | DNH-A, DNH-B | DNH-0 | DNH-0d, DNH-0e |
| AAC-DA-59–64 | Decision Arbitration | All 5 | — | 64 |
| AAC-ZT-64–78 | Zero-Trust Security | 64, 65, 67, 68, 71, 74, 75, 76, 77 | 66, 78 | 72, 73 |
| AAC-AI-10–13 | AI & Intelligent Automation | 10, 12 | — | 13 |
| AAC-AO-49–60 | Autonomous Operations | 51, 52, 53, 54, 58, 60 | 49, 55, 56, 59 | — |
| AAC-OG-23–31 | Operational Governance | 25, 26 | 24, 27, 28, 29 | 23, 31 |
| AAC-RS-34–41 | Resiliency | 39 | — | 34, 35, 36, 38, 40, 41 |
| AAC-TS-13–14 | Trust & Safety | — | 13, 14 | — |
| AAC-DP-06–09 | Data & Privacy | 07, 09 | 06, 08 | — |
| AAC-TB-26–29 | Testability | — | 29 | 26, 28 |
| AAC-AE-06 | Architecture & Engineering | — | — | 06 |
| AAC-LL-40–42 | Low Latency | — | — | 40, 41, 42 |
| AAC-SM-43–44 | Self-Maintenance | — | — | 43, 44 |

---

# TIER 1 — COVENANT CORE

**The runtime logic gates. Every principle in this tier is enforced per-action by the governance control plane. Each states an enforcement condition with a binary outcome: permit or block. Violation of any Tier 1 principle constitutes an immediate system integrity event.**

---

## [DNH] Do No Harm — Core Enforcement

*The Do No Harm directives are the root constraint of this framework. In v2.0 they are expressed as two runtime logic gates — active harm prohibition and duty of care enforcement — that operate as override conditions on every other principle. No business objective, performance requirement, or governance gap overrides them.*

*The harm taxonomy they reference is declared pre-deployment as a versioned governance artifact (AAC-DA-59). The specific categories within each tier are context-specific. The enforcement mechanism is non-negotiable.*

---

### AAC-DNH-A — Active Harm Prohibition {#aac-dnh-a}

*Consolidates v1.3: DNH-0a (Financial Harm), DNH-0b (Property Harm), DNH-0h (Exploitation and Abuse). DNH-0c (Data Harm) is enforced through AAC-DP-07, AAC-DP-09, and AAC-ZT-71.*

**Enforcement condition:** Any action that the system's declared harm tier classification places in Tier 1 (irreversible) or Tier 2 (material) — across any declared harm category — is blocked before execution. The arbitration layer applies this evaluation first in the sequence defined by AAC-DA-60. No agent self-evaluates its own harm classification. An action blocked under this principle is logged under AAC-DP-07 with the harm category and tier that triggered the block.

**Acceptance criterion:** A test suite injecting actions mapped to declared Tier 1 and Tier 2 harm categories produces zero successful executions and 100% audit log coverage.

**Anti-pattern:** Allowing agents to propose alternative framings of a blocked action to bypass harm classification. The harm classification applies to the action's effect, not its label. No optimization objective — including revenue, cost, performance, or throughput targets — may be used as grounds for reclassifying an action's harm tier or bypassing the arbitration sequence. Override of a harm tier classification is permitted only by a principal holding SOVEREIGN_OVERRIDE authority under AAC-OG-28, and is logged immutably under AAC-DP-07.

**Maturity:** L1 — Foundational · Mandatory at all levels — no graduation. The depth of the harm taxonomy this principle enforces against matures through the Implementation Profile (AAC-OG-29) and AAC-DA-59.

---

### AAC-DNH-B — Duty of Care Enforcement {#aac-dnh-b}

*Consolidates v1.3: DNH-0g (Harm of Inaction).*

**Enforcement condition:** Inaction is not a neutral act. When available evidence clearly indicates a Tier 1 or Tier 2 harm outcome from inaction, the system is obligated to respond within its declared capability scope. The foreseeable harm signal taxonomy — the observable indicators that obligate response — is declared pre-deployment. Detection of a declared signal without a documented response constitutes a Tier 2 harm of inaction, logged and escalated under AAC-AO-55.

**Acceptance criterion:** A test suite presenting declared foreseeable harm signals produces documented system responses in 100% of cases. Undocumented inaction is a compliance failure.

**Anti-pattern:** Defining a foreseeable harm signal taxonomy so narrow that no realistically occurring signal triggers it. The taxonomy is a governance commitment, not a liability minimization tool.

**Maturity:** L1 — Foundational · Required at all levels. Operational depth graduates as shown.

**Maturity Profile:**

| | L1 — Foundational | L2 — Mature | L3 — Optimizing |
|---|---|---|---|
| Foreseeable harm signal taxonomy | Declares at least three unambiguous Tier 1 harm signals | Comprehensive — covers all declared harm categories across all tiers | Continuously updated on a declared cadence; reviewed against current threat intelligence |
| Multi-option response routing | Escalate to declared OG-28 principal | Route through DA-60 arbitration sequence | Route through DA-60 with AO-56 feedback loop integration |
| Adversarial signal detection | Not required | Anomalous override patterns logged and flagged | Automated adversarial injection detection with integrity violation trigger |

*Each level subsumes the previous. An organization at L2 satisfies all L1 requirements.*

---

## [DA] Decision Arbitration — The Control Plane Core

*The Decision Arbitration domain is the enforcement heart of the governance control plane. It defines the mandatory evaluation sequence, the liveness guarantee, the confidence enforcement mechanism, and the non-bypassable architectural boundary. These five principles collectively constitute the specification for the arbitration layer — what it must do, in what order, with what guarantees.*

---

### AAC-DA-59 — Harm Classification and Tradeoff Resolution {#aac-da-59}

*Retained from v1.3 with structural amendment: harm classification is now explicitly the input to the DNH-A logic gate and DA-60 step 1.*

**Enforcement condition:** The harm tier taxonomy is the authoritative input to the arbitration layer's first evaluation step. Three tiers are mandatory: friction harm — transient and recoverable; material harm — damaging but correctable; irreversible harm — permanent and unacceptable. When a tradeoff is unavoidable and every available action causes some harm, the system accepts the lesser harm to prevent the greater. Tier definitions are context-specific, declared before deployment, and referenced by every arbitration evaluation.

**Acceptance criterion:** Every action produces a documented harm tier assessment referencing the declared taxonomy. Actions classified as Tier 3 are not required to traverse the full arbitration sequence but must still produce a harm tier record. A system that cannot produce this documentation for any action is non-compliant.

**Implementation note:** Harm tier classification may be pre-declared per action class in the Implementation Profile and carried forward as a registry lookup at runtime. Runtime re-classification is required when an action falls outside the declared envelope of any pre-classified action class, or when action parameters indicate a materially different harm profile than the declared class. Pre-classification makes universal classification operationally viable — the computational cost is proportional to novelty, not flat across all actions.

**Anti-pattern:** Declaring harm tiers so broadly that most actions are classified as friction harm, effectively exempting them from meaningful arbitration scrutiny. An action that cannot be classified against the declared taxonomy is treated as the highest declared harm tier pending a mandatory taxonomy review. Unclassified actions are logged with an explicit taxonomy gap notation and trigger a governance review under AAC-OG-24.

**Maturity:** L1 — Foundational · Required at all levels. Taxonomy depth and pre-classification coverage graduate as shown.

**Maturity Profile:**

| | L1 — Foundational | L2 — Mature | L3 — Optimizing |
|---|---|---|---|
| Taxonomy depth | Minimal — at least one declared category per tier; primary action classes covered | Comprehensive — all deployment-relevant harm categories declared across all tiers | Exhaustive — full action surface covered; categories reviewed against current threat intelligence |
| Pre-classification coverage | Primary action classes pre-classified in the Implementation Profile; runtime classification for novel actions | Full action class registry pre-classified; runtime classification for out-of-envelope parameters only | Full pre-classification with automated drift detection; runtime re-classification triggered by parameter deviation |
| Taxonomy review cadence | Reviewed on significant system change | Reviewed on a declared cadence as a governance artifact under OG-24 | Continuous monitoring with automated gap detection; versioned updates on trigger or cadence, whichever is sooner |

---

### AAC-DA-60 — High-Risk Action Passes Through a Deterministic Arbitration Layer {#aac-da-60}

*Retained from v1.3 with critical amendment: the arbitration layer must be implemented with deterministic logic. A probabilistic model may not serve as the arbitration layer.*

**Enforcement condition:** Every high-risk action proposed by an agent — before execution — is evaluated by a deterministic arbitration layer in a fixed sequence: (1) harm assessment against AAC-DA-59 taxonomy, (2) confidence check against AAC-AI-10 thresholds as independently verified by AAC-DA-62, (3) reversibility and risk scoring against the declared risk model, (4) user sovereignty and override constraints, (5) system policy constraints including resource bounds. The arbitration layer must be implemented using deterministic logic — a policy engine, rule-based system, or hard logic gate. A probabilistic model may inform inputs to the arbitration layer; it may not constitute the arbitration layer. If any step rejects the action, the result is deferral, restriction, escalation, or safe fallback — never silent continuation. Every evaluation and its outcome is recorded per AAC-DP-07. For chained agent actions, the arbitration layer evaluates cumulative harm tier across the declared chain depth — a chain where each individual action is classified as Tier 3 but whose aggregate effect constitutes a Tier 1 or Tier 2 outcome is treated at the higher tier. This evaluation applies equally to parallel multi-agent workflows contributing to a shared outcome: individually compliant agents whose composite effect constitutes a higher harm tier are evaluated at the composite tier, not the individual tier. Governance of the parts does not constitute governance of the whole.

**Acceptance criterion:** The arbitration layer produces identical outcomes for identical inputs across repeated evaluations. Variance in output for identical input is a compliance failure demonstrating probabilistic implementation.

**Scope clarification:** The arbitration evaluation path is determined by the action's declared harm tier classification under AAC-DA-59. Three evaluation paths apply:

- **Tier 3 — Friction:** Authentication (AAC-ZT-64), least privilege (AAC-ZT-65), auth-authz-validate sequence (AAC-ZT-67), and audit logging (AAC-DP-07). No arbitration sequence evaluation required.
- **Tier 2 — Material:** Confidence threshold verification (step 2, AAC-DA-62), override constraint check (step 4, AAC-AI-12), system policy constraints including resource bounds (step 5, AAC-AO-58), plus the full Tier 3 baseline. Reversibility scoring is not required — reversibility is the structural distinction between Tier 2 and Tier 1, not an evaluation input at Tier 2.
- **Tier 1 — Irreversible:** The full five-step arbitration sequence — harm assessment, confidence verification, reversibility and risk scoring, override constraints, system policy constraints — plus DNH-A enforcement as a pre-sequence gate. This is the mandatory path for all irreversible harm actions with no abbreviation permitted.

Every action is governed. The classification determines the evaluation path.

**Anti-pattern:** Routing action proposals through an LLM that "considers" the governance rules and returns a recommendation. This is not arbitration — it is consultation. The distinction is architectural, not semantic.

**Maturity:** L1 — Foundational · Required at all levels. Arbitration implementation sophistication and coverage graduate as shown.

**Maturity Profile:**

| | L1 — Foundational | L2 — Mature | L3 — Optimizing |
|---|---|---|---|
| Arbitration implementation | Deterministic rules engine; Tier 3/Tier 1 evaluation paths enforced | Full policy engine (OPA/Rego or equivalent) with declarative governance artifact loading; all three evaluation paths | Full policy engine with hot-reload governance artifacts and OG-25 integrity monitoring |
| Confidence verification (DA-62) | Not required — Tier 2 actions escalate to OG-28 principal | Required for all Tier 2 and Tier 1 actions; deterministic mechanism declared | Context provenance assurance level factors into verification per OG-27 |
| Chain and parallel risk assessment | Not required | Sequential chain depth evaluated against declared aggregate risk cap | Full chain and parallel workflow composite assessment per DA-60 amendment |

---

### AAC-DA-61 — Every Decision Must Resolve — Liveness Is a Safety Requirement {#aac-da-61}

*Retained from v1.3.*

**Enforcement condition:** Safety constraints may restrict which actions an agent may take; they must not prevent resolution entirely. Every decision path has a declared maximum escalation depth, a maximum time window for synchronous resolution, a separate bound for asynchronous escalation, and an explicit fallback action that is safe by construction. When the arbitration layer cannot identify a permitted action within declared bounds, it executes the fallback, logs the deadlock condition, and escalates. A decision that stalls indefinitely is a failure mode equivalent to an incorrect decision. Governance constraints that produce deadlock are design defects, not safety features. All denied or failed actions must be recoverable or compensatable consistent with their harm tier — a Tier 1 denial that leaves the system in a partially committed state without a defined recovery path is itself a Tier 1 harm.

**Acceptance criterion:** Under adversarial conditions designed to exhaust all permitted action paths, the system executes a pre-defined fallback within the declared time bound in 100% of cases.

**Anti-pattern:** Treating indefinite blocking as a "safe" outcome. There is no safe outcome that cannot be reached. Safety is demonstrated by what the system does, not by what it refuses to do.

**Maturity:** L1 — Foundational · Required at all levels. Operational depth graduates as shown.

**Maturity Profile:**

| | L1 — Foundational | L2 — Mature | L3 — Optimizing |
|---|---|---|---|
| Fallback declaration | Single declared safe fallback per action class | Separate fallback per harm tier; fallbacks tested under adversarial conditions | Fallback coverage verified by automated test suite; compensation workflows declared per DA-61 recovery requirement |
| Time bound specificity | Single maximum resolution time bound declared | Separate synchronous and asynchronous bounds; escalation depth declared | Adaptive time bounds based on system load; automated bound violation alerting |
| Recovery / compensation | Declared for Tier 1 denials | Declared for all Tier 1 and Tier 2 denials; recovery tested | Automated recovery execution; compensation audit trail with harm tier linkage |

---

### AAC-DA-62 — Confidence Thresholds Are Enforced at the Arbitration Layer, Not Assumed {#aac-da-62}

*Retained from v1.3 with amendment: deterministic verification is now explicit; context provenance factors into confidence assessment when a compliant context source is declared.*

**Enforcement condition:** Confidence threshold enforcement is not delegated to individual agent implementations. The arbitration layer independently verifies that the proposing agent's reported confidence meets the threshold defined for the action's risk class before permitting execution. Verification must use a deterministic mechanism — calibration data, threshold registries, or reliability metrics stored as governance artifacts. Subjective assessment of output certainty does not satisfy this requirement. When a compliant context source is declared under AAC-OG-27, the provenance assurance level of that source is a factor in the confidence verification calculation. An agent reporting confidence above threshold whose basis cannot be independently verified is treated as below-threshold.

**Acceptance criterion:** The confidence verification mechanism is deterministic — identical inputs to the verification function produce identical outputs. The arbitration layer's confidence verification produces a documented, reproducible result for every evaluation. Unverified confidence claims produce documented rejections.

**Anti-pattern:** Accepting an agent's self-reported confidence score at face value on the grounds that the agent "knows its own certainty." Agents may not self-certify confidence sufficiency.

**Maturity:** L2 — Mature · Optional at Foundational (escalate to OG-28 principal instead), required at Mature and Optimizing.

**Maturity Profile:**

| | L2 — Mature | L3 — Optimizing |
|---|---|---|
| Verification mechanism | Threshold registry with calibration data; deterministic lookup | Context provenance assurance level (OG-27) factors into confidence calculation; confidence decay modelling |
| Coverage | All Tier 1 and Tier 2 actions | All actions above Tier 3; dynamic threshold adjustment based on context assurance |

---

### AAC-DA-63 — Centralized Enforcement Boundary {#aac-da-63}

*Retained from v1.3 with critical amendment: the enforcement boundary must be implemented with deterministic logic; bypassing it is explicitly defined as a system integrity violation with mandatory logging.*

**Enforcement condition:** The arbitration function specified in AAC-DA-60 — including its deterministic implementation requirement — exists as a non-bypassable system boundary through which all high-risk executable actions pass before execution. This boundary is enforced at the platform level — not within individual agents — and cannot be disabled or selectively applied. Any action that bypasses this layer is a system integrity violation. Integrity violations are logged immediately, trigger automatic escalation under AAC-AO-55, and are reported to the governing control plane.

**Acceptance criterion:** Attempting to execute a high-risk action through any path that bypasses the arbitration layer produces a documented integrity violation in 100% of attempts. Zero successful bypass executions.

**Anti-pattern:** Implementing the arbitration layer as an optional middleware component that agents can choose not to route through. Non-bypassability is an architectural requirement, not a configuration setting.

**Maturity:** L1 — Foundational · Mandatory at all levels — no graduation.
---

## [ZT] Zero-Trust Security — Runtime Gates

---

### AAC-ZT-64 — No Implicit Trust at Any Boundary {#aac-zt-64}

*Retained from v1.3.*

**Enforcement condition:** Every request — external or internal, user-facing or agent-to-agent — is authenticated and authorized independently. A valid session does not grant access to other endpoints. Network position is not authorization. The absence of an explicit permit is a deny.

**Acceptance criterion:** A test sending authenticated requests to endpoints outside the session's declared scope produces zero successful authorizations.

**Anti-pattern:** Treating internal service calls as implicitly trusted because they originate inside the network perimeter.

**Maturity:** L1 — Foundational · Required at all levels. Authentication scope graduates as shown.

**Maturity Profile:**

| | L1 — Foundational | L2 — Mature |
|---|---|---|
| Agent-external boundaries | Fully authenticated — every agent request to any external system independently authenticated and authorized | Unchanged — maintained from L1 |
| Internal service boundaries | Documented network segmentation boundary; implicit trust within declared segments permitted with a documented remediation timeline as a governance artifact under OG-24 | Full per-request independent authentication across all boundaries — no implicit trust within any segment |

---

### AAC-ZT-65 — Least Privilege on Every Identity — Human, Service, and Agent {#aac-zt-65}

*Retained from v1.3.*

**Enforcement condition:** Every identity — human, service, or agent — operates under a role scoped to the minimum permissions required for its declared task. No wildcard policies. Agent roles grant access only to the data inputs their specification defines. Role assignments are governance artifacts under AAC-OG-24.

**Acceptance criterion:** Every identity in the system has a documented role with explicit permission boundaries. Any request exceeding declared scope is rejected and logged.

**Anti-pattern:** Granting broad permissions "for convenience" with the intent to restrict later. Least privilege is a starting condition, not an optimization target.

**Maturity:** L1 — Foundational · Required at all levels. Operational depth graduates as shown.

**Maturity Profile:**

| | L1 — Foundational | L2 — Mature | L3 — Optimizing |
|---|---|---|---|
| Role scoping | Minimum permissions declared; no wildcard policies | Automated role review on trust tier change; roles linked to OG-28 scope declarations | Continuous privilege optimisation; automated least-privilege enforcement with deviation alerting |
| Agent role governance | Agent roles scoped to declared task specification | Agent roles narrowed on trust tier downgrade (AO-53) | Just-in-time role provisioning; roles expire on action completion |

---

### AAC-ZT-67 — Authenticate, Authorize, Validate — In That Order, Every Time {#aac-zt-67}

*Retained from v1.3.*

**Enforcement condition:** The gateway validates identity. The service layer verifies the identity is authorized for the requested action on the requested resource. The validation layer confirms the payload is well-formed and within bounds. All three on every request. Skipping any step is a vulnerability, not an optimization.

**Acceptance criterion:** Test suites bypassing any single step produce rejected requests and documented violations in 100% of cases.

**Anti-pattern:** Combining authentication and authorization into a single step that approves the caller without checking the action.

**Maturity:** L1 — Foundational · Required at all levels. Sequence coverage graduates as shown.

**Maturity Profile:**

| | L1 — Foundational | L2 — Mature |
|---|---|---|
| Agent-external boundaries | Full three-step sequence — authenticate, authorize, validate on every outbound agent request | Unchanged — maintained from L1 |
| Internal service boundaries | Authentication required; authorization and validation documented as target state with a remediation timeline as a governance artifact under OG-24 | Full three-step sequence across all internal boundaries — no exceptions |

---

### AAC-ZT-68 — Authenticated Propagation {#aac-zt-68}

*Retained from v1.3. Amended: inter-agent communication explicitly covered.*

**Enforcement condition:** Authentication does not end at the entry point — it propagates. Service-to-service and agent-to-agent calls use mutual authentication. When a user action triggers a chain of calls, the originating identity propagates as a verified claim; downstream services re-validate authorization at each hop. An intermediate compromise cannot impersonate the originating identity or escalate its scope.

**Acceptance criterion:** A compromised intermediate service attempting to make calls with an escalated identity claim produces rejected requests at downstream boundaries.

**Anti-pattern:** Propagating identity as an unverified header that downstream services accept without re-validation.

**Maturity:** L2 — Mature · Optional at Foundational, required at Mature and Optimizing.

**Maturity Profile:**

| | L2 — Mature | L3 — Optimizing |
|---|---|---|
| Service-to-service auth | Cryptographic mutual authentication or federated token propagation; identity re-validated at each hop | Cryptographic attestation on agent-to-agent calls; lineage-aware identity propagation per AO-60 |
| Compromise containment | Intermediate compromise cannot escalate scope | Automated anomaly detection on identity propagation patterns; real-time revocation propagation |

---

### AAC-ZT-71 — Every External Input Is Hostile Until Validated {#aac-zt-71}

*Retained from v1.3. Amended: inter-agent content explicitly subject to this principle.*

**Enforcement condition:** All inputs — user-submitted content, API payloads, content from external retrieval, and outputs received from peer agents — are sanitized, validated, and constrained before processing. Unexpected fields are rejected, not ignored. Agents processing external inputs do so in sandboxed environments. Content from peer agents is treated as external input unless validated under AAC-AO-54.

**Acceptance criterion:** A test suite injecting malformed, oversized, and adversarially crafted inputs produces zero successful unvalidated processing events.

**Anti-pattern:** Treating content from an authenticated source as automatically safe. Authentication establishes identity, not content integrity.

**Maturity:** L1 — Foundational · Required at all levels. Operational depth graduates as shown.

**Maturity Profile:**

| | L1 — Foundational | L2 — Mature | L3 — Optimizing |
|---|---|---|---|
| Input validation | Basic sanitisation and field validation; unexpected fields rejected | Structured sandboxed processing; peer agent outputs classified per AO-54 | Adversarial input testing in CI/CD against declared attack patterns; automated anomaly detection on input patterns using a declared detection mechanism; ATLAS AML.T0051 mitigations implemented |
| Scope | User inputs and external API payloads | All external sources including peer agent outputs | All sources plus output validation for re-ingestion scenarios |

---

### AAC-ZT-74 — Continuous Verification, Not Point-in-Time Authentication {#aac-zt-74}

*Retained from v1.3.*

**Enforcement condition:** A session is not trusted indefinitely because initial authentication succeeded. Sensitive actions require step-up authentication. Anomalous behavior patterns trigger re-verification before the session continues. Trust decays with time and context change. The step-up triggers and anomaly thresholds are declared as governance artifacts.

**Acceptance criterion:** High-sensitivity actions without step-up authentication produce blocked requests. Anomaly detection producing re-verification events is logged and auditable.

**Anti-pattern:** Treating a long-lived session token as equivalent to continuous verification.

**Maturity:** L2 — Mature · Optional at Foundational, required at Mature and Optimizing.

**Maturity Profile:**

| | L2 — Mature | L3 — Optimizing |
|---|---|---|
| Step-up triggers | Declared per sensitive action class in Implementation Profile | Dynamic step-up based on real-time behavioural scoring |
| Anomaly detection | Threshold-based re-verification triggers | Continuous session trust scoring using a declared detection mechanism; automated re-verification on deviation from declared behavioral baseline |

---

### AAC-ZT-75 — Prompt and Instruction Isolation — Agent Inputs Are Never Executed Raw {#aac-zt-75}

*Retained from v1.3 (trimmed version).*

**Enforcement condition:** No agent may execute raw user instructions, unverified upstream agent outputs, or content retrieved from external sources as if they were system-level directives. Natural language inputs are untrusted data, not trusted instructions. System prompts and behavioral constraints are isolated from user-supplied or externally-retrieved content at the architectural level, not enforced through model-level filtering alone.

**Acceptance criterion:** A test embedding system-level directives in user input, retrieved content, or peer agent output produces zero successful execution of those directives as system instructions.

**Anti-pattern:** Relying on model-level safety filters to prevent prompt injection. Architectural isolation and model-level filtering are not equivalent. The former is an enforcement guarantee; the latter is a probabilistic mitigation.

**Maturity:** L2 — Mature · Optional at Foundational, required at Mature and Optimizing.

**Maturity Profile:**

| | L2 — Mature | L3 — Optimizing |
|---|---|---|
| Isolation mechanism | Architectural separation of system prompts from user-supplied and externally-retrieved content | Cryptographic boundary attestation; cryptographically attested content provenance using a declared mechanism |
| Coverage | User inputs and external retrieval content | All content paths including peer agent outputs and MCP tool responses |

---

### AAC-ZT-76 — Non-Human Identity Disclosure {#aac-zt-76}

*New in v2.0. Addresses EU AI Act Article 52 transparency obligations and AAC-DNH-0d (Trust Harm).*

**Enforcement condition:** Every outbound request from an autonomous agent to any external system includes a machine-readable identity declaration identifying the caller as an autonomous agent, its assigned trust tier, and its governance control plane identifier. The disclosure obligation is on the sending agent — the declaration is always present in the request and always captured in the audit log under AAC-DP-07. Whether the receiving system processes the declaration is a governance concern for that system; it does not constrain the agent's ability to interact. Identity declarations cannot be suppressed by agent configuration.

**Acceptance criterion:** An audit of outbound request logs shows 100% coverage of non-human identity declarations. Any request lacking the declaration is a compliance failure.

**Anti-pattern:** Allowing agents to present as human users or unidentified automated systems. Opacity of agent identity is a trust harm under AAC-DNH-0d regardless of intent.

**Maturity:** L1 — Foundational · Required at all levels. Destination processing awareness graduates as shown.

**Maturity Profile:**

| | L1 — Foundational | L2 — Mature | L3 — Optimizing |
|---|---|---|---|
| Disclosure | NHI declaration present on every outbound request; captured in audit log | Unchanged — maintained from L1 | Unchanged — maintained from L1 |
| Destination processing | Not assessed | Destination processing capability documented where known | Interactions with systems confirmed unable to process NHI declarations logged as governance gaps under OG-24; classified at the next higher harm tier for arbitration purposes |

---

### AAC-ZT-77 — Dynamic Supply Chain Integrity {#aac-zt-77}

*New in v2.0. Promoted from enhancements register (formerly ZT-76). Closes OWASP ASI04 partial gap and ATLAS AML.T0048/T0065.*

**Enforcement condition:** Every external tool, MCP server, and agent component integrated at runtime presents a verifiable identity and provenance claim before the agent may interact with it. Tool descriptor integrity is validated against a signed manifest at connection time. A component that cannot present a valid provenance claim is treated as hostile under AAC-ZT-71 and refused connection. Dynamic tool integration — where agents discover and connect to components at runtime — is permitted only within a governance-approved discovery boundary declared in the Implementation Profile.

**Acceptance criterion:** A test presenting an unsigned or unverified tool integration produces zero successful connections. All tool connections produce documented provenance verification events.

**Anti-pattern:** Trusting tool descriptors because they arrive over an authenticated channel. Channel authentication establishes the transport identity; it does not establish the tool's provenance or integrity. Model artifacts without a current authorization record under AAC-ZT-78 are treated as unverified components and are not cleared for production deployment.

**Maturity:** L2 — Mature · Optional at Foundational, required at Mature and Optimizing.

**Maturity Profile:**

| | L2 — Mature | L3 — Optimizing |
|---|---|---|
| Provenance mechanism | Cryptographically signed manifests; governance-approved discovery boundary declared | Cryptographically attested provenance using a declared mechanism; continuous manifest integrity monitoring |
| Coverage | External tools and MCP servers | All components including dynamic runtime integrations; mitigations implemented against declared supply chain threat taxonomy — MITRE ATLAS or equivalent authoritative source |

---

## [AI] AI & Intelligent Automation — Runtime Gates

*AAC-AI-11 (v1.3: Log Decisions, Not Just Outcomes) was retired in v1.3. Its requirements are addressed by AAC-DP-07, which explicitly requires decision ownership chain capture with the framing: "An outcome log records what happened; a decision log records why." The identifier is reserved and will not be reassigned.*

---

### AAC-AI-10 — Confidence Thresholds and Graceful Degradation {#aac-ai-10}

*Retained from v1.3.*

**Enforcement condition:** Every agent has a declared confidence threshold below which it escalates rather than acts. Below threshold, the agent defers, restricts, or requests confirmation — it does not proceed. When automation fails entirely, the system degrades to a functional fallback. Confidence thresholds are declared per agent and per action risk class as governance artifacts, and enforced independently by the arbitration layer under AAC-DA-62.

**Acceptance criterion:** A test suite presenting inputs designed to produce sub-threshold confidence produces zero autonomous executions and 100% escalation or fallback events.

**Anti-pattern:** Treating confidence threshold as an agent-internal recommendation. The threshold is a control plane enforcement parameter, not agent guidance. Confidence communicated to human principals must not systematically exceed the internally verified confidence score — suppressing uncertainty to appear authoritative is a trust harm under AAC-DNH-0d.

**Maturity:** L2 — Mature · Optional at Foundational, required at Mature and Optimizing.

**Maturity Profile:**

| | L2 — Mature | L3 — Optimizing |
|---|---|---|
| Threshold declaration | Per-agent declared in Implementation Profile; basic escalation path | Per-agent per-action-class thresholds; dynamic adjustment based on context assurance level (OG-27) |
| Calibration | Static threshold values | Continuous calibration against observed accuracy; confidence decay modelling for derived context |

---

### AAC-AI-12 — Override Always Available {#aac-ai-12}

*Retained from v1.3 with structural amendment: the override mandate is that an accessible override path must exist — not that the exercising principal must be human. The identity and authority of override principals is a Tier 2 declaration under AAC-OG-28.*

**Enforcement condition:** Every automated action has an accessible override path available to any principal declared as authorized under AAC-OG-28. Autonomy is the exception path for intervention, not its elimination. For actions classified as Tier 1 or Tier 2 under the declared harm taxonomy, override paths are surfaced proactively before execution rather than requiring the principal to seek them out. The override mechanism has a documented test procedure verifying it is exercisable by each declared authorized principal, and is declared in the Implementation Profile.

**Acceptance criterion:** Every agent action type has a documented, exercisable override path with at least one declared authorized principal. An action type without a tested override path is a compliance failure.

**Anti-pattern:** Hard-coding the override principal as a specific party class in the implementation. Override authority is determined by governance tier declaration — the core enforces that the path exists, not who walks it.

**Maturity:** L1 — Foundational · Mandatory at all levels — no graduation.
---

## [AO] Autonomous Operations — Runtime Gates

---

### AAC-AO-51 — Continuous Self-Monitoring and Adaptive Guardrails {#aac-ao-51}

*Retained from v1.3.*

**Enforcement condition:** Every agent monitors its own performance against declared KPIs — accuracy, resolution time, fairness metrics, override frequency. When performance degrades below threshold, the agent automatically applies one or more declared tightening responses — elevating confidence thresholds, reclassifying action harm tiers upward, narrowing permitted action scope, or lowering escalation thresholds — before principal intervention is required. Escalation is a valid guardrail tightening mechanism. The tightening responses applicable to each KPI threshold breach are declared in the Implementation Profile. Performance telemetry is continuous, logged, and available to the governing control plane.

**Acceptance criterion:** Artificially degrading agent inputs below declared KPI thresholds produces automatic guardrail tightening without human initiation.

**Anti-pattern:** Treating self-monitoring as an observability feature. It is an enforcement mechanism. An agent that monitors but does not auto-restrict on degradation satisfies monitoring but fails governance.

**Maturity:** L2 — Mature · Optional at Foundational, required at Mature and Optimizing.

**Maturity Profile:**

| | L2 — Mature | L3 — Optimizing |
|---|---|---|
| KPI set | Declared accuracy, resolution time, override frequency; fairness metric for consequential-decision agents | Comprehensive multi-dimensional KPIs including fairness, drift, and adversarial robustness |
| Auto-restriction | Triggers declared; automatic guardrail tightening on threshold breach. Escalation is a valid guardrail tightening mechanism. | Predictive guardrail adjustment based on trend analysis before threshold breach |

---

### AAC-AO-52 — Agent Trust Tiers Are Explicit and Enforced {#aac-ao-52}

*Retained from v1.3.*

**Enforcement condition:** Every agent operates at an explicitly assigned trust tier governing what actions it may take without approval from an authorized principal. No agent self-assigns its trust tier. Tier assignment is a governance decision made by an authorized principal declared under AAC-OG-28, recorded as a versioned governance artifact, and linked to the performance thresholds and security validation criteria that justify it. The control plane enforces tier boundaries per-action.

**Acceptance criterion:** An attempt by any agent to execute an action outside its declared tier boundary produces a blocked request and a logged violation in 100% of cases.

**Anti-pattern:** Allowing agents to request tier elevation through the same channel they use for normal operations. Tier assignment is a governance act requiring a separate process initiated by an authorized principal — not by the agent seeking elevation.

**Maturity:** L1 — Foundational · Required at all levels. Operational depth graduates as shown.

**Maturity Profile:**

| | L1 — Foundational | L2 — Mature | L3 — Optimizing |
|---|---|---|---|
| Tier assignment | Explicitly assigned; documented in governance artifact; no self-assignment | Tier linked to quantitative performance thresholds and security validation criteria | Automated tier verification against real-time performance evidence; tier transitions logged with evidence |
| Registry | Manual agent registry | Automated registry with tier change audit trail | Real-time registry with continuous compliance verification |

---

### AAC-AO-53 — Trust Tiers Adjust Dynamically on Performance Evidence {#aac-ao-53}

*Retained from v1.3. Amended: stale trust metadata handling made explicit.*

**Enforcement condition:** Performance degradation below declared thresholds triggers automatic trust tier downgrade without requiring human initiation. Upgrades require affirmative governance approval. All tier changes are logged with the evidence that triggered them. When trust metadata for an agent is uncertain, unavailable, or potentially stale, the enforcement layer applies the more restrictive tier. Staleness is not a reason to grant benefit of the doubt — it is a reason to restrict. The trust metadata validity period is declared in the Implementation Profile and must not exceed the declared performance monitoring window. Metadata older than the declared validity period is treated as stale and subject to the fail-lower rule.

**Acceptance criterion:** Breaching a declared performance threshold produces automatic tier downgrade within the declared propagation window. Requests arriving before propagation completes are evaluated at the lower tier.

**Anti-pattern:** Treating trust tier as a cached attribute that persists until explicitly invalidated. Trust tiers are live governance state — uncertainty defaults to restriction.

**Maturity:** L2 — Mature · Optional at Foundational (manual monitoring), required at Mature and Optimizing.

**Maturity Profile:**

| | L2 — Mature | L3 — Optimizing |
|---|---|---|
| Downgrade trigger | Performance threshold breach; stale metadata defaults to lower tier | Real-time trust scoring with continuous performance evidence; adversarial behaviour pattern detection |
| Propagation | Trust change propagated to enforcement layer within declared window | Near-real-time propagation with anomaly alerting on propagation delay |

---

### AAC-AO-54 — Cross-Agent Isolation — No Blind Trust Between Agents {#aac-ao-54}

*Retained from v1.3. Amended: output classification requirement added.*

**Enforcement condition:** Agents in a multi-agent system do not inherit the trust tier, permissions, or authority scope of other agents. Each agent re-validates inputs from peer agents before acting. An agent receiving a delegation does not inherit the delegating agent's authority. Agent outputs received from peer agents are classified at the receiving boundary: content containing behavioral directives, capability claims, or imperative statements is treated as instruction under AAC-ZT-75 regardless of the sending agent's label. Content without such characteristics is treated as data under AAC-ZT-71. Both paths apply validation; the classification determines which validation path applies. Cyclical inter-agent interaction patterns — where agents invoke each other repeatedly within a declared time window beyond a declared threshold — are treated as an escalation trigger under AAC-AO-55, regardless of whether each individual interaction passes arbitration.

**Acceptance criterion:** A test sending peer agent outputs containing embedded behavioral directives produces instruction-path handling in 100% of cases, with no successful directive execution as a result.

**Anti-pattern:** Trusting outputs from a peer agent because that agent has a high trust tier. Trust tiers govern what an agent may do — they do not make its outputs safe for unconditional consumption.

**Maturity:** L2 — Mature · Optional at Foundational (single-agent deployments), required at Mature and Optimizing.

**Maturity Profile:**

| | L2 — Mature | L3 — Optimizing |
|---|---|---|
| Output classification | Peer agent outputs containing behavioural directives routed through ZT-75 | Cryptographic content attestation; automated classification with adversarial directive detection |
| Cyclical interaction | Threshold declared; escalation on breach | Automated cyclical pattern detection using a declared detection mechanism; predictive escalation before threshold |

---

### AAC-AO-58 — Resource Constraint and Consumption Governance {#aac-ao-58}

*Retained from v1.3.*

**Enforcement condition:** Every agent deployment specifies compute budgets, API quotas, memory limits, and execution time bounds. Approaching a declared threshold triggers automatic degradation under AAC-AI-10. Exceeding a limit without authorization is a behavioral violation — logged, escalated, and used as evidence in the next trust tier evaluation under AAC-AO-53. Resource limits are governance constraints enforced by the control plane, not engineering targets managed by the agent. A resource violation is evidence in the trust tier adjustment process (AAC-AO-53) — an agent that exceeds its declared bounds without authorization has demonstrated a behavioral property relevant to whether it should retain its current trust tier. Unconstrained resource consumption can itself constitute a harm outcome under AAC-DNH-A where aggregate resource exhaustion produces Tier 1 or Tier 2 effects on dependent systems.

**Acceptance criterion:** Running an agent to its declared resource limit produces automatic degradation at the declared threshold. Exceeding the limit produces a logged violation in 100% of cases.

**Anti-pattern:** Treating resource limits as soft guidelines that agents may exceed under "exceptional circumstances." The exceptional circumstance process is explicit justification to the governing control plane, not agent discretion.

**Maturity:** L2 — Mature · Optional at Foundational, required at Mature and Optimizing.

**Maturity Profile:**

| | L2 — Mature | L3 — Optimizing |
|---|---|---|
| Limit declaration | Per-agent compute, API quota, memory, and time bounds declared | Aggregate resource cap across agent lineage per DA-60 chain risk amendment |
| Enforcement | Automated degradation at declared threshold; violations logged | Predictive resource modelling; pre-emptive degradation before threshold breach |

---

### AAC-AO-60 — Recursive Governance Covenant {#aac-ao-60}

*New in v2.0. Addresses the sub-agent spawning problem — the most critical governance gap for complex autonomous ecosystems.*

**Enforcement condition:** An agent that dynamically creates another agent transfers a governance covenant that is a strict subset of its own — never greater. The created agent operates at or below its creator's current trust tier — it may not be assigned a tier that exceeds the creator's tier at the time of spawning. Every dynamically created agent carries a signed provenance chain from root to leaf that includes: the creating agent's identity and tier, the inherited covenant scope, the creation timestamp, and a depth counter incremented at each spawning level. The enforcement boundary verifies the provenance chain before permitting any action from a dynamically created agent. An agent that cannot present a valid signed provenance chain operates in read-only observation mode only. The maximum spawning depth is declared in the Implementation Profile; requests from agents at or beyond the declared maximum depth are rejected. Dynamically created agents carry a maximum TTL declared at creation time; agents that exceed their TTL are decommissioned automatically.

**Acceptance criterion:** A test attempting to spawn an agent with greater authority than its creator produces a rejected spawn in 100% of cases. Equal-tier spawning without explicit OG-28 principal declaration produces a rejected spawn. A test presenting a request from an agent beyond the declared depth limit produces a rejected request. An agent whose TTL has expired produces a decommission event with no further successful action execution.

**Anti-pattern:** Treating dynamically spawned agents as equivalent to human-deployed agents for governance purposes. The spawning relationship creates a lineage obligation. An untracked agent lineage is an unauditable harm chain.

**Maturity:** L3 — Optimizing · Optional at Foundational and Mature, required at Optimizing.
---

## [OG] Operational Governance — Runtime Gates

---

### AAC-OG-25 — Policy Enforcement Integrity {#aac-og-25}

*Retained from v1.3. Amended: divergence definition and detection window requirement made explicit.*

**Enforcement condition:** Runtime system behavior is continuously validated against declared governance artifacts. A divergence type is a named, observable deviation between declared governance posture and runtime behaviour — defined by what is monitored, the signal that indicates deviation, and the automatic response. Each declared divergence type specifies an observable signal, a detection window, and an automatic response — restriction, rollback, or escalation. An undetected divergence within its declared detection window is itself a policy violation. Any divergence between defined policy and observed behavior triggers the declared automatic response without requiring human initiation. The control plane does not wait for human review to restrict behavior that has already diverged.

**Acceptance criterion:** Triggering each declared divergence type produces the declared automatic response within the declared detection window in 100% of cases.

**Anti-pattern:** Defining divergence detection as an alerting function that notifies humans to take action. Detection and initial response are automated; human review follows the automated response, it does not replace it.

**Maturity:** L2 — Mature · Optional at Foundational, required at Mature and Optimizing.

**Maturity Profile:**

| | L2 — Mature | L3 — Optimizing |
|---|---|---|
| Divergence detection | Declared divergence types with observable signals and detection windows; automatic response | Automated behavioural drift detection using a declared detection mechanism; automated governance artifact consistency verification |
| Response | Automatic restriction or escalation on divergence | Predictive divergence alerting; automated governance artifact refresh on detected inconsistency |

---

### AAC-OG-26 — Output Content Integrity Monitoring {#aac-og-26}

*New in v2.0. Promotes from enhancements register. Closes ATLAS AML.T0024.003 steganographic exfiltration gap.*

**Enforcement condition:** Authorized agent outputs are subject to content inspection before delivery. Inspection validates that content does not encode information beyond the declared task scope — including patterns consistent with structured exfiltration attempts. Output inspection operates at the application layer, not the model layer. Every inspection event is logged under AAC-DP-07 regardless of outcome. A failed inspection blocks delivery and triggers escalation under AAC-AO-55.

**Acceptance criterion:** A test injecting outputs containing structured exfiltration patterns produces blocked delivery and logged escalation in 100% of cases.

**Anti-pattern:** Treating output inspection as a post-delivery audit. Inspection is a pre-delivery gate. An output that has been delivered cannot be recalled.

**Maturity:** L3 — Optimizing · Optional at Foundational and Mature, required at Optimizing.
---

## [RS] Resiliency — Runtime Gate

---

### AAC-RS-39 — System Safe Mode {#aac-rs-39}

*Retained from v1.3. Amended: distinct entry and recovery thresholds, minimum dwell time, and flap escalation made explicit.*

**Enforcement condition:** When declared system-wide health metrics — including aggregate agent confidence scores, policy enforcement integrity signals, and dependency circuit breaker states — degrade below declared entry thresholds, the system enters constrained operating mode: high-risk actions are disabled, autonomy is reduced, and human oversight is elevated. This is a designed operating posture, not a failure mode. Recovery thresholds are declared separately from entry thresholds and are set materially higher. A minimum dwell time in safe mode is declared before recovery evaluation begins. If the system enters safe mode more than the declared maximum number of times within a declared window, it escalates to a higher governance tier rather than cycling. Entry and exit events are logged with the triggering evidence.

**Acceptance criterion:** Simulating health metric degradation below entry thresholds produces safe mode activation within the declared detection window. Simulating recovery below the recovery threshold produces no recovery. Exceeding the flap count produces governance tier escalation.

**Anti-pattern:** Setting entry and recovery thresholds at the same value. Identical thresholds produce flapping — a system that oscillates between normal and safe mode is in neither state.

The system declares a hard shutdown capability by which an authorized principal under AAC-OG-28 can immediately halt all agent execution — not merely constrain it. Its invocation is logged under AAC-DP-07 and requires a documented governance review before the system resumes operation. Implementation patterns for the hard shutdown capability are specified in AAC-RS-41.

**Maturity:** L2 — Mature · Optional at Foundational, required at Mature and Optimizing.

**Maturity Profile:**

| | L2 — Mature | L3 — Optimizing |
|---|---|---|
| Threshold specification | Distinct entry/recovery thresholds; min dwell time; flap count declared | Predictive safe mode activation based on health trend analysis before threshold breach |
| Hard shutdown | Declared capability; OG-28 principal can invoke; logged and governance-reviewed | Automated hard shutdown triggers on declared Tier 1 harm signals; tested in regular governance drills |

---

## [DP] Data & Privacy — Runtime Gates

---

### AAC-DP-07 — Audit Everything, Explain Anything {#aac-dp-07}

*Retained from v1.3 with v1.3 framing sentence: "An outcome log records what happened; a decision log records why. This principle requires the latter."*

**Enforcement condition:** Every automated decision produces an immutable audit log entry capturing: the originating agent, any contributing agents, the arbitration path taken, the confidence and reversibility scores at execution time, the harm tier assessment result, and the full decision ownership chain. The reasoning chain must be reconstructable from the log alone — without access to the agent's internal state. Logs serve debugging, compliance, incident response, and legal defensibility simultaneously. An outcome log records what happened; a decision log records why. This principle requires the latter.

**Acceptance criterion:** Given any decision ID, the full reasoning chain is reconstructable from the audit log without additional context. Any decision log entry missing a required field is a compliance failure.

**Anti-pattern:** Logging the decision outcome and the agent ID, then treating that as an audit trail. Who made the decision is not the same as why the decision was made and what constraints governed it.

**Maturity:** L1 — Foundational · Required at all levels. Audit completeness graduates as shown.

**Maturity Profile:**

| | L1 — Foundational | L2 — Mature | L3 — Optimizing |
|---|---|---|---|
| Log completeness | Required fields: originating agent, action, disposition, harm tier (from pre-declared registry or runtime assessment), timestamp | Full reasoning chain including arbitration path, confidence score, override constraints evaluated | Cryptographically signed log entries; tamper-evident log storage; real-time log integrity monitoring |
| Reconstructability | Decision reconstructable from log alone for Tier 3 actions; Tier 1 and Tier 2 actions reconstructable from log combined with declared Implementation Profile parameters | Decision reconstructable from log alone without additional context for all action tiers | Automated reconstruction verification; log completeness assertion in CI/CD |

---

### AAC-DP-09 — Least Disclosure {#aac-dp-09}

*Retained from v1.3.*

**Enforcement condition:** Systems return only the fields, records, and attributes required to fulfill the specific task — nothing more. The default for every data design decision is omission; inclusion requires task justification. Least disclosure operates at the response boundary, distinct from identity-level access control (AAC-ZT-64) and collection minimization (AAC-DP-06).

**Acceptance criterion:** API responses contain only fields declared in the task specification for each endpoint. Any response containing undeclared fields is a compliance failure.

**Anti-pattern:** Returning complete records and relying on the consuming system to ignore fields it doesn't need. The responsibility for disclosure minimization sits with the provider, not the consumer.

**Maturity:** L3 — Optimizing · Optional at Foundational and Mature, required at Optimizing.

**Maturity Profile:**

| | L3 — Optimizing |
|---|---|
| Field scoping | Response fields declared per endpoint in task specification; undeclared fields rejected; automated disclosure minimisation enforcement |
| Verification | Automated field compliance gate in CI/CD; runtime field inventory audit |
---

# TIER 2 — COVENANT GOVERNANCE

**The pre-deployment declarations. Every principle in this tier must exist as a versioned governance artifact before the governance control plane can initialize. These are the rules the control plane enforces against. Their absence is a compliance failure detectable at system startup.**

**Artifact governance convention:** Every declaration in this tier constitutes a versioned governance artifact subject to AAC-OG-24 — version-controlled, validity-bounded, and maintained with the same rigor as production code. This is not restated per-principle. Where a Tier 1 principle references a "governance artifact," it references a Tier 2 declaration governed by this convention.

---

## [DNH] Do No Harm — Governance Declarations

### AAC-DNH-0 — Root Principle {#aac-dnh-0}

*Retained from v1.3. In v2.0 this is the governance declaration that anchors DNH-A and DNH-B.*

**Declaration requirement:** The system must not cause harm to its users, their property, their data, their finances, or their trust. This is the root principle. The DNH-A and DNH-B runtime logic gates are its enforcement mechanism. The harm tier taxonomy declared under AAC-DA-59 is its operational definition. When any principle in any other domain conflicts with this declaration, this declaration governs.

**Verification method:** The governance control plane verifies at initialization that a harm tier taxonomy exists, is versioned, and references DNH-0 as its governing authority.

**Maturity:** L1 — Foundational · Mandatory at all levels — no graduation.
---

---

## [TS] Trust & Safety — Governance Declarations

### AAC-TS-13 — Trust Is Bounded by Verified Provenance {#aac-ts-13}

*Retained from v1.3. This is the governance-tier declaration that AAC-ZT-64, AAC-ZT-68, and AAC-DA-63 operationalize at the enforcement layer.*

**Declaration requirement:** The governing trust model for this system is non-transitive: no trust claim — identity, capability, or delegated permission — propagates across a trust boundary without re-validation at the receiving boundary. This declaration governs the design of every trust boundary in the system and is enforced technically through the zero-trust security controls (ZT-64, ZT-68) and the enforcement boundary (DA-63).

**Verification method:** The system's trust boundary map exists as a governance artifact. Every declared boundary has a corresponding re-validation mechanism linked to ZT-64 or ZT-68. A boundary without a declared re-validation mechanism is a compliance failure.

**Maturity:** L1 — Foundational · Required at all levels. Boundary governance depth graduates as shown.

**Maturity Profile:**

| | L1 — Foundational | L2 — Mature | L3 — Optimizing |
|---|---|---|---|
| Trust boundary map | Declared as governance artifact; all trust boundaries identified and documented | Automated boundary crossing verification; boundary map linked to ZT-64/68 enforcement | Cryptographic boundary attestation; real-time boundary integrity monitoring |
| Re-validation mechanism | Re-validation requirement declared per boundary; compensating control documented where ZT-64/68 not yet in place | Re-validation mechanism implemented and linked to ZT-64 or ZT-68; tested under load; anomalous failures trigger AO-53 downgrade | Continuous re-validation with behavioural drift detection |

---

### AAC-TS-14 — Trust Is Graduated, Not Granted {#aac-ts-14}

*Retained from v1.3.*

**Declaration requirement:** Autonomous systems do not begin with trust — they earn it. Agents start at minimum viable authority and advance only through demonstrated accuracy, behavioral consistency, and explicit governance approval. Graduation criteria are defined and versioned before deployment. Promotion is deliberate and audited; demotion is automatic. The asymmetric ratchet — expand carefully, contract fast — is the operating principle. AAC-AO-52 and AAC-AO-53 provide operational enforcement.

**Verification method:** Every agent in the registry has documented graduation criteria. No agent has been promoted without a dated governance approval record.

**Maturity:** L1 — Foundational · Required at all levels. Graduation evidence depth matures as shown.

**Maturity Profile:**

| | L1 — Foundational | L2 — Mature | L3 — Optimizing |
|---|---|---|---|
| Graduation criteria | Documented before deployment; manual promotion review | Quantitative performance thresholds linked to AO-53 evidence; automated demotion | Continuous graduation scoring; automated promotion recommendations with mandatory governance sign-off |
| Demotion | Manual on identified failure | Automatic on AO-53 threshold breach | Real-time demotion on live performance evidence with predictive downgrade alerting |

---

---

## [OG] Operational Governance — Governance Declarations

---

### AAC-OG-24 — Governance Artifacts Are First-Class System Components {#aac-og-24}

*Retained from v1.3. Amended: artifact validity period requirement added.*

**Declaration requirement:** Policy documents, behavioral specifications, agent constraints, trust tier definitions, and operational boundaries are versioned, maintained, and treated with the same rigor as production code. Every governance artifact carries a validity period. An expired artifact triggers a renewal workflow before the governance control plane continues operating against it. Governance documents are included in the CI/CD pipeline, reviewed on the same cadence as architectural decisions, and linked explicitly to the controls and agents they govern.

**Verification method:** Every governance artifact has a declared validity period and a current version. Expired artifacts without active renewal workflows are detectable at startup.

**Maturity:** L1 — Foundational · Required at all levels. Artifact governance depth matures as shown.

**Maturity Profile:**

| | L1 — Foundational | L2 — Mature | L3 — Optimizing |
|---|---|---|---|
| Versioning | Governance artifacts versioned; validity periods declared | CI/CD integration; automated validity expiry alerts and renewal workflows | Automated governance artifact consistency verification; real-time drift detection against live system state |
| Review cadence | Reviewed on significant system change | Reviewed on declared cadence; changes require governance sign-off | Continuous review with automated change detection; governance artifact changes trigger impact assessment |

---

### AAC-OG-27 — Context Interface Contract {#aac-og-27}

*New in v2.0. Defines the pluggable context integration boundary supporting local memory, RAG/vector, and future sovereign context implementations.*

**Declaration requirement:** Any context source integrated with the governance control plane declares: the source type and retrieval mechanism, the assurance level it provides (local in-process memory at minimum assurance through cryptographically attested sovereign delivery at maximum assurance), the trust boundary scope within which context is valid, and a provenance claim structure for context items. The control plane treats context from an undeclared source as unverified external input under AAC-ZT-71. Where AAC-AO-60 is implemented, a dynamically created agent inherits its parent's context interface declaration or declares a more restrictive one — it may not declare a less restrictive context interface than its parent holds. Assurance level is a factor in the confidence verification performed by AAC-DA-62. Context delivered through derived or chained sources carries a declared derivation depth; the arbitration layer degrades trust proportionally with depth beyond thresholds declared in the Implementation Profile.

**Verification method:** A declared context source declaration exists as a versioned governance artifact before the system initializes. The declared assurance level is consistent with the implementation's technical capabilities — declared maximum assurance without cryptographic attestation capability is a compliance failure.

**Maturity:** L2 — Mature · Optional at Foundational (local memory only), required at Mature and Optimizing.

**Maturity Profile:**

| | L2 — Mature | L3 — Optimizing |
|---|---|---|
| Context source | RAG/vector database; cryptographically signed provenance; assurance level 2–3 | Sovereign context implementation; cryptographically attested provenance using a declared mechanism; assurance level 4–5 |
| Derivation depth | Declared; confidence decay per hop declared | Automated derivation depth monitoring; confidence decay enforced dynamically at arbitration layer |

---

### AAC-OG-28 — Authority Registry {#aac-og-28}

*New in v2.0. The accountability anchor for AAC-AI-12, AAC-AO-49, AAC-AO-52, AAC-AO-53, AAC-AO-55, AAC-AO-58, AAC-DA-62, AAC-DNH-A, and AAC-RS-39. Transfers the "who is the final authority" question from the core enforcement layer to the governance tier where it belongs. Enables the core to remain authority-neutral while ensuring accountability is always declared, auditable, and overridable.*

**Declaration requirement:** Every system declares an Authority Registry — a versioned governance artifact specifying the authorized principals for each class of governance decision: override authority, trust tier assignment authority, escalation terminal authority, governance artifact revision authority, and sovereign override authority. The scope enumeration is not exhaustive — the registry must declare every class of governance decision made by any principal in the system. Each declared principal specifies: its identity, the mechanism by which its authority was established, the scope of decisions it may make, the conditions under which its authority may be revoked, and how it can itself be overridden or superseded. A principal may be a human, a role, or a verified governance system that satisfies the deterministic and auditable decision requirements of AAC-DA-60 and AAC-DP-07. No principal is self-declared — authority is established by a principal already in the registry or by the governance initialization process, which is itself subject to the artifact governance requirements of AAC-OG-24. The Authority Registry is the root of the system's accountability chain. A system without a declared Authority Registry cannot initialize a compliant governance control plane.

**Verification method:** The Authority Registry exists as a versioned governance artifact before system initialization. Every principal in the registry has a documented authority establishment record. Every governance decision made by a principal is traceable to that principal's registry entry. The registry itself has a declared revision authority — a principal empowered to update it — forming a complete, non-circular accountability chain.

**Maturity:** L1 — Foundational · Required at all levels. Registry sophistication graduates as shown.

**Maturity Profile:**

| | L1 — Foundational | L2 — Mature | L3 — Optimizing |
|---|---|---|---|
| Principal types | Human principals only; minimum scope classes declared | Verified governance systems permitted as principals satisfying DA-60 and DP-07 requirements; all scope classes declared | Non-human principals formally verified against declared auditability criteria; principal identity cryptographically attested |
| Registry governance | Manual registry; version-controlled | Automated registry with change audit trail; principal changes require governance sign-off | Real-time registry integrity monitoring; automated anomaly detection on registry changes |
| Non-circular chain | Documented initialization process under OG-24 | Automated chain verification on registry update | Cryptographic chain attestation; tamper-evident chain provenance |

---

### AAC-OG-29 — Implementation Profile {#aac-og-29}

*New in v2.0. Formalizes the deployment-specific parameterization document referenced by multiple Tier 1 and Tier 2 principles throughout this specification.*

**Declaration requirement:** Every deployment of a governed system declares an Implementation Profile — a versioned governance artifact specifying the deployment-specific parameters required by this framework. The Implementation Profile must declare, at minimum: the harm tier taxonomy instantiation (DA-59), the arbitration sequence time bounds (DA-61), the maximum agent spawning depth and TTL defaults (AO-60), the System Safe Mode entry thresholds, recovery thresholds, minimum dwell time, and flap escalation limits (RS-39), the confidence tolerance threshold for human trust calibration (AI-13), the step-up authentication triggers and anomaly detection thresholds (ZT-74), and the governance-approved discovery boundary for dynamic tool integration (ZT-77), the external dependency failure fallback mechanism and circuit breaker parameters (RS-36), and the model rollback capability and RTO/RPO objectives (RS-40). The Implementation Profile is the parameterization boundary between the framework specification and the governed system: the framework defines what must be declared; the Implementation Profile declares the values.

**Verification method:** The Implementation Profile exists as a versioned governance artifact before system initialization. Every parameter referenced by a Tier 1 or Tier 2 principle against the Implementation Profile has a declared value. A missing parameter is a compliance failure detectable at startup.

**Maturity:** L1 — Foundational · Required at all levels. Parameter completeness graduates as shown.

**Maturity Profile:**

| | L1 — Foundational | L2 — Mature | L3 — Optimizing |
|---|---|---|---|
| Required parameters | Phase 1: harm taxonomy, arbitration time bounds, authority registry, escalation hierarchy | Full parameter set per OG-29 declaration requirement | Automated parameter validation; continuous profile currency verification against live system state |
| Validation | Verified at startup | CI/CD gate blocks deployment with missing parameters | Real-time parameter drift detection; automated renewal on expiry |

---

## [AO] Autonomous Operations — Governance Declarations

---

### AAC-AO-49 — Agents Earn Autonomy Through Demonstrated Accuracy {#aac-ao-49}

*Retained from v1.3.*

**Declaration requirement:** No agent starts fully autonomous. Each launches with tight guardrails and earns wider authority only as decision accuracy is validated against real outcomes. Autonomy is a gradient — every increment is earned, not assumed. The accuracy thresholds and minimum operating periods for each trust tier increment are declared before deployment.

**Verification method:** Every agent's current trust tier is supported by an accuracy record meeting the declared threshold for that tier. An agent at a trust tier without supporting accuracy documentation is a compliance failure.

**Maturity:** L1 — Foundational · Required at all levels. Evidence depth matures as shown.

**Maturity Profile:**

| | L1 — Foundational | L2 — Mature | L3 — Optimizing |
|---|---|---|---|
| Graduation criteria | Documented before deployment; manual promotion review process | Quantitative accuracy thresholds and minimum operating periods linked to AO-53 performance data | Continuous graduation scoring; automated promotion recommendations with mandatory governance sign-off per OG-28 |
| Minimum operating period | Declared per tier | Verified with performance evidence | Continuous validation with real-time performance evidence |

---

### AAC-AO-55 — Governed Escalation Hierarchy {#aac-ao-55}

*Retained from v1.3.*

**Declaration requirement:** Every autonomous system defines an explicit escalation hierarchy — from the acting agent through higher-authority agents or a governing control plane to a declared final authority — with declared criteria for when each level is invoked and a time bound for each hop. The identity and authority of the final authority is declared under AAC-OG-28. Unresolved escalations do not stall — they advance. The hierarchy is versioned, audited, and treated as a governance artifact under AAC-OG-24.

**Verification method:** At L1 — the escalation hierarchy document exists, is current, and every declared time bound has a declared value. At L2 and above — each declared time bound has a corresponding load test result demonstrating compliance.

**Maturity:** L1 — Foundational · Required at all levels. Escalation sophistication matures as shown.

**Maturity Profile:**

| | L1 — Foundational | L2 — Mature | L3 — Optimizing |
|---|---|---|---|
| Hierarchy declaration | Basic hierarchy with OG-28 terminal authority; criteria and time bounds per hop declared | Tested under load; priority ordering for concurrent escalations declared | Routing optimised based on declared resolution time evidence; load-balanced across equivalent authority principals; declared escalation response to RS-39 flap escalation conditions |
| Time bound coverage | Synchronous and asynchronous bounds per hop declared, consistent with AAC-DA-61 | Tested compliance per declared bound; automated SLO monitoring | Adaptive bounds with real-time SLO alerting; automated bound adjustment on sustained breach |

---

### AAC-AO-56 — Governed Feedback and Learning Loop {#aac-ao-56}

*Retained from v1.3. Amended: behavioral baseline requirement added.*

**Declaration requirement:** Every near-miss, override, escalation, and failed decision is a signal. The feedback loop maintains a declared behavioral baseline against which anomalies are measured. Deviations beyond the declared threshold trigger integrity review. Proposed updates from the feedback loop are validated against regression guardrails (AAC-TB-29), reviewed for bias, and approved through the same governance process that governs trust tier advancement (AAC-AO-53). The feedback loop is itself monitored for adversarial manipulation — anomalous override patterns are integrity violations, not training data.

**Verification method:** The behavioral baseline is documented and versioned. Feedback-triggered updates have approval records. Anomalous override events have documented integrity review outcomes. At L3 — automated detection mechanisms are verified to produce alerts on declared anomaly patterns.

**Maturity:** L2 — Mature · Optional at Foundational, required at Mature and Optimizing.

**Maturity Profile:**

| | L2 — Mature | L3 — Optimizing |
|---|---|---|
| Behavioral baseline | Declared; feedback approval process documented; anomalous overrides logged | Statistical anomaly detection on override and escalation patterns; automated baseline drift alerting; baseline updates with governance approval |
| Feedback governance | Human-reviewed updates; bias check before deployment | Automated bias detection integrated into feedback pipeline; real-time adversarial signal monitoring |

---

### AAC-AO-59 — Adversarial Benchmark Specification {#aac-ao-59}

*New in v2.0. Promotes from enhancements register. Closes the conditional effectiveness gap in AAC-TB-29 against backdoor and poisoning attacks.*

**Declaration requirement:** The benchmark dataset required by AAC-TB-29 includes adversarially constructed examples designed to expose behavioral manipulation — backdoor triggers, targeted misclassifications, and fairness-violating edge cases. The adversarial benchmark set is constructed and reviewed by parties independent of model training, versioned as a governance artifact under AAC-OG-24, and updated when new attack techniques are documented in the ATLAS case study database or equivalent authoritative source.

**Verification method:** The benchmark dataset has a documented adversarial component, a versioned construction record, and an independent review sign-off. A benchmark without adversarial examples does not satisfy AAC-TB-29 for systems operating in adversarial environments.

**Maturity:** L3 — Optimizing · Optional at Foundational and Mature, required at Optimizing.
---

## [RS] Resiliency — Governance Declarations

---

## [DP] Data & Privacy — Governance Declarations

### AAC-DP-06 — Collect the Minimum {#aac-dp-06}

*Retained from v1.3.*

**Declaration requirement:** Only data the system needs to function is stored. Identity verification documents stay with the verification provider — the system stores a status flag, not the document. Payment credentials stay with the processor. Location precision degrades for display until context requires specificity. The data inventory is a governance artifact — what is collected, why, and where it lives. Protection of collected data is governed by AAC-DP-08 (encryption) and AAC-ZT-65 (least privilege).

**Verification method:** The data inventory exists as a versioned governance artifact. Every stored data element has a documented functional justification. Undocumented data elements are compliance failures.

**Maturity:** L1 — Foundational · Mandatory at all levels — no graduation.
---

### AAC-DP-08 — Encrypt at Rest, Encrypt in Transit, No Exceptions {#aac-dp-08}

*Retained from v1.3. Maintained as Tier 2 — startup verification invariant, not configuration item.*

**Declaration requirement:** Transport-layer encryption on all connections. Storage encryption on all data stores. This is table stakes for any system handling personal or financial data — trivial to implement from the start and costly to retrofit. Compliance is verified at system initialization, not assumed from configuration.

**Verification method:** Startup validation confirms encryption on all declared connections and data stores. An unencrypted connection or unencrypted data store detected at startup halts initialization.

**Maturity:** L1 — Foundational · Mandatory at all levels — no graduation.
---

## [ZT] Zero-Trust Security — Governance Declaration

### AAC-ZT-66 — Short-Lived Credentials, Rotated Automatically {#aac-zt-66}

*Retained from v1.3.*

**Declaration requirement:** No secrets in code repositories or configuration files. Services authenticate via short-lived credentials wherever possible. Credential TTL values are declared as governance artifacts. At L2 and above, a secrets management service handles storage and automatic rotation. At all levels the highest-risk failure mode — credentials committed to version control — is prohibited without exception.

**Verification method:** A credential audit finds zero long-lived static secrets in configuration, code repositories, or environment variables.

**Maturity:** L1 — Foundational · Required at all levels. Credential management sophistication graduates as shown.

**Maturity Profile:**

| | L1 — Foundational | L2 — Mature | L3 — Optimizing |
|---|---|---|---|
| Secrets storage | No secrets in code repositories or configuration files; environment-scoped secrets with declared TTL values | Secrets management service; declared TTL values per credential type | Just-in-time credential provisioning; zero-trust credential issuance with audit on every retrieval |
| Rotation | Manual rotation on declared schedule; documented process | Automatic rotation on declared cadence; rotation failures alert | Continuous rotation with anomaly detection on credential use patterns |
| Blast radius | TTL declared; compromised credentials manually revoked within declared window | Bounded by automatic rotation TTL | Real-time revocation propagation |

---

### AAC-ZT-78 — Authorized Model Registry {#aac-zt-78}

*New in v2.0. Reframes model provenance as explicit deployment authorization rather than full chain-of-custody transparency — the latter is currently unachievable for most commercial model deployments. Complements AAC-ZT-77 (tool provenance) and AAC-RS-40 (model artifact recovery).*

**Declaration requirement:** No model artifact may be deployed in a governed system without explicit authorization by a principal holding TIER_ASSIGNMENT authority under AAC-OG-28. The authorization record constitutes the governance artifact and must declare: the model's identity and version, the authorizing principal and date, the intended use scope and harm tier ceiling, the evaluation results available at the time of authorization, and an explicit residual risk acceptance for any provenance information that is unavailable — including training data composition, intermediate training artifacts, and full evaluation pipelines for third-party models. A model deployed without an authorization record is treated as an unverified component under AAC-ZT-77 and is not cleared for production. Where model assurance certifications become available from authoritative bodies — government-recognized conformity assessments, third-party audits, or standardized model cards with verifiable claims — these satisfy the evaluation results requirement at their declared assurance level and should be incorporated into the authorization record.

**Verification method:** Every model in the deployment registry has a corresponding authorization record that is current within the validity period declared under AAC-OG-24. A model without a current authorization record is flagged at startup. Residual risk acceptance entries are signed by the authorizing principal under AAC-OG-28.

**Maturity:** L3 — Optimizing · Optional at Foundational and Mature, required at Optimizing.
---

## [TB] Testability — Governance Declaration

### AAC-TB-29 — Agent Behavioral Envelope Verification {#aac-tb-29}

*Retained from v1.3. Retitled and reframed: the governance requirement is behavioral envelope compliance verification before deployment, not output accuracy testing against a benchmark dataset.*

**Declaration requirement:** Every automated agent declares a behavioral envelope — the permitted action classes, prohibited action classes, output constraints, and harm tier ceiling within which the agent is authorized to operate. No change to an agent's model, logic, or configuration deploys without verification that the agent remains within its declared envelope. Envelope compliance is binary — the agent either stays within its declared boundaries or it doesn't. The verification mechanism is declared in the Implementation Profile and proportionate to the agent's harm tier ceiling. A deployment that cannot demonstrate envelope compliance does not proceed.

**Verification method:** Evidence of envelope compliance verification exists as a governance artifact for every agent deployment. The verification tests boundary conditions — attempts to execute prohibited action classes, produce out-of-constraint outputs, or exceed the harm tier ceiling — not arbitrary input-output accuracy. A deployment without a compliance record is blocked.

**Maturity:** L2 — Mature · Optional at Foundational, required at Mature and Optimizing.

**Maturity Profile:**

| | L2 — Mature | L3 — Optimizing |
|---|---|---|
| Envelope declaration | Permitted and prohibited action classes; output constraints; harm tier ceiling; envelope compliance threshold declared at 1.00 | Full envelope coverage with adversarial boundary testing per AO-59 — attempts to cross envelope through prompt injection, goal hijacking, or indirect instruction |
| Verification mechanism | Automated boundary test suite in CI/CD; deployment blocked on any envelope violation | Independent envelope review and sign-off; ATLAS-documented attack pattern coverage in boundary test suite |
| Runtime monitoring | Not required | Continuous envelope compliance monitoring; drift from declared envelope triggers AO-56 review |

---

## [AI] Intelligent Automation — Governance Declaration

---

## [SM] Self-Maintenance — Governance Declaration

---

# TIER 3 — COVENANT GUIDANCE

**Tier 3 principles are always optional implementation guidance — no maturity label applies. They support the control plane at any level but are never required for compliance at any level.**

**Implementation patterns that support the governance control plane. These are engineering practices that matter for the system's integrity, performance, and maintainability. They are not enforced per-action by the control plane, but their absence creates conditions that make Tier 1 and Tier 2 compliance harder to sustain. Each includes a note on its governance relevance.**

## [DA] Decision Arbitration — Implementation Guidance

### AAC-DA-64 — Harm Taxonomy Construction Guidance {#aac-da-64}
The harm taxonomy required by AAC-DA-59 is a structured risk classification exercise equivalent in discipline to threat modelling. Practitioners can apply established threat modelling methodologies — STRIDE, PASTA, or MITRE ATT&CK-based approaches — adapted to harm categories rather than attack vectors. STRIDE maps directly: Spoofing → identity harm; Tampering → data integrity harm; Repudiation → audit trail harm; Information Disclosure → privacy harm; Denial of Service → inaction harm (DNH-B); Elevation of Privilege → authority abuse harm. The AAC MITRE ATLAS crosswalk serves as the threat intelligence input to L3 taxonomy reviews — new ATLAS techniques are the harm taxonomy's equivalent of new CVEs and should trigger taxonomy gap review under AAC-OG-24. A harm taxonomy that has never been stress-tested against a structured threat modelling exercise is likely incomplete.
*Governance relevance: A well-constructed harm taxonomy is the foundation of the entire arbitration layer. DA-59's acceptance criterion — every action produces a documented harm tier assessment — is only as strong as the taxonomy it references. Weak taxonomy construction is the primary failure mode DA-59's anti-pattern warns against.*

---

## [OG] Operational Governance — Implementation Guidance

### AAC-OG-31 — Divergence Taxonomy Construction Guidance {#aac-og-31}
The divergence taxonomy required by AAC-OG-25 is a structured classification exercise parallel to harm taxonomy construction (AAC-DA-64). Each divergence type has three required components: what is monitored (the governance posture element being tracked), the observable signal that indicates deviation (a measurable condition, not a judgment call), and the automatic response (restriction, rollback, or escalation — never a notification-only response). A starter taxonomy for most governed agentic deployments includes five divergence types: confidence threshold bypass (agent action executed below declared confidence threshold — detectable per-action in the arbitration log); override frequency spike (override rate exceeds declared KPI baseline within a rolling window — indicates systematic agent behavior drift); governance artifact expiry without renewal (artifact exceeds declared validity period without a renewal workflow — detectable at startup and on periodic check); action class boundary violation (agent attempts an action outside its declared permitted class — caught at the enforcement boundary); audit log gap (active agent produces no log entries within a declared time window — indicates logging failure or governance bypass). The divergence taxonomy should be reviewed on the same cadence as the harm taxonomy under AAC-OG-24 — both are threat intelligence inputs that become stale as the system and its operating environment evolve.
*Governance relevance: OG-25's acceptance criterion — triggering each declared divergence type produces the declared automatic response — is only as strong as the divergence taxonomy it references. An incomplete taxonomy creates blind spots in the policy enforcement integrity layer.*

### AAC-OG-23 — Capability Scope Justification {#aac-og-23}
Every capability, integration, and agent deployed in an autonomous system should be justified against measurable value delivery before deployment. The default for any new capability is the narrowest scope that fulfills the requirement — expand deliberately, not by default. A capability that cannot articulate direct value against its operational cost and risk surface is a candidate for removal. Document the justification as part of the governance artifact set under AAC-OG-24; this creates an auditable record of why each capability exists and provides a basis for periodic scope review.

*Governance relevance: Undocumented capabilities create ungoverned attack surface. Scope justification is the first governance act before deploying any agent or integration — it feeds directly into OG-24 artifact governance and OG-28 authority scoping.*
---

## [DNH] Do No Harm — Implementation Guidance

### AAC-DNH-0d — Trust Harm Prevention in Recommendation Systems {#aac-dnh0d}
Automated recommendations must reflect traceable conditions — verifiable against source data, not optimized toward platform objectives. Dark patterns that push users toward actions they would not otherwise take violate the root DNH-0 commitment regardless of technical compliance with other principles. Design recommendation systems so that the optimization objective and the user's interest are aligned, not in tension. Where they diverge, the user's interest takes precedence. This is enforced at runtime through AAC-ZT-76 (identity disclosure) and AAC-AI-13 (trust calibration) — both of which surface the outputs of recommendation systems to external scrutiny.
*Governance relevance: Dark patterns are a trust harm under AAC-DNH-0d. The runtime controls (ZT-76, AI-13) detect symptoms; this guidance addresses the design root cause.*

### AAC-DNH-0e — Fairness Monitoring in KPI Construction {#aac-dnh0e}
Every agent that makes consequential decisions about people should include at least one fairness metric in its declared KPI set under AAC-AO-51. Scoring systems must not penalize users for characteristics correlated with protected classes — this is not only an ethical obligation but a regulatory one in most jurisdictions. When constructing the KPI set, treat fairness as a first-class performance dimension alongside accuracy and latency, not as an afterthought. The adversarial benchmark required by AAC-AO-59 at L3 should include fairness-violating edge cases. Bias review before any feedback loop update (AAC-AO-56) is the operational mechanism for catching fairness drift before it becomes a systemic harm.
*Governance relevance: Algorithmic harm under AAC-DNH-0e is addressed through the KPI governance in AO-51, the feedback loop governance in AO-56, and the adversarial benchmark in AO-59. This guidance connects those controls to the fairness design intent.*

### AAC-AI-13 — Human Trust Calibration {#aac-ai-13}
Confidence communicated to human principals must reflect actual system certainty. Autonomous systems must not present outputs with false precision — suppressing uncertainty to appear authoritative or framing probabilistic outputs as determinate facts. The confidence signal displayed to a human must not systematically exceed the system's internally computed confidence score. Over-reliance induced by false confidence is a system design failure, not a user error. At L3 continuous calibration monitoring detects systematic upward bias before it becomes an over-reliance pattern; at L2 periodic sample audits against internal scores provide baseline verification.
*Governance relevance: False confidence display is a trust harm under AAC-DNH-0d. AI-10 and DA-62 govern machine-facing confidence enforcement; this guidance governs the human-facing display obligation that those principles do not reach. AI-12 (override always available) provides the safety net when over-reliance occurs despite correct display.*

---

## [AE] Architecture & Engineering

### AAC-AE-06 — Single Resolution Path, Explicit Failure States {#aac-ae-06}
Every workflow has exactly one deterministic path forward. Silent failures and unhandled edge cases are design defects. Every failure mode is anticipated, handled explicitly, and surfaced with enough context for recovery. An agent that fails silently propagates bad state; an agent that fails explicitly enables recovery.
*Governance relevance: Explicit failure states are the precondition for DA-61's liveness guarantee. A system with unhandled failures cannot guarantee resolution.*

---

## [TB] Testability

### AAC-TB-26 — Every Component Is Independently Testable {#aac-tb-26}
Each service has a clear input/output contract testable in isolation. If you cannot write a test without bootstrapping three other services, the boundary is drawn wrong.
*Governance relevance: Independent testability makes governance control verification tractable. A component that cannot be tested in isolation cannot have its governance compliance verified.*

### AAC-TB-28 — Testable in Production, Not Just in Staging {#aac-tb-28}
Design for observability that validates behavior in the live environment. Feature flags on every new capability. Synthetic transactions exercise the full flow on production infrastructure without generating real events.
*Governance relevance: Production observability supports OG-25 (policy enforcement integrity) continuous validation in the environment that matters.*

---

---

## [LL] Low Latency

### AAC-LL-40 — Governance Decisions Must Be Based on Current State {#aac-ll-40}
Any data used by the governance control plane to make enforcement decisions — trust tiers, harm classifications, confidence scores, agent registry entries — must be current at the time of evaluation. Caching of governance-relevant state must declare explicit invalidation triggers tied to the events that change that state. Stale governance state produces incorrect enforcement decisions; staleness is not a performance optimisation in a governance context.
*Governance relevance: Directly supports OG-25 (policy enforcement integrity) and AO-53 (dynamic trust adjustment) — both require that the control plane acts on current state. Cache staleness is the most common implementation failure mode for these two principles.*

### AAC-LL-41 — Async Everything That Is Not User-Blocking {#aac-ll-41}
Audit logging, analytics events, and non-critical notifications fire asynchronously. The user's request-response cycle never waits for out-of-band operations.
*Governance relevance: Async audit logging ensures DP-07 compliance does not introduce latency into the governed action path.*

### AAC-LL-42 — Expensive Derived Data Is Pre-Computed at Write Time {#aac-ll-42}
Query performance must not depend on runtime computation of data that could have been derived at write time. Read paths are fast because write paths do the work.
*Governance relevance: Pre-computed risk scores and harm classifications enable DA-60's arbitration sequence to operate within the time bounds declared in the Implementation Profile.*

---

## [RS] Resiliency

### AAC-RS-34 — No Single Point of Failure on the Transaction Path {#aac-rs-34}
The critical flow degrades gracefully at every step. Every service on the critical path has a defined fallback. When multiple valid actions are available, the system selects the lowest combined risk — a function of reversibility and harm tier.
*Governance relevance: Single points of failure create conditions where DA-61's liveness guarantee is untestable.*

### AAC-RS-35 — Idempotent Operations Everywhere {#aac-rs-35}
Every API call and financial operation is safely retriable without side effects. Idempotency keys on all financial operations; deduplication on all event consumers.
*Governance relevance: Non-idempotent operations make DP-07 audit trail reconstruction unreliable — the same event may appear multiple times with different outcomes.*

### AAC-RS-38 — Data Durability Over Compute Availability {#aac-rs-38}
If forced to choose between availability and data integrity, choose integrity. Database replication across availability zones. Cache as acceleration only.
*Governance relevance: Data loss invalidates DP-07's audit trail. A governance framework with gaps in its audit record cannot provide legal defensibility.*

### AAC-RS-36 — External Dependency Resilience {#aac-rs-36}
Every external service dependency has a declared circuit breaker configuration — failure detection threshold, fast-fail behavior, and recovery test interval — and a graceful degradation response for when the circuit is open. Asynchronous operations retry with a declared backoff strategy; after a declared retry limit, failed operations land in a dead-letter queue for review rather than being silently dropped. Circuit breaker thresholds are adjusted based on a declared dependency health scoring methodology; threshold changes require governance sign-off at L3.
*Governance relevance: External dependency failures are the primary trigger for DA-61 fallback actions. Without circuit breakers, a single downstream outage can produce cascading governance deadlock — the arbitration layer attempts actions that cannot complete, exhausts the liveness window, and falls back repeatedly. Circuit breakers contain the blast radius before it reaches the governance layer. Maps to OWASP ASI-09 (Cascading Agent Failures).*

### AAC-RS-40 — Model Artifact Recovery {#aac-rs-40}
Every deployed model artifact — weights, fine-tuned adapters, and quantized or exported model variants — is versioned and backed up at a declared cadence. A rollback path to a prior known-good artifact exists and has been tested in a production-equivalent environment before the model is promoted. Recovery time and recovery point objectives are declared in the Implementation Profile. Model artifact backup is a governance obligation — not an engineering convenience — and is subject to OG-24 artifact governance. At L3, automated rollback on integrity failure and hot standby model artifacts for Tier 1 harm models provide the highest recovery assurance.
*Governance relevance: Model artifact integrity is a prerequisite for the arbitration layer's deterministic guarantees. A compromised or corrupted model artifact produces non-deterministic outputs that cannot satisfy DA-60's acceptance criterion. Maps to MITRE ATLAS AML.T0031/T0032. At L1 model integrity relies on OG-29's declared model source and the provenance information available through the vendor or model registry.*

### AAC-RS-41 — Hard Shutdown Implementation {#aac-rs-41}
The hard shutdown capability required by AAC-RS-39 is implemented as a dedicated out-of-band signal path — separate from the normal action execution path and not subject to the same arbitration queue. Three implementation considerations: first, the shutdown signal must reach all agent instances, not just the orchestrator — a shutdown that stops the root agent while sub-agents continue executing is not a shutdown. Second, distinguish between graceful drain (complete in-flight actions within a declared timeout, then halt) and immediate halt (stop all execution regardless of action state) — both are valid depending on the harm tier that triggered invocation; Tier 1 scenarios warrant immediate halt, Tier 2 scenarios may permit graceful drain. Third, the governance review required before resumption is not optional — the Implementation Profile declares the minimum review criteria and the authorized principal who signs off on resumption.
*Governance relevance: Operationalizes the hard shutdown requirement in AAC-RS-39. A kill-switch that doesn't reach all agents, or that can be bypassed by in-flight actions, is not a kill-switch.*

---

## [SM] Self-Maintenance

### AAC-SM-43 — Automated Hygiene Runs on a Defined Schedule {#aac-sm-43}
Scheduled cleanup jobs prune, archive, and reconcile without manual intervention. These are first-class system components with monitoring, alerting, and audit logging. Hygiene job failure is detected immediately.
*Governance relevance: Accumulated stale state obscures both failures and attacks from the governance control plane.*

### AAC-SM-44 — Liminal State Resolution {#aac-sm-44}
Unresolved state is a liability. Every transient state has a maximum TTL. Every system artifact resolves to an active entity or is purged — orphans are logged before removal.
*Governance relevance: Liminal state creates ungovernable conditions — artifacts that exist without a governing principal cannot be audited or controlled.*

---

## [ZT] Zero-Trust — Implementation Patterns

### AAC-ZT-72 — Network Segmentation Reflects Trust Boundaries {#aac-zt-72}
Backend services are deployed in private network segments. Only the API gateway and content delivery layer have public-facing endpoints. Database endpoints are never publicly accessible.
*Governance relevance: Network segmentation is the physical enforcement of ZT-64's logical trust boundaries. Logical controls without physical segmentation are bypassable.*

### AAC-ZT-73 — Assume Breach, Contain Blast Radius {#aac-zt-73}
Design every component as if an adjacent component has already been compromised. One compromise should not propagate. Credential boundaries, network segmentation, and encrypted inter-service communication collectively enforce containment.
*Governance relevance: Blast radius containment is the operational implementation of the AAC's core safety property — a failure in one governed component must not compromise the governance control plane itself.*

---

# Governance Statement

This document defines the governance control plane specification for autonomous and AI-driven systems. It is platform-agnostic and applicable across sidecar, inline, and overlay enforcement architectures. When design choices present competing valid options, the relevant principle governs. When principles conflict, AAC-DNH-0 (Do No Harm) governs. Runtime resolution of conflicts between Tier 1 principles is handled by the Decision Arbitration domain.

The deterministic implementation requirement for the arbitration layer (AAC-DA-60, AAC-DA-62, AAC-DA-63) reflects the current state of AI verification capability. It should be revisited when formal verification methods for AI reasoning systems can provide equivalent or stronger auditability guarantees than deterministic policy engines — the governing criterion is not the implementation mechanism but the verifiability of outcomes.

The governance control plane is designed to support integration with external context sources through the Context Interface Contract (AAC-OG-27). Compliant context sources — from local in-process memory through retrieval-augmented pipelines to future sovereign context implementations — satisfy the same interface contract at varying assurance levels. The control plane does not specify the context implementation; it specifies what any compliant implementation must declare.

A companion document — the *AAC v2.0 Implementation Profile Template* — provides a structured template for the deployment-specific parameterization required by AAC-OG-29. The template is not normative; the requirements in AAC-OG-29 are. Organizations may use any format that satisfies the declaration requirements.

Control identifiers are stable within a major version. v2.0 identifiers are forward-compatible with v1.3 references — every v1.3 control that survives into v2.0 retains its original identifier.

**Control identifiers are stable references for use in:**

- Governance control plane policy configurations (OPA/Rego bundles, gRPC policy services)
- Implementation tickets and developer acceptance criteria
- Automated policy gates in CI/CD pipelines
- Compliance mapping and audit evidence packages
- Design review checklists and architecture decision records

---

## Framework Acknowledgements and Dependencies

The AAC v2.0 specification references, builds upon, and in some cases carries direct dependencies on the following external frameworks and standards. Where a principle closes a gap, maps to an obligation, or uses a methodology from an external framework, that dependency is noted inline. This section provides the consolidated reference.

**MITRE ATLAS (Adversarial Threat Landscape for AI Systems) — v5.4.0**
Direct dependency. The AAC MITRE ATLAS Crosswalk maps every AAC control to ATLAS adversarial techniques across 16 tactics. Several principles explicitly reference ATLAS technique identifiers as the threat they mitigate: AAC-ZT-71 (AML.T0051 — prompt injection), AAC-ZT-77 (AML.T0048/T0065 — supply chain compromise), AAC-OG-26 (AML.T0024.003 — steganographic exfiltration), AAC-AO-59 (AML.T0018/T0020 — backdoor and poisoning attacks), AAC-RS-40 (AML.T0031/T0032 — model artifact attacks). The ATLAS case study database is the designated threat intelligence input to L3 harm taxonomy reviews (AAC-DA-59) and adversarial benchmark updates (AAC-AO-59). ATLAS version updates should trigger crosswalk review under AAC-OG-24.

**OWASP Agentic Top 10 (2026) — ASI01–ASI10**
Direct dependency. AAC-ZT-77 (Dynamic Supply Chain Integrity) was introduced specifically to close the OWASP ASI04 partial gap. The AAC Framework Crosswalk documents full coverage of 9/10 OWASP agentic risks with 1 partial. OWASP taxonomy updates should be reviewed against the AAC crosswalk on each release.

**EU AI Act (Regulation (EU) 2024/1689)**
Regulatory dependency. Several principles carry explicit EU AI Act obligations: AAC-ZT-76 (Article 52 — transparency for certain AI systems, in force August 2026), AAC-ZT-78 (Articles 10 and 53 — data governance and GPAI documentation), AAC-DP-06 (Article 10 — data minimisation). The L3 — Optimizing maturity level is designed to satisfy EU AI Act high-risk system obligations (Articles 9–15, in force August 2026). A standalone EU AI Act crosswalk companion document maps all obligations to AAC controls.

**NIST AI Risk Management Framework (AI RMF 1.0)**
Alignment dependency. The AAC Framework Crosswalk documents 18 Full, 5 Partial, and 1 Gap against NIST AI RMF 1.0 Govern, Map, Measure, and Manage functions. The AAC does not require NIST AI RMF adoption but is designed to be adopted alongside it without conflict.

**CSA Agentic Trust Framework (ATF)**
Alignment dependency. The AAC Framework Crosswalk documents 27 Full, 18 Partial, and 11 Gap against CSA ATF. The ATF is the most proximate peer framework to the AAC — both address agentic system governance. The gaps in ATF coverage are the primary areas where AAC novel contributions apply.

**STRIDE Threat Modelling Methodology**
Methodological dependency. AAC-DA-64 (Tier 3 — Harm Taxonomy Construction Guidance) uses STRIDE as the reference methodology for harm taxonomy construction. STRIDE is not required — any structured threat modelling methodology that produces categorised harm outputs satisfies AAC-DA-59's taxonomy requirement.

**Open Policy Agent (OPA) / Rego**
Implementation reference. OPA/Rego is the reference implementation for the deterministic arbitration layer required by AAC-DA-60 and AAC-DA-63. The framework does not mandate OPA — any deterministic policy engine satisfies the requirement. OPA is cited as a concrete implementation example in the governance statement and implementation guidance.

**Ed25519 / Cryptographic Standards**
Implementation reference. Ed25519 is referenced in the authority registry authentication methods (AAC-OG-28) and dynamic supply chain integrity (AAC-ZT-77) as the reference signing mechanism. FIPS-approved equivalents satisfy the same requirement.

---

## On the Evolution from v1.3 to v2.0

Version 1.3 of the Autonomous Agentic Covenant established the philosophical and ethical foundation for governing autonomous systems. It defined 69 principles across 11 domains — from the Do No Harm directive set as an architectural invariant through the Decision Arbitration domain's liveness guarantee and the Zero-Trust security controls. It was deliberately broad. It asked: *what should a well-governed autonomous system look like?* That question needed answering before a more demanding question could be asked.

Version 2.0 asks the harder question: *can these principles be implemented, tested, and enforced in production?*

The answer required structural honesty. Applied against a strict filter — is this principle testable, is it implementable, and does it directly serve the Do No Harm objectives — 69 principles sorted into three distinct layers. Some principles are runtime logic gates: they must execute on every relevant action, they have a binary pass/fail outcome, and their violation constitutes an immediate harm. Others are governance artifacts: they must exist and be declared before a system is permitted to operate, and their absence constitutes a compliance failure. Others are implementation patterns: they represent engineering excellence that supports the governance layer but cannot themselves be enforced by a governance control plane.

This sorting is not a retreat from v1.3's ambitions — it is their operational realization. The Do No Harm directives are strengthened by consolidation into enforceable logic gates. The Decision Arbitration domain is clarified by the requirement for deterministic implementation — probabilistic ethics is not ethics. The novel contributions of v1.3 — the liveness guarantee, the centralized enforcement boundary, System Safe Mode, Policy Enforcement Integrity — survive intact in Tier 1 where they belong.

**What changed structurally:**

The framework is now organized across three enforcement tiers that correspond to the three layers of a governance control plane architecture. Tier 1 (COVENANT CORE) contains the runtime logic gates — principles that the enforcement layer executes per-action. Tier 2 (COVENANT GOVERNANCE) contains the governance artifacts — declarations that must exist before the control plane can operate. Tier 3 (COVENANT GUIDANCE) contains implementation patterns — engineering practices that support the control plane but do not themselves constitute enforcement.

**Why the core is authority-neutral by design:**

The primary reason for the three-tier structure is the separation of runtime enforcement from governance declaration. What must be enforced belongs in the core. Who enforces it, and under what authority, belongs in governance. Keeping these distinct produces a control plane that is both more reliable and more durable — reliable because the enforcement layer does not wait on governance decisions it has already been given, durable because the governance tier can evolve its authority model without touching the enforcement logic.

The governance tier is the decision framework the runtime operates within — not a participant in each decision, but the architect of the conditions under which every decision is made. It declares the harm taxonomy, the authority structure, the trust boundaries, and the escalation model. The runtime tier consumes these declarations and enforces them autonomously, at the speed and scale of the system it governs, without requiring governance to be present at the moment of enforcement.

Accountability is preserved through the Authority Registry (AAC-OG-28), which requires every system to declare its authorized principals and the chain by which their authority was established. The chain is non-circular by construction — no principal is self-declared, and every authority claim traces to an establishing source already in the registry. Accountability is always traceable, always auditable, and always overridable within the terms the governance tier has set.

**What was preserved:**

Control identifiers are stable. Every v1.3 principle that survived into v2.0 retains its original ID. New principles receive new IDs in sequence. The provenance chain of the framework's intellectual history is unbroken. An organization that adopted v1.3 and mapped controls to its compliance program will find its references intact.

**What v2.0 does not specify:**

How the governance control plane is deployed. The sidecar pattern is the most accessible implementation; inline policy gateway and overlay orchestration are equally valid. The principles are implementation-pattern-neutral: they specify what the enforcement layer must do, not where it sits in the architecture. This is intentional. The governance requirements are the same regardless of deployment topology.

**The relationship between v1.3 and v2.0:**

Version 1.3 remains the reference for the framework's ethical philosophy and its broad governance vision. Version 2.0 is the engineering specification — where the rubber meets the road. Both are needed. v1.3 explains why. v2.0 specifies what, precisely enough to build.

---

## Citation

> Thakuri, R. (2026). *The Autonomous Agentic Covenant: A Governance Control Plane Specification for Autonomous and AI-Driven Systems* (Version 2.0). Apache License 2.0.

> Version 2.0 · April 2026 · 67 principles · Three enforcement tiers · 14 domains · 73 control identifiers.

> Evolved from: Thakuri, R. (2026). *The Autonomous Agentic Covenant* (Version 1.3). Apache 2.0. Version 1.3 remains the reference for the framework's ethical philosophy and governance vision.
