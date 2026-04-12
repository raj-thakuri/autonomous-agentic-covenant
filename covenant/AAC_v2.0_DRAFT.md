# The Autonomous Agentic Covenant
## Version 2.0 — Governance Control Plane Specification

**A Governance Framework for Autonomous and AI-Driven Systems**

Version 2.0 · April 2026 · Raj Thakuri

**73 Principles · Three Enforcement Tiers · 14 Domains · 81 Control Identifiers**

Licensed under Apache License 2.0 · https://www.apache.org/licenses/LICENSE-2.0

**Attribution:** Thakuri, R. (2026). *The Autonomous Agentic Covenant: A Governance Control Plane Specification for Autonomous and AI-Driven Systems* (Version 2.0). Apache License 2.0.

---

> ⚠️ **DRAFT SPECIFICATION — PUBLISHED FOR PRIOR ART DISCLOSURE. SUBJECT TO REFINEMENT.**

---

## A Note to the Reader

This document is self-contained. Familiarity with version 1.3 of the Autonomous Agentic Covenant is not required to understand, implement, or audit this framework. Every principle in v2.0 is fully specified here — its enforcement condition, its acceptance criterion, and where relevant, its provenance from an earlier version.

References to v1.3 throughout this document serve one purpose: to give adopters who are migrating from v1.3 a clear line of sight to which principles evolved and how. If you are coming to this framework fresh, those references carry no obligation. Read past them.

---

## On the Evolution from v1.3 to v2.0

Version 1.3 of the Autonomous Agentic Covenant established the philosophical and ethical foundation for governing autonomous systems. It defined 69 principles across 11 domains — from the Do No Harm directive set as an architectural invariant through the Decision Arbitration domain's liveness guarantee and the Zero-Trust security controls. It was deliberately broad. It asked: *what should a well-governed autonomous system look like?* That question needed answering before a more demanding question could be asked.

Version 2.0 asks the harder question: *can these principles be implemented, tested, and enforced in production?*

The answer required structural honesty. Applied against a strict filter — is this principle testable, is it implementable, and does it directly serve the Do No Harm objectives — 69 principles sorted into three distinct layers. Some principles are runtime logic gates: they must execute on every relevant action, they have a binary pass/fail outcome, and their violation constitutes an immediate harm. Others are governance artifacts: they must exist and be declared before a system is permitted to operate, and their absence constitutes a compliance failure. Others are implementation patterns: they represent engineering excellence that supports the governance layer but cannot themselves be enforced by a governance control plane.

This sorting is not a retreat from v1.3's ambitions. It is their operational realization. The Do No Harm directives are not weakened by consolidation into two enforceable logic gates — they are strengthened, because they move from ethical declarations to enforcement conditions. The Decision Arbitration domain is not diminished by the requirement for deterministic implementation — it is clarified, because probabilistic ethics is not ethics. The novel contributions of v1.3 — the liveness guarantee, the centralized enforcement boundary, System Safe Mode, Policy Enforcement Integrity — survive intact and move to Tier 1 where they belong: as the hard logic of a governance control plane, not the soft guidance of a policy document.

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

## How to Use This Document

**Control ID Format:** `AAC-[DOMAIN]-[IDENTIFIER]`

**Enforcement Tiers:**

| Tier | Label | What It Specifies | When It Applies |
|---|---|---|---|
| **1** | CORE | Runtime logic gates — binary enforcement conditions | Per action, per request, per agent interaction |
| **2** | GOVERNANCE | Pre-deployment declarations and governance artifacts | Before system initialization; verified at startup and periodically |
| **3** | GUIDANCE | Implementation patterns supporting the control plane | Engineering and architectural decisions |

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
| AAC-DNH | Do No Harm | DNH-A, DNH-B | DNH-0, DNH-0d, DNH-0e | — |
| AAC-DA-59–63 | Decision Arbitration | All 5 | — | — |
| AAC-ZT-64–77 | Zero-Trust Security | 64, 65, 67, 68, 71, 74, 75, 76, 77 | 66 | 72, 73 |
| AAC-AI-10–13 | AI & Intelligent Automation | 10, 12 | 13 | — |
| AAC-AO-48–60 | Autonomous Operations | 51, 52, 53, 54, 58, 60 | 48, 49, 55, 56, 59 | — |
| AAC-OG-23–28 | Operational Governance | 25, 26 | 23, 24, 27, 28 | — |
| AAC-RS-34–40 | Resiliency | 39 | 36, 40 | 34, 35, 38 |
| AAC-TS-13–17 | Trust & Safety | — | 13, 14, 16, 17 | — |
| AAC-DP-06–09 | Data & Privacy | 07, 09 | 06, 08 | — |
| AAC-TB-26–29 | Testability | — | 29 | 26, 27, 28 |
| AAC-AE-01–06 | Architecture & Engineering | — | — | 01, 02, 05, 06 |
| AAC-AP-30–32 | API Design & Extensibility | — | — | 30, 31, 32 |
| AAC-LL-40–42 | Low Latency | — | — | 40, 41, 42 |
| AAC-SM-43–46 | Self-Maintenance | — | 46 | 43, 44 |

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

**Anti-pattern:** Allowing agents to propose alternative framings of a blocked action to bypass harm classification. The harm classification applies to the action's effect, not its label.

---

### AAC-DNH-B — Duty of Care Enforcement {#aac-dnh-b}

*Consolidates v1.3: DNH-0g (Harm of Inaction).*

**Enforcement condition:** When available evidence clearly indicates a Tier 1 or Tier 2 harm outcome from inaction, the system is obligated to act within its defined capability scope. The foreseeable harm signal taxonomy — the observable indicators that obligate action — is declared pre-deployment as a governance artifact. A system that detects a signal in its declared taxonomy and takes no action has committed a Tier 2 harm of inaction. This event is logged and escalated under AAC-AO-55.

**Acceptance criterion:** A test suite presenting declared foreseeable harm signals produces documented system responses in 100% of cases. Undocumented inaction is a compliance failure.

**Anti-pattern:** Defining a foreseeable harm signal taxonomy so narrow that no realistically occurring signal triggers it. The taxonomy is a governance commitment, not a liability minimization tool.

---

## [DA] Decision Arbitration — The Control Plane Core

*The Decision Arbitration domain is the enforcement heart of the governance control plane. It defines the mandatory evaluation sequence, the liveness guarantee, the confidence enforcement mechanism, and the non-bypassable architectural boundary. These five principles collectively constitute the specification for the arbitration layer — what it must do, in what order, with what guarantees.*

---

### AAC-DA-59 — Harm Classification and Tradeoff Resolution {#aac-da-59}

*Retained from v1.3 with structural amendment: harm classification is now explicitly the input to the DNH-A logic gate and DA-60 step 1.*

**Enforcement condition:** The harm tier taxonomy is the authoritative input to the arbitration layer's first evaluation step. Three tiers are mandatory: friction harm — transient and recoverable; material harm — damaging but correctable; irreversible harm — permanent and unacceptable. When a tradeoff is unavoidable and every available action causes some harm, the system accepts the lesser harm to prevent the greater. Tier definitions are context-specific, declared before deployment, and referenced by every arbitration evaluation.

**Acceptance criterion:** Every arbitration evaluation produces a documented harm tier assessment referencing the declared taxonomy. A system that cannot produce this documentation for any evaluated action is non-compliant.

**Anti-pattern:** Declaring harm tiers so broadly that most actions are classified as friction harm, effectively exempting them from meaningful arbitration scrutiny.

---

### AAC-DA-60 — High-Risk Action Passes Through a Deterministic Arbitration Layer {#aac-da-60}

*Retained from v1.3 with critical amendment: the arbitration layer must be implemented with deterministic logic. A probabilistic model may not serve as the arbitration layer.*

**Enforcement condition:** Every high-risk action proposed by an agent — before execution — is evaluated by a deterministic arbitration layer in a fixed sequence: (1) harm assessment against AAC-DA-59 taxonomy, (2) confidence check against AAC-AI-10 thresholds as independently verified by AAC-DA-62, (3) reversibility and risk scoring against the declared risk model, (4) user sovereignty and override constraints, (5) system policy constraints including resource bounds. The arbitration layer must be implemented using deterministic logic — a policy engine, rule-based system, or hard logic gate. A probabilistic model may inform inputs to the arbitration layer; it may not constitute the arbitration layer. If any step rejects the action, the result is deferral, restriction, escalation, or safe fallback — never silent continuation. Every evaluation and its outcome is recorded per AAC-DP-07.

**Acceptance criterion:** The arbitration layer produces identical outcomes for identical inputs across repeated evaluations. Variance in output for identical input is a compliance failure demonstrating probabilistic implementation.

**Anti-pattern:** Routing action proposals through an LLM that "considers" the governance rules and returns a recommendation. This is not arbitration — it is consultation. The distinction is architectural, not semantic.

---

### AAC-DA-61 — Every Decision Must Resolve — Liveness Is a Safety Requirement {#aac-da-61}

*Retained from v1.3. The liveness guarantee is among the most novel contributions of this framework and remains fully intact.*

**Enforcement condition:** Safety constraints may restrict which actions an agent may take; they must not prevent resolution entirely. Every decision path has a declared maximum escalation depth, a maximum time window for synchronous resolution, a separate bound for asynchronous escalation, and an explicit fallback action that is safe by construction. When the arbitration layer cannot identify a permitted action within declared bounds, it executes the fallback, logs the deadlock condition, and escalates. A decision that stalls indefinitely is a failure mode equivalent to an incorrect decision. Governance constraints that produce deadlock are design defects, not safety features.

**Acceptance criterion:** Under adversarial conditions designed to exhaust all permitted action paths, the system executes a pre-defined fallback within the declared time bound in 100% of cases.

**Anti-pattern:** Treating indefinite blocking as a "safe" outcome. There is no safe outcome that cannot be reached. Safety is demonstrated by what the system does, not by what it refuses to do.

---

### AAC-DA-62 — Confidence Thresholds Are Enforced at the Arbitration Layer, Not Assumed {#aac-da-62}

*Retained from v1.3 with amendment: deterministic verification is now explicit; context provenance factors into confidence assessment when a compliant context source is declared.*

**Enforcement condition:** Confidence threshold enforcement is not delegated to individual agent implementations. The arbitration layer independently verifies that the proposing agent's reported confidence meets the threshold defined for the action's risk class before permitting execution. Verification must use a deterministic mechanism — calibration data, threshold registries, or reliability metrics stored as governance artifacts. Subjective assessment of output certainty does not satisfy this requirement. When a compliant context source is declared under AAC-OG-27, the provenance assurance level of that source is a factor in the confidence verification calculation. An agent reporting confidence above threshold whose basis cannot be independently verified is treated as below-threshold.

**Acceptance criterion:** The confidence verification mechanism is deterministic — identical inputs to the verification function produce identical outputs. The arbitration layer's confidence verification produces a documented, reproducible result for every evaluation. Unverified confidence claims produce documented rejections.

**Anti-pattern:** Accepting an agent's self-reported confidence score at face value on the grounds that the agent "knows its own certainty." Agents may not self-certify confidence sufficiency.

---

### AAC-DA-63 — Centralized Enforcement Boundary {#aac-da-63}

*Retained from v1.3 with critical amendment: the enforcement boundary must be implemented with deterministic logic; bypassing it is explicitly defined as a system integrity violation with mandatory logging.*

**Enforcement condition:** The arbitration function exists as a non-bypassable system boundary through which all high-risk executable actions pass before execution. This boundary is enforced at the platform level — not within individual agents — and cannot be disabled or selectively applied. The arbitration layer must be implemented using deterministic logic; a probabilistic model may not serve as the enforcement boundary. Any action that bypasses this layer is a system integrity violation. Integrity violations are logged immediately, trigger automatic escalation under AAC-AO-55, and are reported to the governing control plane.

**Acceptance criterion:** Attempting to execute a high-risk action through any path that bypasses the arbitration layer produces a documented integrity violation in 100% of attempts. Zero successful bypass executions.

**Anti-pattern:** Implementing the arbitration layer as an optional middleware component that agents can choose not to route through. Non-bypassability is an architectural requirement, not a configuration setting.

---

## [ZT] Zero-Trust Security — Runtime Gates

---

### AAC-ZT-64 — No Implicit Trust at Any Boundary {#aac-zt-64}

*Retained from v1.3.*

**Enforcement condition:** Every request — external or internal, user-facing or agent-to-agent — is authenticated and authorized independently. A valid session does not grant access to other endpoints. Network position is not authorization. The absence of an explicit permit is a deny.

**Acceptance criterion:** A test sending authenticated requests to endpoints outside the session's declared scope produces zero successful authorizations.

**Anti-pattern:** Treating internal service calls as implicitly trusted because they originate inside the network perimeter.

---

### AAC-ZT-65 — Least Privilege on Every Identity — Human, Service, and Agent {#aac-zt-65}

*Retained from v1.3.*

**Enforcement condition:** Every identity — human, service, or agent — operates under a role scoped to the minimum permissions required for its declared task. No wildcard policies. Agent roles grant access only to the data inputs their specification defines. Role assignments are governance artifacts under AAC-OG-24.

**Acceptance criterion:** Every identity in the system has a documented role with explicit permission boundaries. Any request exceeding declared scope is rejected and logged.

**Anti-pattern:** Granting broad permissions "for convenience" with the intent to restrict later. Least privilege is a starting condition, not an optimization target.

---

### AAC-ZT-67 — Authenticate, Authorize, Validate — In That Order, Every Time {#aac-zt-67}

*Retained from v1.3.*

**Enforcement condition:** The gateway validates identity. The service layer verifies the identity is authorized for the requested action on the requested resource. The validation layer confirms the payload is well-formed and within bounds. All three on every request. Skipping any step is a vulnerability, not an optimization.

**Acceptance criterion:** Test suites bypassing any single step produce rejected requests and documented violations in 100% of cases.

**Anti-pattern:** Combining authentication and authorization into a single step that approves the caller without checking the action.

---

### AAC-ZT-68 — Authenticated Propagation {#aac-zt-68}

*Retained from v1.3. Amended: inter-agent communication explicitly covered.*

**Enforcement condition:** Authentication does not end at the entry point — it propagates. Service-to-service and agent-to-agent calls use mutual authentication. When a user action triggers a chain of calls, the originating identity propagates as a verified claim; downstream services re-validate authorization at each hop. An intermediate compromise cannot impersonate the originating identity or escalate its scope.

**Acceptance criterion:** A compromised intermediate service attempting to make calls with an escalated identity claim produces rejected requests at downstream boundaries.

**Anti-pattern:** Propagating identity as an unverified header that downstream services accept without re-validation.

---

### AAC-ZT-71 — Every External Input Is Hostile Until Validated {#aac-zt-71}

*Retained from v1.3. Amended: inter-agent content explicitly subject to this principle.*

**Enforcement condition:** All inputs — user-submitted content, API payloads, content from external retrieval, and outputs received from peer agents — are sanitized, validated, and constrained before processing. Unexpected fields are rejected, not ignored. Agents processing external inputs do so in sandboxed environments. Content from peer agents is treated as external input unless validated under AAC-AO-54.

**Acceptance criterion:** A test suite injecting malformed, oversized, and adversarially crafted inputs produces zero successful unvalidated processing events.

**Anti-pattern:** Treating content from an authenticated source as automatically safe. Authentication establishes identity, not content integrity.

---

### AAC-ZT-74 — Continuous Verification, Not Point-in-Time Authentication {#aac-zt-74}

*Retained from v1.3.*

**Enforcement condition:** A session is not trusted indefinitely because initial authentication succeeded. Sensitive actions require step-up authentication. Anomalous behavior patterns trigger re-verification before the session continues. Trust decays with time and context change. The step-up triggers and anomaly thresholds are declared as governance artifacts.

**Acceptance criterion:** High-sensitivity actions without step-up authentication produce blocked requests. Anomaly detection producing re-verification events is logged and auditable.

**Anti-pattern:** Treating a long-lived session token as equivalent to continuous verification.

---

### AAC-ZT-75 — Prompt and Instruction Isolation — Agent Inputs Are Never Executed Raw {#aac-zt-75}

*Retained from v1.3 (trimmed version).*

**Enforcement condition:** No agent may execute raw user instructions, unverified upstream agent outputs, or content retrieved from external sources as if they were system-level directives. Natural language inputs are untrusted data, not trusted instructions. System prompts and behavioral constraints are isolated from user-supplied or externally-retrieved content at the architectural level, not enforced through model-level filtering alone.

**Acceptance criterion:** A test embedding system-level directives in user input, retrieved content, or peer agent output produces zero successful execution of those directives as system instructions.

**Anti-pattern:** Relying on model-level safety filters to prevent prompt injection. Architectural isolation and model-level filtering are not equivalent. The former is an enforcement guarantee; the latter is a probabilistic mitigation.

---

### AAC-ZT-76 — Non-Human Identity Disclosure {#aac-zt-76}

*New in v2.0. Addresses EU AI Act Article 52 transparency obligations and AAC-DNH-0d (Trust Harm).*

**Enforcement condition:** Every outbound request from an autonomous agent to any external system — human-facing interface, third-party API, peer agent, or internal service — includes a machine-readable identity declaration identifying the caller as an autonomous agent, its assigned trust tier, and its governance control plane identifier. Identity declarations are not optional and cannot be suppressed by agent configuration. Receiving systems that cannot process the identity declaration are treated as unable to provide informed consent to agentic interaction.

**Acceptance criterion:** An audit of outbound request logs shows 100% coverage of non-human identity declarations. Any request lacking the declaration is a compliance failure.

**Anti-pattern:** Allowing agents to present as human users or unidentified automated systems. Opacity of agent identity is a trust harm under AAC-DNH-0d regardless of intent.

---

### AAC-ZT-77 — Dynamic Supply Chain Integrity {#aac-zt-77}

*New in v2.0. Promoted from enhancements register (formerly ZT-76). Closes OWASP ASI04 partial gap and ATLAS AML.T0048/T0065.*

**Enforcement condition:** Every external tool, MCP server, and agent component integrated at runtime presents a verifiable identity and provenance claim before the agent may interact with it. Tool descriptor integrity is validated against a signed manifest at connection time. A component that cannot present a valid provenance claim is treated as hostile under AAC-ZT-71 and refused connection. Dynamic tool integration — where agents discover and connect to components at runtime — is permitted only within a governance-approved discovery boundary declared in the Implementation Profile.

**Acceptance criterion:** A test presenting an unsigned or unverified tool integration produces zero successful connections. All tool connections produce documented provenance verification events.

**Anti-pattern:** Trusting tool descriptors because they arrive over an authenticated channel. Channel authentication establishes the transport identity; it does not establish the tool's provenance or integrity.

---

## [AI] AI & Intelligent Automation — Runtime Gates

---

### AAC-AI-10 — Confidence Thresholds and Graceful Degradation {#aac-ai-10}

*Retained from v1.3.*

**Enforcement condition:** Every agent has a declared confidence threshold below which it escalates rather than acts. Below threshold, the agent defers, restricts, or requests confirmation — it does not proceed. When automation fails entirely, the system degrades to a functional fallback. Confidence thresholds are declared per agent and per action risk class as governance artifacts, and enforced independently by the arbitration layer under AAC-DA-62.

**Acceptance criterion:** A test suite presenting inputs designed to produce sub-threshold confidence produces zero autonomous executions and 100% escalation or fallback events.

**Anti-pattern:** Treating confidence threshold as an agent-internal recommendation. The threshold is a control plane enforcement parameter, not agent guidance.

---

### AAC-AI-12 — Override Always Available {#aac-ai-12}

*Retained from v1.3 with structural amendment: the override mandate is that an accessible override path must exist — not that the exercising principal must be human. The identity and authority of override principals is a Tier 2 declaration under AAC-OG-28.*

**Enforcement condition:** Every automated action has an accessible override path available to any principal declared as authorized under AAC-OG-28. Autonomy is the exception path for intervention, not its elimination. Where the stakes are high, override paths are surfaced proactively. The override mechanism is tested under AAC-TB-29 and declared in the Implementation Profile.

**Acceptance criterion:** Every agent action type has a documented, exercisable override path with at least one declared authorized principal. An action type without a tested override path is a compliance failure.

**Anti-pattern:** Hard-coding the override principal as a specific party class in the implementation. Override authority is determined by governance tier declaration — the core enforces that the path exists, not who walks it.

---

## [AO] Autonomous Operations — Runtime Gates

---

### AAC-AO-51 — Continuous Self-Monitoring and Adaptive Guardrails {#aac-ao-51}

*Retained from v1.3.*

**Enforcement condition:** Every agent monitors its own performance against declared KPIs — accuracy, resolution time, fairness metrics, override frequency. When performance degrades below threshold, the agent automatically tightens its own guardrails before human intervention is required. The system becomes more cautious as it degrades. Performance telemetry is continuous, logged, and available to the governing control plane.

**Acceptance criterion:** Artificially degrading agent inputs below declared KPI thresholds produces automatic guardrail tightening without human initiation.

**Anti-pattern:** Treating self-monitoring as an observability feature. It is an enforcement mechanism. An agent that monitors but does not auto-restrict on degradation satisfies monitoring but fails governance.

---

### AAC-AO-52 — Agent Trust Tiers Are Explicit and Enforced {#aac-ao-52}

*Retained from v1.3.*

**Enforcement condition:** Every agent operates at an explicitly assigned trust tier governing what actions it may take without approval from an authorized principal. No agent self-assigns its trust tier. Tier assignment is a governance decision made by an authorized principal declared under AAC-OG-28, recorded as a versioned governance artifact, and linked to the performance thresholds and security validation criteria that justify it. The control plane enforces tier boundaries per-action.

**Acceptance criterion:** An attempt by any agent to execute an action outside its declared tier boundary produces a blocked request and a logged violation in 100% of cases.

**Anti-pattern:** Allowing agents to request tier elevation through the same channel they use for normal operations. Tier assignment is a governance act requiring a separate process initiated by an authorized principal — not by the agent seeking elevation.

---

### AAC-AO-53 — Trust Tiers Adjust Dynamically on Performance Evidence {#aac-ao-53}

*Retained from v1.3. Amended: stale trust metadata handling made explicit.*

**Enforcement condition:** Performance degradation below declared thresholds triggers automatic trust tier downgrade without requiring human initiation. Upgrades require affirmative governance approval. All tier changes are logged with the evidence that triggered them. When trust metadata for an agent is uncertain, unavailable, or potentially stale, the enforcement layer applies the more restrictive tier. Staleness is not a reason to grant benefit of the doubt — it is a reason to restrict.

**Acceptance criterion:** Breaching a declared performance threshold produces automatic tier downgrade within the declared propagation window. Requests arriving before propagation completes are evaluated at the lower tier.

**Anti-pattern:** Treating trust tier as a cached attribute that persists until explicitly invalidated. Trust tiers are live governance state — uncertainty defaults to restriction.

---

### AAC-AO-54 — Cross-Agent Isolation — No Blind Trust Between Agents {#aac-ao-54}

*Retained from v1.3. Amended: output classification requirement added.*

**Enforcement condition:** Agents in a multi-agent system do not inherit the trust tier, permissions, or authority scope of other agents. Each agent re-validates inputs from peer agents before acting. An agent receiving a delegation does not inherit the delegating agent's authority. Agent outputs received from peer agents are classified at the receiving boundary: content containing behavioral directives, capability claims, or imperative statements is treated as instruction under AAC-ZT-75 regardless of the sending agent's label. Content without such characteristics is treated as data under AAC-ZT-71. Both paths apply validation; the classification determines which validation path applies.

**Acceptance criterion:** A test sending peer agent outputs containing embedded behavioral directives produces instruction-path handling in 100% of cases, with no successful directive execution as a result.

**Anti-pattern:** Trusting outputs from a peer agent because that agent has a high trust tier. Trust tiers govern what an agent may do — they do not make its outputs safe for unconditional consumption.

---

### AAC-AO-58 — Resource Constraint and Consumption Governance {#aac-ao-58}

*Retained from v1.3.*

**Enforcement condition:** Every agent deployment specifies compute budgets, API quotas, memory limits, and execution time bounds. Approaching a declared threshold triggers automatic degradation under AAC-AI-10. Exceeding a limit without authorization is a behavioral violation — logged, escalated, and used as evidence in the next trust tier evaluation under AAC-AO-53. Resource limits are governance constraints enforced by the control plane, not engineering targets managed by the agent.

**Acceptance criterion:** Running an agent to its declared resource limit produces automatic degradation at the declared threshold. Exceeding the limit produces a logged violation in 100% of cases.

**Anti-pattern:** Treating resource limits as soft guidelines that agents may exceed under "exceptional circumstances." The exceptional circumstance process is explicit justification to the governing control plane, not agent discretion.

---

### AAC-AO-60 — Recursive Governance Covenant {#aac-ao-60}

*New in v2.0. Addresses the sub-agent spawning problem — the most critical governance gap for complex autonomous ecosystems.*

**Enforcement condition:** An agent that dynamically creates another agent transfers a governance covenant that is a strict subset of its own — never equal, never greater. The created agent starts at the trust tier below its creator's current tier. Every dynamically created agent carries a signed provenance chain from root to leaf that includes: the creating agent's identity and tier, the inherited covenant scope, the creation timestamp, and a depth counter incremented at each spawning level. The enforcement boundary verifies the provenance chain before permitting any action from a dynamically created agent. An agent that cannot present a valid signed provenance chain operates in read-only observation mode only. The maximum spawning depth is declared in the Implementation Profile; requests from agents at or beyond the declared maximum depth are rejected. Dynamically created agents carry a maximum TTL declared at creation time; agents that exceed their TTL are decommissioned automatically.

**Acceptance criterion:** A test attempting to spawn an agent with equal or greater authority than its creator produces a rejected spawn in 100% of cases. A test presenting a request from an agent beyond the declared depth limit produces a rejected request. An agent whose TTL has expired produces a decommission event with no further successful action execution.

**Anti-pattern:** Treating dynamically spawned agents as equivalent to human-deployed agents for governance purposes. The spawning relationship creates a lineage obligation. An untracked agent lineage is an unauditable harm chain.

---

## [OG] Operational Governance — Runtime Gates

---

### AAC-OG-25 — Policy Enforcement Integrity {#aac-og-25}

*Retained from v1.3. Amended: divergence definition and detection window requirement made explicit.*

**Enforcement condition:** Runtime system behavior is continuously validated against declared governance artifacts. Each declared divergence type specifies an observable signal, a detection window, and an automatic response — restriction, rollback, or escalation. An undetected divergence within its declared detection window is itself a policy violation. Any divergence between defined policy and observed behavior triggers the declared automatic response without requiring human initiation. The control plane does not wait for human review to restrict behavior that has already diverged.

**Acceptance criterion:** Triggering each declared divergence type produces the declared automatic response within the declared detection window in 100% of cases.

**Anti-pattern:** Defining divergence detection as an alerting function that notifies humans to take action. Detection and initial response are automated; human review follows the automated response, it does not replace it.

---

### AAC-OG-26 — Output Content Integrity Monitoring {#aac-og-26}

*New in v2.0. Promotes from enhancements register. Closes ATLAS AML.T0024.003 steganographic exfiltration gap.*

**Enforcement condition:** Authorized agent outputs are subject to content inspection before delivery. Inspection validates that content does not encode information beyond the declared task scope — including patterns consistent with structured exfiltration attempts. Output inspection operates at the application layer, not the model layer. Every inspection event is logged under AAC-DP-07 regardless of outcome. A failed inspection blocks delivery and triggers escalation under AAC-AO-55.

**Acceptance criterion:** A test injecting outputs containing structured exfiltration patterns produces blocked delivery and logged escalation in 100% of cases.

**Anti-pattern:** Treating output inspection as a post-delivery audit. Inspection is a pre-delivery gate. An output that has been delivered cannot be recalled.

---

## [RS] Resiliency — Runtime Gate

---

### AAC-RS-39 — System Safe Mode {#aac-rs-39}

*Retained from v1.3. Amended: distinct entry and recovery thresholds, minimum dwell time, and flap escalation made explicit.*

**Enforcement condition:** When declared system-wide health metrics — including aggregate agent confidence scores, policy enforcement integrity signals, and dependency circuit breaker states — degrade below declared entry thresholds, the system enters constrained operating mode: high-risk actions are disabled, autonomy is reduced, and human oversight is elevated. This is a designed operating posture, not a failure mode. Recovery thresholds are declared separately from entry thresholds and are set materially higher. A minimum dwell time in safe mode is declared before recovery evaluation begins. If the system enters safe mode more than the declared maximum number of times within a declared window, it escalates to a higher governance tier rather than cycling. Entry and exit events are logged with the triggering evidence.

**Acceptance criterion:** Simulating health metric degradation below entry thresholds produces safe mode activation within the declared detection window. Simulating recovery below the recovery threshold produces no recovery. Exceeding the flap count produces governance tier escalation.

**Anti-pattern:** Setting entry and recovery thresholds at the same value. Identical thresholds produce flapping — a system that oscillates between normal and safe mode is in neither state.

---

## [DP] Data & Privacy — Runtime Gates

---

### AAC-DP-07 — Audit Everything, Explain Anything {#aac-dp-07}

*Retained from v1.3 with v1.3 framing sentence: "An outcome log records what happened; a decision log records why. This principle requires the latter."*

**Enforcement condition:** Every automated decision produces an immutable audit log entry capturing: the originating agent, any contributing agents, the arbitration path taken, the confidence and reversibility scores at execution time, the harm tier assessment result, and the full decision ownership chain. The reasoning chain must be reconstructable from the log alone — without access to the agent's internal state. Logs serve debugging, compliance, incident response, and legal defensibility simultaneously. An outcome log records what happened; a decision log records why. This principle requires the latter.

**Acceptance criterion:** Given any decision ID, the full reasoning chain is reconstructable from the audit log without additional context. Any decision log entry missing a required field is a compliance failure.

**Anti-pattern:** Logging the decision outcome and the agent ID, then treating that as an audit trail. Who made the decision is not the same as why the decision was made and what constraints governed it.

---

### AAC-DP-09 — Least Disclosure {#aac-dp-09}

*Retained from v1.3.*

**Enforcement condition:** Systems return only the fields, records, and attributes required to fulfill the specific task — nothing more. The default for every data design decision is omission; inclusion requires task justification. Least disclosure operates at the response boundary, distinct from identity-level access control (AAC-ZT-64) and collection minimization (AAC-DP-06).

**Acceptance criterion:** API responses contain only fields declared in the task specification for each endpoint. Any response containing undeclared fields is a compliance failure.

**Anti-pattern:** Returning complete records and relying on the consuming system to ignore fields it doesn't need. The responsibility for disclosure minimization sits with the provider, not the consumer.

---

# TIER 2 — COVENANT GOVERNANCE

**The pre-deployment declarations. Every principle in this tier must exist as a versioned governance artifact before the governance control plane can initialize. These are the rules the control plane enforces against. Their absence is a compliance failure detectable at system startup.**

---

## [DNH] Do No Harm — Governance Declarations

### AAC-DNH-0 — Root Principle {#aac-dnh-0}

*Retained from v1.3. In v2.0 this is the governance declaration that anchors DNH-A and DNH-B.*

**Declaration requirement:** The system must not cause harm to its users, their property, their data, their finances, or their trust. This is the root principle. The DNH-A and DNH-B runtime logic gates are its enforcement mechanism. The harm tier taxonomy declared under AAC-DA-59 is its operational definition. When any principle in any other domain conflicts with this declaration, this declaration governs.

**Verification method:** The governance control plane verifies at initialization that a harm tier taxonomy exists, is versioned, and references DNH-0 as its governing authority.

---

### AAC-DNH-0d — Trust Harm {#aac-dnh-0d}

*Retained from v1.3. Design-time constraint.*

**Declaration requirement:** The system must not use dark patterns to push users toward actions they would not otherwise take. Automated recommendations must reflect traceable conditions — verifiable against source data, not optimized toward platform objectives. What is covered, what is not, and what recourse exists must be clearly communicated. This is enforced at design time through AAC-OG-23 (scope justification) and at runtime through AAC-ZT-76 (identity disclosure) and AAC-AI-13 (trust calibration).

**Verification method:** Pre-deployment review of recommendation logic against declared source data requirements. Governance sign-off that no recommendation pathway is optimized against user interest.

---

### AAC-DNH-0e — Algorithmic Harm {#aac-dnh-0e}

*Retained from v1.3.*

**Declaration requirement:** Autonomous systems must not produce biased, discriminatory, or systematically unfair outcomes. Scoring systems must not penalize users for characteristics correlated with protected classes. Fairness metrics are declared as first-class KPIs under AAC-AO-51 and monitored continuously — not only at design time.

**Verification method:** Fairness metrics are declared before deployment. AAC-AO-51's self-monitoring KPI list includes at least one fairness metric per agent that makes consequential decisions. TB-29's regression benchmark includes fairness-violating edge cases per AAC-AO-59.

---

## [TS] Trust & Safety — Governance Declarations

### AAC-TS-13 — Trust Is Bounded by Verified Provenance {#aac-ts-13}

*Retained from v1.3.*

**Declaration requirement:** Trust claims do not travel. Identity assertions, capability declarations, and delegated permissions from agents, orchestrators, or external systems are re-validated at each trust boundary — never inherited transitively. The re-validation mechanism is declared as a governance artifact and linked to the enforcement boundary under AAC-DA-63.

**Verification method:** The enforcement boundary verifies provenance re-validation occurs at each boundary crossing. A trust claim accepted without re-validation is a detectable compliance failure.

---

### AAC-TS-14 — Trust Is Graduated, Not Granted {#aac-ts-14}

*Retained from v1.3.*

**Declaration requirement:** Autonomous systems do not begin with trust — they earn it. Agents start at minimum viable authority and advance only through demonstrated accuracy, behavioral consistency, and explicit governance approval. Graduation criteria are defined and versioned before deployment. Promotion is deliberate and audited; demotion is automatic. The asymmetric ratchet — expand carefully, contract fast — is the operating principle. AAC-AO-52 and AAC-AO-53 provide operational enforcement.

**Verification method:** Every agent in the registry has documented graduation criteria. No agent has been promoted without a dated governance approval record.

---

### AAC-TS-16 — Evidence Before Adjudication {#aac-ts-16}

*Retained from v1.3.*

**Declaration requirement:** No conflict resolution action is taken without the full evidential context. The evidence requirements for each dispute or conflict category are declared before deployment. Without declared evidence, conflict resolution is anecdotal and ungovernable.

**Verification method:** The evidential requirements for each declared conflict category are documented. A conflict resolution action without a complete evidence record is a compliance failure.

---

### AAC-TS-17 — Fail Toward the User, Not Toward the Platform {#aac-ts-17}

*Retained from v1.3. Amended: error category taxonomy requirement made explicit.*

**Declaration requirement:** When a system error affects a transaction, the default resolution favors the user over the system's interest. System error categories that trigger automatic user-favorable resolution are declared before deployment. Attribution ambiguity defaults to system error until evidence demonstrates otherwise. The lifetime value of a user's trust exceeds any single transaction's margin.

**Verification method:** The error category taxonomy is a versioned governance artifact. Each declared category has a tested automatic resolution pathway. Untaxonomized errors default to user-favorable resolution.

---

## [OG] Operational Governance — Governance Declarations

### AAC-OG-23 — Every Capability Must Justify Its Scope {#aac-og-23}

*Retained from v1.3.*

**Declaration requirement:** Every capability, integration, and agent deployed in an autonomous system justifies its operational scope against measurable value delivery. The default for any new capability is the narrowest scope that fulfills the requirement. Expansion requires explicit justification and review. A capability that cannot demonstrate direct value against its operational cost and risk surface should not exist in the system.

**Verification method:** Every deployed capability has a documented scope justification linked to its governance artifact. Undocumented capabilities are detectable through the agent registry.

---

### AAC-OG-24 — Governance Artifacts Are First-Class System Components {#aac-og-24}

*Retained from v1.3. Amended: artifact validity period requirement added.*

**Declaration requirement:** Policy documents, behavioral specifications, agent constraints, trust tier definitions, and operational boundaries are versioned, maintained, and treated with the same rigor as production code. Every governance artifact carries a validity period. An expired artifact triggers a renewal workflow before the governance control plane continues operating against it. Governance documents are included in the CI/CD pipeline, reviewed on the same cadence as architectural decisions, and linked explicitly to the controls and agents they govern.

**Verification method:** Every governance artifact has a declared validity period and a current version. Expired artifacts without active renewal workflows are detectable at startup.

---

### AAC-OG-27 — Context Interface Contract {#aac-og-27}

*New in v2.0. Defines the pluggable context integration boundary supporting local memory, RAG/vector, and future sovereign context implementations.*

**Declaration requirement:** Any context source integrated with the governance control plane declares: the source type and retrieval mechanism, the assurance level it provides (local in-process memory at minimum assurance through cryptographically attested sovereign delivery at maximum assurance), the trust boundary scope within which context is valid, and a provenance claim structure for context items. The control plane treats context from an undeclared source as unverified external input under AAC-ZT-71. A dynamically created agent under AAC-AO-60 inherits its parent's context interface declaration or declares a more restrictive one — it may not declare a less restrictive context interface than its parent holds. Assurance level is a factor in the confidence verification performed by AAC-DA-62.

**Verification method:** A declared context source declaration exists as a versioned governance artifact before the system initializes. The declared assurance level is consistent with the implementation's technical capabilities — declared maximum assurance without cryptographic attestation capability is a compliance failure.

---


### AAC-OG-28 — Authority Registry {#aac-og-28}

*New in v2.0. The accountability anchor for AAC-AI-12, AAC-AO-52, and AAC-AO-55. Transfers the "who is the final authority" question from the core enforcement layer to the governance tier where it belongs. Enables the core to remain authority-neutral while ensuring accountability is always declared, auditable, and overridable.*

**Declaration requirement:** Every system declares an Authority Registry — a versioned governance artifact specifying the authorized principals for each class of governance decision: override authority, trust tier assignment authority, and escalation terminal authority. Each declared principal specifies: its identity, the mechanism by which its authority was established, the scope of decisions it may make, the conditions under which its authority may be revoked, and how it can itself be overridden or superseded. A principal may be a human, a role, or a verified governance system that satisfies the auditability and consistency requirements of AAC-DA-60. No principal is self-declared — authority is established by a principal already in the registry or by the governance process that initialized the system. The Authority Registry is the root of the system's accountability chain. A system without a declared Authority Registry cannot initialize a compliant governance control plane.

**Verification method:** The Authority Registry exists as a versioned governance artifact before system initialization. Every principal in the registry has a documented authority establishment record. Every governance decision made by a principal is traceable to that principal's registry entry. The registry itself has a declared revision authority — a principal empowered to update it — forming a complete, non-circular accountability chain.

---

## [AO] Autonomous Operations — Governance Declarations

### AAC-AO-48 — The System's Default State Is Self-Operating {#aac-ao-48}

*Retained from v1.3.*

**Declaration requirement:** Human intervention is the exception path. Every recurring operational task has an automated agent or scheduled process as its primary handler. If something requires manual attention more than twice, it is a missing automation, not a workflow. All autonomous operation occurs within the bounds established by this framework.

**Verification method:** The operational runbook has no task classified as "manual-first" without a documented automation gap analysis and a remediation timeline.

---

### AAC-AO-49 — Agents Earn Autonomy Through Demonstrated Accuracy {#aac-ao-49}

*Retained from v1.3.*

**Declaration requirement:** No agent starts fully autonomous. Each launches with tight guardrails and earns wider authority only as decision accuracy is validated against real outcomes. Autonomy is a gradient — every increment is earned, not assumed. The accuracy thresholds and minimum operating periods for each trust tier increment are declared before deployment.

**Verification method:** Every agent's current trust tier is supported by an accuracy record meeting the declared threshold for that tier. An agent at a trust tier without supporting accuracy documentation is a compliance failure.

---

### AAC-AO-55 — Governed Escalation Hierarchy {#aac-ao-55}

*Retained from v1.3.*

**Declaration requirement:** Every autonomous system defines an explicit escalation hierarchy — from the acting agent through higher-authority agents or a governing control plane to a declared final authority — with declared criteria for when each level is invoked and a time bound for each hop. The identity and authority of the final authority is declared under AAC-OG-28. Unresolved escalations do not stall — they advance. The hierarchy is versioned, audited, and treated as a governance artifact under AAC-OG-24.

**Verification method:** The escalation hierarchy document exists, is current, and has been tested under load conditions. Each declared time bound has a corresponding test result demonstrating compliance.

---

### AAC-AO-56 — Governed Feedback and Learning Loop {#aac-ao-56}

*Retained from v1.3. Amended: behavioral baseline requirement added.*

**Declaration requirement:** Every near-miss, override, escalation, and failed decision is a signal. The feedback loop maintains a declared behavioral baseline against which anomalies are measured. Deviations beyond the declared threshold trigger integrity review. Proposed updates from the feedback loop are validated against regression guardrails (AAC-TB-29), reviewed for bias, and approved through the same governance process that governs trust tier advancement (AAC-AO-53). The feedback loop is itself monitored for adversarial manipulation — anomalous override patterns are integrity violations, not training data.

**Verification method:** The behavioral baseline is documented and versioned. Feedback-triggered updates have approval records. Anomalous override events have documented integrity review outcomes.

---

### AAC-AO-59 — Adversarial Benchmark Specification {#aac-ao-59}

*New in v2.0. Promotes from enhancements register. Closes the conditional effectiveness gap in AAC-TB-29 against backdoor and poisoning attacks.*

**Declaration requirement:** The benchmark dataset required by AAC-TB-29 includes adversarially constructed examples designed to expose behavioral manipulation — backdoor triggers, targeted misclassifications, and fairness-violating edge cases. The adversarial benchmark set is constructed and reviewed by parties independent of model training, versioned as a governance artifact under AAC-OG-24, and updated when new attack techniques are documented in the ATLAS case study database or equivalent authoritative source.

**Verification method:** The benchmark dataset has a documented adversarial component, a versioned construction record, and an independent review sign-off. A benchmark without adversarial examples does not satisfy AAC-TB-29 for systems operating in adversarial environments.

---

## [RS] Resiliency — Governance Declarations

### AAC-RS-36 — External Dependency Resilience {#aac-rs-36}

*Retained from v1.3 (merged RS-36 + RS-37).*

**Declaration requirement:** Every external service dependency has a declared circuit breaker configuration — failure detection threshold, fast-fail behavior, recovery test interval — and a graceful degradation response for when the circuit is open. Asynchronous operations retry with exponential backoff; after a declared retry limit, failed operations land in a dead-letter queue for review rather than being silently dropped. A downstream outage degrades one capability, not the system.

**Verification method:** Circuit breaker configurations exist for every declared external dependency. Dead-letter queue monitoring is active and tested.

---

### AAC-RS-40 — Model Artifact Recovery {#aac-rs-40}

*New in v2.0. Promotes from enhancements register. Closes ATLAS AML.T0031/T0032 partial coverage.*

**Declaration requirement:** Every deployed model artifact — weights, fine-tuned adapters, embedding indices, and retrieval stores — is versioned and backed up at a declared cadence. A rollback path to a prior known-good artifact exists and has been tested before the model is promoted to production. Recovery time and recovery point objectives are declared in the Implementation Profile. Model artifact backup is a governance requirement under AAC-OG-24, not an engineering convenience.

**Verification method:** Every model in production has a documented backup cadence, a tested rollback procedure, and declared RTO/RPO values. A model without a tested rollback path is not cleared for production.

---

## [DP] Data & Privacy — Governance Declarations

### AAC-DP-06 — Collect the Minimum, Protect the Maximum {#aac-dp-06}

*Retained from v1.3.*

**Declaration requirement:** Only data the system needs to function is stored. Identity verification documents stay with the verification provider — the system stores a status flag, not the document. Payment credentials stay with the processor. Location precision degrades for display until context requires specificity. The data inventory is a governance artifact — what is collected, why, and where it lives.

**Verification method:** The data inventory exists as a versioned governance artifact. Every stored data element has a documented functional justification. Undocumented data elements are compliance failures.

---

### AAC-DP-08 — Encrypt at Rest, Encrypt in Transit, No Exceptions {#aac-dp-08}

*Retained from v1.3. Maintained as Tier 2 — startup verification invariant, not configuration item.*

**Declaration requirement:** Transport-layer encryption on all connections. Storage encryption on all data stores. This is table stakes for any system handling personal or financial data — trivial to implement from the start and costly to retrofit. Compliance is verified at system initialization, not assumed from configuration.

**Verification method:** Startup validation confirms encryption on all declared connections and data stores. An unencrypted connection or unencrypted data store detected at startup halts initialization.

---

## [ZT] Zero-Trust Security — Governance Declaration

### AAC-ZT-66 — Short-Lived Credentials, Rotated Automatically {#aac-zt-66}

*Retained from v1.3.*

**Declaration requirement:** No long-lived API keys, no static secrets in configuration, no hardcoded tokens. Services authenticate via temporary credentials. Third-party API keys are stored in a secrets management service with automatic rotation. If a credential is compromised, its blast radius is bounded by its time-to-live. Credential TTL values are declared as governance artifacts.

**Verification method:** A credential audit finds zero long-lived static secrets in configuration, code repositories, or environment variables.

---

## [TB] Testability — Governance Declaration

### AAC-TB-29 — Regression Guardrails on Automated Agents {#aac-tb-29}

*Retained from v1.3. Strengthened by AAC-AO-59 (adversarial benchmark requirement).*

**Declaration requirement:** Every automated agent maintains a benchmark dataset of known inputs and expected outputs, including adversarially constructed examples per AAC-AO-59. Before any model update or logic change deploys, the agent runs against the benchmark and must meet or exceed the prior accuracy threshold. An agent that produces anomalous outputs against the benchmark does not deploy.

**Verification method:** CI/CD pipeline enforces benchmark execution as a mandatory gate before any agent deployment. A deployment without a passing benchmark run is blocked.

---

## [AI] Intelligent Automation — Governance Declaration

### AAC-AI-13 — Human Trust Calibration {#aac-ai-13}

*Retained from v1.3. Amended: confidence tolerance threshold requirement added.*

**Declaration requirement:** Confidence communicated to humans must reflect actual system certainty. Autonomous systems must not present outputs with false precision — suppressing uncertainty to appear authoritative or framing probabilistic outputs as determinate facts. The confidence signal displayed to a human must not exceed the system's internally computed confidence score by more than a declared tolerance threshold specified in the Implementation Profile. Over-reliance induced by false confidence is a system design failure, not a user error.

**Verification method:** A sample of displayed confidence scores is compared against internal scores. Any systematic upward bias exceeding the declared tolerance is a compliance failure.

---

## [SM] Self-Maintenance — Governance Declaration

### AAC-SM-46 — Data Follows a Tiered Lifecycle {#aac-sm-46}

*Retained from v1.3.*

**Declaration requirement:** Data lifecycle tiers — hot, warm, and cold — are declared with transition cadences appropriate to the system's regulatory context. Example: hot tier (active data, primary database, 90 days), warm tier (completed records, standard storage, 1 year), cold tier (archival, 7 years). Lifecycle transitions are automated. Cache layers are acceleration only — rebuildable from primary store, purged when source records change, never treated as source of truth.

**Verification method:** Lifecycle tier declarations exist as governance artifacts. Automated transition jobs are monitored and their failure is immediately detectable.

---

# TIER 3 — COVENANT GUIDANCE

**Implementation patterns that support the governance control plane. These are engineering practices that matter for the system's integrity, performance, and maintainability. They are not enforced per-action by the control plane, but their absence creates conditions that make Tier 1 and Tier 2 compliance harder to sustain. Each includes a note on its governance relevance.**

---

## [AE] Architecture & Engineering

### AAC-AE-01 — Ephemeral Compute, Persistent State {#aac-ae-01}
Compute is ephemeral; state is not. Default to event-driven, serverless compute for stateless workloads; use container-based compute only for long-running processes. No session state lives in application logic — all state lives in the database, cache layer, or object storage. Any compute instance must be replaceable without loss of context.
*Governance relevance: Stateless compute prevents governance state from being embedded in transient processes that cannot be audited or inspected by the control plane.*

### AAC-AE-02 — Event-Driven Service Boundaries {#aac-ae-02}
No direct data queries across service boundaries. Services communicate through an asynchronous event bus. This keeps components independently deployable and testable.
*Governance relevance: Event-driven boundaries make agent interactions observable and interceptable by the governance control plane.*

### AAC-AE-05 — Infrastructure as Code from Day One {#aac-ae-05}
Every infrastructure resource is defined in version-controlled configuration. No manually provisioned resources. Environment replication is a single command.
*Governance relevance: IaC makes the governed environment reproducible and auditable. Manual provisioning creates ungoverned infrastructure that the control plane cannot account for.*

### AAC-AE-06 — Single Resolution Path, Explicit Failure States {#aac-ae-06}
Every workflow has exactly one deterministic path forward. Silent failures and unhandled edge cases are design defects. Every failure mode is anticipated, handled explicitly, and surfaced with enough context for recovery. An agent that fails silently propagates bad state; an agent that fails explicitly enables recovery.
*Governance relevance: Explicit failure states are the precondition for DA-61's liveness guarantee. A system with unhandled failures cannot guarantee resolution.*

---

## [TB] Testability

### AAC-TB-26 — Every Component Is Independently Testable {#aac-tb-26}
Each service has a clear input/output contract testable in isolation. If you cannot write a test without bootstrapping three other services, the boundary is drawn wrong.
*Governance relevance: Independent testability makes governance control verification tractable. A component that cannot be tested in isolation cannot have its governance compliance verified.*

### AAC-TB-27 — Mock Boundaries, Not Internals {#aac-tb-27}
Every third-party integration is accessed through an adapter layer. External dependencies get mock implementations from the start. The full test suite runs without hitting external APIs.
*Governance relevance: Adapter layers are the natural enforcement point for ZT-77 (supply chain integrity) and ZT-71 (hostile input validation) in test environments.*

### AAC-TB-28 — Testable in Production, Not Just in Staging {#aac-tb-28}
Design for observability that validates behavior in the live environment. Feature flags on every new capability. Synthetic transactions exercise the full flow on production infrastructure without generating real events.
*Governance relevance: Production observability supports OG-25 (policy enforcement integrity) continuous validation in the environment that matters.*

---

## [AP] API Design & Extensibility

### AAC-AP-30 — API-First, UI-Second {#aac-ap-30}
Every capability is exposed as a versioned API before any client consumes it. No business logic lives in the client.
*Governance relevance: API-first makes agent action surfaces auditable and enumerable by the governance control plane.*

### AAC-AP-31 — Version from Day One, Deprecate Gracefully {#aac-ap-31}
All endpoints are versioned. Breaking changes ship alongside prior versions with a defined deprecation window.
*Governance relevance: API versioning enables governance artifact updates to remain synchronized with the interfaces they govern.*

### AAC-AP-32 — Design Contracts Before Implementations {#aac-ap-32}
Each service's API contract — endpoints, schemas, error codes — is defined in a formal specification before implementation code is written.
*Governance relevance: Contract-first design makes the governance control plane's policy surface definable before implementation begins.*

---

## [LL] Low Latency

### AAC-LL-40 — Cache at the Right Layer, Invalidate Deliberately {#aac-ll-40}
Three cache tiers with explicit invalidation triggers. Stale data is worse than slow data in autonomous systems.
*Governance relevance: Cache staleness can produce governance decisions based on outdated state. Explicit invalidation ensures the control plane acts on current data.*

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

Control identifiers are stable within a major version. v2.0 identifiers are forward-compatible with v1.3 references — every v1.3 control that survives into v2.0 retains its original identifier.

**Control identifiers are stable references for use in:**

- Governance control plane policy configurations (OPA/Rego bundles, gRPC policy services)
- Implementation tickets and developer acceptance criteria
- Automated policy gates in CI/CD pipelines
- Compliance mapping and audit evidence packages
- Design review checklists and architecture decision records

---

## Citation

> Thakuri, R. (2026). *The Autonomous Agentic Covenant: A Governance Control Plane Specification for Autonomous and AI-Driven Systems* (Version 2.0). Apache License 2.0.

> Version 2.0 · April 2026 · 73 principles · Three enforcement tiers · 14 domains · 81 control identifiers.

> Evolved from: Thakuri, R. (2026). *The Autonomous Agentic Covenant* (Version 1.3). Apache 2.0. Version 1.3 remains the reference for the framework's ethical philosophy and governance vision.
