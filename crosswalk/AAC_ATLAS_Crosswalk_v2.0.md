# AAC v2.0 — MITRE ATLAS Threat Mitigation Crosswalk

**Version:** 2.0
**Date:** April 2026
**ATLAS Reference:** MITRE ATLAS v5.4.0
**Apache License 2.0**

---

## Purpose and Structure

This crosswalk is a **threat mitigation instrument**, not a governance alignment document. It maps AAC v2.0 controls to MITRE ATLAS adversarial techniques, identifying which techniques the control plane mitigates and how. It is designed for use in threat modeling exercises, red team scope definition, and security program gap analysis.

This crosswalk is structured differently from the AAC Governance Framework Crosswalk. Coverage ratings here reflect **defensive effectiveness** against adversarial techniques — not conceptual alignment with a governance standard.

**Coverage ratings:**
- **Mitigates** — The AAC control directly and substantially reduces the risk or effectiveness of this technique. An attacker using this technique against a compliant AAC deployment faces a meaningful governance barrier.
- **Partial** — The AAC control provides some mitigation but does not fully address the technique, or mitigates a sub-technique but not the full technique family.
- **Not Addressed** — The technique operates below or outside the governance control plane's scope. No AAC control meaningfully mitigates this technique.

**Enforcement tier notation:** Mitigations marked **(L2)** or **(L3)** only apply at the declared maturity level.

**Key changes from v1.3:** Four of five v1.3 gap areas are closed or addressed in v2.0. Dynamic supply chain integrity closed by AAC-ZT-77. Output content integrity monitoring closed by AAC-OG-26 (L3). Adversarial benchmark specification closed by AAC-AO-59 (L3). Model artifact recovery addressed by AAC-OG-29 RS-40 parameter. Passive OSINT reconnaissance remains not addressed — this is inherent to deployment environment, not the governance control plane.

---

## Tactic Coverage Summary

| ATLAS Tactic | Techniques Mapped | Mitigates | Partial | Not Addressed |
|---|---|---|---|---|
| Reconnaissance | 5 | 1 | 1 | 3 |
| Resource Development | 3 | 1 | 1 | 1 |
| Initial Access | 4 | 2 | 1 | 1 |
| ML Attack Staging | 5 | 2 | 2 | 1 |
| Execution | 4 | 3 | 1 | 0 |
| Persistence | 3 | 2 | 1 | 0 |
| Defense Evasion | 3 | 2 | 1 | 0 |
| Discovery | 3 | 1 | 1 | 1 |
| Collection | 3 | 2 | 1 | 0 |
| Exfiltration | 4 | 3 | 1 | 0 |
| Impact | 6 | 4 | 1 | 1 |
| **Total** | **43** | **23** | **12** | **8** |

---

## Tactic 1 — Reconnaissance

*Adversary gathers information about the target AI system, its architecture, training data, model artifacts, and deployment environment.*

| Technique | ID | Coverage | Primary AAC Controls | Rationale |
|---|---|---|---|---|
| Search for Victim's Publicly Available AI Research | AML.T0000 | **Not Addressed** | — | Public information gathering is outside the governance control plane's scope. |
| Search Victim's AI Assets | AML.T0001 | **Not Addressed** | — | Asset enumeration from external position is not mitigable by the control plane. |
| Acquire Public ML Artifacts | AML.T0002 | **Not Addressed** | — | Public artifact acquisition predates deployment; governance cannot prevent it. |
| Discover AI Organizational Model | AML.T0004 | **Partial** | OG-28, ZT-76 | **AAC-OG-28** (Authority Registry) and **AAC-ZT-76** (NHI Disclosure) limit adversary knowledge of internal governance structure. ZT-76 discloses agent identity and trust tier on every outbound request — this is an intentional transparency trade-off (regulatory requirement) that creates a minimal reconnaissance surface. OG-28's internal accountability chain is not externally exposed. Partial: governance structure cannot be fully obscured. |
| Victim Research via Inference API | AML.T0005 | **Mitigates** | DA-63, ZT-64, ZT-65 | **AAC-DA-63** (Centralized Enforcement Boundary) routes all agent actions through the non-bypassable arbitration layer, preventing reconnaissance-oriented probing from producing unintended disclosures. **AAC-ZT-64** and **AAC-ZT-65** restrict API access to least-privilege declared scope, limiting the attack surface available to an adversary probing the inference API. |

---

## Tactic 2 — Resource Development

*Adversary establishes resources to support operations — acquiring infrastructure, developing tools, or staging attack components.*

| Technique | ID | Coverage | Primary AAC Controls | Rationale |
|---|---|---|---|---|
| Acquire Infrastructure | AML.T0008 | **Not Addressed** | — | Infrastructure acquisition by adversaries predates and is external to the governance control plane. |
| Develop Capabilities | AML.T0009 | **Partial** | ZT-77, ZT-78 | **AAC-ZT-77** (Supply Chain Integrity) mitigates adversary capability development targeted at the supply chain — components without cryptographically verifiable provenance are refused. **AAC-ZT-78** (Authorized Model Registry) at L3 requires explicit authorization records for all model artifacts, raising the cost of introducing adversarially developed model components. |
| Establish Accounts | AML.T0010 | **Mitigates** | OG-28, ZT-64, ZT-67 | **AAC-OG-28** (Authority Registry) declares the non-circular accountability chain — every authorized principal is established by a prior registry entry. **AAC-ZT-67** (Auth-Authz-Validate) enforces the authentication sequence on every request, making unauthorized account establishment detectable. The non-circular chain prevents adversary-controlled accounts from claiming authority through a compromised intermediate principal. |

---

## Tactic 3 — Initial Access

*Adversary gains entry to the AI system or its environment.*

| Technique | ID | Coverage | Primary AAC Controls | Rationale |
|---|---|---|---|---|
| Phishing | AML.T0011 | **Not Addressed** | — | Social engineering attacks on personnel are outside the governance control plane's scope. Organizational security training and MFA are the appropriate controls. |
| Exploit Public-Facing ML Application | AML.T0012 | **Partial** | ZT-71, DA-63 | **AAC-ZT-71** (Hostile Input Validation) validates all external inputs including those that may carry exploit payloads. **AAC-DA-63** (Centralized Enforcement Boundary) ensures exploited execution paths cannot produce high-harm actions without traversing the arbitration layer. Partial: application-layer vulnerability exploitation is mitigated at the governance layer but the exploit itself must be addressed by the engineering and operations layer. |
| ML Supply Chain Compromise | AML.T0047 | **Mitigates** | ZT-77, ZT-78 | **AAC-ZT-77** directly addresses supply chain compromise — every external tool, MCP server, and agent component requires cryptographically verifiable provenance before connection. Components without valid provenance are refused. Dynamic discovery is disabled at L1. **AAC-ZT-78** at L3 extends coverage to model artifacts with explicit authorization records and residual risk acceptance declarations. |
| Exploit API | AML.T0016 | **Mitigates** | ZT-64, ZT-67, ZT-68, DA-63 | **AAC-ZT-64** (No Implicit Trust) and **AAC-ZT-67** (Auth-Authz-Validate) enforce independent authentication on every API request. **AAC-ZT-68** at L2 extends mutual authentication to service-to-service communication. **AAC-DA-63** ensures API exploitation cannot produce high-harm actions without traversing the arbitration boundary. |

---

## Tactic 4 — ML Attack Staging

*Adversary prepares ML-specific attack components — crafting adversarial examples, staging poisoned data, or creating proxy models.*

| Technique | ID | Coverage | Primary AAC Controls | Rationale |
|---|---|---|---|---|
| Create Proxy ML Model | AML.T0005 | **Partial** | ZT-78, AO-59 | **AAC-ZT-78** at L3 requires explicit authorization records for all model artifacts — a proxy model introduced into the deployment would fail authorization. **AAC-AO-59** at L3 requires adversarially constructed boundary tests that should detect proxy model behavioral divergence. Partial: proxy model creation is external to the control plane; mitigation only applies at deployment boundary. |
| Poison Training Data | AML.T0020 | **Partial** | AO-56, ZT-71, DP-06 | **AAC-AO-56** (Governed Feedback Loop) requires bias review and governance approval before any feedback-triggered update deploys, making training data poisoning through feedback channels detectable. **AAC-ZT-71** validates all inputs including training pipeline inputs at L2+. **AAC-DP-06** (Collect the Minimum) requires data inventory with functional justification, providing lineage documentation. Partial: historical training data poisoning predating deployment is not mitigable by runtime governance. |
| Craft Adversarial Data | AML.T0043 | **Mitigates** | ZT-71, ZT-75, DA-62 | **AAC-ZT-71** (Hostile Input Validation) directly targets adversarially crafted inputs — all external inputs are validated before processing. **AAC-ZT-75** (Instruction Isolation) prevents adversarially crafted content from being treated as system instructions. **AAC-DA-62** (Confidence Enforcement) independently verifies model confidence before permitting Tier 2 and Tier 1 actions — adversarially crafted inputs that reduce confidence below threshold trigger escalation rather than execution. |
| Backdoor ML Model | AML.T0018 | **Mitigates** | ZT-78, AO-59, TB-29 | **AAC-ZT-78** at L3 requires explicit authorization records for all model artifacts with known and unknown provenance documented; backdoored models introduced into the supply chain require residual risk acceptance from an OG-28 principal. **AAC-AO-59** at L3 includes adversarial boundary testing that should detect behavioral anomalies consistent with backdoor triggers. **AAC-TB-29** (Behavioral Envelope) detects backdoor-triggered actions that cross the declared boundary. |
| Train Proxy via Stolen Data | AML.T0006 | **Not Addressed** | — | Proxy model training using externally stolen data is conducted entirely outside the deployment environment. The governance control plane has no visibility into adversary infrastructure. |

---

## Tactic 5 — Execution

*Adversary executes malicious ML-specific actions within the AI system or through its inference API.*

| Technique | ID | Coverage | Primary AAC Controls | Rationale |
|---|---|---|---|---|
| LLM Prompt Injection — Direct | AML.T0051.000 | **Mitigates** | ZT-71, ZT-75, DA-63 | **AAC-ZT-71** (Hostile Input Validation) validates all user-supplied inputs and rejects unexpected fields. **AAC-ZT-75** (Instruction Isolation) architecturally separates user-supplied content from system directives — injected instructions in user content cannot reach the system prompt layer. **AAC-DA-63** (Centralized Enforcement Boundary) ensures even if a direct injection reaches the agent, it cannot produce a high-harm action without traversing the non-bypassable arbitration layer. |
| LLM Prompt Injection — Indirect | AML.T0051.001 | **Mitigates** | ZT-71, ZT-75, OG-27, DA-63 | **AAC-OG-27** (Context Interface Contract) governs all context sources — undeclared context sources containing injected instructions are treated as hostile input per ZT-71. **AAC-ZT-75** prevents externally retrieved content from being treated as system instructions regardless of source. **AAC-DA-63** provides the final enforcement boundary. This is the most comprehensive AAC mitigation — indirect prompt injection is addressed at three independent layers. |
| LLM Jailbreak | AML.T0054 | **Mitigates** | DA-60, DA-63, TB-29, DNH-A | **AAC-DA-63** (Centralized Enforcement Boundary) ensures jailbreak attempts that reach the agent cannot produce Tier 1 or Tier 2 actions without traversing the full arbitration sequence. **AAC-DA-60** (Tiered Evaluation) means Tier 1 actions require the full five-step sequence with DNH-A pre-gate — no jailbreak can circumvent the liveness-guaranteed arbitration layer. **AAC-TB-29** detects jailbreak-produced actions that cross the behavioral envelope. **AAC-DNH-A**'s optimization override prohibition means no jailbreak framing that presents harmful actions as "helpful" or "optimal" can bypass the harm tier classification. |
| Execute Against Production ML | AML.T0036 | **Partial** | DA-62, DA-60, AO-51 | **AAC-DA-62** (Confidence Enforcement) monitors model confidence — adversarial inputs that cause confidence degradation trigger escalation before execution. **AAC-DA-60** enforces the evaluation sequence. **AAC-AO-51** (Self-Monitoring) detects anomalous patterns consistent with adversarial execution in the KPI stream. Partial: detection is probabilistic and depends on confidence degradation being observable. |

---

## Tactic 6 — Persistence

*Adversary maintains access to the AI system or its governance layer across sessions and deployments.*

| Technique | ID | Coverage | Primary AAC Controls | Rationale |
|---|---|---|---|---|
| Poison ML Model | AML.T0028 | **Mitigates** | ZT-78, AO-56, OG-24 | **AAC-ZT-78** at L3 requires full authorization records for all model artifacts — an adversarially poisoned model artifact introduced into the supply chain fails the authorization check. **AAC-AO-56** (Governed Feedback Loop) requires bias review and governance approval before any feedback-triggered update deploys, blocking persistence via feedback poisoning. **AAC-OG-24** (Governance as Code) maintains versioned governance artifacts, making unauthorized changes detectable through diff. |
| Establish Persistence via Backdoor | AML.T0018 | **Mitigates** | ZT-78, TB-29, OG-25 | As noted in ML Attack Staging — **AAC-ZT-78** authorization records, **AAC-TB-29** behavioral envelope monitoring, and **AAC-OG-25** (Policy Enforcement Integrity) together detect and respond to behavioral persistence mechanisms. OG-25 provides continuous runtime monitoring against declared governance artifacts — behavioral drift consistent with backdoor activation triggers a policy integrity violation. |
| Compromise ML Pipeline | AML.T0010 | **Partial** | OG-24, ZT-77 | **AAC-OG-24** (Governance as Code) treats governance artifacts as production code with CI/CD integration, providing integrity verification for the governance pipeline itself. **AAC-ZT-77** governs supply chain components in the ML pipeline. Partial: the AAC governs the governance control plane and deployment boundary; the broader ML training and pipeline infrastructure requires additional security controls outside the AAC's scope. |

---

## Tactic 7 — Defense Evasion

*Adversary attempts to avoid detection by the governance control plane or monitoring systems.*

| Technique | ID | Coverage | Primary AAC Controls | Rationale |
|---|---|---|---|---|
| Evade ML Model | AML.T0015 | **Mitigates** | DA-62, AO-51, OG-25 | **AAC-DA-62** (Confidence Enforcement) is the primary mitigation — adversarial inputs that reduce model confidence below threshold trigger escalation rather than execution, making evasion costly. **AAC-AO-51** (Self-Monitoring) monitors behavioral KPIs for anomalous patterns. **AAC-OG-25** (Policy Enforcement Integrity) provides continuous monitoring for behavioral drift consistent with evasion. |
| Bypass ML Detection | AML.T0040 | **Mitigates** | DA-63, DP-07, OG-25 | **AAC-DA-63** (Non-Bypassable Enforcement Boundary) is architecturally non-circumventable — the governance control plane cannot be bypassed at the action level without producing an integrity violation. **AAC-DP-07** (Audit Everything) records every decision with full reasoning chain — evasion attempts that produce unusual arbitration patterns are detectable in the audit log. **AAC-OG-25** provides the runtime monitoring that surfaces these patterns. |
| Obfuscate Adversarial Samples | AML.T0043 | **Partial** | ZT-71, DA-62 | **AAC-ZT-71** (Hostile Input Validation) applies input validation that catches many obfuscation patterns. **AAC-DA-62** (Confidence Enforcement) detects confidence degradation caused by obfuscated adversarial inputs. Partial: the AAC does not require adversarial input detection as a specific mechanism — it requires validation and confidence enforcement, which are compensating but not purpose-built mitigations for obfuscated attacks. **AAC-AO-59** at L3 extends coverage through declared adversarial test patterns. |

---

## Tactic 8 — Discovery

*Adversary enumerates the AI system's capabilities, configuration, and governance structure.*

| Technique | ID | Coverage | Primary AAC Controls | Rationale |
|---|---|---|---|---|
| Discover AI Model Artifacts | AML.T0044 | **Partial** | ZT-65, ZT-64, ZT-67 | **AAC-ZT-65** (Least Privilege) restricts model artifact access to declared minimum permissions. **AAC-ZT-64** and **AAC-ZT-67** enforce independent authentication before any artifact access. Partial: the AAC governs access control but cannot prevent discovery from an already-authenticated principal operating within their declared permissions. |
| Discover ML Artifacts | AML.T0045 | **Not Addressed** | — | Discovery of externally accessible ML artifacts (public repositories, research publications) is outside the governance control plane's scope. |
| Active Scanning for AI Systems | AML.T0035 | **Mitigates** | ZT-64, ZT-67, DA-63 | **AAC-ZT-64** (No Implicit Trust) ensures every request is independently authenticated — scanning from unauthorized positions is blocked at authentication. **AAC-DA-63** logs all access attempts including those that fail authentication, enabling detection of active scanning patterns in the audit log. |

---

## Tactic 9 — Collection

*Adversary gathers data from or about the AI system — model weights, training data, context, or inference outputs.*

| Technique | ID | Coverage | Primary AAC Controls | Rationale |
|---|---|---|---|---|
| Collect ML Model Artifacts | AML.T0045 | **Mitigates** | ZT-65, ZT-64, DP-07 | **AAC-ZT-65** (Least Privilege) restricts model artifact access to declared minimum permissions. **AAC-ZT-64** enforces authentication before access. **AAC-DP-07** (Audit Everything) creates an immutable record of all model artifact access decisions, enabling post-hoc detection of collection activity. |
| Collect User Information via API | AML.T0017 | **Mitigates** | DP-06, ZT-65, DA-60 | **AAC-DP-06** (Collect the Minimum) restricts what data the system holds — an adversary can only collect what exists. **AAC-ZT-65** restricts which agents can access what data. **AAC-DA-60** evaluates data retrieval actions against the harm taxonomy — bulk data collection will produce Material or Irreversible classification, triggering escalation or denial. |
| Obtain Victim Credentials | AML.T0019 | **Partial** | ZT-66, ZT-64, ZT-67 | **AAC-ZT-66** (Short-Lived Credentials) limits the value of stolen credentials through mandatory TTLs and rotation. **AAC-ZT-64** and **AAC-ZT-67** enforce re-authentication on every request, limiting lateral use of captured credentials. Partial: credential theft itself is not preventable by the governance control plane — the mitigation is time-bounding the utility of stolen credentials. |

---

## Tactic 10 — Exfiltration

*Adversary extracts data from the AI system through its inference interface, context, or outputs.*

| Technique | ID | Coverage | Primary AAC Controls | Rationale |
|---|---|---|---|---|
| Exfiltrate Information via Inference API | AML.T0024.000 | **Mitigates** | DA-60, DP-07, ZT-65 | **AAC-DA-60** evaluates every output action against the harm taxonomy — bulk inference-based exfiltration produces Material or Irreversible classification. **AAC-DP-07** logs every decision including inference API calls, enabling detection of repeated extraction patterns. **AAC-ZT-65** restricts the data scope available to each agent. |
| Reconstruct Training Data via Inference | AML.T0024.001 | **Partial** | DA-62, DP-09, AO-51 | **AAC-DA-62** (Confidence Enforcement) monitors output confidence — reconstruction attacks often produce high-confidence outputs for sensitive training examples. **AAC-DP-09** (Least Disclosure) at L3 enforces field-level response scoping that limits the completeness of reconstruction attempts. **AAC-AO-51** (Self-Monitoring) monitors for anomalous query patterns consistent with reconstruction attacks. Partial: reconstruction from inference is difficult to prevent definitively — these controls raise the cost and reduce the yield. |
| Model Inversion | AML.T0024.002 | **Partial** | DA-60, AO-51, DP-09 | **AAC-DA-60** can classify systematic model inversion probing as Material harm if the behavioral envelope (TB-29) and foreseeable harm signals (DNH-B) are properly configured. **AAC-AO-51** monitors for anomalous query volume patterns. **AAC-DP-09** at L3 limits response completeness. Partial: model inversion is primarily an ML privacy concern requiring architectural mitigations (differential privacy, output perturbation) outside the governance control plane's scope. |
| Exfiltrate via Steganography | AML.T0024.003 | **Mitigates** | OG-26 | **AAC-OG-26** (Output Content Integrity Monitoring) at L3 directly addresses this technique — outputs are inspected before delivery for statistical patterns consistent with covert data exfiltration including steganographic embedding. This is the specific technique OG-26 was designed to close. At L1 and L2, this technique is not mitigated by the AAC — OG-26 is an L3 control. |

---

## Tactic 11 — Impact

*Adversary degrades, disrupts, or corrupts the AI system's functionality, outputs, or governance layer.*

| Technique | ID | Coverage | Primary AAC Controls | Rationale |
|---|---|---|---|---|
| Denial of ML Service | AML.T0029 | **Mitigates** | DA-61, RS-39, AO-58 | **AAC-DA-61** (Liveness Guarantee) is the foundational mitigation — a system that cannot make forward progress under adversarial load has a declared fallback that executes within time bounds. **AAC-RS-39** (System Safe Mode) at L2 provides degraded-mode operation that maintains governance integrity under reduced capacity. **AAC-AO-58** (Resource Constraint Governance) declares per-agent resource limits that prevent any single agent from consuming enough resources to cause denial. |
| Spamming ML System | AML.T0030 | **Mitigates** | AO-58, DA-61, DA-60 | **AAC-AO-58** (Resource Governance) declares API quotas and request rate limits. **AAC-DA-61** ensures spam-induced resource exhaustion triggers fallback rather than deadlock. **AAC-DA-60** evaluates every action — high-volume spam that degrades confidence triggers escalation under DA-62 before execution. |
| Corrupt ML Model | AML.T0031 | **Mitigates** | ZT-78, OG-29, AO-59 | **AAC-ZT-78** at L3 requires authorization records with provenance verification for all model artifacts — corrupted models introduced at the artifact level fail the authorization check. **AAC-OG-29** (RS-40 parameter) declares model rollback capability and RTO/RPO — corruption is recoverable within declared bounds. **AAC-AO-59** at L3 includes adversarial behavioral testing that should detect corruption-induced behavioral anomalies. |
| Manipulate Model Prediction | AML.T0046 | **Partial** | DA-62, TB-29, AO-59 | **AAC-DA-62** (Confidence Enforcement) detects prediction confidence degradation from manipulation. **AAC-TB-29** (Behavioral Envelope) detects manipulation-induced outputs that cross the declared boundary. **AAC-AO-59** at L3 extends coverage to adversarial manipulation testing. Partial: subtle prediction manipulation that stays within declared confidence and behavioral bounds is not detectable at the governance layer without purpose-built ML integrity monitoring. |
| Functional Extraction | AML.T0044 | **Not Addressed** | — | Model functional extraction (replication via systematic querying) is not meaningfully mitigable by the governance control plane beyond the access controls already noted under Collection. Rate limiting via AO-58 raises the cost but cannot prevent determined functional extraction over time. |
| Erode Model Integrity | AML.T0032 | **Mitigates** | AO-53, OG-25, AO-56 | **AAC-AO-53** (Dynamic Trust Adjustment) monitors behavioral KPIs and automatically demotes trust tier on degradation — model integrity erosion that produces measurable performance decline triggers an automatic governance response. **AAC-OG-25** (Policy Enforcement Integrity) detects behavioral drift from declared governance artifacts. **AAC-AO-56** (Governed Feedback Loop) at L2 ensures the feedback channel cannot be used to systematically erode model integrity without governance approval. |

---

## Gap Analysis — v1.3 to v2.0

| v1.3 Gap | Status in v2.0 | Closing Control |
|---|---|---|
| Dynamic supply chain integrity | **Closed** | AAC-ZT-77 (Dynamic Supply Chain Integrity) — provenance verification on all external tools, MCP servers, and components; cryptographically signed manifests at L2 |
| Output content integrity monitoring | **Closed (L3)** | AAC-OG-26 (Output Content Integrity Monitoring) — statistical inspection of outputs before delivery; closes AML.T0024.003 steganographic exfiltration gap |
| Adversarial benchmark specification | **Closed (L3)** | AAC-AO-59 (Adversarial Benchmark Specification) — declared adversarial test categories with MITRE ATLAS or equivalent threat taxonomy at L3; runtime anomaly monitoring |
| Model artifact recovery | **Addressed** | AAC-OG-29 (RS-40 parameter) + Tier 3 RS-40 guidance — RTO/RPO declared, rollback procedure required, test frequency specified; not a Tier 1/2 enforcement gate but a required governance parameter |
| Passive OSINT reconnaissance | **Remains** | Intentional — passive reconnaissance of publicly available information is outside the scope of any governance control plane. Architectural mitigations (minimal public disclosure, scrubbing public artifacts) are the appropriate response. |

**New gap identified in v2.0:** Subtle prediction manipulation within declared confidence and behavioral bounds (AML.T0046 partial) — this requires ML integrity monitoring architecture outside the governance control plane. Recommended future AAC enhancement: Tier 2 principle governing ML integrity monitoring requirements.

---

## Principal AAC Controls by ATLAS Tactic

| AAC Control | ATLAS Tactics Addressed |
|---|---|
| AAC-ZT-71 (Hostile Input Validation) | Execution, Defense Evasion, ML Attack Staging |
| AAC-ZT-75 (Instruction Isolation) | Execution, Defense Evasion |
| AAC-DA-63 (Enforcement Boundary) | Execution, Initial Access, Defense Evasion, Discovery |
| AAC-DA-60 (Tiered Arbitration) | Execution, Collection, Exfiltration, Impact |
| AAC-DA-61 (Liveness Guarantee) | Impact, Persistence |
| AAC-DA-62 (Confidence Enforcement) | Execution, Defense Evasion, Exfiltration, Impact |
| AAC-ZT-77 (Supply Chain Integrity) | Initial Access, Resource Development, Persistence |
| AAC-ZT-78 (Authorized Model Registry) | ML Attack Staging, Persistence, Impact |
| AAC-OG-25 (Policy Enforcement Integrity) | Defense Evasion, Persistence, Impact |
| AAC-OG-26 (Output Content Integrity) | Exfiltration |
| AAC-AO-53 (Dynamic Trust Adjustment) | Defense Evasion, Impact |
| AAC-AO-56 (Governed Feedback Loop) | Persistence, ML Attack Staging |
| AAC-AO-58 (Resource Governance) | Impact |
| AAC-AO-59 (Adversarial Benchmark) | ML Attack Staging, Defense Evasion, Impact |
| AAC-TB-29 (Behavioral Envelope) | Execution, Persistence, Impact |
| AAC-DP-07 (Audit Everything) | Discovery, Collection, Defense Evasion |
| AAC-ZT-66 (Short-Lived Credentials) | Collection |
| AAC-ZT-64/67/68 (Auth Chain) | Reconnaissance, Initial Access, Discovery |
| AAC-OG-29 (Implementation Profile) | Impact |

---

## Red Team Guidance

For red teams assessing AAC-compliant deployments, the highest-value attack surfaces at each maturity level are:

**Against an L1 deployment:**
The absence of safe mode monitoring, behavioral baseline, and adversarial testing creates exploitable gaps. The most productive attack vectors are: (1) indirect prompt injection through undeclared context sources not yet governed by OG-27; (2) model inversion and reconstruction via inference API — L1 lacks DP-09 and OG-26 coverage; (3) subtle prediction manipulation within declared confidence bounds — AO-51 KPI monitoring is L1 but may lack specificity without the L2 performance monitoring window. Behavioral envelope verification at L1 may use manual verification, creating a window between deployments.

**Against an L2 deployment:**
Safe mode and behavioral baseline provide significantly better coverage. Most productive vectors: (1) adversarial inputs designed to stay within confidence thresholds while producing harmful outputs — DA-62 requires threshold passage, not adversarial input detection; (2) supply chain attacks targeting the model artifact (ZT-78 is L3 — L2 relies on model source declaration, not full authorization records); (3) governance latency exploitation — the synchronous arbitration bound is a time window.

**Against an L3 deployment:**
The most complete governance posture. Remaining gaps are architectural rather than governance: (1) functional model extraction through systematic querying within declared rate limits; (2) subtle prediction manipulation within declared behavioral bounds; (3) passive OSINT reconnaissance of publicly available system information.

---

*This crosswalk is a threat modeling instrument. It should be read alongside the AAC Governance Framework Crosswalk, which serves a different purpose: governance alignment. The two documents are complementary.*

*This crosswalk is published under Apache License 2.0 as a companion document to the Autonomous Agentic Covenant v2.0 specification.*

*Thakuri, R. (2026). AAC v2.0 MITRE ATLAS Threat Mitigation Crosswalk. Companion to: The Autonomous Agentic Covenant (Version 2.0). Apache License 2.0.*
