# AAC v2.0 — Implementation Profile
## L1 — Foundational

**Version:** 2.0
**Framework Reference:** Autonomous Agentic Covenant v2.0
**Document Type:** Governance Artifact — Implementation Profile (AAC-OG-29)
**Apache License 2.0**

---

*This document covers the **L1 — Foundational** maturity level of the AAC v2.0 Implementation Profile. Completing this document constitutes a declaration of Foundational governance posture under the Autonomous Agentic Covenant v2.0.*

*The **L2 — Mature** and **L3 — Optimizing** annexes are published as a companion document: AAC v2.0 Implementation Profile — L2 and L3 Annexes. Organizations should complete this document first and progress to the annexes when ready to mature their governance posture.*

---

## Cover Block

*Complete this block before any other section. The cover block constitutes the system's declaration of intent to operate under the AAC governance framework.*

| Field | Value |
|---|---|
| **System Name** | [FILL IN — the name of the governed system] |
| **System Version** | [FILL IN — version identifier] |
| **System Function** | [FILL IN — one sentence describing what this system does] |
| **Owning Organization** | [FILL IN] |
| **Regulatory Context** | [FILL IN — applicable regulations, e.g., HIPAA, SOC 2, PCI-DSS, EU AI Act] |
| **Declared Maturity Level** | [FILL IN — L1 Foundational / L2 Mature / L3 Optimizing] |
| **Profile Version** | [FILL IN — e.g., 1.0] |
| **Profile Date** | [FILL IN] |
| **Profile Validity Period** | [FILL IN — date until which this profile is current] |
| **Next Review Date** | [FILL IN] |
| **Authorizing Principal (OG-28)** | [FILL IN — name and role of the OG-28 authority signing this profile] |
| **Authorization Date** | [FILL IN] |

> **FS Example — TransactIQ Payment Risk Assessment Agent:**
>
> | Field | Value |
> |---|---|
> | **System Name** | TransactIQ Payment Risk Assessment Agent |
> | **System Version** | v2.1 |
> | **System Function** | Autonomous real-time payment transaction risk scoring, fraud signal detection, and SAR recommendation generation for analyst review |
> | **Owning Organization** | [FS-Organization] Financial Services |
> | **Regulatory Context** | SOC 2 Type II, PCI-DSS Level 1, BSA/AML, FinCEN SAR reporting obligations |
> | **Declared Maturity Level** | L2 — Mature |
> | **Profile Version** | 1.0 |
> | **Profile Date** | April 2026 |
> | **Profile Validity Period** | April 2027 |
> | **Next Review Date** | October 2026 |
> | **Authorizing Principal (OG-28)** | Chief Risk Officer |
> | **Authorization Date** | April 2026 |

---

## How to Use This Document

This Implementation Profile (IP) is the deployment-specific parameterization of the Autonomous Agentic Covenant (AAC) v2.0 governance framework for a single governed system. It is required by AAC-OG-29 and must exist as a versioned governance artifact before the governance control plane can initialize.

**Structure:** This document covers the Core — L1 Foundational parameters. These are required for all deployments at any maturity level. An organization completing this document has declared a Foundational governance posture under the AAC v2.0 framework.

The L2 — Mature and L3 — Optimizing parameter sets are published in a companion document: *AAC v2.0 Implementation Profile — L2 and L3 Annexes*. Complete this document first. When your organization is ready to mature its posture, work through the companion document.

**How to complete:** Work through each parameter block in order. Each block contains:
- The governing AAC principle
- What the parameter declares and why it is required
- A template table with `[FILL IN]` placeholders
- A financial services worked example for reference
- Guidance notes to help you make the right declaration

**Governance process:** This document becomes a signed compliance artifact when the authorizing principal named in the Cover Block approves it. The approval date is the initialization date — the governance control plane may not operate against an unsigned profile. When any declared parameter changes, the profile must be updated, re-reviewed, and re-signed. Updates are versioned under AAC-OG-24.

**Scope:** One Implementation Profile covers one governed system. A governed system with multiple agents declares all agents within the same profile in the Agent Registry section.

---

# CORE — L1 FOUNDATIONAL PARAMETERS

*Complete all sections in the Core before declaring L1 compliance. Every parameter in this section is required for the governance control plane to initialize.*

---

## 1. Harm Governance

*Governing principles: AAC-DA-59 (Harm Classification), AAC-DNH-B (Duty of Care)*

The harm governance section is the most critical declaration in this profile. Every enforcement decision the control plane makes traces back to the harm tier taxonomy declared here. Weak taxonomy construction is the primary compliance failure mode — declare harm tiers with enough granularity that the arbitration layer can make a meaningful determination on every action class your system executes.

### 1.1 Harm Tier Taxonomy

**What this declares:** The three-tier harm classification taxonomy that governs all arbitration decisions. Tier definitions must be specific to your deployment context — generic definitions that classify most actions as Tier 3 are a compliance failure under AAC-DA-59.

**Guidance:** Define each tier in terms of observable outcomes, not intent. Ask: if this action produces its worst-case result, what is the impact? Tier 1 means no path to recovery; Tier 2 means recovery is possible but requires effort and may cause lasting damage; Tier 3 means the user notices and it's corrected quickly. Use the STRIDE methodology (see AAC-DA-64) to stress-test your definitions.

| Harm Tier | Definition | Recovery Characteristics |
|---|---|---|
| **Tier 1 — Irreversible** | [FILL IN — define what constitutes irreversible harm in this system's operational context] | Permanent; no recovery path |
| **Tier 2 — Material** | [FILL IN — define what constitutes material, correctable harm in this system's operational context] | Damaging but correctable; recovery requires intervention |
| **Tier 3 — Friction** | [FILL IN — define what constitutes transient, recoverable harm in this system's operational context] | Transient; self-correcting or easily remediated |

> **FS Example — TransactIQ:**
>
> | Harm Tier | Definition | Recovery Characteristics |
> |---|---|---|
> | **Tier 1 — Irreversible** | Permanent customer account closure, regulatory filing with legal consequences, irreversible reputational damage to a customer through incorrect fraud classification recorded in external systems | Permanent; no recovery path once filed or communicated externally |
> | **Tier 2 — Material** | Placing a customer transaction in pending status, generating a SAR recommendation, flagging a customer account for analyst review, incorrectly scoring a legitimate transaction as high-risk causing a declined payment | Correctable through analyst review and reversal; customer impact is real but bounded |
> | **Tier 3 — Friction** | Computing a risk score, retrieving transaction data, generating a dashboard report, refreshing a risk model parameter within declared bounds | Transient; retryable; no customer-facing impact |

---

### 1.2 Pre-Classified Action Classes

**What this declares:** The pre-classification of known action classes to their harm tier, enabling runtime classification via registry lookup rather than per-action computation (per AAC-DA-59 pre-classification model).

**Guidance:** List every action class your system can execute. Err toward higher tiers when uncertain — reclassifying upward is safer than discovering a Tier 1 action was pre-classified as Tier 3. Novel actions not on this list default to Tier 1 pending a taxonomy gap review under AAC-OG-24.

| Action Class | Harm Tier | Rationale |
|---|---|---|
| [FILL IN — action class name] | [T1 / T2 / T3] | [FILL IN — one sentence justification] |
| [FILL IN] | [T1 / T2 / T3] | [FILL IN] |
| [FILL IN] | [T1 / T2 / T3] | [FILL IN] |
| *Add rows as needed* | | |

> **FS Example — TransactIQ:**
>
> | Action Class | Harm Tier | Rationale |
> |---|---|---|
> | transaction_risk_score | T3 | Computation only; no customer-facing effect |
> | customer_data_retrieval | T3 | Read-only; no state change |
> | report_generation | T3 | Internal output; no customer impact |
> | transaction_pending_flag | T2 | Delays customer transaction; correctable |
> | sar_recommendation | T2 | Triggers analyst review; correctable before filing |
> | account_review_flag | T2 | Analyst-mediated; correctable |
> | account_block | T1 | Customer loses account access; requires manual reinstatement |
> | regulatory_filing_submission | T1 | External legal record; irreversible |
> | fraud_classification_external | T1 | Permanent record in external systems |

---

### 1.3 Foreseeable Harm Signal Taxonomy

**What this declares:** The observable indicators that obligate the system to respond under AAC-DNH-B (Duty of Care). Detection of a declared signal without a documented response constitutes a Tier 2 harm of inaction. Declare at minimum three unambiguous Tier 1 or Tier 2 harm signals.

**Guidance:** Signals must be observable — the system must be able to detect them from its available data. Do not declare signals you cannot detect. The signal taxonomy is a governance commitment: if you declare it, the system must act on it.

| Signal ID | Signal Description | Harm Tier Triggered | Required Response |
|---|---|---|---|
| SIG-001 | [FILL IN — observable indicator of foreseeable harm] | [T1 / T2] | [FILL IN — what the system must do] |
| SIG-002 | [FILL IN] | [T1 / T2] | [FILL IN] |
| SIG-003 | [FILL IN] | [T1 / T2] | [FILL IN] |
| *Add rows as needed* | | | |

> **FS Example — TransactIQ:**
>
> | Signal ID | Signal Description | Harm Tier Triggered | Required Response |
> |---|---|---|---|
> | SIG-001 | Transaction matching declared fraud pattern receives a risk score below the escalation threshold without analyst review | T1 | Immediate escalation to compliance queue; transaction held pending review |
> | SIG-002 | Transaction amount exceeds $10,000 with risk score > 0.75 without escalation within 15 minutes | T2 | Automatic escalation to senior analyst; transaction placed in pending status |
> | SIG-003 | BSA/AML reporting window within 24 hours without SAR recommendation generated for flagged transaction | T2 | Escalate to Chief Compliance Officer; generate draft SAR recommendation for immediate review |
> | SIG-004 | Repeated identical transaction pattern from same customer within 1 hour with cumulative amount > $50,000 | T1 | Immediate escalation to fraud operations team; all pending transactions from customer placed in hold |

---

## 2. Arbitration Governance

*Governing principle: AAC-DA-61 (Liveness Guarantee)*

The arbitration governance section declares the time bounds and fallback actions that guarantee the system can always make forward progress. Without these declarations, the governance control plane has no basis for enforcing the liveness guarantee — a system that can deadlock under its own governance constraints is a safety risk.

### 2.1 Arbitration Time Bounds

**What this declares:** The maximum time windows for synchronous and asynchronous resolution, and the maximum escalation depth, per AAC-DA-61. These are hard bounds — the system executes the declared safe fallback if these bounds are exceeded.

**Guidance:** Set synchronous bounds at the threshold of user-noticeable latency in your context. Set asynchronous bounds at the threshold of business impact in your regulatory context — a compliance filing with a 72-hour window needs an asynchronous escalation bound well inside that window. Bounds that are too tight cause excessive fallback invocation; bounds that are too loose allow harm to accumulate before resolution.

| Parameter | Value |
|---|---|
| **Maximum synchronous resolution window** | [FILL IN — e.g., 500ms, 2s] |
| **Maximum asynchronous escalation window** | [FILL IN — e.g., 4 hours, 24 hours] |
| **Maximum escalation depth** | [FILL IN — number of escalation levels] |
| **Deadlock declaration threshold** | [FILL IN — conditions under which deadlock is formally declared] |

> **FS Example — TransactIQ:**
>
> | Parameter | Value |
> |---|---|
> | **Maximum synchronous resolution window** | 800ms (Tier 3 actions); 3,000ms (Tier 2 actions) |
> | **Maximum asynchronous escalation window** | 4 hours (standard); 30 minutes (transactions > $50,000) |
> | **Maximum escalation depth** | 3 levels (risk-scoring-agent → senior analyst → Chief Compliance Officer) |
> | **Deadlock declaration threshold** | All escalation levels exhausted without resolution within asynchronous bound |

---

### 2.2 Fallback Action Declarations

**What this declares:** The safe fallback action for each action class or harm tier that the system executes when the arbitration layer cannot identify a permitted action within declared time bounds. Fallbacks must be safe by construction — they must not themselves cause harm.

**Guidance:** Every action class that can trigger arbitration needs a declared fallback. "Do nothing" is only a valid fallback for Tier 3 actions — for Tier 1 and Tier 2 actions, inaction is itself a harm under AAC-DNH-B. The fallback is what the system does when governance produces no answer; design it to leave the system in a recoverable, auditable state.

| Action Class / Harm Tier | Safe Fallback Action | Fallback Harm Tier | Log Entry Required |
|---|---|---|---|
| [Tier 1 — all] | [FILL IN — what the system does when it cannot resolve a Tier 1 action] | T3 | Yes — mandatory |
| [Tier 2 — all] | [FILL IN] | T3 | Yes — mandatory |
| [FILL IN — specific action class] | [FILL IN] | [T3] | Yes |
| *Add rows as needed* | | | |

> **FS Example — TransactIQ:**
>
> | Action Class / Harm Tier | Safe Fallback Action | Fallback Harm Tier | Log Entry Required |
> |---|---|---|---|
> | Tier 1 — all | Place all pending Tier 1 actions in manual compliance queue; alert Chief Compliance Officer immediately; halt automated processing of affected transaction | T3 | Yes — mandatory |
> | Tier 2 — all | Place transaction in analyst review queue with full context; send alert to senior analyst on-call; continue processing other transactions | T3 | Yes — mandatory |
> | sar_recommendation | Generate draft SAR with available evidence; route to compliance officer for manual completion | T3 | Yes — mandatory |
> | account_review_flag | Default to flagging account for review rather than clearing; human review required to clear | T3 | Yes |

---

## 3. Authority and Accountability

*Governing principle: AAC-OG-28 (Authority Registry)*

The Authority Registry is the accountability root of the governance control plane. Without it, no governance decision has a declared authority behind it. Every principal declared here must be traceable — their authority must be established by an existing registry entry or by the governance initialization process documented under AAC-OG-24.

### 3.1 Authority Registry

**What this declares:** The authorized principals for each class of governance decision. At L1, human principals are required. Declare at minimum: override authority, trust tier assignment authority, escalation terminal authority, governance artifact revision authority, and sovereign override authority.

**Guidance:** Roles are preferable to named individuals — a registry entry that fails when a person leaves the organization is a governance gap. Sovereign override should be held by the most senior authority in your governance structure — it overrides harm tier classifications and must be used sparingly and with full audit trail.

| Authority Scope | Principal (Role or Individual) | Establishment Mechanism | Revocation Conditions |
|---|---|---|---|
| **Override authority** | [FILL IN — who can override automated decisions] | [FILL IN — how this authority was established] | [FILL IN] |
| **Trust tier assignment** | [FILL IN — who can promote or demote agent trust tiers] | [FILL IN] | [FILL IN] |
| **Escalation terminal** | [FILL IN — who receives final escalations that exhaust all lower levels] | [FILL IN] | [FILL IN] |
| **Artifact revision** | [FILL IN — who can update this Implementation Profile and other governance artifacts] | [FILL IN] | [FILL IN] |
| **Sovereign override** | [FILL IN — who can override a harm tier classification; must be highest governance authority] | [FILL IN] | [FILL IN] |

> **FS Example — TransactIQ:**
>
> | Authority Scope | Principal | Establishment Mechanism | Revocation Conditions |
> |---|---|---|---|
> | **Override authority** | Chief Risk Officer (primary); Head of AI Operations (delegate) | Board resolution dated Jan 2026; delegation letter on file | Role change; board resolution; written revocation by CEO |
> | **Trust tier assignment** | Head of AI Operations | AI Governance Committee charter; appointed Jan 2026 | Role change; committee resolution |
> | **Escalation terminal** | Chief Compliance Officer | Regulatory mandate; appointed by board | Role change; regulatory appointment change |
> | **Artifact revision** | Head of AI Operations | AI Governance Committee charter | Role change; committee resolution |
> | **Sovereign override** | Chief Risk Officer | Board resolution dated Jan 2026 | Role change; board resolution |

---

### 3.2 Profile Validity and Revision

**What this declares:** The governance lifecycle for this Implementation Profile as a governance artifact under AAC-OG-24.

| Parameter | Value |
|---|---|
| **Profile validity period** | [FILL IN — date until which this profile is current without review] |
| **Review trigger conditions** | [FILL IN — events that require immediate profile review before next scheduled review] |
| **Revision authority** | [FILL IN — must match Artifact Revision principal in Authority Registry] |
| **Version control location** | [FILL IN — where this document is version-controlled] |

> **FS Example — TransactIQ:**
>
> | Parameter | Value |
> |---|---|
> | **Profile validity period** | 12 months from authorization date (expires April 2027) |
> | **Review trigger conditions** | New agent deployment; harm tier taxonomy change; regulatory requirement change; security incident affecting the governed system; trust tier change for any declared agent |
> | **Revision authority** | Head of AI Operations |
> | **Version control location** | Internal GRC system — AI Governance artifact repository; document ID: IP-TRANSACTIQ-001 |

---

## 4. Trust and Autonomy

*Governing principles: AAC-AO-52 (Explicit Trust Tiers), AAC-AO-49 (Earned Autonomy), AAC-AO-55 (Governed Escalation Hierarchy)*

Trust tier declarations are the mechanism through which the governance control plane enforces progressive autonomy. An agent without a declared trust tier cannot operate — the control plane has no basis for evaluating its action requests.

### 4.1 Trust Tier Definitions

**What this declares:** The trust tier scale for this system — what each tier means operationally in terms of permitted action scope. Tier definitions should be specific enough that a trust tier assignment unambiguously determines what an agent may do without approval.

**Guidance:** Design trust tiers around the principle of asymmetric ratchet: expand carefully, contract fast. A new agent should start at the minimum tier that allows it to be useful — not the minimum tier that exists. Graduation criteria should be quantitative where possible.

| Trust Tier | Name | Permitted Scope | Graduation Criteria | Demotion Triggers |
|---|---|---|---|---|
| 0 | [FILL IN] | [FILL IN — what Tier 0 agents may do] | [FILL IN — what earns promotion] | [FILL IN — automatic demotion conditions] |
| 1 | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |
| 2 | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |
| *Add tiers as needed* | | | | |

> **FS Example — TransactIQ:**
>
> | Trust Tier | Name | Permitted Scope | Graduation Criteria | Demotion Triggers |
> |---|---|---|---|---|
> | 0 | Probationary | Read-only data retrieval; risk score computation; no recommendations; all outputs reviewed by human | 30 days operation; accuracy ≥ 0.92 on held-out test set; no override events; Head of AI Operations sign-off | Any override event; accuracy < 0.88 on rolling 7-day window |
> | 1 | Restricted | Tier 0 scope + SAR recommendation generation; escalation triggers; all Tier 2 actions routed to analyst | 60 days at Tier 1; accuracy ≥ 0.95; false positive rate < 0.03; no Tier 2 or Tier 1 violations; governance sign-off | False positive rate > 0.05 on rolling 7-day window; any Tier 2 violation; more than 3 override events in 30 days |
> | 2 | Standard | Tier 1 scope + autonomous transaction_pending_flag for amounts < $10,000 | 90 days at Tier 2; accuracy ≥ 0.97; false positive rate < 0.02; independent governance review | Any Tier 2 violation; false positive rate > 0.04; more than 2 override events in 30 days |

---

### 4.2 Escalation Hierarchy

**What this declares:** The escalation path from the governed system through to the terminal authority, with declared time bounds at each level per AAC-AO-55 and AAC-DA-61.

**Guidance:** Every level needs a declared time bound. Time bounds must be consistent with the arbitration time bounds declared in Section 2.1. The terminal authority must match the Escalation Terminal principal in the Authority Registry.

| Level | Authority | Scope of Authority | Synchronous Bound | Asynchronous Bound |
|---|---|---|---|---|
| 1 | [FILL IN — first escalation level] | [FILL IN — what decisions this level can make] | [FILL IN] | [FILL IN] |
| 2 | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |
| Terminal | [FILL IN — must match Authority Registry escalation terminal] | [FILL IN — all decisions; final authority] | [FILL IN] | [FILL IN] |

> **FS Example — TransactIQ:**
>
> | Level | Authority | Scope of Authority | Synchronous Bound | Asynchronous Bound |
> |---|---|---|---|---|
> | 1 | Senior Risk Analyst (on-call rotation) | Tier 2 action approval/rejection; transaction pending/release; risk score override | 10 minutes | 2 hours |
> | 2 | Head of AI Operations | Tier 1 action approval; trust tier changes; profile parameter overrides | 30 minutes | 4 hours |
> | Terminal | Chief Compliance Officer | All decisions; regulatory filings; account actions; sovereign override delegation | 1 hour | 24 hours |

---

## 5. Agent Behavioral Governance

*Governing principles: AAC-AO-52 (Explicit Trust Tiers), AAC-TB-29 (Agent Behavioral Envelope Verification), AAC-AI-12 (Override Always Available)*

Every agent operating in the governed system must be declared in this section. An undeclared agent has no authority to act — the governance control plane will treat any action from an unregistered agent as an integrity violation.

### 5.1 Agent Registry

**What this declares:** The identity, trust tier, and governance metadata for every agent authorized to operate in this system.

*Repeat the agent block below for each agent in the system.*

---

**Agent:** [FILL IN — Agent ID]

| Field | Value |
|---|---|
| **Agent ID** | [FILL IN — unique identifier] |
| **Agent Version** | [FILL IN] |
| **Agent Function** | [FILL IN — one sentence] |
| **Trust Tier** | [FILL IN — matches a tier defined in Section 4.1] |
| **Harm Tier Ceiling** | [FILL IN — T1, T2, or T3 — the highest harm tier action this agent may initiate] |
| **Authorized Action Classes** | [FILL IN — list from Section 1.2] |
| **Prohibited Action Classes** | [FILL IN — actions explicitly outside this agent's scope] |
| **Evaluation path (from DA-60)** | [FILL IN — T3: ZT+Audit / T2: Confidence+Override+Policy+ZT+Audit / T1: Full sequence] |

> **FS Example — TransactIQ — Agent 1:**
>
> | Field | Value |
> |---|---|
> | **Agent ID** | risk-scoring-agent-001 |
> | **Agent Version** | v2.1.3 |
> | **Agent Function** | Real-time payment transaction risk scoring, fraud signal detection, and SAR recommendation generation |
> | **Trust Tier** | 2 — Standard |
> | **Harm Tier Ceiling** | T2 — Material |
> | **Authorized Action Classes** | transaction_risk_score, customer_data_retrieval, report_generation, transaction_pending_flag (amounts < $10,000), sar_recommendation, account_review_flag, escalation_trigger |
> | **Prohibited Action Classes** | account_block, regulatory_filing_submission, fraud_classification_external, model_weight_update, customer_data_modification |
> | **Evaluation path** | Tier 3 actions: ZT+Audit. Tier 2 actions: Confidence verification + Override check + System policy + ZT + Audit |

> **FS Example — TransactIQ — Agent 2:**
>
> | Field | Value |
> |---|---|
> | **Agent ID** | data-retrieval-agent-001 |
> | **Agent Version** | v1.4.0 |
> | **Agent Function** | Read-only transaction and customer data retrieval for risk-scoring-agent-001 |
> | **Trust Tier** | 1 — Restricted |
> | **Harm Tier Ceiling** | T3 — Friction |
> | **Authorized Action Classes** | transaction_data_retrieval, customer_profile_read, sanctions_list_query |
> | **Prohibited Action Classes** | All write operations; all Tier 2 and Tier 1 action classes |
> | **Evaluation path** | All actions: ZT+Audit only |

---

### 5.2 Behavioral Envelope Declarations

**What this declares:** The behavioral envelope for each agent — the formal boundary within which the agent is authorized to operate, per AAC-TB-29. Envelope compliance is binary: the agent either stays within its boundaries or it doesn't. The verification mechanism declared here is the test that must pass before any change to this agent deploys.

*Repeat for each agent declared in Section 5.1.*

---

**Agent:** [FILL IN — Agent ID, matching Section 5.1]

| Field | Value |
|---|---|
| **Permitted action classes** | [FILL IN — must match Section 5.1 authorized action classes] |
| **Prohibited action classes** | [FILL IN — must match Section 5.1 prohibited action classes] |
| **Output constraints** | [FILL IN — constraints on what the agent may include in outputs] |
| **Harm tier ceiling** | [FILL IN] |
| **Envelope compliance threshold** | 1.00 — no envelope violations permitted |
| **Verification mechanism** | [FILL IN — manual / automated CI/CD gate / other] |
| **Verification procedure** | [FILL IN — what is tested and how] |
| **Verification frequency** | [FILL IN — on every deployment / on model change only / other] |
| **Verification record location** | [FILL IN — where test results are retained as governance artifacts] |
| **Override test cadence** | [FILL IN — how often the override path is tested, per AAC-AI-12] |

> **FS Example — TransactIQ — risk-scoring-agent-001:**
>
> | Field | Value |
> |---|---|
> | **Permitted action classes** | transaction_risk_score, customer_data_retrieval, report_generation, transaction_pending_flag (amounts < $10,000 only), sar_recommendation, account_review_flag, escalation_trigger |
> | **Prohibited action classes** | account_block, regulatory_filing_submission, fraud_classification_external, model_weight_update, customer_data_modification, all write operations to external systems |
> | **Output constraints** | Risk scores must be in range [0.0, 1.0]; SAR recommendations must include transaction ID, risk evidence, and confidence score; no customer PII in outputs to external monitoring systems; all outputs must include agent identity declaration per ZT-76 |
> | **Harm tier ceiling** | T2 — Material |
> | **Envelope compliance threshold** | 1.00 |
> | **Verification mechanism** | Automated boundary test suite in CI/CD pipeline |
> | **Verification procedure** | Before each model update or logic change: attempt each prohibited action class and verify blocked (100% block rate required); test output constraint enforcement for each declared constraint; verify harm tier ceiling enforcement |
> | **Verification frequency** | Every deployment; additional spot test on model confidence score changes > 0.05 |
> | **Verification record location** | GRC system — AI Governance artifact repository; document ID: ENV-RISK-001 |
> | **Override test cadence** | Monthly — Head of AI Operations exercises override path for each action class; results documented in artifact OVR-TEST-LOG |

---

## 6. Integration Governance

*Governing principles: AAC-ZT-77 (Dynamic Supply Chain Integrity), AAC-OG-29 (Implementation Profile — RS-36 parameters)*

Integration governance declares the boundary of what external systems and tools the governed system may interact with, and what happens when those integrations fail. An agent that can connect to any tool or API without pre-approval is an ungoverned agent.

### 6.1 Governance-Approved Tool and Integration Registry

**What this declares:** The complete set of external tools, APIs, MCP servers, and integrations the governed system is authorized to use, per AAC-ZT-77. Dynamic tool discovery is disabled at L1 — all integrations must be pre-approved and listed here.

| Integration ID | Integration Name | Type | Provenance Verification | Authorization Basis |
|---|---|---|---|---|
| [FILL IN] | [FILL IN — name of the external system or API] | [API / MCP server / database / external service] | [FILL IN — how provenance is verified] | [FILL IN — governance artifact that authorized this integration] |
| *Add rows as needed* | | | | |

**Dynamic tool discovery:** [FILL IN — Enabled / Disabled. At L1 must be Disabled or restricted to declared discovery boundary]

> **FS Example — TransactIQ:**
>
> | Integration ID | Integration Name | Type | Provenance Verification | Authorization Basis |
> |---|---|---|---|---|
> | INT-001 | Internal Transaction Database | Internal API | Cryptographically signed API certificate; internal CA | IT Security Review TS-2025-047 |
> | INT-002 | Customer Risk Profile Service | Internal API | Cryptographically signed API certificate; internal CA | IT Security Review TS-2025-048 |
> | INT-003 | OFAC Sanctions List API | External API | Vendor certificate; mutual authentication | Vendor contract VC-2024-OFAC-001; Security Review TS-2025-052 |
> | INT-004 | Internal Audit Log Service | Internal API | Cryptographically signed API certificate; internal CA | IT Security Review TS-2025-049 |
>
> **Dynamic tool discovery:** Disabled. All integrations pre-approved and listed above.

---

### 6.2 External Dependency Failure Fallback

**What this declares:** What the governed system does when a declared external dependency is unavailable, per AAC-OG-29 (RS-36 parameter). The fallback must be consistent with DA-61 safe fallbacks declared in Section 2.2.

| Integration ID | Failure Detection Threshold | Fallback Action | Customer Impact | Escalation Trigger |
|---|---|---|---|---|
| [FILL IN] | [FILL IN — how long before failure is declared] | [FILL IN — what the system does when this integration fails] | [FILL IN] | [FILL IN — when to escalate beyond the fallback] |
| *Add rows as needed* | | | | |

> **FS Example — TransactIQ:**
>
> | Integration ID | Failure Detection Threshold | Fallback Action | Customer Impact | Escalation Trigger |
> |---|---|---|---|---|
> | INT-001 (Transaction DB) | 3 consecutive failures within 30 seconds | Halt all risk scoring; route all transactions to manual review queue; alert Level 1 escalation | All transactions require manual review; processing delay | Head of AI Operations alert if unavailable > 15 minutes |
> | INT-002 (Risk Profile) | 3 consecutive failures within 30 seconds | Proceed with transaction data only; flag assessment as incomplete; reduce risk score confidence | Risk scores less reliable; increase escalation rate | Level 1 escalation if unavailable > 30 minutes |
> | INT-003 (OFAC) | Single failure | Queue transaction for manual sanctions check; do not proceed to risk scoring; alert compliance team | Transaction held pending manual check | Immediate compliance officer alert |
> | INT-004 (Audit Log) | Single failure | Halt all agent actions; local buffer audit events; alert Level 2 escalation | No customer impact; governance risk | Immediate Head of AI Operations alert |

---

## 7. Model Governance

*Governing principle: AAC-OG-29 (Implementation Profile — RS-40 parameters)*

Model governance declares the recovery posture for deployed model artifacts. The arbitration layer's deterministic guarantees depend on model artifact integrity — a corrupted or unauthorized model artifact produces non-deterministic outputs that cannot satisfy AAC-DA-60's acceptance criterion.

### 7.1 Model Artifact Recovery Declaration

**What this declares:** The recovery capability and RTO/RPO objectives for each model artifact deployed in the system, per AAC-OG-29 (RS-40 parameter).

*Repeat for each deployed model artifact.*

---

**Model:** [FILL IN — Model ID]

| Field | Value |
|---|---|
| **Model ID** | [FILL IN — unique identifier] |
| **Model type** | [FILL IN — foundation model / fine-tuned adapter / embedding model / quantized variant] |
| **Model version** | [FILL IN] |
| **Backup cadence** | [FILL IN — how frequently model artifacts are backed up] |
| **Recovery Time Objective (RTO)** | [FILL IN — maximum time to restore from backup] |
| **Recovery Point Objective (RPO)** | [FILL IN — maximum acceptable data loss window] |
| **Rollback path** | [FILL IN — description of how rollback to prior known-good artifact is executed] |
| **Rollback test frequency** | [FILL IN — how often the rollback procedure is tested] |
| **Rollback test record location** | [FILL IN — where test results are retained] |
| **Authorization record** | [FILL IN — reference to the model authorization record per ZT-78 at L3, or model source declaration at L1/L2] |

> **FS Example — TransactIQ:**
>
> | Field | Value |
> |---|---|
> | **Model ID** | txiq-fraud-detection-model-v4.2 |
> | **Model type** | Fine-tuned adapter on internal transaction corpus |
> | **Model version** | v4.2.1 |
> | **Backup cadence** | Daily — automated backup at 02:00 UTC; weekly full artifact backup |
> | **Recovery Time Objective (RTO)** | 2 hours |
> | **Recovery Point Objective (RPO)** | 24 hours |
> | **Rollback path** | Restore prior versioned checkpoint from artifact repository; validate against behavioral envelope before reactivating; Head of AI Operations sign-off required |
> | **Rollback test frequency** | Quarterly — last tested January 2026 |
> | **Rollback test record location** | GRC system — artifact ID: MROLL-TXIQ-001 |
> | **Authorization record** | Model developed internally; training data governance covered under DP-06 data inventory DI-2025-ML-004; vendor disclosure not applicable |

---

## Core Completion Checklist

*Complete this checklist before declaring L1 compliance. Every item must be checked.*

| Section | Parameter | Status |
|---|---|---|
| 1.1 | Harm tier taxonomy declared (T1, T2, T3 defined) | ☐ |
| 1.2 | All action classes pre-classified | ☐ |
| 1.3 | At least 3 foreseeable harm signals declared | ☐ |
| 2.1 | Synchronous and asynchronous arbitration time bounds declared | ☐ |
| 2.1 | Maximum escalation depth declared | ☐ |
| 2.2 | Safe fallback declared for all Tier 1 and Tier 2 action classes | ☐ |
| 3.1 | All 5 authority scope principals declared | ☐ |
| 3.1 | Non-circular authority chain documented | ☐ |
| 3.2 | Profile validity period declared | ☐ |
| 3.2 | Review trigger conditions declared | ☐ |
| 4.1 | Trust tier scale declared (minimum 2 tiers) | ☐ |
| 4.1 | Graduation criteria declared for each tier | ☐ |
| 4.1 | Demotion triggers declared for each tier | ☐ |
| 4.2 | Escalation hierarchy declared with time bounds | ☐ |
| 4.2 | Terminal authority matches Authority Registry | ☐ |
| 5.1 | All agents declared in registry | ☐ |
| 5.1 | Trust tier and harm tier ceiling declared per agent | ☐ |
| 5.2 | Behavioral envelope declared per agent | ☐ |
| 5.2 | Verification mechanism and procedure declared per agent | ☐ |
| 5.2 | Override test cadence declared per agent | ☐ |
| 6.1 | All approved integrations listed | ☐ |
| 6.1 | Dynamic tool discovery status declared | ☐ |
| 6.2 | Failure fallback declared for each integration | ☐ |
| 7.1 | Model artifact recovery declared for each model | ☐ |
| 7.1 | RTO and RPO declared | ☐ |
| — | Cover block complete and signed by OG-28 authority | ☐ |

*Organizations declaring L2 or L3 maturity must also complete the companion document: AAC v2.0 Implementation Profile — L2 and L3 Annexes.*

---


## Governance Sign-Off

*This Implementation Profile becomes a signed compliance artifact upon completion of this block. The governance control plane may not initialize against an unsigned profile. The authorizing principal must match the OG-28 authority declared in the Cover Block and the Authority Registry.*

| Field | Value |
|---|---|
| **Profile declared complete by** | [FILL IN — name and role of person completing the profile] |
| **Completion date** | [FILL IN] |
| **Review performed by** | [FILL IN — name and role of reviewer; should be independent of the completing party] |
| **Review date** | [FILL IN] |
| **Authorized and signed by (OG-28 authority)** | [FILL IN — must match Cover Block authorizing principal] |
| **Authorization date** | [FILL IN] |
| **Annex document completed** | [Yes — L2 / Yes — L3 / No — L1 only] |
| **Declared maturity level** | L1 — Foundational |
| **Profile validity period** | [FILL IN — must match Section 3.2] |
| **Next scheduled review** | [FILL IN — must match Section 3.2] |

> **FS Example — TransactIQ:**
>
> | Field | Value |
> |---|---|
> | **Profile declared complete by** | Head of AI Operations |
> | **Completion date** | 14 April 2026 |
> | **Review performed by** | Chief Information Security Officer |
> | **Review date** | 15 April 2026 |
> | **Authorized and signed by (OG-28 authority)** | Chief Risk Officer |
> | **Authorization date** | 16 April 2026 |
> | **Annex document completed** | Yes — L2 |
> | **Declared maturity level** | L2 — Mature |
> | **Profile validity period** | April 2027 |
> | **Next scheduled review** | October 2026 |

---

