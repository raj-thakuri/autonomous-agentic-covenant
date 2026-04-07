# The Autonomous Agentic Covenant (AAC)

**A Governance Framework for Autonomous and AI-Driven Systems**

Version 1.3 · April 2026 · Prepared by Raj Thakuri

**69 Principles + 9 Foundational Directives · 11 Domains · 78 Control Identifiers**

---

## License & Attribution

This work is licensed under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). You are free to share and adapt this material for any purpose, including commercially, provided you give appropriate credit.

**Attribution format:**
> Thakuri, R. (2026). *The Autonomous Agentic Covenant: A Governance Framework for Autonomous and AI-Driven Systems* (Version 1.3). CC BY 4.0. https://creativecommons.org/licenses/by/4.0/

---

## How to Use This Document

Each principle carries a structured Control Identifier using the format `AAC-[DOMAIN]-[NUMBER]`. These identifiers are stable references for use in design reviews, implementation tickets, audit evidence, compliance mappings, and automated policy checks.

**Control ID Format:** `AAC-[DOMAIN]-[NN]`

**Example:** `AAC-ZT-64` = Autonomous Agentic Covenant · Zero-Trust domain · Control 64

---

## Domain Index

| Control IDs | Domain | Scope | Principles |
|---|---|---|---|
| AAC-DNH-0–0h | [Do No Harm](#do-no-harm) | Foundational — governs all other principles | 9 directives |
| AAC-AE-01–06 | [Architecture & Engineering](#architecture--engineering) | Structural decisions for scalable, maintainable systems | 4 |
| AAC-TB-26–29 | [Testability](#testability) | Isolation, mocking, production verification, AI regression | 4 |
| AAC-AP-30–32 | [API Design & Extensibility](#api-design--extensibility) | Contracts, versioning, future integration readiness | 3 |
| AAC-LL-40–42 | [Low Latency](#low-latency) | Caching strategy, async processing, write-time computation | 3 |
| AAC-DP-06–09 | [Data & Privacy](#data--privacy) | Data collection, protection, and lifecycle governance | 4 |
| AAC-AI-10–13 | [AI & Intelligent Automation](#ai--intelligent-automation) | Behavioral guardrails for automated decision systems | 4 |
| AAC-TS-13–17 | [Trust & Safety](#trust--safety) | Trust provenance, graduation, accountability, system-level fairness | 4 |
| AAC-OG-23–25 | [Operational Governance](#operational-governance) | Capability scope justification, governance artifact standards, policy enforcement | 3 |
| AAC-RS-34–39 | [Resiliency](#resiliency) | Fault tolerance, idempotency, data durability, system safe mode | 5 |
| AAC-SM-43–46 | [Self-Maintenance](#self-maintenance) | Automated cleanup, lifecycle management, hygiene | 3 |
| AAC-AO-48–58 | [Autonomous Operations](#autonomous-operations) | Progressive autonomy, trust tiers, cross-agent isolation, escalation, feedback loop, resource governance | 9 |
| AAC-DA-59–63 | [Decision Arbitration](#decision-arbitration) | Harm classification, deterministic resolution, liveness guarantee, confidence enforcement, centralized boundary | 5 |
| AAC-ZT-64–75 | [Zero-Trust Security](#zero-trust-security) | Continuous verification, least privilege, breach containment, instruction isolation | 10 |

---

## [DNH] Do No Harm

*Foundational — this principle supersedes all others. When any design decision, automated behavior, business rule, or operational choice conflicts with these directives, the Do No Harm directive wins.*

> **Governance Note:** AAC-DNH controls operate as override constraints. Any principle in any other domain that would produce an outcome violating AAC-DNH-0 is automatically subordinated. This is not a priority ordering — it is an architectural invariant. When tradeoffs between harm categories are unavoidable, the system must resolve them through a defined harm classification hierarchy. The runtime arbitration mechanism is the Decision Arbitration domain, beginning at [AAC-DA-59](#aac-da-59).

### AAC-DNH-0 — Root Principle {#aac-dnh-0}

The platform must not cause harm to its users, their property, their data, their finances, or their trust. This is the root principle. Everything below elaborates on what 'do no harm' means operationally across the specific dimensions of risk a platform creates.

### AAC-DNH-0a — Financial Harm {#aac-dnh-0a}

Never hold, lose, or misallocate user money. Payment captures, deposit holds, payouts, and refunds must be provably correct at every step. If the system is uncertain about a financial state, it freezes the action and alerts rather than guessing. An incorrect payout is not a bug to fix in the next sprint; it is a harm to remediate immediately. The user never absorbs the cost of a platform failure.

### AAC-DNH-0b — Property Harm {#aac-dnh-0b}

Protect the physical or digital assets users entrust to the platform. Every design decision that touches an asset's lifecycle — identity verification, condition documentation, insurance coverage, deposit holds, dispute resolution — exists to honor the promise of safeguarding. If the platform cannot adequately protect an asset in a given transaction, the transaction should not proceed.

### AAC-DNH-0c — Data Harm {#aac-dnh-0c}

Never expose, leak, or misuse personal information. Users provide identity documents, financial credentials, location data, transaction history, and communication records. Any exposure of this data — through a breach, a logging mistake, or a careless model training decision — is a harm. Security controls are the enforcement mechanism, but this principle states the why: because data exposure causes real harm to real people, not because compliance requires it. Disclosure minimization at the system boundary is governed by AAC-DP-09.

### AAC-DNH-0d — Trust Harm {#aac-dnh-0d}

Never deceive, manipulate, or create false confidence. The platform must not use dark patterns to push users toward actions they would not otherwise take. Automated recommendations must reflect genuine conditions, not platform revenue objectives disguised as user benefit. Coverage, protections, and policies must be clearly communicated — what is covered, what is not, and what the recourse process looks like.

### AAC-DNH-0e — Algorithmic Harm {#aac-dnh-0e}

Automated agents must not produce biased, discriminatory, or systematically unfair outcomes. Pricing models must not systematically disadvantage certain geographies or demographics. Scoring systems must not penalize users for characteristics correlated with protected classes. Detection agents must not disproportionately flag users based on patterns that proxy for race, age, or socioeconomic status. Agents are audited against fairness metrics as part of regression testing. When bias is detected, the agent's autonomy is immediately restricted until the bias is corrected.

### AAC-DNH-0f — Community Harm {#aac-dnh-0f}

The platform must not degrade the communities it operates in. If the platform enables behaviors that harm the local environment — commercial-scale operations masquerading as peer activity, facilitation of unsafe or regulated transactions, or externalities imposed on third parties — those are platform-attributable harms. Category restrictions, transaction velocity limits, and prohibited item or activity policies exist to prevent the platform from becoming a vector for community-level negative externalities.

### AAC-DNH-0g — Harm of Inaction {#aac-dnh-0g}

Failing to act when the system can prevent foreseeable harm is itself a harm. If available evidence clearly indicates a dangerous outcome and the system proceeds anyway, it shares liability for any resulting harm. Automated agents are not just operational efficiency tools — they are the platform's duty-of-care infrastructure.

### AAC-DNH-0h — Exploitation and Abuse {#aac-dnh-0h}

The platform must actively defend against users who weaponize its systems against other users or against the platform itself. The platform has a duty to detect, prevent, and respond to exploitation patterns — not just reactively after harm occurs, but proactively through system design. This means velocity limits on sensitive actions, behavioral pattern detection, cross-account correlation, and graduated enforcement: warning, then restriction of specific capabilities, then suspension, then permanent ban. Exploitation that succeeds erodes trust for every honest user on the platform.

---

## [AE] Architecture & Engineering

*Structural decisions for scalable, maintainable systems.*

### AAC-AE-01 — Ephemeral Compute, Persistent State {#aac-ae-01}

Compute is ephemeral; state is not. Default to event-driven, serverless compute for stateless workloads; use container-based compute only for long-running processes such as persistent connections or model inference. No session state lives in application logic — all state lives in the database, cache layer, or object storage. Any compute instance must be replaceable without loss of context.

### AAC-AE-02 — Event-Driven Service Boundaries {#aac-ae-02}

No direct database queries across service boundaries. Services communicate through an asynchronous event bus. This keeps components independently deployable and testable — critical for sequential development by small teams.

### AAC-AE-05 — Infrastructure as Code from Day One {#aac-ae-05}

Every infrastructure resource is defined in version-controlled configuration. No manually provisioned resources. When the environment needs replication — staging, disaster recovery, multi-region — it should be a single command.

### AAC-AE-06 — Single Resolution Path, Explicit Failure States {#aac-ae-06}

Every workflow — human-facing or agent-to-agent — has exactly one deterministic path forward. Ambiguous branching, silent failures, and unhandled edge cases are design defects. Every failure mode is anticipated, handled explicitly, and surfaced with enough context for the receiving party — human or agent — to understand what failed and what recovery is available. A dead end is never an acceptable system state. An agent that fails silently propagates bad state; an agent that fails explicitly enables recovery.

---

## [TB] Testability

*Isolation, mocking, production verification, and AI regression.*

### AAC-TB-26 — Every Component Is Independently Testable {#aac-tb-26}

Each service must have a clear input/output contract that can be tested in isolation without standing up the full platform. Unit tests validate internal logic, integration tests validate the contract between two services, and end-to-end tests validate the critical transaction path. If you cannot write a test for a component without bootstrapping three others, the boundary is drawn wrong.

### AAC-TB-27 — Mock Boundaries, Not Internals {#aac-tb-27}

Every third-party integration is accessed through an adapter layer with a defined interface. External dependencies — payment processors, identity verification providers, AI model APIs — get a mock or stub implementation from the start. The full test suite runs without hitting a single external API.

### AAC-TB-28 — Testable in Production, Not Just in Staging {#aac-tb-28}

Design for observability that validates behavior in the live environment. Feature flags on every new capability for dark deployment and selective enablement. Synthetic transactions that exercise the full flow on production infrastructure without generating real financial events.

### AAC-TB-29 — Regression Guardrails on Automated Agents {#aac-tb-29}

Every automated agent maintains a benchmark dataset of known inputs and expected outputs. Before any model update or logic change deploys, the agent runs against the benchmark and must meet or exceed the prior accuracy threshold. An agent that suddenly produces anomalous outputs should be caught before it reaches a user.

---

## [AP] API Design & Extensibility

*Contracts, versioning, and future integration readiness.*

### AAC-AP-30 — API-First, UI-Second {#aac-ap-30}

Every capability is exposed as a versioned API before any client consumes it. Frontend applications are clients of the API, not the inverse. No business logic lives in the client — the API is the product, the interface is a presentation layer.

### AAC-AP-31 — Version from Day One, Deprecate Gracefully {#aac-ap-31}

All API endpoints are versioned. When a breaking change is needed, the new version ships alongside the old one with a defined deprecation window. This costs nothing to implement at the start and prevents forced migrations when multiple clients cannot update simultaneously.

### AAC-AP-32 — Design Contracts Before Implementations {#aac-ap-32}

Each service's API contract — endpoints, request/response schemas, error codes, rate limits — is defined in a formal specification before implementation code is written. Both producer and consumer sides build in parallel against the contract.

---

## [LL] Low Latency

*Caching strategy, async processing, and write-time computation.*

### AAC-LL-40 — Cache at the Right Layer, Invalidate Deliberately {#aac-ll-40}

Three cache tiers: edge cache for static assets (TTL hours), application cache for computed results (TTL minutes), and in-process cache for reference data (TTL on deploy). Each tier has explicit invalidation triggers. Stale data is worse than slow data in a transactional platform.

### AAC-LL-41 — Async Everything That Is Not User-Blocking {#aac-ll-41}

Media processing, notification dispatch, automated agent calls, audit logging, and analytics events all fire asynchronously via the event bus. The user's request-response cycle never waits for a thumbnail to generate or an email to send.

### AAC-LL-42 — Expensive Derived Data Is Pre-Computed at Write Time {#aac-ll-42}

Query performance must not depend on runtime computation of data that could have been derived and stored at write time. Any attribute that is expensive to calculate, frequently queried, or required for sorting and filtering — proximity scores, relevance rankings, aggregate metrics, classification outputs — is computed when the underlying data changes, not when it is requested. Read paths are fast because write paths do the work. This is invisible at small scale and becomes the difference between a responsive system and an unusable one at production volume.

---

## [DP] Data & Privacy

*Data collection, protection, and lifecycle governance.*

### AAC-DP-06 — Collect the Minimum, Protect the Maximum {#aac-dp-06}

Only store data the platform needs to function. Identity verification documents stay with the third-party verification provider — the platform stores a status flag, not the documents. Payment credentials stay with the payment processor. Location precision degrades for display until context requires specificity.

### AAC-DP-07 — Audit Everything, Explain Anything {#aac-dp-07}

Every automated decision, every financial transaction, every dispute resolution action gets an immutable audit log entry. If a user asks why a decision was made, the reasoning chain must be reconstructable from the log. Audit records must capture not just the outcome but the decision ownership chain: the originating agent, any contributing agents, the arbitration path taken, and the confidence and reversibility scores at the time of execution. This serves debugging, compliance, incident response, and legal defensibility simultaneously. An outcome log records what happened; a decision log records why. This principle requires the latter.

### AAC-DP-08 — Encrypt at Rest, Encrypt in Transit, No Exceptions {#aac-dp-08}

Transport-layer encryption on all connections. Storage encryption on all data stores. This is table stakes for any platform handling personal or financial data, and trivial to implement from the start but painful to retrofit.

### AAC-DP-09 — Least Disclosure {#aac-dp-09}

Authorization governs who may access a resource. Least Disclosure governs how much of it they receive. Systems return only the fields, records, and attributes required to fulfill the specific task — nothing more. The default for every data design decision is omission; inclusion requires justification against the task. This principle operates at the response boundary and is distinct from AAC-ZT-64 (identity-level access) and AAC-DP-06 (collection and storage).

---

## [AI] AI & Intelligent Automation

*Behavioral guardrails for automated decision systems.*

### AAC-AI-10 — Confidence Thresholds and Graceful Degradation {#aac-ai-10}

Every agent has a defined confidence threshold below which it escalates rather than acts. Below threshold, it defers, restricts, or requests confirmation — it does not guess. When automation fails entirely, the system degrades to a functional fallback, never a dead end.

### AAC-AI-11 — Log Decisions, Not Just Outcomes {#aac-ai-11}

Automated agents log their reasoning chain, not just the final action. An outcome is 'priced at $35/day.' A decision log includes: market value, category benchmark, comparable items, utilization rate, demand index. The second form enables debugging, retraining, and explainability.

### AAC-AI-12 — Human Override Always Available {#aac-ai-12}

Every automated action has a manual override path. Autonomy means making human intervention the exception — not eliminating it. Users and operators can inspect, challenge, and override any agent decision. Where the stakes are high, override paths are surfaced proactively, not buried.

### AAC-AI-13 — Human Trust Calibration {#aac-ai-13}

Confidence communicated to humans must reflect actual system certainty. Autonomous systems must not present outputs, recommendations, or decisions with false precision — suppressing uncertainty to appear authoritative, or framing probabilistic outputs as determinate facts. Over-reliance induced by false confidence is a system design failure, not a user error. Confidence signals are surfaced honestly, scaled to the stakes of the action, and paired with escalation and override paths that allow humans to exercise meaningful judgment. The goal is appropriate trust — neither blind deference nor reflexive skepticism.

---

## [TS] Trust & Safety

*Trust provenance, graduation, accountability, and system-level fairness.*

### AAC-TS-13 — Trust Is Bounded by Verified Provenance {#aac-ts-13}

Trust claims do not travel. Identity assertions, capability declarations, and delegated permissions from agents, orchestrators, or external systems are re-validated at each trust boundary — never inherited transitively from the calling context. A compromised upstream agent cannot propagate elevated trust downstream. This principle governs the philosophy of trust origin; AAC-ZT-64 and AAC-AO-54 govern the enforcement mechanisms.

### AAC-TS-14 — Trust Is Graduated, Not Granted {#aac-ts-14}

Autonomous systems do not begin with trust — they earn it. Agents start at minimum viable authority and advance only through demonstrated accuracy, behavioral consistency, and explicit governance approval. Graduation criteria are defined and versioned before deployment. Promotion is deliberate; demotion is automatic. This asymmetric ratchet ensures trust expands carefully and contracts fast. AAC-AO-52 and AAC-AO-53 provide the operational implementation.

### AAC-TS-16 — Evidence Before Adjudication {#aac-ts-16}

No dispute resolution action is taken without evidence. Condition documentation, transaction terms, and communication logs must exist before the system attempts to resolve anything. Without it, dispute resolution is anecdotal.

### AAC-TS-17 — Fail Toward the User, Not Toward the Platform {#aac-ts-17}

When a system error affects a transaction — a payment glitch, a notification that did not send, a state machine that got stuck — the default resolution favors the user over the platform's financial interest. Absorb the cost of the error. The lifetime value of a user's trust far exceeds any single transaction's margin.

---

## [OG] Operational Governance

*Capability scope justification, governance artifact standards, and policy enforcement.*

### AAC-OG-23 — Every Capability Must Justify Its Scope {#aac-og-23}

Every capability, integration, and agent deployed in an autonomous system must justify its operational scope against measurable value delivery. Scope creep in autonomous systems is not merely a cost issue — it is a governance risk. An agent granted broader access or capability than its task requires creates unnecessary attack surface, complicates audit, and increases blast radius on failure. The default for any new capability is the narrowest scope that fulfills the requirement. Expansion requires explicit justification and review. If a capability cannot demonstrate direct value against its operational cost and risk surface, it should not exist in the system.

### AAC-OG-24 — Governance Artifacts Are First-Class System Components {#aac-og-24}

Policy documents, behavioral specifications, agent constraints, trust tier definitions, and operational boundaries are not administrative afterthoughts — they are versioned, maintained, and treated with the same rigor as code. A governance document that is out of date, ambiguous, or inconsistent with deployed behavior is a system defect. Governance artifacts are included in the CI/CD pipeline, reviewed on the same cadence as architectural decisions, and linked explicitly to the controls and agents they govern. When a system behavior changes, the governing artifact changes with it.

### AAC-OG-25 — Policy Enforcement Integrity {#aac-og-25}

Runtime system behavior must be continuously validated against declared governance artifacts. Any divergence between defined policy and observed behavior is treated as a system defect and triggers automatic restriction, rollback, or escalation.

---

## [RS] Resiliency

*Fault tolerance, idempotency, data durability, and system safe mode.*

### AAC-RS-34 — No Single Point of Failure on the Transaction Path {#aac-rs-34}

The critical flow must degrade gracefully at every step. If the notification service is down, the transaction still processes and notifications retry. If an automated pricing agent is unreachable, the manually set price is used. Every service on the critical path has a defined fallback behavior. When multiple valid actions are available, the system selects the action with the lowest combined risk — evaluated as a function of reversibility and impact. Reversibility is scored on a continuous scale from fully reversible (showing a recommendation) to fully irreversible (executing a financial transfer); impact is scored by blast radius and harm tier. When scores are equivalent, prefer the more reversible action. This replaces binary reversible/irreversible classification with a scored model that supports nuanced runtime arbitration.

### AAC-RS-35 — Idempotent Operations Everywhere {#aac-rs-35}

Every API call, event handler, and financial operation must be safely retriable without side effects. A payment webhook that fires twice does not double-charge. Idempotency keys on all financial operations; deduplication on all event consumers. For systems handling real money, this is non-negotiable.

### AAC-RS-36 — External Dependency Resilience {#aac-rs-36}

Every call to an external service is wrapped in failure-aware handling. A circuit breaker detects sustained failure, fast-fails subsequent requests with a graceful degradation response, and periodically tests for recovery — a downstream outage degrades one capability, not the platform. Asynchronous operations retry with exponential backoff on transient failures; after a defined retry limit, failed operations land in a dead-letter queue for review rather than being silently dropped.

### AAC-RS-38 — Data Durability Over Compute Availability {#aac-rs-38}

If forced to choose between 'the API is responding' and 'the data is intact,' always choose data integrity. Database replication across availability zones. Cache layers used as acceleration, never as source of truth. A platform that is down for 10 minutes is an inconvenience. A platform that lost transaction history is a trust catastrophe.

### AAC-RS-39 — System Safe Mode {#aac-rs-39}

When system-wide confidence, integrity, or dependency health degrades below defined thresholds, the platform enters a constrained operating mode in which high-risk actions are disabled, autonomy is reduced, and human oversight is elevated until stability is restored.

---

## [SM] Self-Maintenance

*Automated cleanup, lifecycle management, and hygiene.*

### AAC-SM-43 — Automated Hygiene Runs on a Defined Schedule {#aac-sm-43}

The platform runs scheduled cleanup jobs that prune, archive, and reconcile without manual intervention. These are first-class system components with their own monitoring, alerting, and audit logging. If a hygiene job fails, it is detected immediately, not when a user reports stale data.

### AAC-SM-44 — Liminal State Resolution {#aac-sm-44}

Unresolved state is a liability. Every transient state in every state machine has a maximum TTL; the cleanup process enforces it and notifies affected parties when states are terminated. Every system artifact must resolve to an active entity or be purged — orphans are logged before removal to surface the upstream condition that created them.

### AAC-SM-46 — Data Follows a Tiered Lifecycle {#aac-sm-46}

Hot tier: active transaction data in the primary database, 90 days. Warm tier: completed transactions and audit logs in standard object storage, 1 year. Cold tier: archival storage, 7 years aligned with financial record retention norms. Lifecycle transitions are automated. Cache layers are acceleration layers only — anything in cache must be rebuildable from the primary store, actively purged when source records are modified or deleted, and never treated as a source of truth.

---

## [AO] Autonomous Operations

*Progressive autonomy, coordination, trust tiers, cross-agent isolation, escalation hierarchy, feedback loop, and resource governance.*

### AAC-AO-48 — The Platform's Default State Is Self-Operating {#aac-ao-48}

Human intervention is the exception path, not the normal operating mode. Every recurring operational task — pricing adjustments, support resolution, dispute mediation, fraud screening, infrastructure scaling, data cleanup — has an automated agent or scheduled process as its primary handler. If something requires manual attention more than twice, that is a missing automation, not a workflow. All autonomous operation occurs within the bounds established by this governance framework.

### AAC-AO-49 — Agents Earn Autonomy Through Demonstrated Accuracy {#aac-ao-49}

No agent starts fully autonomous. Each launches with tight guardrails and earns wider authority only as decision accuracy is validated against real outcomes. Autonomy is a gradient, not a switch — every increment is earned, not assumed.

### AAC-AO-51 — Continuous Self-Monitoring and Adaptive Guardrails {#aac-ao-51}

Every agent monitors its own performance against defined KPIs — accuracy, resolution time, fairness metrics, override frequency. When performance degrades below threshold, the agent automatically tightens its own guardrails before any human intervention is required. The system becomes more cautious as it degrades, not less. Performance telemetry is continuous, logged, and available to the governing control plane.

### AAC-AO-52 — Agent Trust Tiers Are Explicit and Enforced {#aac-ao-52}

Every agent operates at an explicitly assigned trust tier that governs what actions it may take without human approval. Trust tiers are defined by the deploying system appropriate to its context, ranging from read-only observation through suggestion, conditional execution, autonomous operation within bounded scope, and full autonomy with mandatory audit. No agent self-assigns its trust tier. Tier assignment is a governance decision made by humans, recorded as a versioned governance artifact (AAC-OG-24), and linked to the performance thresholds and security validation criteria that justify it. This principle provides the operational scaffolding for the trust graduation model established in AAC-TS-13.

### AAC-AO-53 — Trust Tiers Adjust Dynamically on Performance Evidence {#aac-ao-53}

Agent trust tiers are not permanently assigned. Performance degradation below defined thresholds triggers automatic downgrade — the agent's permitted action scope narrows without requiring human intervention to initiate the restriction. Trust tier upgrades require affirmative governance approval: a human or governance process explicitly validates that accuracy, fairness, and behavioral consistency warrant the expanded authority. This creates an asymmetric ratchet: downgrade is automatic and immediate; upgrade is deliberate and audited. Neither direction is silent — all tier changes are logged with the evidence that triggered them.

### AAC-AO-54 — Cross-Agent Isolation — No Blind Trust Between Agents {#aac-ao-54}

Agents operating in a multi-agent system must not blindly trust the outputs, identity claims, or delegated permissions of other agents. Each agent re-validates inputs it receives from peer agents or orchestrators before acting on them. An agent receiving a task delegation does not inherit the delegating agent's trust tier, permissions, or authority scope — it operates within its own assigned tier regardless of instruction source. This closes the confused deputy attack vector in multi-agent orchestration: a compromised or manipulated upstream agent cannot escalate the downstream agent's effective permissions. Cross-agent communication is treated as an untrusted external input at the receiving boundary, subject to the same validation requirements as AAC-ZT-71.

### AAC-AO-55 — Governed Escalation Hierarchy {#aac-ao-55}

No agent is the final authority on its own decisions. Every autonomous system defines an explicit escalation hierarchy — from the acting agent, through higher-authority agents or a governing control plane, to human review — with clear criteria for when each level is invoked. Escalation is triggered by confidence failures, trust tier constraints, DA arbitration outcomes, or detected performance degradation. Each escalation hop is bounded in time; unresolved escalations do not stall — they advance. The hierarchy is versioned, audited, and treated as a governance artifact under AAC-OG-24.

### AAC-AO-56 — Governed Feedback and Learning Loop {#aac-ao-56}

Every near-miss, override, escalation, and failed decision is a signal. Autonomous systems must maintain a feedback loop in which operational outcomes systematically inform model tuning, threshold adjustment, and policy updates. Feedback ingestion is not automatic: proposed updates are validated against regression guardrails (AAC-TB-29), reviewed for bias, and approved through the same governance process that governs trust tier advancement (AAC-AO-53). The feedback loop is itself monitored for adversarial manipulation — anomalous override patterns or systematic signal injection are integrity violations, not training data.

### AAC-AO-58 — Resource Constraint and Consumption Governance {#aac-ao-58}

Agents must operate within defined resource boundaries. Every agent deployment specifies compute budgets, API quotas, memory limits, and execution time bounds appropriate to its task scope. Agents must not engage in recursive, looping, or high-velocity behaviors that exhaust these boundaries — whether through design, manipulation, or unexpected task expansion. Approaching a defined resource threshold triggers automatic degradation under AAC-AI-10: the agent reduces its operational intensity, surfaces the condition to the governing control plane, and requires explicit justification before continuing high-intensity operation. Resource limits are treated as governance constraints, not engineering targets — exceeding them without authorization is a behavioral violation, not a performance metric.

---

## [DA] Decision Arbitration

*Harm classification, deterministic runtime resolution, liveness guarantee, confidence enforcement, and centralized boundary.*

> **Note:** AAC-DA-60 scopes full arbitration to high-risk actions. Tier classification defined in AAC-DA-59 governs what constitutes high-risk. Deploying systems must declare this in their Implementation Profile.

### AAC-DA-59 — Harm Classification and Tradeoff Resolution {#aac-da-59}

The system must have a defined mechanism for resolving harm tradeoffs. Harm classification appropriate to the system's operational context must be defined before deployment, organized across three tiers of increasing severity: friction harm — transient and inconvenient, including latency, explainability gaps, and degraded experience; material harm — damaging but recoverable, including temporary financial loss, incorrect automated decisions, and asset degradation; and irreversible harm — permanent and unacceptable, including loss of life, physical safety compromise, unrecoverable financial loss, and data breach. When a tradeoff is unavoidable, the system must accept the lesser harm to prevent the greater. Tier definitions are context-specific, recorded as versioned governance artifacts before deployment, and referenced by the arbitration sequence in AAC-DA-60.

### AAC-DA-60 — Every Agent Action Passes Through a Deterministic Arbitration Layer {#aac-da-60}

Every action proposed by an agent — before execution — must be evaluated by a logically consistent arbitration layer that applies the framework's constraints in a defined sequence. The mandatory evaluation order is: (1) harm assessment against the system's defined harm tier classification (AAC-DA-59), (2) confidence check against AAC-AI-10 thresholds, (3) reversibility and risk scoring against AAC-RS-34, (4) user sovereignty and override constraints, (5) system policy constraints such as latency and cost bounds. An action may only proceed if it satisfies all layers in sequence. If any layer rejects the action, the arbitration result determines whether to defer, restrict, escalate, or apply a safe fallback — never to proceed. The arbitration layer itself is audited: every evaluation and its outcome is recorded per AAC-DP-07.

### AAC-DA-61 — Every Decision Must Resolve — Liveness Is a Safety Requirement {#aac-da-61}

Safety constraints may restrict which actions an agent may take, but they must not prevent resolution entirely. A system that cannot make forward progress under its own safety constraints has a design defect, not a safety feature. Every decision path must have a defined resolution: a maximum escalation depth, a maximum time window for synchronous resolution and a separate bound for asynchronous escalation, and an explicit fallback action that is safe by construction. Fallback actions are defined at system design time, not improvised at runtime. When the arbitration layer cannot identify a permitted action within the defined bounds, it executes the fallback, logs the deadlock condition, and escalates to human review. A decision that stalls indefinitely is a failure mode equivalent to an incorrect decision.

### AAC-DA-62 — Confidence Thresholds Are Enforced at the Arbitration Layer, Not Assumed {#aac-da-62}

Confidence threshold enforcement is not delegated to individual agent implementations. The arbitration layer independently verifies that the proposing agent's reported confidence meets the threshold defined for the action's risk and reversibility class before permitting execution. Agents may not self-certify confidence sufficiency. If an agent reports confidence above threshold but the arbitration layer cannot verify the basis for that claim, the action is treated as below-threshold. This prevents confidence inflation — an agent reporting false certainty to bypass its own guardrails — and ensures that the threshold mechanism operates as a system-level control rather than a per-agent convention.

### AAC-DA-63 — Centralized Enforcement Boundary {#aac-da-63}

The arbitration function must exist as a non-bypassable system boundary through which all executable actions pass prior to execution. This boundary is enforced at the platform level — not within individual agents — and cannot be disabled or selectively applied. Any action that bypasses this layer is considered a system integrity violation.

---

## [ZT] Zero-Trust Security

*Continuous verification, least privilege, breach containment, and instruction isolation.*

### AAC-ZT-64 — No Implicit Trust at Any Boundary {#aac-zt-64}

Every request — external or internal, user-facing or service-to-service — is authenticated and authorized independently. A valid user session does not grant blanket access to all endpoints. Being inside the network perimeter is not an authorization.

### AAC-ZT-65 — Least Privilege on Every Identity — Human, Service, and Agent {#aac-zt-65}

Compute roles are scoped to the minimum permissions each service requires. The media service can write to listing storage but cannot read audit logs. Automated agents operate under roles that grant access only to the data inputs their specification defines. No wildcard policies.

### AAC-ZT-66 — Short-Lived Credentials, Rotated Automatically {#aac-zt-66}

No long-lived API keys, no static secrets in configuration, no hardcoded tokens. Services authenticate via temporary credentials. Third-party API keys are stored in a secrets management service with automatic rotation. If a credential is compromised, its blast radius is bounded by its time-to-live.

### AAC-ZT-67 — Authenticate, Authorize, Validate — In That Order, Every Time {#aac-zt-67}

The gateway validates identity. The service layer checks whether that identity is authorized for the requested action on the requested resource. The validation layer confirms the payload is well-formed and within bounds. All three on every request. Skipping any one is a vulnerability.

### AAC-ZT-68 — Authenticated Propagation {#aac-zt-68}

Authentication does not end at the entry point — it propagates. Service-to-service calls use mutual authentication; the event bus enforces identity-based access policies so only authorized publishers emit and only authorized consumers subscribe. When a user action triggers a chain of service calls, the originating user's identity and authorization context propagates as a verified claim; downstream services re-validate authorization at each hop.

### AAC-ZT-71 — Every External Input Is Hostile Until Validated {#aac-zt-71}

User-submitted content is sanitized, validated, and constrained before storage or processing. API payloads are validated against strict schemas — unexpected fields are rejected, not ignored. Automated agents processing external inputs do so in sandboxed environments that cannot reach other services if the input is adversarial.

### AAC-ZT-72 — Network Segmentation Reflects Trust Boundaries {#aac-zt-72}

Backend services are deployed in private network segments with no direct internet access. Only the API gateway and content delivery layer have public-facing endpoints. Services handling financial data are in dedicated segments with tighter access rules. Database endpoints are never publicly accessible.

### AAC-ZT-73 — Assume Breach, Contain Blast Radius {#aac-zt-73}

Design every component as if an adjacent component has already been compromised. One service being compromised should not grant access to data in another service. An automated agent being exploited should not be able to exfiltrate data outside its authorized scope. Credential boundaries, network segmentation, and encrypted inter-service communication collectively enforce containment.

### AAC-ZT-74 — Continuous Verification, Not Point-in-Time Authentication {#aac-zt-74}

A session is not trusted indefinitely because initial authentication succeeded. Sensitive actions — changing financial details, deleting content, withdrawing funds — require step-up authentication. If behavior patterns change dramatically, anomaly detection triggers re-verification before allowing the session to continue. Trust decays with time and context changes.

### AAC-ZT-75 — Prompt and Instruction Isolation — Agent Inputs Are Never Executed Raw {#aac-zt-75}

No agent may execute raw user instructions, unverified upstream agent outputs, or content retrieved from external sources as if they were system-level directives. Natural language inputs are treated as untrusted data, not trusted instructions. System prompts and behavioral constraints are isolated from user-supplied or externally-retrieved content at the architectural level, not enforced through model-level filtering alone.

---

## Governance Statement

This document defines the governing design principles for all autonomous and AI-driven systems. These principles are platform-agnostic and applicable across serverless, container-based, and microservices architectures. They serve as the decision-making framework when design choices present competing valid options.

When domains conflict, **AAC-DNH-0 (Do No Harm)** governs. Runtime resolution of conflicts between principles is handled by the **Decision Arbitration domain (AAC-DA)**. Control identifiers are stable references for use in:

- Design review checklists and architecture decision records (ADRs)
- Implementation tickets and developer acceptance criteria
- Automated policy gates in CI/CD pipelines
- Compliance mapping and audit evidence packages
- Vendor evaluation and third-party risk assessments

---

## Citation

> Thakuri, R. (2026). *The Autonomous Agentic Covenant: A Governance Framework for Autonomous and AI-Driven Systems* (Version 1.3). Licensed under CC BY 4.0.
>
> Version 1.3 · April 2026 · 69 numbered principles + 9 foundational directives · 78 control identifiers · 11 domains.