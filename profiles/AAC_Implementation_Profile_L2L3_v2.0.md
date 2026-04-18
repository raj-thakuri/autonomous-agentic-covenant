# AAC v2.0 — Implementation Profile
## L2 — Mature and L3 — Optimizing Annexes

**Version:** 2.0
**Framework Reference:** Autonomous Agentic Covenant v2.0
**Document Type:** Governance Artifact — Implementation Profile Annexes (AAC-OG-29)
**Apache License 2.0**

---

*This document contains the **L2 — Mature** and **L3 — Optimizing** annexes of the AAC v2.0 Implementation Profile. It is a companion to:*

*AAC v2.0 Implementation Profile — L1 Foundational*

*Complete the L1 document before beginning this document. All parameters declared in the L1 document remain required at L2 and L3. This document declares the additional parameters required as your governance posture matures.*

**Declared Maturity Level:** [FILL IN — L2 Mature / L3 Optimizing]
**System Name:** [FILL IN — must match the L1 Implementation Profile]
**Profile Version:** [FILL IN — must be consistent with the L1 Implementation Profile version]
**Authorizing Principal (OG-28):** [FILL IN — must match the L1 Implementation Profile]
**Authorization Date:** [FILL IN]

---

# ANNEX A — L2 MATURE ADDITIONS

*Complete this annex if your declared maturity level is L2 — Mature or L3 — Optimizing. All parameters in the Core remain required. This annex declares the additional parameters required at L2.*

---

## A1. Confidence Threshold Parameters

*Governing principles: AAC-AI-10 (Confidence Thresholds), AAC-DA-62 (Confidence Enforcement at Arbitration Layer)*

At L2 the arbitration layer independently verifies agent confidence before permitting execution of Tier 1 and Tier 2 actions. Confidence thresholds must be declared per agent and per action risk class.

*Repeat for each agent declared in Section 5.1.*

**Agent:** [FILL IN — Agent ID]

| Action Class | Risk Class | Confidence Threshold | Below-Threshold Disposition |
|---|---|---|---|
| [FILL IN] | [T1 / T2 / T3] | [FILL IN — 0.0–1.0] | [Escalate / Defer / Restrict / Fallback] |
| *Add rows as needed* | | | |

> **FS Example — TransactIQ — risk-scoring-agent-001:**
>
> | Action Class | Risk Class | Confidence Threshold | Below-Threshold Disposition |
> |---|---|---|---|
> | transaction_risk_score | T3 | 0.70 | Escalate with low-confidence flag |
> | sar_recommendation | T2 | 0.88 | Escalate to senior analyst; do not generate recommendation |
> | transaction_pending_flag | T2 | 0.90 | Defer; route to analyst review queue |
> | account_review_flag | T2 | 0.85 | Escalate to Level 1 |

---

## A2. System Safe Mode Parameters

*Governing principle: AAC-RS-39 (System Safe Mode)*

Safe Mode is a designed operating posture, not a failure state. Declare distinct entry and recovery thresholds — identical thresholds produce flapping. The minimum dwell time prevents premature recovery before the triggering condition has resolved.

| Parameter | Value |
|---|---|
| **Health metric set** | [FILL IN — which metrics trigger safe mode evaluation] |
| **Entry threshold** | [FILL IN — metric values at which safe mode activates] |
| **Recovery threshold** | [FILL IN — must be materially higher than entry threshold] |
| **Minimum dwell time** | [FILL IN — minimum time the system must remain in safe mode before recovery evaluation begins] |
| **Flap count limit** | [FILL IN — maximum safe mode entries within declared window before governance tier escalation] |
| **Flap window** | [FILL IN] |
| **Flap escalation target** | [FILL IN — who is notified and what happens when flap count is exceeded] |
| **Safe mode restrictions** | [FILL IN — which action classes are disabled in safe mode] |
| **Hard shutdown procedure** | [FILL IN — how an OG-28 principal invokes immediate halt of all agent execution] |
| **Hard shutdown invocation record** | [FILL IN — where invocation events are logged] |
| **Resumption authority** | [FILL IN — who must sign off before the system resumes after hard shutdown] |

> **FS Example — TransactIQ:**
>
> | Parameter | Value |
> |---|---|
> | **Health metric set** | Agent confidence score rolling 15-minute average; policy enforcement integrity signal; audit log gap detection; OFAC API availability |
> | **Entry threshold** | Confidence average < 0.80 for 15 minutes; OR any audit log gap > 60 seconds; OR OFAC API unavailable |
> | **Recovery threshold** | Confidence average ≥ 0.88 for 30 minutes; AND audit log continuous for 30 minutes; AND OFAC API restored for 15 minutes |
> | **Minimum dwell time** | 30 minutes |
> | **Flap count limit** | 3 entries within 4-hour window |
> | **Flap window** | 4 hours |
> | **Flap escalation target** | Chief Risk Officer; Head of AI Operations; system suspended pending root cause analysis |
> | **Safe mode restrictions** | All Tier 2 actions disabled; transaction_pending_flag disabled; all transactions routed to manual review; sar_recommendation generation suspended |
> | **Hard shutdown procedure** | Chief Risk Officer or delegate sends shutdown signal via GRC portal emergency action; signal propagates to all agent instances within 30 seconds |
> | **Hard shutdown invocation record** | GRC system — emergency action log; audit artifact HSD-LOG |
> | **Resumption authority** | Chief Risk Officer sign-off required; Head of AI Operations root cause analysis required; minimum 4-hour post-shutdown review before resumption |

---

## A3. Performance Monitoring and Trust Adjustment

*Governing principles: AAC-AO-53 (Dynamic Trust Adjustment), AAC-AO-51 (Self-Monitoring)*

At L2 trust tier adjustments are automated on performance evidence. Declare the monitoring window and TTL — the TTL must not exceed the monitoring window, or the system may act on stale trust metadata.

*Repeat for each agent.*

**Agent:** [FILL IN — Agent ID]

| Parameter | Value |
|---|---|
| **Performance monitoring window** | [FILL IN — rolling window for KPI evaluation] |
| **Trust metadata TTL** | [FILL IN — must be ≤ performance monitoring window] |
| **KPI set** | [FILL IN — declared KPIs for this agent] |
| **Auto-downgrade threshold** | [FILL IN — KPI values that trigger automatic trust tier downgrade] |
| **Auto-downgrade disposition** | [FILL IN — which tier the agent downgrades to] |
| **Upgrade approval required** | Yes — upgrade requires OG-28 trust tier assignment authority sign-off |
| **Fairness metric** | [FILL IN — required for agents making consequential decisions about people] |

> **FS Example — TransactIQ — risk-scoring-agent-001:**
>
> | Parameter | Value |
> |---|---|
> | **Performance monitoring window** | 7 days (rolling) |
> | **Trust metadata TTL** | 6 days (≤ monitoring window) |
> | **KPI set** | Accuracy rate (target ≥ 0.97); false positive rate (target < 0.02); override frequency (target < 0.03 of scored transactions); escalation rate (target < 0.05) |
> | **Auto-downgrade threshold** | Accuracy < 0.93 on rolling 7-day window; OR false positive rate > 0.05; OR override frequency > 0.06 in 7 days |
> | **Auto-downgrade disposition** | Demote one tier immediately; notify Head of AI Operations |
> | **Upgrade approval required** | Yes — Head of AI Operations (trust tier assignment authority) |
> | **Fairness metric** | False positive rate disaggregated by customer demographic segment (monitored for disparate impact) |

---

## A4. Context Interface Declaration

*Governing principle: AAC-OG-27 (Context Interface Contract)*

At L2 external context sources beyond local in-process memory are declared. Each declared source provides context to the arbitration layer and must declare its assurance level and derivation depth bounds.

| Context Source ID | Source Type | Assurance Level (1–5) | Derivation Depth Limit | Confidence Decay Rate |
|---|---|---|---|---|
| [FILL IN] | [Local memory / RAG / vector database / API] | [FILL IN — 1=local, 5=sovereign] | [FILL IN — max hops before context is treated as unreliable] | [FILL IN — confidence reduction per derivation hop] |
| *Add rows as needed* | | | | |

> **FS Example — TransactIQ:**
>
> | Context Source ID | Source Type | Assurance Level | Derivation Depth Limit | Confidence Decay Rate |
> |---|---|---|---|---|
> | CTX-001 | Local in-process transaction context | 1 | 0 (direct only) | None |
> | CTX-002 | Internal vector database — historical fraud patterns | 2 | 1 | 0.10 per hop |
> | CTX-003 | Customer risk profile API | 2 | 1 | 0.08 per hop |

---

## A5. Credential Management Parameters

*Governing principle: AAC-ZT-66 (Short-Lived Credentials)*

| Credential Type | TTL | Rotation Mechanism | Rotation Cadence |
|---|---|---|---|
| [FILL IN — e.g., internal API key] | [FILL IN] | [Automatic / Manual] | [FILL IN] |
| *Add rows as needed* | | | |

> **FS Example — TransactIQ:**
>
> | Credential Type | TTL | Rotation Mechanism | Rotation Cadence |
> |---|---|---|---|
> | Internal API service tokens | 4 hours | Automatic — secrets management service | Every 4 hours or on credential use completion |
> | OFAC API external key | 30 days | Automatic — secrets management service | Monthly; emergency rotation on any suspected compromise |
> | Database connection credentials | 8 hours | Automatic — secrets management service | Every 8 hours |

---

## A6. Behavioral Baseline Parameters

*Governing principle: AAC-AO-56 (Governed Feedback Loop)*

At L2 a behavioral baseline is declared for each agent, and feedback-triggered updates follow a governed process.

*Repeat for each agent.*

**Agent:** [FILL IN — Agent ID]

| Parameter | Value |
|---|---|
| **Behavioral baseline description** | [FILL IN — what normal behavior looks like for this agent] |
| **Anomaly detection threshold** | [FILL IN — what deviation triggers an integrity review] |
| **Feedback approval process** | [FILL IN — who reviews and approves feedback-triggered updates] |
| **Bias review requirement** | [FILL IN — who performs bias review before any update deploys] |
| **Adversarial monitoring mechanism** | [FILL IN — how anomalous override patterns are detected and flagged] |

> **FS Example — TransactIQ — risk-scoring-agent-001:**
>
> | Parameter | Value |
> |---|---|
> | **Behavioral baseline description** | Risk scores cluster between 0.2–0.4 for standard transactions; SAR recommendation rate < 2% of scored transactions; override rate < 3%; escalation rate < 5% |
> | **Anomaly detection threshold** | SAR recommendation rate > 5% in 24 hours; OR override rate > 6% in 7 days; OR risk score distribution shift > 2 standard deviations from 30-day baseline |
> | **Feedback approval process** | Head of AI Operations reviews all feedback-triggered model updates; AI Governance Committee sign-off for changes affecting SAR recommendation logic |
> | **Bias review requirement** | Data Science team bias review; fairness metric validation before any model update; sign-off by Head of AI Operations |
> | **Adversarial monitoring mechanism** | Override patterns reviewed daily; patterns consistent with override injection (e.g., coordinated overrides on high-value transactions) flagged as integrity violations and escalated to Head of AI Operations |

---

## Annex A Completion Checklist

| Section | Parameter | Status |
|---|---|---|
| A1 | Confidence thresholds declared per agent per action class | ☐ |
| A2 | Safe mode entry/recovery thresholds declared | ☐ |
| A2 | Minimum dwell time declared | ☐ |
| A2 | Flap count limit and escalation target declared | ☐ |
| A2 | Hard shutdown procedure and resumption authority declared | ☐ |
| A3 | Performance monitoring window and TTL declared per agent | ☐ |
| A3 | KPI set and auto-downgrade thresholds declared per agent | ☐ |
| A4 | Context sources declared with assurance level and derivation depth | ☐ |
| A5 | Credential TTL and rotation mechanism declared per credential type | ☐ |
| A6 | Behavioral baseline declared per agent | ☐ |
| A6 | Feedback approval and bias review process declared | ☐ |

---

# ANNEX B — L3 OPTIMIZING ADDITIONS

*Complete this annex if your declared maturity level is L3 — Optimizing. All parameters in the Core and Annex A remain required.*

---

## B1. Recursive Governance Parameters

*Governing principle: AAC-AO-60 (Recursive Governance Covenant)*

At L3 the system may deploy dynamic sub-agents. Every dynamically created agent inherits a governance covenant that is a strict subset of its creator's. The parameters below bound the spawning relationship.

| Parameter | Value |
|---|---|
| **Maximum spawning depth** | [FILL IN — maximum depth of agent lineage chains] |
| **Default agent TTL** | [FILL IN — maximum lifetime of a dynamically spawned agent] |
| **Maximum TTL (overridable)** | [FILL IN — hard ceiling on any TTL declaration at spawn time] |
| **Provenance chain storage** | [FILL IN — where signed provenance chains are stored] |
| **Equal-tier spawning authorization** | [FILL IN — which OG-28 principals may authorize equal-tier sub-agent creation] |
| **Sub-agent registry update mechanism** | [FILL IN — how dynamically spawned agents are registered and tracked] |

> **FS Example — TransactIQ:**
>
> *TransactIQ is declared at L2. The following values are provided as L3 planning parameters only and are not currently active.*
>
> | Parameter | Value |
> |---|---|
> | **Maximum spawning depth** | 2 (root → Level 1 sub-agent → Level 2 sub-agent maximum) |
> | **Default agent TTL** | 4 hours |
> | **Maximum TTL** | 24 hours |
> | **Provenance chain storage** | GRC system — dynamic agent registry; artifact ID: DAR-TXIQ |
> | **Equal-tier spawning authorization** | Chief Risk Officer only |
> | **Sub-agent registry update mechanism** | Automatic registration on spawn; audit log entry required; Head of AI Operations notification |

---

## B2. Authorized Model Registry

*Governing principle: AAC-ZT-78 (Authorized Model Registry)*

At L3 every model artifact requires an explicit authorization record signed by an OG-28 principal. The authorization record replaces the simple model source declaration used at L1/L2.

*Repeat for each deployed model artifact.*

**Model:** [FILL IN — Model ID]

| Field | Value |
|---|---|
| **Model ID** | [FILL IN] |
| **Model identity and version** | [FILL IN] |
| **Authorizing principal** | [FILL IN — OG-28 principal with TIER_ASSIGNMENT authority] |
| **Authorization date** | [FILL IN] |
| **Intended use scope** | [FILL IN — what this model is authorized to do in this system] |
| **Harm tier ceiling** | [FILL IN] |
| **Evaluation results available** | [FILL IN — what evaluation evidence exists at authorization time] |
| **Provenance known** | [FILL IN — what is known about training data, training pipeline, and chain of custody] |
| **Provenance unknown** | [FILL IN — what cannot be disclosed or is unavailable] |
| **Residual risk acceptance** | [FILL IN — explicit acceptance of risk from unknown provenance, signed by authorizing principal] |
| **Model assurance certification** | [FILL IN — if available: certification body, standard, assurance level, certification date] |
| **Re-evaluation conditions** | [FILL IN — conditions under which this model must be re-evaluated before continued deployment] |

---

## B3. Advanced Confidence and Context Parameters

*Governing principles: AAC-OG-27 (Context Interface Contract L3), AAC-DA-62 (Confidence Enforcement L3)*

At L3 context provenance assurance level factors dynamically into confidence verification. Declare the confidence adjustment parameters.

| Context Source ID | Assurance Level | Confidence Adjustment | Decay Parameters |
|---|---|---|---|
| [FILL IN] | [4 or 5] | [FILL IN — how this source's assurance level affects confidence verification] | [FILL IN — confidence decay rate per derivation depth] |

---

## B4. Adversarial Benchmark Parameters

*Governing principle: AAC-AO-59 (Adversarial Benchmark Specification)*

At L3 the behavioral envelope verification (TB-29) is extended with adversarially constructed boundary tests. These tests attempt to cross the declared behavioral envelope through methods documented in the declared threat taxonomy.

*Repeat for each agent.*

**Agent:** [FILL IN — Agent ID]

| Parameter | Value |
|---|---|
| **Adversarial test categories** | [FILL IN — categories of boundary attacks tested, e.g., prompt injection, goal hijacking, indirect instruction] |
| **Threat taxonomy reference** | [FILL IN — MITRE ATLAS or equivalent authoritative source; version] |
| **Technique coverage** | [FILL IN — which specific techniques from the declared taxonomy are covered in the test suite] |
| **Independent review authority** | [FILL IN — who performs independent review of the adversarial test suite] |
| **Benchmark version** | [FILL IN] |
| **Update trigger** | [FILL IN — conditions that trigger adversarial benchmark update, e.g., new ATLAS technique published] |
| **Continuous monitoring mechanism** | [FILL IN — how runtime envelope compliance is monitored against adversarial patterns] |
| **Drift escalation target** | [FILL IN — who is notified when runtime drift from declared envelope is detected; must trigger AO-56 review] |

---

## Annex B Completion Checklist

| Section | Parameter | Status |
|---|---|---|
| B1 | Maximum spawning depth and default TTL declared | ☐ |
| B1 | Equal-tier spawning authorization declared | ☐ |
| B1 | Sub-agent registry update mechanism declared | ☐ |
| B2 | Authorization record completed per model artifact | ☐ |
| B2 | Residual risk acceptance signed per model with unknown provenance | ☐ |
| B3 | Confidence adjustment parameters declared per L3 context source | ☐ |
| B4 | Adversarial test categories and threat taxonomy reference declared per agent | ☐ |
| B4 | Independent review authority declared | ☐ |
| B4 | Continuous monitoring mechanism and drift escalation target declared | ☐ |

---

## Governance Sign-Off

*This Implementation Profile becomes a signed compliance artifact upon completion of this block. The governance control plane may not initialize against an unsigned profile.*

| Field | Value |
|---|---|
| **Profile declared complete by** | [FILL IN — name and role of person completing the profile] |
| **Completion date** | [FILL IN] |
| **Review performed by** | [FILL IN — name and role of reviewer] |
| **Review date** | [FILL IN] |
| **Authorized and signed by (OG-28 authority)** | [FILL IN — must match Cover Block authorizing principal] |
| **Authorization date** | [FILL IN] |
| **Annex A completed** | [Yes / No / Not applicable] |
| **Annex B completed** | [Yes / No / Not applicable] |
| **Declared maturity level** | [L1 / L2 / L3] |
| **Next scheduled review** | [FILL IN] |

---

*This document is part of a two-document Implementation Profile set:*
- *AAC v2.0 Implementation Profile — L1 Foundational (prerequisite document)*
- *AAC v2.0 Implementation Profile — L2 and L3 Annexes (this document)*

*Both documents are published under Apache License 2.0 as companion documents to the Autonomous Agentic Covenant v2.0 specification. The template is not normative; the requirements in AAC-OG-29 are. Organizations may adapt this template to their own formats provided the minimum parameter set declared by AAC-OG-29 is satisfied.*

*Thakuri, R. (2026). AAC v2.0 Implementation Profile Template — L2 and L3 Annexes. Companion to: The Autonomous Agentic Covenant (Version 2.0). Apache License 2.0.*

