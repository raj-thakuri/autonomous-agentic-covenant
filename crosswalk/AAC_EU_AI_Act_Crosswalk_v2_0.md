# AAC v2.0 — EU AI Act Compliance Crosswalk

**Version:** 2.0
**Date:** April 2026
**Regulation Reference:** Regulation (EU) 2024/1689 of the European Parliament and of the Council (EU AI Act)
**Apache License 2.0**

---

> **⚠️ 2026 Compliance Alert:** The majority of EU AI Act obligations for high-risk AI systems take effect **August 2026**. Organizations deploying autonomous agentic systems in high-risk categories must demonstrate compliance with Articles 9–15 by that date. This crosswalk identifies which obligations the AAC v2.0 governance control plane satisfies and which require additional organizational action.

---

## Purpose and Scope

This crosswalk maps AAC v2.0 principles to EU AI Act obligations, identifying the technical controls that satisfy each article requirement and the gaps that require organizational process beyond the control plane.

**Important scoping note:** The AAC v2.0 is a technical governance control plane specification. The EU AI Act imposes obligations at three levels: (1) technical controls, (2) organizational processes, and (3) regulatory compliance procedures (conformity assessment, registration, incident reporting). The AAC directly addresses level 1. Levels 2 and 3 require organizational action regardless of technical posture — they are noted as **Process Gap** items throughout this document.

**Coverage ratings:**
- **Satisfies** — The AAC control directly and substantially satisfies this EU AI Act obligation. A compliant AAC deployment produces the technical evidence required by this article.
- **Partial** — The AAC control addresses the technical requirement but the article also imposes organizational or procedural obligations outside the control plane's scope.
- **Gap** — The EU AI Act obligation has no meaningful AAC coverage at the technical level.
- **Process Gap** — The obligation is satisfied by the AAC at the technical level but requires additional organizational action (documentation format, conformity assessment, registration, etc.) to achieve regulatory compliance.

**Applicability:** This crosswalk is relevant to organizations deploying AAC-governed agentic systems that fall within the EU AI Act's definition of high-risk AI systems (Annex III) or general-purpose AI (GPAI) systems subject to Title VIIIb obligations. Organizations should first determine whether their systems fall within these categories before using this crosswalk for compliance planning.

---

## EU AI Act Compliance Calendar

| Date | Provisions Taking Effect | AAC Readiness |
|---|---|---|
| **August 2024** | Regulation enters into force | — |
| **February 2025** | Article 5 (Prohibited AI practices) | AAC-DNH-A, DNH-B, DNH-0 provide partial technical coverage |
| **August 2025** | Articles 51–56 (GPAI model obligations) | AAC-ZT-78, OG-27 provide partial deployment-side coverage |
| **⚠️ August 2026** | Articles 9–15 (High-risk AI system requirements) | L3 AAC deployment satisfies most technical requirements |
| **⚠️ August 2026** | Article 16 (Provider obligations) | Process Gap — conformity assessment, registration required |
| **⚠️ August 2026** | Article 26 (Deployer obligations) | Partial — AAC satisfies technical obligations; process obligations remain |
| **August 2027** | Annex I products with AI components | Sector-specific — assess against product category |

---

## Article-by-Article Crosswalk

---

### Article 5 — Prohibited AI Practices
**In force since:** February 2025
**Applicability:** All AI systems

Article 5 prohibits specific AI practices regardless of risk classification, including subliminal manipulation, exploitation of vulnerabilities, social scoring, real-time biometric identification in public spaces, and emotion recognition in workplace/education contexts.

| Obligation | Coverage | AAC Controls | Rationale |
|---|---|---|---|
| 5(1)(a): No subliminal manipulation techniques | **Partial** | DNH-A, DNH-B, AI-12 | **AAC-DNH-A** (Active Harm Prohibition) prohibits actions with harmful intent regardless of framing. **AAC-AI-12** (Override Available) ensures users can always reject automated outputs — a technical safeguard against manipulation. **AAC-DNH-B** (Duty of Care) obligates the system to act when foreseeable harm is detected. Partial: the AAC prohibits harmful manipulation at the governance layer but does not audit for subliminal intent in outputs — this requires human review of output design. |
| 5(1)(b): No exploitation of vulnerabilities | **Partial** | DNH-A, DNH-B, DA-59 | **AAC-DNH-A** and **AAC-DNH-B** prohibit actions that cause harm to vulnerable populations. **AAC-DA-59** (Harm Classification) allows deployers to define vulnerability-specific harm categories. Partial: the AAC cannot detect exploitative design intent — output content review and system design governance are required. |
| 5(1)(c): No social scoring by public authorities | **Gap** | — | Social scoring systems are a system design prohibition. The AAC governs how a system behaves, not what it is designed to do. Organizations must ensure their system design does not constitute social scoring before deploying the AAC governance layer. |
| 5(1)(d): No real-time remote biometric identification | **Gap** | — | System design prohibition. AAC does not govern what sensors or data streams a system uses — this must be addressed at system design and deployment authorization stages. |
| 5(3): Prohibition on emotion recognition in workplace/education | **Gap** | — | System design prohibition — outside AAC scope. |

**Summary:** Article 5 prohibitions are primarily system design and deployment decisions, not runtime governance controls. The AAC provides compensating controls for manipulation risks but cannot substitute for design-level compliance review.

---

### Article 9 — Risk Management System
**⚠️ In force:** August 2026
**Applicability:** High-risk AI systems

Article 9 requires a documented, continuously updated risk management system covering risk identification, estimation, evaluation, and residual risk assessment throughout the system lifecycle.

| Obligation | Coverage | AAC Controls | Rationale |
|---|---|---|---|
| 9(1): Continuous risk management process | **Satisfies** | OG-24, OG-29, OG-28, AO-55 | **AAC-OG-24** (Governance as Code) implements continuous risk management through version-controlled, validity-bounded governance artifacts with CI/CD integration. **AAC-OG-29** (Implementation Profile) is the deployment-specific risk parameterization artifact. **AAC-OG-28** (Authority Registry) declares risk accountability. **AAC-AO-55** (Escalation Hierarchy) formalizes the risk escalation process. Together these four controls operationalize a continuously maintained risk management system. |
| 9(2): Identify and analyze known and foreseeable risks | **Satisfies** | DA-59, DNH-B, OG-29 | **AAC-DA-59** (Harm Classification) requires the deployer to declare the harm taxonomy — a structured risk identification exercise. **AAC-DNH-B** (Duty of Care) requires a foreseeable harm signal taxonomy as a governance artifact (minimum 3 signals at L1, 5 at L3). **AAC-OG-29** (Implementation Profile) formalizes this risk identification as a signed artifact. |
| 9(3): Estimate and evaluate risks that may emerge | **Satisfies** | DA-60, DA-61, AO-51, OG-25 | **AAC-DA-60** (Tiered Arbitration) evaluates risk on every action at runtime. **AAC-AO-51** (Self-Monitoring) continuously estimates behavioral risk through KPI monitoring. **AAC-OG-25** (Policy Enforcement Integrity) monitors for emergent risk through behavioral drift detection. **AAC-DA-61** (Liveness Guarantee) ensures risk evaluation cannot produce deadlock. |
| 9(4): Adopt risk management measures | **Satisfies** | DA-60, RS-39, AO-55, DA-63 | **AAC-DA-60** implements tiered risk treatment at every action. **AAC-RS-39** at L2 provides system-level risk treatment through Safe Mode. **AAC-AO-55** routes unresolved risks to human governance authority. **AAC-DA-63** (Non-Bypassable Boundary) ensures risk treatment cannot be circumvented. |
| 9(6): Testing for residual risks | **Satisfies** | TB-29, AO-59, OG-24 | **AAC-TB-29** (Behavioral Envelope Verification) requires pre-deployment testing as a governance artifact. **AAC-AO-59** at L3 extends to adversarial residual risk testing against declared threat taxonomy. **AAC-OG-24** requires test results to be versioned governance artifacts. |
| 9(7): Risk management documentation | **Process Gap** | OG-29, OG-24 | The AAC produces the technical risk management artifacts (Implementation Profile, governance artifacts, test records). However, EU AI Act Article 9 requires a specific **risk management system document** in a format suitable for regulatory submission and audit. The Implementation Profile serves as the technical input but must be wrapped in the documentation format required by implementing acts. |

---

### Article 10 — Data and Data Governance
**⚠️ In force:** August 2026
**Applicability:** High-risk AI systems

Article 10 imposes data governance obligations on training, validation, and testing datasets — relevance, representativeness, error freedom, and completeness.

| Obligation | Coverage | AAC Controls | Rationale |
|---|---|---|---|
| 10(2): Data governance practices for training/validation/test data | **Partial** | DP-06, AO-56, ZT-78 | **AAC-DP-06** (Collect the Minimum) requires a data inventory with functional justification — partial coverage of data governance documentation. **AAC-AO-56** (Governed Feedback Loop) at L2 requires bias review and governance approval for feedback-triggered updates. **AAC-ZT-78** at L3 requires provenance documentation for model artifacts including training data lineage. Partial: Article 10 requires active governance of training datasets — the AAC governs the deployed system's data handling, not the model development process. |
| 10(3): Training data relevance and representativeness | **Partial** | AO-51, AO-56, AO-59 | **AAC-AO-51** (Self-Monitoring) requires fairness metrics in the KPI set for consequential-decision agents. **AAC-AO-56** requires bias review before updates. **AAC-AO-59** at L3 includes adversarial testing that can detect representativeness failures. Partial: active training dataset governance requires ML engineering processes outside the deployment control plane. |
| 10(5): Use of special categories of data | **Partial** | DP-06, DP-08, ZT-65 | **AAC-DP-06** (data inventory), **AAC-DP-08** (encrypt always), and **AAC-ZT-65** (least privilege) collectively govern special category data handling. Partial: Article 10(5) imposes specific conditions on using sensitive data in training — this requires data engineering governance beyond runtime control. |

---

### Article 11 — Technical Documentation
**⚠️ In force:** August 2026
**Applicability:** High-risk AI systems (providers)

Article 11 requires technical documentation to be produced before market placement and kept updated. Annex IV specifies the required content.

| Obligation | Coverage | AAC Controls | Rationale |
|---|---|---|---|
| 11(1): Technical documentation before market placement | **Partial** | OG-29, OG-24, ZT-78 | **AAC-OG-29** (Implementation Profile) is the closest AAC equivalent — a signed, versioned, deployment-specific governance artifact. **AAC-OG-24** ensures governance artifacts are maintained with production code rigor. **AAC-ZT-78** at L3 produces model authorization records. Partial: Annex IV specifies a detailed technical documentation structure (general description, detailed description, capabilities and limitations, monitoring and control, risk management, etc.) that exceeds the Implementation Profile scope. The Implementation Profile is a strong technical input to Annex IV documentation but is not a substitute for it. |
| 11(2): Technical documentation updated on changes | **Satisfies** | OG-24, OG-29 | **AAC-OG-24** (Governance as Code) requires governance artifacts to be versioned and updated on any material change. **AAC-OG-29** declares review trigger conditions including model updates, harm taxonomy changes, and regulatory changes. The profile validity period and review cadence directly satisfy the continuous update obligation. |

**Process Gap:** Providers must prepare Annex IV technical documentation in a format acceptable to notified bodies and national authorities. The Implementation Profile serves as technical input. A technical documentation package that includes the Implementation Profile, governance crosswalk references, test records (TB-29, AO-59), and model authorization records (ZT-78) provides a strong foundation.

---

### Article 12 — Record-Keeping
**⚠️ In force:** August 2026
**Applicability:** High-risk AI systems

Article 12 requires high-risk AI systems to automatically log events throughout operation, with logs retained to the minimum necessary period.

| Obligation | Coverage | AAC Controls | Rationale |
|---|---|---|---|
| 12(1): Automatic logging of events | **Satisfies** | DP-07, DA-60, DA-63 | **AAC-DP-07** (Audit Everything) is the direct control — every automated decision produces an immutable log entry capturing the originating agent, arbitration path, confidence score, harm tier assessment, and full decision ownership chain. **AAC-DA-60** records every arbitration evaluation outcome. **AAC-DA-63** logs all integrity violations immediately. The reasoning chain is reconstructable from the log alone at L2; the log alone is sufficient at L3. |
| 12(2): Logs enable post-market monitoring | **Satisfies** | DP-07, OG-25, AO-53 | **AAC-DP-07** produces the audit trail that enables post-market monitoring. **AAC-OG-25** (Policy Enforcement Integrity) provides continuous runtime monitoring against declared governance artifacts — the monitoring output is itself a log. **AAC-AO-53** (Dynamic Trust Adjustment) produces trust tier event records that enable behavioral trend analysis. |
| 12(3): Retention period aligned with regulation | **Process Gap** | DP-07 | The AAC requires audit logging but does not prescribe retention periods — these are declared in the Implementation Profile's `regulatory_context` field and must be mapped to applicable retention requirements. EU AI Act Article 12(3) references product liability legislation and sector-specific requirements. Organizations must declare retention periods in the Implementation Profile accordingly. |

---

### Article 13 — Transparency and Provision of Information
**⚠️ In force:** August 2026 (high-risk systems and Article 50 transparency obligations)
**Applicability:** High-risk AI systems

Article 13 requires high-risk AI systems to be designed and developed with sufficient transparency to enable deployers to use them correctly, and to include information enabling informed decision-making.

| Obligation | Coverage | AAC Controls | Rationale |
|---|---|---|---|
| 13(1): Sufficient transparency for deployers | **Satisfies** | OG-29, DP-07, ZT-76 | **AAC-OG-29** (Implementation Profile) is the deployer transparency artifact — it declares the system's harm taxonomy, behavioral envelopes, trust tiers, escalation hierarchy, and fallback behaviors. **AAC-DP-07** provides decision-level transparency through the audit log. **AAC-ZT-76** (NHI Disclosure) ensures every agent action is attributable to a declared identity. |
| 13(2): Instructions of use to deployers | **Partial** | OG-29, OG-24 | The Implementation Profile and governance documentation serve as deployer instructions. Partial: Article 13(2) specifies a minimum content set for instructions of use (Annex IV §2(d)) that includes intended use limitations, performance metrics, known limitations, and human oversight requirements. The Implementation Profile covers most of this but must be formatted as instructions of use. |
| 13(3)(b): Identity and contact of provider | **Process Gap** | — | Provider identification is an organizational and regulatory requirement — not addressable by the governance control plane. |
| 13(3)(d): Characteristics, capabilities, and limitations | **Partial** | OG-29, TB-29, DA-59 | **AAC-OG-29** declares capabilities through the agent registry and behavioral envelopes. **AAC-TB-29** (Behavioral Envelope) formalizes capabilities and limitations. **AAC-DA-59** (Harm Classification) declares the harm taxonomy as a limitation structure. Partial: Article 13(3)(d) requires specific performance metrics and accuracy levels in a format suitable for deployer decision-making. |
| 50(1): Transparency for AI systems interacting with natural persons | **Satisfies** | ZT-76 | **AAC-ZT-76** (Non-Human Identity Disclosure) directly satisfies Article 50(1) — every outbound request discloses agent identity, trust tier, and control plane ID. At L3, non-processing destinations that might assume human identity receive elevated harm tier classification triggering additional disclosure. **In force: August 2026.** |

---

### Article 14 — Human Oversight
**⚠️ In force:** August 2026
**Applicability:** High-risk AI systems

Article 14 requires high-risk AI systems to be designed to enable effective human oversight. Deployers must assign qualified natural persons and implement appropriate technical and organizational measures.

| Obligation | Coverage | AAC Controls | Rationale |
|---|---|---|---|
| 14(1): Enable effective human oversight | **Satisfies** | AI-12, AO-55, OG-28, RS-39 | **AAC-AI-12** (Override Always Available) mandates accessible override paths for all OG-28 principals. For Tier 1 and Tier 2 actions, override paths are surfaced proactively. **AAC-AO-55** (Escalation Hierarchy) declares the human oversight chain with time bounds. **AAC-OG-28** (Authority Registry) makes oversight accountability explicit. **AAC-RS-39** at L2 provides hard shutdown capability as the ultimate oversight mechanism. |
| 14(2): Enable monitoring and detection of anomalies | **Satisfies** | OG-25, AO-51, AO-53, DP-07 | **AAC-OG-25** (Policy Enforcement Integrity) provides continuous monitoring for behavioral anomalies against declared governance artifacts. **AAC-AO-51** (Self-Monitoring) monitors KPIs against declared thresholds. **AAC-AO-53** (Dynamic Trust Adjustment) automatically responds to performance anomalies. **AAC-DP-07** provides the audit trail for human review of detected anomalies. |
| 14(3): Override and interruption capability | **Satisfies** | AI-12, RS-39, DNH-A | **AAC-AI-12** provides per-action override. **AAC-RS-39** at L2 provides system-level override through Safe Mode entry and hard shutdown. **AAC-DNH-A** includes the SOVEREIGN_OVERRIDE clause — the highest governance authority can override harm tier classifications. **AAC-RS-41** (Tier 3) specifies hard shutdown implementation including out-of-band signal path. |
| 14(4): Natural persons able to understand system outputs | **Partial** | DP-07, DA-60, OG-29 | **AAC-DP-07** (include_reasoning field) captures the decision reasoning chain in the audit log. **AAC-DA-60** enforces deterministic arbitration that makes output reasoning traceable. **AAC-OG-29** (Implementation Profile) documents the system's harm taxonomy and evaluation logic. Partial: Article 14(4) requires specific competence of assigned human overseers — the AAC enables understanding through transparency but cannot ensure human competence. |
| 14(5): Deployer-assigned oversight persons | **Process Gap** | OG-28 | **AAC-OG-28** (Authority Registry) declares oversight principals. However, Article 14(5) requires deployers to formally assign qualified natural persons to oversight roles — an organizational HR and role-assignment process that produces input to OG-28 but exceeds the AAC's scope. |

---

### Article 15 — Accuracy, Robustness, and Cybersecurity
**⚠️ In force:** August 2026
**Applicability:** High-risk AI systems

Article 15 requires high-risk AI systems to achieve appropriate levels of accuracy, robustness, and cybersecurity throughout the lifecycle, including resilience to attempts to alter outputs through adversarial techniques.

| Obligation | Coverage | AAC Controls | Rationale |
|---|---|---|---|
| 15(1): Appropriate accuracy levels | **Satisfies** | DA-62, AI-10, AO-51, TB-29 | **AAC-DA-62** (Confidence Enforcement) independently verifies model confidence before permitting Tier 2 and Tier 1 actions — a runtime accuracy enforcement mechanism. **AAC-AI-10** (Confidence Thresholds) requires declared thresholds with graceful degradation. **AAC-AO-51** (Self-Monitoring) monitors accuracy KPIs continuously. **AAC-TB-29** (Behavioral Envelope Verification) validates accuracy before deployment. |
| 15(3): Resilience to third-party adversarial techniques | **Satisfies** | ZT-71, ZT-75, DA-62, AO-59 | **AAC-ZT-71** (Hostile Input Validation) provides adversarial input defense. **AAC-ZT-75** (Instruction Isolation) mitigates adversarial instruction injection. **AAC-DA-62** (Confidence Enforcement) detects confidence degradation from adversarial inputs. **AAC-AO-59** at L3 requires adversarial boundary testing against declared threat taxonomy (MITRE ATLAS or equivalent), directly satisfying the "resilience to adversarial techniques" requirement. |
| 15(4): Technical robustness measures | **Satisfies** | DA-61, RS-39, AO-58 | **AAC-DA-61** (Liveness Guarantee) is the foundational robustness control — a system that cannot make forward progress under its own governance constraints has a design defect. **AAC-RS-39** at L2 provides graceful degradation in Safe Mode. **AAC-AO-58** (Resource Governance) prevents resource exhaustion. Together these three controls implement the technical robustness requirements. |
| 15(5): Cybersecurity measures | **Satisfies** | ZT-64–77, DA-63, DP-08 | The entire Zero-Trust domain addresses cybersecurity requirements. **AAC-ZT-64** (No Implicit Trust), **ZT-65** (Least Privilege), **ZT-67** (Auth-Authz-Validate), **ZT-68** (Authenticated Propagation), **ZT-71** (Hostile Input Validation), **ZT-74** (Continuous Verification), **ZT-75** (Instruction Isolation), **ZT-76** (NHI Disclosure), **ZT-77** (Supply Chain Integrity) collectively address the cybersecurity requirement across the attack surface. **AAC-DA-63** (Non-Bypassable Boundary) ensures cybersecurity controls cannot be circumvented. |

---

### Article 16 — Obligations of High-Risk AI System Providers
**⚠️ In force:** August 2026
**Applicability:** Providers (developers) of high-risk AI systems

| Obligation | Coverage | AAC Controls | Rationale |
|---|---|---|---|
| 16(a): Quality management system | **Partial** | OG-24, OG-29 | **AAC-OG-24** (Governance as Code) implements a quality management system for governance artifacts. **AAC-OG-29** declares the quality parameters. Partial: Article 16(a) requires a formal quality management system (Article 17) including organizational procedures — the AAC provides the technical quality controls but not the organizational QMS infrastructure. |
| 16(b): Technical documentation (Annex IV) | **Process Gap** | OG-29, OG-24, ZT-78 | AAC produces strong technical inputs to Annex IV documentation. Formal Annex IV-compliant documentation package requires organizational process. |
| 16(e): Conformity assessment | **Process Gap** | — | Conformity assessment is a regulatory procedure requiring notified body involvement or internal assessment against harmonized standards. The AAC's control plane produces evidence that supports conformity assessment but cannot substitute for it. |
| 16(f): Registration in EU database | **Process Gap** | — | Regulatory registration requirement — outside AAC scope. |
| 16(h): Post-market monitoring system | **Partial** | OG-25, AO-51, AO-53, DP-07 | **AAC-OG-25**, **AO-51**, **AO-53**, and **DP-07** collectively implement the technical post-market monitoring infrastructure. Partial: Article 16(h) also requires a post-market monitoring plan and incident reporting process that exceeds the technical control plane. |
| 16(i): Serious incident reporting | **Process Gap** | DP-07, AO-55 | **AAC-DP-07** produces the audit record. **AAC-AO-55** escalates serious incidents. However, EU AI Act incident reporting requires formal notification to national authorities within defined timeframes — an organizational and regulatory process. |

---

### Article 26 — Obligations of High-Risk AI System Deployers
**⚠️ In force:** August 2026
**Applicability:** Deployers of high-risk AI systems

| Obligation | Coverage | AAC Controls | Rationale |
|---|---|---|---|
| 26(1): Use in accordance with instructions | **Satisfies** | OG-29, TB-29, DA-60 | The Implementation Profile (OG-29) declares the authorized use scope. **AAC-TB-29** (Behavioral Envelope) enforces use within declared boundaries. **AAC-DA-60** evaluates every action against the declared harm taxonomy. Together these ensure the system is used within declared parameters. |
| 26(2): Assign human oversight | **Partial** | OG-28, AO-55 | **AAC-OG-28** declares oversight principals. **AAC-AO-55** formalizes the escalation hierarchy. Partial: Article 26(2) requires deployers to formally assign qualified persons to oversight — an HR and organizational process with AAC as the technical underpinning. |
| 26(5): Notify provider of serious incidents | **Process Gap** | DP-07 | **AAC-DP-07** captures serious incident evidence. Formal provider notification is an organizational process outside AAC scope. |
| 26(6): Fundamental rights impact assessment | **Partial** | DA-59, AO-51, AO-56 | **AAC-DA-59** (Harm Classification) provides the framework for impact assessment. **AAC-AO-51** requires fairness monitoring. **AAC-AO-56** requires bias review. Partial: Article 26(6) requires a formal fundamental rights impact assessment for public authorities and certain deployers — a documented organizational process the AAC supports through its monitoring infrastructure. |

---

### Articles 51–56 — General-Purpose AI (GPAI) Models
**In force:** August 2025
**Applicability:** GPAI model providers and downstream system providers

| Obligation | Coverage | AAC Controls | Rationale |
|---|---|---|---|
| 53(1)(a): Technical documentation for GPAI | **Partial** | ZT-78, OG-27 | **AAC-ZT-78** at L3 (Authorized Model Registry) requires provenance documentation and authorization records for all deployed GPAI models. **AAC-OG-27** (Context Interface Contract) governs GPAI model use as a context source. Partial: Article 53 obligations are primarily on GPAI providers, not deployers — the AAC addresses the deployment-side governance of GPAI models, not the model provider's obligations. |
| 53(1)(b): Policy on GPAI model copyright | **Gap** | — | Copyright policy for training data is a provider obligation outside the deployment control plane's scope. |
| 53(2)(a): Systemic risk identification | **Partial** | DA-59, DNH-B | **AAC-DA-59** and **AAC-DNH-B** enable deployers to identify foreseeable harm signals from GPAI models. Partial: systemic risk identification at the scale Article 53(2) addresses (societal-level impact of frontier GPAI models) is beyond deployment-level governance. |

---

## Coverage Summary

### By Article Family

| Article | Topic | Coverage | 2026 Deadline |
|---|---|---|---|
| Article 5 | Prohibited practices | Partial / Gap | No (Feb 2025) |
| Article 9 | Risk management system | Satisfies | ⚠️ Aug 2026 |
| Article 10 | Data governance | Partial | ⚠️ Aug 2026 |
| Article 11 | Technical documentation | Partial + Process Gap | ⚠️ Aug 2026 |
| Article 12 | Record-keeping | Satisfies + Process Gap | ⚠️ Aug 2026 |
| Article 13 | Transparency | Satisfies + Partial | ⚠️ Aug 2026 |
| Article 14 | Human oversight | Satisfies + Process Gap | ⚠️ Aug 2026 |
| Article 15 | Accuracy / Robustness / Cybersecurity | Satisfies | ⚠️ Aug 2026 |
| Article 16 | Provider obligations | Partial + Process Gap | ⚠️ Aug 2026 |
| Article 26 | Deployer obligations | Satisfies + Partial | ⚠️ Aug 2026 |
| Article 50 | Transparency (AI identity) | Satisfies | ⚠️ Aug 2026 |
| Articles 51–56 | GPAI obligations | Partial + Gap | No (Aug 2025) |

### Obligation Count

| Rating | Count |
|---|---|
| Satisfies | 14 |
| Partial | 12 |
| Process Gap | 8 |
| Gap | 3 |

---

## 2026 Readiness — What the AAC Covers and What It Doesn't

### What an L3 AAC deployment satisfies by August 2026

A fully deployed L3 AAC governance control plane, with a signed Implementation Profile, produces technical evidence satisfying the following Article obligations directly:

- **Article 9** — Risk management system (continuous, documented, parameterized, tested)
- **Article 12** — Automatic logging with full reasoning chain, reconstructable audit trail
- **Article 13(1)** — Deployer transparency through the Implementation Profile and audit log
- **Article 14(1)-(3)** — Human oversight mechanisms, override capability, hard shutdown
- **Article 15** — Accuracy enforcement (DA-62), adversarial robustness (ZT-71, AO-59), cybersecurity (ZT domain), technical robustness (DA-61, RS-39)
- **Article 26(1)** — Use within declared parameters enforced by the behavioral envelope

### What still requires organizational action beyond the AAC

Regardless of AAC maturity level, the following must be addressed organizationally:

**Documentation and process:**
- Annex IV technical documentation package — the Implementation Profile is a strong input but must be formatted per Annex IV requirements
- Quality management system (Article 17) — the AAC's OG-24 governance infrastructure is the technical layer; QMS procedures are organizational
- Fundamental rights impact assessment (Article 26(6)) — the AAC monitoring infrastructure supports this; the formal FRIA requires organizational process

**Regulatory procedures:**
- Conformity assessment (Article 16(e)) — notified body or self-assessment against harmonized standards; AAC evidence is input
- Registration in EU AI Act database (Article 16(f))
- Serious incident reporting to national authorities (Article 73) — AAC produces the audit evidence; notification process is organizational
- Post-market monitoring plan (Article 72) — AAC produces monitoring data; the plan document is organizational

**Data governance:**
- Training data governance per Article 10(2)-(5) — the AAC governs the deployed system; training pipeline data governance requires ML engineering process

---

## ⚠️ August 2026 Compliance Checklist

For organizations subject to the August 2026 high-risk AI system requirements, the following AAC-based items should be complete:

**Technical controls (AAC-satisfiable):**
- [ ] AAC v2.0 L3 deployment with signed Implementation Profile
- [ ] Harm classification taxonomy declared per DA-59 (including foreseeable harm signals ≥ 5 at L3)
- [ ] Behavioral envelopes declared and verified per TB-29
- [ ] Adversarial benchmark specification per AO-59 with ATLAS-aligned test categories
- [ ] Authorized model registry per ZT-78 with residual risk acceptance for all GPAI models
- [ ] Human oversight authority declared per OG-28 with SOVEREIGN_OVERRIDE principal
- [ ] Override mechanisms tested and documented per AI-12 (monthly cadence)
- [ ] Safe mode with hard shutdown capability per RS-39/RS-41
- [ ] Continuous monitoring per OG-25, AO-51, AO-53 with declared KPI set
- [ ] Audit logging per DP-07 with include_reasoning: true on all Tier 1 and Tier 2 gates

**Organizational process (required beyond AAC):**
- [ ] Annex IV technical documentation package compiled using Implementation Profile as primary input
- [ ] Quality management system procedures established per Article 17
- [ ] Conformity assessment completed (self-assessment or notified body)
- [ ] Registration in EU AI Act database completed
- [ ] Qualified human overseers formally assigned per Article 14(5) and 26(2)
- [ ] Serious incident reporting procedure established per Article 73
- [ ] Post-market monitoring plan documented per Article 72
- [ ] Fundamental rights impact assessment completed where required per Article 26(6)
- [ ] Data governance documentation for training data per Article 10

---

*This crosswalk is provided for informational purposes and does not constitute legal advice. Organizations should consult legal counsel for EU AI Act compliance determinations. Regulation (EU) 2024/1689 and implementing acts should be consulted directly for authoritative obligation definitions.*

*This crosswalk is published under Apache License 2.0 as a companion document to the Autonomous Agentic Covenant v2.0 specification.*

*Thakuri, R. (2026). AAC v2.0 EU AI Act Compliance Crosswalk. Companion to: The Autonomous Agentic Covenant (Version 2.0). Apache License 2.0.*
