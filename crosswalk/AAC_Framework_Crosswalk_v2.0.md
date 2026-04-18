# AAC v2.0 — Governance Framework Crosswalk

**Version:** 2.0
**Date:** April 2026
**Frameworks Covered:** CSA Agentic Trust Framework (ATF) · OWASP Agentic Top 10 (2026) · NIST AI Risk Management Framework 1.0
**Apache License 2.0**

---

## Purpose and Scope

This crosswalk maps every Tier 1 and Tier 2 principle of the Autonomous Agentic Covenant v2.0 to the three major governance frameworks against which the AAC is positioned. Tier 3 principles are implementation guidance and are not mapped — they support the governance layer without constituting enforcement obligations.

**Coverage ratings:**
- **Full** — The AAC principle directly addresses and satisfies the framework control or risk. The mapping is substantive, not incidental.
- **Partial** — The AAC principle addresses part of the framework control or risk, or provides a compensating mechanism without full coverage.
- **Gap** — The framework control or risk has no meaningful AAC coverage. Identified gaps are opportunities for future framework development.

**Key changes from v1.3:** The v2.0 crosswalk reflects significant structural changes — three enforcement tiers, three maturity levels, new principles (ZT-76, ZT-77, ZT-78, OG-27, OG-28, OG-29, AO-60, OG-26, RS-41, DA-64, OG-31), retired principles (TS-16, TS-17, AO-48, SM-46, AE-01/02/05, AP-30/31/32, TB-27), and six principles absorbed into consolidated controls. Coverage ratings reflect the revised principle set.

---

## Section 1 — CSA Agentic Trust Framework (ATF)

The CSA ATF is the most proximate peer framework to the AAC. Both address agentic system governance. The gaps in ATF coverage are the primary areas where AAC novel contributions apply — particularly the Decision Arbitration domain's liveness guarantee, the Authority Registry, and the Implementation Profile.

### Summary

| CSA ATF Control | Coverage | Primary AAC Controls |
|---|---|---|
| ATF-1.1: Agent Identity and Authentication | **Full** | ZT-64, ZT-67, ZT-76 |
| ATF-1.2: Agent Authorization and Least Privilege | **Full** | ZT-65, AO-52, OG-28 |
| ATF-1.3: Agent Delegation and Trust Inheritance | **Full** | AO-52, AO-53, AO-60, TS-13, TS-14 |
| ATF-2.1: Behavioral Specification and Constraints | **Full** | TB-29, OG-29, DA-59 |
| ATF-2.2: Goal and Objective Governance | **Full** | DNH-A, DNH-B, DA-59, DA-60 |
| ATF-2.3: Action Space Restrictions | **Full** | ZT-65, AO-52, TB-29, DA-60 |
| ATF-3.1: Context and Memory Security | **Full** | OG-27, ZT-71, ZT-75 |
| ATF-3.2: Tool and Plugin Governance | **Full** | ZT-77, ZT-71 |
| ATF-3.3: External Integration Security | **Full** | ZT-64, ZT-67, ZT-68, ZT-77 |
| ATF-4.1: Human Oversight and Control | **Full** | AI-12, AO-55, OG-28, RS-39 |
| ATF-4.2: Override and Intervention Mechanisms | **Full** | AI-12, RS-39, DNH-A |
| ATF-4.3: Escalation and Incident Response | **Full** | AO-55, DA-61, RS-39 |
| ATF-5.1: Audit Logging and Traceability | **Full** | DP-07, DA-60, DA-63 |
| ATF-5.2: Decision Explainability | **Partial** | DP-07, DA-60 |
| ATF-5.3: Compliance and Regulatory Alignment | **Partial** | OG-24, OG-29, ZT-76 |
| ATF-6.1: Data Minimization and Privacy | **Full** | DP-06, DP-09, DP-08 |
| ATF-6.2: Output Filtering and Sanitization | **Partial** | OG-26, ZT-71, ZT-75 |
| ATF-6.3: Sensitive Data Handling | **Full** | DP-06, DP-08, ZT-65 |
| ATF-7.1: Resiliency and Fault Tolerance | **Full** | DA-61, RS-39 |
| ATF-7.2: Resource Governance | **Full** | AO-58, DA-61 |
| ATF-7.3: Multi-Agent Coordination Security | **Full** | AO-54, AO-60, ZT-68, TS-13 |

**Overall:** 17 Full · 4 Partial · 0 Gap

---

### Detailed Mappings

#### ATF-1.1 — Agent Identity and Authentication | **Full**

Every agent request is independently authenticated and authorized per **AAC-ZT-64** (No Implicit Trust). The three-step auth-authz-validate sequence in **AAC-ZT-67** formalizes the authentication sequence. **AAC-ZT-76** (Non-Human Identity Disclosure) extends this to outbound requests — every agent discloses its identity, trust tier, and control plane ID on every outbound call. At L2, **AAC-ZT-68** (Authenticated Propagation) extends mutual authentication to service-to-service hops, preventing identity spoofing within agent chains.

---

#### ATF-1.2 — Agent Authorization and Least Privilege | **Full**

**AAC-ZT-65** (Least Privilege) declares minimum permissions per identity type — human, service, and agent. **AAC-AO-52** (Explicit Trust Tiers) maps every agent to an explicitly assigned trust tier governing which actions it may take. **AAC-OG-28** (Authority Registry) declares the authorized principals for each class of governance decision, forming the non-circular accountability chain that governs all authorization decisions.

---

#### ATF-1.3 — Agent Delegation and Trust Inheritance | **Full**

**AAC-AO-52** and **AAC-AO-53** together govern trust tier assignment and dynamic adjustment. **AAC-AO-60** (Recursive Governance Covenant) addresses delegation specifically — spawned agents operate at or below their creator's trust tier; equal-tier delegation requires explicit OG-28 principal authorization. **AAC-TS-13** (Trust Bounded by Provenance) declares that trust claims do not travel transitively. **AAC-TS-14** (Trust Is Graduated) formalizes the earned autonomy model — agents start at minimum authority and advance only through demonstrated accuracy.

---

#### ATF-2.1 — Behavioral Specification and Constraints | **Full**

**AAC-TB-29** (Agent Behavioral Envelope Verification) is the direct coverage — every agent declares a behavioral envelope (permitted action classes, prohibited action classes, output constraints, harm tier ceiling) before deployment. **AAC-OG-29** (Implementation Profile) formalizes the deployment-specific parameterization. **AAC-DA-59** (Harm Classification) provides the taxonomy against which behavioral constraints are evaluated at runtime.

---

#### ATF-2.2 — Goal and Objective Governance | **Full**

**AAC-DNH-A** (Active Harm Prohibition) establishes that no optimization objective may override a harm tier classification — the governance layer is not subordinated to business goals. **AAC-DNH-B** (Duty of Care) governs inaction — the system is obligated to act when foreseeable harm is detectable, regardless of whether acting serves optimization objectives. **AAC-DA-59** and **AAC-DA-60** together define the harm-classification-driven evaluation sequence that governs every action against declared governance objectives.

---

#### ATF-2.3 — Action Space Restrictions | **Full**

**AAC-ZT-65** (Least Privilege) restricts action scope to declared minimum permissions. **AAC-AO-52** (Trust Tiers) further restricts which action classes are available at each trust tier. **AAC-TB-29** (Behavioral Envelope) declares prohibited action classes explicitly — attempted execution is a system integrity violation per **AAC-DA-63**. **AAC-DA-60** enforces action restrictions at runtime through the deterministic arbitration layer.

---

#### ATF-3.1 — Context and Memory Security | **Full**

**AAC-OG-27** (Context Interface Contract) governs all context sources — undeclared sources are treated as hostile input. Assurance levels (1–5) and derivation depth bounds constrain context trust. **AAC-ZT-71** (Hostile Input Validation) addresses all external inputs including context payloads. **AAC-ZT-75** (Instruction Isolation) prevents user-supplied and externally-retrieved content from being treated as system directives.

---

#### ATF-3.2 — Tool and Plugin Governance | **Full**

**AAC-ZT-77** (Dynamic Supply Chain Integrity) is the direct coverage — every external tool and MCP server presents a verifiable identity and provenance claim before connection. Tools without valid provenance are treated as hostile under ZT-71 and refused connection. Dynamic tool discovery is disabled at L1; governance-approved discovery boundary declared at L2+.

---

#### ATF-3.3 — External Integration Security | **Full**

**AAC-ZT-64** and **AAC-ZT-67** ensure every external request is independently authenticated through the three-step sequence. **AAC-ZT-68** (Authenticated Propagation) extends authentication to service-to-service communication at L2. **AAC-ZT-77** closes the tool provenance gap. Together these four controls cover the full external integration surface.

---

#### ATF-4.1 — Human Oversight and Control | **Full**

**AAC-AI-12** (Override Always Available) mandates that every automated action has an accessible override path for any authorized OG-28 principal. For Tier 1 and Tier 2 actions, override paths are surfaced proactively before execution. **AAC-AO-55** (Escalation Hierarchy) declares the human oversight chain with time bounds. **AAC-OG-28** (Authority Registry) declares who holds override authority. **AAC-RS-39** (System Safe Mode) provides the system-level posture change mechanism including hard shutdown.

---

#### ATF-4.2 — Override and Intervention Mechanisms | **Full**

**AAC-AI-12** is the per-action override mechanism — tested, declared in the Implementation Profile, and available to all OG-28 principals. **AAC-RS-39** provides the system-level override via Safe Mode entry and hard shutdown capability. **AAC-DNH-A** includes a SOVEREIGN_OVERRIDE clause — the OG-28 principal holding this scope may override harm tier classifications, with immutable audit logging under DP-07.

---

#### ATF-4.3 — Escalation and Incident Response | **Full**

**AAC-AO-55** (Governed Escalation Hierarchy) declares the complete escalation chain with time bounds at each level. **AAC-DA-61** (Liveness Guarantee) ensures escalation cannot produce deadlock — the system executes a declared fallback when bounds are exceeded. **AAC-RS-39** (System Safe Mode) addresses system-level incident response including flap escalation and hard shutdown with mandatory governance review before resumption.

---

#### ATF-5.1 — Audit Logging and Traceability | **Full**

**AAC-DP-07** (Audit Everything) is direct and comprehensive — every automated decision produces an immutable log entry capturing originating agent, contributing agents, arbitration path, confidence score, harm tier assessment, and full decision ownership chain. The reasoning chain must be reconstructable from the log alone. **AAC-DA-60** records every arbitration evaluation outcome. **AAC-DA-63** logs all integrity violations immediately.

---

#### ATF-5.2 — Decision Explainability | **Partial**

**AAC-DP-07** requires the decision reasoning chain to be reconstructable from the audit log — this addresses after-the-fact explainability. The `include_reasoning` field in enforcement gates captures the full rationale. However, the AAC does not require real-time explainability to users during action execution — it requires auditability, which is the stronger governance property but not the full explainability obligation ATF-5.2 implies for human-facing systems.

---

#### ATF-5.3 — Compliance and Regulatory Alignment | **Partial**

**AAC-OG-24** (Governance as Code) requires all governance artifacts to be version-controlled, validity-bounded, and CI/CD integrated — the operational infrastructure for regulatory compliance. **AAC-OG-29** (Implementation Profile) formalizes the deployment-specific compliance parameterization. **AAC-ZT-76** addresses EU AI Act Article 52 transparency. The AAC does not prescribe specific regulatory frameworks — it provides the governance control plane infrastructure that regulatory compliance is built on. Organizations must map their specific regulatory obligations to AAC parameters in the Implementation Profile.

---

#### ATF-6.1 — Data Minimization and Privacy | **Full**

**AAC-DP-06** (Collect the Minimum) requires a data inventory as a governance artifact with functional justification for every collected element. **AAC-DP-08** (Encrypt Always) mandates transport and storage encryption verified at startup. **AAC-DP-09** (Least Disclosure) at L3 enforces field-level response scoping. Together these three principles cover the data minimization and privacy lifecycle from collection through storage through disclosure.

---

#### ATF-6.2 — Output Filtering and Sanitization | **Partial**

**AAC-OG-26** (Output Content Integrity Monitoring) at L3 inspects agent outputs before delivery for statistical patterns consistent with covert data exfiltration. **AAC-ZT-71** (Hostile Input Validation) filters inputs rather than outputs. **AAC-ZT-75** (Instruction Isolation) prevents instruction injection through output channels in multi-agent scenarios. The gap: the AAC does not require content filtering for harmful or inappropriate outputs beyond harm tier classification — output content governance is addressed through the behavioral envelope (TB-29) and harm classification (DA-59), not through a dedicated output filtering mechanism.

---

#### ATF-6.3 — Sensitive Data Handling | **Full**

**AAC-DP-06** governs what data is collected and why. **AAC-DP-08** requires encryption at rest and in transit for all data. **AAC-ZT-65** (Least Privilege) restricts data access to the minimum required for each agent's declared function. Together these three controls cover the sensitive data handling lifecycle.

---

#### ATF-7.1 — Resiliency and Fault Tolerance | **Full**

**AAC-DA-61** (Liveness Guarantee) is the foundational resiliency principle — every decision path has a declared time bound, a maximum escalation depth, and a safe fallback that executes on timeout. Governance cannot produce deadlock. **AAC-RS-39** (System Safe Mode) provides graceful degradation when health metrics deteriorate. The Tier 3 resiliency patterns (RS-34, RS-35, RS-36, RS-38, RS-41) provide implementation guidance for the operational resiliency posture.

---

#### ATF-7.2 — Resource Governance | **Full**

**AAC-AO-58** (Resource Constraint and Consumption Governance) declares per-agent compute budgets, API quotas, memory limits, and execution time bounds. Approaching threshold triggers automatic degradation under AI-10; violations are logged as trust tier evidence under AO-53. **AAC-DA-61** (Liveness Guarantee) ensures resource exhaustion cannot produce governance deadlock — the fallback executes within declared time bounds regardless of resource state.

---

#### ATF-7.3 — Multi-Agent Coordination Security | **Full**

**AAC-AO-54** (Cross-Agent Isolation) prevents trust tier inheritance between agents and classifies peer agent outputs before acting on them. **AAC-AO-60** (Recursive Governance Covenant) governs sub-agent spawning with signed lineage chains and depth limits. **AAC-ZT-68** (Authenticated Propagation) at L2 requires cryptographic mutual authentication on agent-to-agent communication. **AAC-TS-13** (Trust Bounded by Provenance) declares the non-transitive trust model that prevents trust claims from propagating through agent chains.

---

## Section 2 — OWASP Agentic Top 10 (2026)

The OWASP Agentic Top 10 is a risk taxonomy focused on the most critical security risks for autonomous agent systems. The AAC addresses all 10 risks, with 9 receiving Full coverage and 1 receiving Partial coverage.

### Summary

| OWASP Risk | Coverage | Primary AAC Controls |
|---|---|---|
| ASI-01: Prompt Injection | **Full** | ZT-71, ZT-75, DA-63 |
| ASI-02: Excessive Agency | **Full** | ZT-65, AO-52, TB-29, DA-60 |
| ASI-03: Agent Memory Poisoning | **Full** | OG-27, ZT-71, AO-56 |
| ASI-04: Tool and Integration Compromise | **Full** | ZT-77, ZT-71 |
| ASI-05: Cascading Agent Failures | **Full** | DA-61, RS-39, AO-55 |
| ASI-06: Insecure Agent Communication | **Full** | ZT-64, ZT-67, ZT-68, ZT-76 |
| ASI-07: Data and Privacy Exposure | **Full** | DP-06, DP-07, DP-08, DP-09, ZT-65 |
| ASI-08: Unconstrained Resource Consumption | **Full** | AO-58, DA-61, AI-10 |
| ASI-09: Agent Trust Boundary Violations | **Full** | TS-13, ZT-64, ZT-67, AO-52 |
| ASI-10: Misleading or Manipulative Behavior | **Partial** | DNH-B, AI-10, AI-12, OG-26 |

**Overall:** 9 Full · 1 Partial · 0 Gap

---

### Detailed Mappings

#### ASI-01 — Prompt Injection | **Full**

**AAC-ZT-71** (Hostile Input Validation) directly addresses prompt injection — all inputs including external retrieval content and peer agent outputs are validated and sanitized before processing. Unexpected fields are rejected; sandboxed processing is required at L2+. **AAC-ZT-75** (Instruction Isolation) architecturally separates system prompts from user-supplied and externally-retrieved content, preventing injected instructions from reaching the system prompt layer. **AAC-DA-63** (Centralized Enforcement Boundary) ensures that even if an injected instruction reaches the agent, it cannot produce a high-risk action without traversing the non-bypassable arbitration boundary.

---

#### ASI-02 — Excessive Agency | **Full**

**AAC-ZT-65** (Least Privilege) restricts every agent to minimum required permissions. **AAC-AO-52** (Explicit Trust Tiers) maps every agent to a trust tier governing its permitted action scope — no agent self-assigns authority. **AAC-TB-29** (Behavioral Envelope) declares prohibited action classes explicitly — attempted execution is a governance integrity violation. **AAC-DA-60** enforces the evaluation path based on harm tier, preventing high-risk actions from executing without satisfying the full arbitration sequence. Together these four controls directly address the excessive agency risk surface.

---

#### ASI-03 — Agent Memory Poisoning | **Full**

**AAC-OG-27** (Context Interface Contract) governs all context sources — undeclared sources are treated as hostile input. Assurance levels bound how much authority context receives in confidence calculations. Derivation depth limits prevent trust from being laundered through chained context hops. **AAC-ZT-71** validates all inputs including retrieval content before it enters the context window. **AAC-AO-56** (Governed Feedback Loop) at L2 monitors the feedback pipeline for adversarial injection — anomalous override patterns are integrity violations, not training data.

---

#### ASI-04 — Tool and Integration Compromise | **Full**

**AAC-ZT-77** (Dynamic Supply Chain Integrity) is the direct control — every external tool, MCP server, and agent component presents a verifiable identity and provenance claim before connection. Cryptographically signed manifests are required at L2; components without valid provenance are refused connection. Dynamic tool discovery is disabled at L1 — only pre-approved integrations listed in the integration registry are permitted. **AAC-ZT-71** treats tool responses as hostile input requiring validation.

---

#### ASI-05 — Cascading Agent Failures | **Full**

**AAC-DA-61** (Liveness Guarantee) directly addresses cascading failure — governance constraints cannot produce deadlock, and a system that stalls indefinitely is a failure equivalent to an incorrect decision. Declared fallback actions execute within time bounds regardless of downstream state. **AAC-RS-39** (System Safe Mode) provides system-level degradation when health metrics deteriorate, preventing cascading failures from propagating through the governance layer. **AAC-AO-55** (Escalation Hierarchy) ensures unresolved situations escalate rather than stall. The Tier 3 RS-36 pattern covers circuit breakers for external dependency cascades.

---

#### ASI-06 — Insecure Agent Communication | **Full**

**AAC-ZT-64** (No Implicit Trust) requires independent authentication of every request — no network position grants access. **AAC-ZT-67** (Auth-Authz-Validate) enforces the three-step sequence on every communication. **AAC-ZT-68** (Authenticated Propagation) at L2 requires cryptographic mutual authentication on service-to-service communication. **AAC-ZT-76** (Non-Human Identity Disclosure) requires agent identity declaration on every outbound request, enabling receiving systems to identify and appropriately handle agentic communication.

---

#### ASI-07 — Data and Privacy Exposure | **Full**

**AAC-DP-06** (Collect the Minimum) governs what data is collected. **AAC-DP-07** (Audit Everything) creates an immutable record of every data access decision. **AAC-DP-08** (Encrypt Always) protects data at rest and in transit. **AAC-DP-09** (Least Disclosure) at L3 enforces field-level response scoping. **AAC-ZT-65** (Least Privilege) restricts data access to the minimum required for each declared function. Together these five controls provide comprehensive data and privacy exposure coverage.

---

#### ASI-08 — Unconstrained Resource Consumption | **Full**

**AAC-AO-58** (Resource Constraint Governance) directly addresses unconstrained consumption — per-agent compute budgets, API quotas, memory limits, and execution time bounds are declared governance artifacts. Approaching threshold triggers automatic degradation under **AAC-AI-10** (Confidence Thresholds and Graceful Degradation). Violations are logged as trust tier evidence under AO-53. **AAC-DA-61** ensures resource exhaustion cannot produce governance deadlock — fallbacks execute within time bounds.

---

#### ASI-09 — Agent Trust Boundary Violations | **Full**

**AAC-TS-13** (Trust Bounded by Provenance) declares the non-transitive trust model — trust claims do not propagate across boundaries without re-validation. **AAC-ZT-64** and **AAC-ZT-67** enforce this at the authentication layer. **AAC-AO-52** (Explicit Trust Tiers) ensures every agent operates within its declared authority scope. **AAC-AO-60** (Recursive Governance Covenant) prevents trust boundary violations in agent spawning — spawned agents cannot exceed their creator's trust tier without explicit authorization.

---

#### ASI-10 — Misleading or Manipulative Behavior | **Partial**

**AAC-DNH-B** (Duty of Care) obligates the system to respond to foreseeable harm signals, which includes detecting when agent behavior is misleading users into harmful decisions. **AAC-AI-10** (Confidence Thresholds) prevents agents from presenting high confidence in low-confidence outputs at the arbitration layer. **AAC-AI-12** (Override Always Available) ensures users can always reject automated outputs, limiting the harm from manipulative behavior. **AAC-OG-26** (Output Content Integrity Monitoring) at L3 inspects outputs for statistical anomalies.

The gap: the AAC does not include a dedicated principle governing deceptive or manipulative agent behavior directed at users — the coverage is through compensating controls. The Tier 3 guidance in DNH-0d (Trust Harm Prevention in Recommendation Systems) addresses dark patterns, but this is design guidance rather than enforcement. This represents the most significant remaining gap between the AAC and the full OWASP ASI-10 risk scope.

---

## Section 3 — NIST AI Risk Management Framework 1.0

The NIST AI RMF 1.0 provides a strategic risk management structure organized around four functions: GOVERN, MAP, MEASURE, and MANAGE. The AAC provides strong operational coverage of the MANAGE and GOVERN functions. MAP and MEASURE are partially addressed — the AAC specifies what must be governed, not the risk identification and measurement processes that precede governance deployment.

### Summary

| NIST AI RMF Function / Category | Coverage | Primary AAC Controls |
|---|---|---|
| GOVERN 1.1: Legal and Regulatory Requirements | **Partial** | OG-24, OG-29, ZT-76 |
| GOVERN 1.2: Trustworthy AI Characteristics | **Full** | DNH-0, DNH-A, DNH-B, DA-59–63 |
| GOVERN 1.3: Risk Management Processes | **Full** | OG-28, OG-29, OG-24, AO-55 |
| GOVERN 1.4: Organizational Risk Policies | **Full** | OG-28, OG-24, OG-29 |
| GOVERN 1.5: Organizational Risk Culture | **Partial** | OG-28, TS-14 |
| GOVERN 1.6: Policies for TEVV | **Full** | TB-29, AO-59, OG-24 |
| GOVERN 2.1: AI Risk Tolerance | **Full** | DA-59, OG-29, DA-60 |
| GOVERN 2.2: Organizational Inventory | **Full** | OG-29, AO-52, DP-06 |
| GOVERN 3.1: Roles and Responsibilities | **Full** | OG-28, AO-55 |
| GOVERN 4.1: Team Diversity and Expertise | **Gap** | — |
| GOVERN 5.1: Policies and Procedures | **Full** | OG-24, OG-29, OG-28 |
| GOVERN 5.2: Mechanisms for AI Risk Management | **Full** | DA-60, DA-61, DA-63, RS-39 |
| GOVERN 6.1: Third Party Risk Policies | **Full** | ZT-77, ZT-78, OG-27 |
| MAP 1.1: Context Establishment | **Partial** | OG-29, DA-59 |
| MAP 1.5: Organizational Risk Tolerance | **Full** | DA-59, OG-29, DA-60 |
| MAP 2.1: Scientific and Technical Knowledge | **Partial** | DA-60, DA-62 |
| MAP 3.5: AI Risk Identification | **Partial** | DA-59, OG-25, AO-51 |
| MEASURE 1.1: Measurement Methods | **Partial** | TB-29, AO-59, AO-51 |
| MEASURE 2.1: AI Risk Evaluation | **Full** | DA-60, DA-62, AO-51 |
| MEASURE 2.5: Bias and Fairness | **Partial** | AO-51, AO-56 |
| MEASURE 2.6: Privacy Risk | **Full** | DP-06, DP-07, DP-08 |
| MEASURE 2.7: Security Risk | **Full** | ZT-64–77, DA-63 |
| MEASURE 3.1: Risk Tracking | **Full** | DP-07, OG-25, AO-53 |
| MEASURE 4.1: Feedback Mechanisms | **Full** | AO-56, AO-51, DP-07 |
| MANAGE 1.1: Risk Treatment | **Full** | DA-60, DNH-A, DNH-B, DA-61 |
| MANAGE 1.2: Risk Prioritization | **Full** | DA-59, DA-60 |
| MANAGE 2.1: Response and Recovery | **Full** | DA-61, RS-39, AO-55 |
| MANAGE 2.4: Incident Disclosure | **Partial** | DP-07, AO-55 |
| MANAGE 3.1: Risk Monitoring | **Full** | OG-25, AO-51, AO-53 |
| MANAGE 4.1: Risk Communication | **Partial** | DP-07, ZT-76 |

**Overall:** 20 Full · 9 Partial · 1 Gap

---

### Detailed Mappings

#### GOVERN 1.1 — Legal and Regulatory Requirements | **Partial**

**AAC-OG-24** (Governance as Code) requires governance artifacts to be version-controlled, validity-bounded, and maintained with the same rigor as production code — the operational infrastructure for regulatory compliance. **AAC-OG-29** (Implementation Profile) formalizes deployment-specific regulatory parameterization. **AAC-ZT-76** addresses EU AI Act Article 52 transparency obligations. The gap: the AAC does not prescribe specific regulatory frameworks or require regulatory compliance mapping — organizations must populate the Implementation Profile's `regulatory_context` field and complete their own compliance mapping. The AAC provides the governance control plane; regulatory compliance requires organizational policy layer on top.

---

#### GOVERN 1.2 — Trustworthy AI Characteristics | **Full**

**AAC-DNH-0** (Root Principle) establishes the foundational trustworthy AI commitment. **AAC-DNH-A** (Active Harm Prohibition) and **AAC-DNH-B** (Duty of Care) operationalize it as enforceable runtime gates. The entire Decision Arbitration domain (**DA-59 through DA-63**) provides the deterministic enforcement mechanism. The AAC's stateless, auditable control plane directly instantiates NIST's trustworthy AI properties: accuracy (DA-62), reliability (DA-61 liveness guarantee), safety (DNH-A), security (ZT domain), explainability (DP-07), privacy (DP domain), and fairness (AO-51 KPI set).

---

#### GOVERN 1.3 — Risk Management Processes | **Full**

**AAC-OG-28** (Authority Registry) declares accountability for all governance decisions. **AAC-OG-29** (Implementation Profile) formalizes the deployment-specific risk management parameterization. **AAC-OG-24** (Governance as Code) requires governance artifacts to follow software engineering rigor. **AAC-AO-55** (Escalation Hierarchy) declares the risk escalation process with time bounds at each level. Together these four controls operationalize the risk management process infrastructure.

---

#### GOVERN 1.4 — Organizational Risk Policies | **Full**

**AAC-OG-28** declares who holds governance authority. **AAC-OG-24** requires governance policies to be versioned, validity-bounded, and treated as production code. **AAC-OG-29** formalizes the deployment-specific policy parameterization as a signed compliance artifact. These three controls directly implement organizational risk policy infrastructure.

---

#### GOVERN 1.5 — Organizational Risk Culture | **Partial**

**AAC-OG-28** (Authority Registry) makes governance accountability explicit and auditable — a structural support for risk culture. **AAC-TS-14** (Trust Is Graduated) embeds the asymmetric ratchet principle (expand carefully, contract fast) as a governance requirement. The gap: the AAC governs systems, not organizations — organizational risk culture is a human and process concern that the AAC's control plane cannot enforce. The framework creates the conditions for a governance culture by making accountability visible and auditable.

---

#### GOVERN 1.6 — Policies for Testing, Evaluation, Validation, and Verification (TEVV) | **Full**

**AAC-TB-29** (Agent Behavioral Envelope Verification) requires pre-deployment verification of behavioral envelope compliance as a governance artifact. **AAC-AO-59** (Adversarial Benchmark Specification) at L3 requires adversarially constructed verification against declared threat taxonomy. **AAC-OG-24** requires all governance artifacts including test results to be versioned and validity-bounded. Together these controls operationalize the TEVV policy requirement.

---

#### GOVERN 2.1 — AI Risk Tolerance | **Full**

**AAC-DA-59** (Harm Classification) is the risk tolerance specification — the three-tier taxonomy declares what levels of harm are acceptable (Tier 3/friction), require human review (Tier 2/material), or are absolutely prohibited (Tier 1/irreversible). **AAC-OG-29** (Implementation Profile) formalizes the deployment-specific risk tolerance parameterization. **AAC-DA-60** enforces risk tolerance through the tiered evaluation path — Tier 1 actions require the full arbitration sequence with no abbreviation permitted.

---

#### GOVERN 2.2 — Organizational AI Inventory | **Full**

**AAC-OG-29** (Implementation Profile) requires a per-system governance artifact before initialization — the system-level inventory. **AAC-AO-52** (Explicit Trust Tiers) requires every agent to be declared in the agent registry — the agent-level inventory. **AAC-DP-06** (Collect the Minimum) requires a data inventory as a governance artifact. Together these three controls provide the organizational AI inventory infrastructure at system, agent, and data levels.

---

#### GOVERN 3.1 — Roles and Responsibilities | **Full**

**AAC-OG-28** (Authority Registry) is the direct control — every governance decision class has a declared authorized principal with documented establishment mechanism, scope, and revocation conditions. The non-circular chain ensures every authority claim is traceable. **AAC-AO-55** declares the escalation hierarchy with named principals at each level. Together these two controls operationalize the roles and responsibilities requirement in a machine-verifiable form.

---

#### GOVERN 4.1 — Team Diversity and Expertise | **Gap**

The AAC does not address organizational team composition. This is a people and process governance concern outside the scope of a technical control plane specification. Organizations must address team diversity and expertise requirements through organizational policy. This gap is intentional — the AAC governs deployed systems, not the organizations that build them.

---

#### GOVERN 5.1 — Policies and Procedures | **Full**

**AAC-OG-24** (Governance as Code) requires all policies to be versioned, validity-bounded, and CI/CD integrated. **AAC-OG-29** (Implementation Profile) is the policy instantiation artifact. **AAC-OG-28** (Authority Registry) declares who holds policy authority. Together these three controls implement the policies and procedures governance requirement with the rigor of production software.

---

#### GOVERN 5.2 — Mechanisms for AI Risk Management | **Full**

**AAC-DA-60** (Deterministic Arbitration Layer) is the runtime risk management mechanism — every high-risk action traverses a fixed evaluation sequence before execution. **AAC-DA-61** (Liveness Guarantee) ensures the mechanism cannot deadlock. **AAC-DA-63** (Centralized Enforcement Boundary) makes the mechanism non-bypassable. **AAC-RS-39** (System Safe Mode) provides the system-level risk management posture for degraded conditions. Together these form the technical risk management mechanism the framework requires.

---

#### GOVERN 6.1 — Third Party Risk Policies | **Full**

**AAC-ZT-77** (Dynamic Supply Chain Integrity) governs third-party tool and integration risk — all external components require verifiable provenance before connection. **AAC-ZT-78** (Authorized Model Registry) at L3 governs third-party model artifact risk through explicit authorization records with residual risk acceptance for unknown provenance. **AAC-OG-27** (Context Interface Contract) governs third-party context sources through declared assurance levels.

---

#### MAP 1.1 — Context Establishment | **Partial**

**AAC-OG-29** (Implementation Profile) formalizes the deployment context declaration. **AAC-DA-59** (Harm Classification) establishes the risk context taxonomy for the governed system. The gap: MAP 1.1 includes broader organizational context — intended use cases, stakeholder impact, societal context — that the AAC does not require. The Implementation Profile's `regulatory_context` and `compliance_targets` fields provide partial coverage, but organizational context mapping requires process beyond the control plane.

---

#### MAP 1.5 — Organizational Risk Tolerance | **Full**

Covered by the harm tier taxonomy (DA-59) and Implementation Profile (OG-29) — as described under GOVERN 2.1. The risk tolerance is machine-verifiable through the DA-60 tiered evaluation paths.

---

#### MAP 2.1 — Scientific and Technical Knowledge | **Partial**

**AAC-DA-60** (Deterministic Arbitration) requires the arbitration layer to use deterministic logic — a technical requirement informed by the current state of AI verification capability. **AAC-DA-62** (Confidence Enforcement) requires confidence verification to use calibration data and threshold registries. The gap: the AAC specifies technical requirements without requiring organizations to maintain scientific knowledge of AI system behavior — this is a process and expertise requirement beyond the control plane.

---

#### MAP 3.5 — AI Risk Identification | **Partial**

**AAC-DA-59** (Harm Classification) establishes the risk identification taxonomy. **AAC-OG-25** (Policy Enforcement Integrity) provides continuous runtime risk monitoring. **AAC-AO-51** (Self-Monitoring) extends risk identification to behavioral KPI monitoring. The gap: MAP 3.5 includes stakeholder impact mapping and societal risk identification that the AAC does not address — its risk identification scope is bounded to the governed system's action surface.

---

#### MEASURE 1.1 — Measurement Methods | **Partial**

**AAC-TB-29** (Behavioral Envelope Verification) defines the pre-deployment measurement requirement. **AAC-AO-59** (Adversarial Benchmark) at L3 extends measurement to adversarial conditions. **AAC-AO-51** (Self-Monitoring) declares the KPI-based runtime measurement framework. The gap: NIST MEASURE 1.1 includes broader measurement methodology requirements — statistical methods, evaluation criteria — beyond what the AAC prescribes. The AAC specifies that measurement must occur and what it must demonstrate; the methodology is implementation-specific.

---

#### MEASURE 2.1 — AI Risk Evaluation | **Full**

**AAC-DA-60** (Tiered Arbitration) evaluates every action's risk before execution. **AAC-DA-62** (Confidence Enforcement) independently verifies the proposing agent's confidence claim. **AAC-AO-51** (Self-Monitoring) continuously evaluates behavioral risk against declared KPIs. Together these three controls implement continuous AI risk evaluation at the action level.

---

#### MEASURE 2.5 — Bias and Fairness | **Partial**

**AAC-AO-51** (Self-Monitoring KPI set) requires at least one fairness metric per consequential-decision agent at L2 — declared as a first-class KPI alongside accuracy and latency. **AAC-AO-56** (Governed Feedback Loop) requires bias review before any feedback-triggered model update deploys. The gap: the AAC specifies that fairness must be monitored and that bias review must occur, but does not prescribe fairness measurement methodologies, protected class definitions, or acceptable bias thresholds — these are implementation-specific and regulatory-context-dependent declarations in the Implementation Profile.

---

#### MEASURE 2.6 — Privacy Risk | **Full**

**AAC-DP-06** (Collect the Minimum) requires data inventory with functional justification. **AAC-DP-07** (Audit Everything) creates an immutable decision log including data access decisions. **AAC-DP-08** (Encrypt Always) addresses privacy risk through cryptographic data protection. These three controls directly address privacy risk measurement and management.

---

#### MEASURE 2.7 — Security Risk | **Full**

The entire Zero-Trust domain (**ZT-64 through ZT-78**) addresses security risk measurement and management. **AAC-DA-63** (Centralized Enforcement Boundary) provides the non-bypassable security enforcement mechanism. The MITRE ATLAS crosswalk provides detailed security risk measurement against adversarial technique taxonomy.

---

#### MEASURE 3.1 — Risk Tracking | **Full**

**AAC-DP-07** (Audit Everything) creates the immutable risk event record. **AAC-OG-25** (Policy Enforcement Integrity) provides continuous runtime risk tracking against declared governance artifacts. **AAC-AO-53** (Dynamic Trust Adjustment) tracks behavioral risk through performance evidence and automatically adjusts trust tier on degradation. Together these three controls implement continuous risk tracking.

---

#### MEASURE 4.1 — Feedback Mechanisms | **Full**

**AAC-AO-56** (Governed Feedback Loop) is the direct control — every override, escalation, near-miss, and failed decision is a signal in a declared behavioral feedback process. Proposed updates are validated against regression guardrails and approved through the same governance process as trust tier advancement. **AAC-AO-51** (Self-Monitoring) provides the KPI-based automated feedback trigger. **AAC-DP-07** provides the audit trail that makes feedback traceable.

---

#### MANAGE 1.1 — Risk Treatment | **Full**

**AAC-DA-60** implements risk treatment at the action level — Tier 1 actions require the full five-step arbitration sequence; Tier 2 actions require confidence verification, override check, and policy check; Tier 3 actions receive ZT+Audit treatment. **AAC-DNH-A** and **AAC-DNH-B** provide the absolute risk treatment constraints. **AAC-DA-61** ensures risk treatment cannot produce deadlock — fallback actions execute within declared time bounds.

---

#### MANAGE 1.2 — Risk Prioritization | **Full**

**AAC-DA-59** (Harm Classification) is the risk prioritization taxonomy — the three-tier structure prioritizes governance resources proportionate to harm potential. **AAC-DA-60** operationalizes the prioritization through tiered evaluation paths — higher harm tier actions receive more intensive governance scrutiny. The pre-classified action registry (DA-59) enables O(1) runtime prioritization without per-action computation.

---

#### MANAGE 2.1 — Response and Recovery | **Full**

**AAC-DA-61** (Liveness Guarantee) requires every decision path to have a declared safe fallback — the response mechanism when governance cannot identify a permitted action. **AAC-RS-39** (System Safe Mode) provides system-level response to degraded conditions. **AAC-AO-55** (Escalation Hierarchy) declares the human response chain for situations requiring principal intervention. Together these three controls implement the response and recovery framework.

---

#### MANAGE 2.4 — Incident Disclosure | **Partial**

**AAC-DP-07** (Audit Everything) provides the immutable incident record required for disclosure. **AAC-AO-55** (Escalation Hierarchy) routes incidents to the appropriate governance authority. The gap: the AAC does not require external incident disclosure — notification to regulators, affected parties, or the public is a regulatory and organizational policy obligation that the AAC's control plane cannot enforce. The audit trail (DP-07) and escalation chain (AO-55) provide the infrastructure for disclosure; the disclosure obligation itself is outside AAC scope.

---

#### MANAGE 3.1 — Risk Monitoring | **Full**

**AAC-OG-25** (Policy Enforcement Integrity) provides continuous runtime monitoring against declared governance artifacts. **AAC-AO-51** (Self-Monitoring) requires agents to monitor their own KPIs against declared thresholds. **AAC-AO-53** (Dynamic Trust Adjustment) automatically responds to performance degradation within the declared monitoring window. Together these three controls implement continuous risk monitoring with automated response.

---

#### MANAGE 4.1 — Risk Communication | **Partial**

**AAC-DP-07** (Audit Everything) provides the auditable record that enables risk communication to internal stakeholders. **AAC-ZT-76** (Non-Human Identity Disclosure) communicates agent identity to external parties on every outbound request. The gap: systematic risk communication to external stakeholders — regulators, affected parties, the public — is outside the AAC's technical control plane scope. The framework enables risk communication through its audit infrastructure; the communication process itself requires organizational policy.

---

## Coverage Summary

### CSA Agentic Trust Framework

| Rating | Count | Percentage |
|---|---|---|
| Full | 17 | 81% |
| Partial | 4 | 19% |
| Gap | 0 | 0% |

Gaps from v1.3 closed in v2.0: ATF-3.2 (Tool Governance) — closed by ZT-77. ATF-7.3 (Multi-Agent Coordination) — closed by AO-54 and AO-60. ATF-4.2 (Override Mechanisms) — strengthened by RS-39 hard shutdown and SOVEREIGN_OVERRIDE clause in DNH-A.

### OWASP Agentic Top 10

| Rating | Count | Percentage |
|---|---|---|
| Full | 9 | 90% |
| Partial | 1 | 10% |
| Gap | 0 | 0% |

Gaps from v1.3 closed in v2.0: ASI-04 (Tool and Integration Compromise) — closed by ZT-77. Remaining partial: ASI-10 (Misleading Behavior) — compensating controls present; dedicated enforcement principle remains a future enhancement opportunity.

### NIST AI RMF 1.0

| Rating | Count | Percentage |
|---|---|---|
| Full | 20 | 67% |
| Partial | 9 | 30% |
| Gap | 1 | 3% |

The single gap (GOVERN 4.1 — Team Diversity) is intentional and permanent — the AAC governs deployed systems, not organizational team composition. Partial ratings in the MAP and MEASURE functions reflect the AAC's deliberate scope: the framework specifies what the governance control plane must enforce, not the organizational processes that precede deployment.

---

## Novel AAC Contributions with No Peer Framework Equivalent

The following AAC v2.0 principles address risks or governance requirements not covered by CSA ATF, OWASP Agentic Top 10, or NIST AI RMF 1.0:

| AAC Principle | Novel Contribution | Why No Peer Coverage |
|---|---|---|
| AAC-DA-61 — Liveness Guarantee | Governance cannot produce deadlock — a system that cannot make forward progress under its own safety constraints has a design defect | Peer frameworks specify what to prohibit; none address the resolution guarantee when prohibitions conflict |
| AAC-DA-60 — Tiered Evaluation Paths | Evaluation depth determined by harm tier (T3=ZT+Audit; T2=Confidence+Override+Policy; T1=Full sequence) | Peer frameworks treat governance as binary (applies/doesn't); AAC ties governance intensity to risk level |
| AAC-OG-28 — Authority Registry | Non-circular accountability chain declared as machine-verifiable governance artifact | Peer frameworks require accountability; none specify a machine-verifiable non-circular chain |
| AAC-OG-29 — Implementation Profile | Parameterization boundary between specification and governed system, signed by governance authority | Peer frameworks describe what to do; none formalize the deployment-specific instantiation as a signed artifact |
| AAC-AO-60 — Recursive Governance Covenant | Sub-agent spawning with signed lineage chain; ceiling-not-floor trust inheritance | Multi-agent governance is acknowledged by peer frameworks but no framework specifies the spawning governance mechanism |
| AAC-TB-29 — Behavioral Envelope Verification | Envelope-only declaration enabling open-ended agent reasoning within declared boundaries | Peer frameworks address testing; none specify the pre-deployment behavioral boundary declaration as the governance mechanism |
| AAC-DA-63 — Non-Bypassable Enforcement Boundary | Architectural requirement with integrity violation logging | Peer frameworks recommend centralized governance; none specify non-bypassability as a structural requirement |

---

*This crosswalk is published under Apache License 2.0 as a companion document to the Autonomous Agentic Covenant v2.0 specification.*

*Thakuri, R. (2026). AAC v2.0 Governance Framework Crosswalk. Companion to: The Autonomous Agentic Covenant (Version 2.0). Apache License 2.0.*
