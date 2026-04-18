
# The Autonomous Agentic Covenant (AAC)

**A Governance Control Plane Specification for Autonomous and AI-Driven Systems**

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)
[![Version](https://img.shields.io/badge/Version-2.0-blue.svg)](CHANGELOG.md)
[![Principles](https://img.shields.io/badge/Principles-67-green.svg)](covenant/AAC_v2.0.md)
[![Maturity Levels](https://img.shields.io/badge/Maturity-L1%20%7C%20L2%20%7C%20L3-orange.svg)](profiles/)

---

## What Is the AAC?

The Autonomous Agentic Covenant is an AI governance firewall for autonomous agent actions. It is a governance control plane specification — not a policy document — that defines how agentic systems must be governed before, during, and after deployment.

The framework organizes 67 governance principles across three enforcement tiers:

- **Tier 1 — COVENANT CORE:** Runtime logic gates evaluated per-action by the arbitration layer. Binary pass/fail.
- **Tier 2 — COVENANT GOVERNANCE:** Pre-deployment declarations that must exist as versioned governance artifacts before the control plane can initialize.
- **Tier 3 — COVENANT GUIDANCE:** Implementation patterns that support the governance layer without constituting enforcement.

The governance control plane is **stateless** — each action is evaluated independently against pre-declared governance artifacts, enabling horizontal scaling without coordination overhead and ensuring enforcement decisions are reproducible and auditable by construction.

The AAC v2.0 specification does not define abstract design principles. It defines enforceable runtime logic gates and pre-declared governance artifacts that collectively govern every agent action. This framework codifies ethics, safety constraints, and governance controls as explicit, version-controlled, and auditable first-class artifacts — not policies to be interpreted, but enforcement conditions to be tested.

---

## Who Is This For?

- **Security architects** designing governance structures for autonomous AI deployments
- **Engineering teams** building agentic systems who need clear, stable, testable design requirements
- **Governance and compliance teams** mapping AI controls to existing frameworks (NIST AI RMF, CSA ATF, EU AI Act, OWASP Agentic Top 10)
- **CISOs and risk leaders** establishing organizational standards for agentic AI
- **Researchers and framework builders** looking for a practitioner-authored reference with prior art standing

---

## Maturity Levels

The AAC v2.0 introduces a three-level maturity framework that determines which principles are required for a given deployment:

| Level | Name | Description | Target |
|---|---|---|---|
| **L1** | Foundational | Minimum viable governance posture. 24 principles required. | Any organization deploying autonomous agents |
| **L2** | Mature | Regulated industry posture. Full control plane governance. | Financial services, healthcare, critical infrastructure |
| **L3** | Optimizing | Gold standard. EU AI Act high-risk compliance. | Advanced multi-agent systems; EU AI Act regulated deployments |

Each level subsumes the previous. An L2 deployment satisfies all L1 requirements. Principles with operational gradients carry **Maturity Profile** tables showing what changes at each level.

---

## What's in This Repository

```
autonomous-agentic-covenant/
├── README.md                                      <- this file
├── LICENSE                                        <- Apache 2.0
├── CHANGELOG.md                                   <- version history
├── covenant/
│   ├── AAC_v2.0.md                               <- primary specification (current)
│   └── AAC_v1.3.md                               <- prior version (reference)
├── profiles/
│   ├── AAC_Implementation_Profile_L1_v2.0.md     <- L1 Foundational template
│   └── AAC_Implementation_Profile_L2L3_v2.0.md   <- L2 and L3 Annexes
├── schema/
│   ├── aac_v2.0_schema.json                      <- JSON Schema (maturity-aware)
│   └── aac_v2.0_instance_fsi.json                <- FSI reference instance (L1)
├── crosswalk/
│   ├── AAC_Framework_Crosswalk_v2.0.md           <- CSA ATF / OWASP / NIST mapping
│   └── AAC_ATLAS_Crosswalk_v2.0.md               <- MITRE ATLAS threat mitigation mapping
│   └── AAC_EU_AI_Act_Crosswalk_v2.0.md           <- EU AI Act 2026 mapping
└── governance/
    └── CONTRIBUTING.md                            <- contribution process
```

**`covenant/`** — The framework specification. Start here. v1.3 is retained for organizations that have mapped compliance programs to prior identifiers — all v1.3 control identifiers that survive into v2.0 retain their original IDs.

**`profiles/`** — Two-document Implementation Profile set. The L1 document covers all Foundational parameters and can be completed independently. The L2/L3 Annexes extend it for Mature and Optimizing deployments. Both include a financial services worked example and a governance sign-off block.

**`schema/`** — Machine-readable schema and reference instance. The JSON Schema uses draft-07 `if-then` conditionals to enforce maturity-level-specific requirements based on `metadata.maturity_level`. A single schema serves all three maturity levels.

**`crosswalk/`** — Two crosswalk documents serving distinct purposes. The Framework Crosswalk is a governance-to-governance alignment exercise. The ATLAS Crosswalk is a threat modeling instrument.

---

## How to Use the AAC

### Path 1 — Read the specification

Start with [`covenant/AAC_v2.0.md`](covenant/AAC_v2.0.md). The domain index links to each domain section. Every principle has a stable anchor (e.g. `#aac-zt-64`) for direct reference in ADRs, tickets, and documentation.

### Path 2 — Deploy a system against it

**Step 1:** Determine your maturity level (L1, L2, or L3) based on your regulatory context and operational capability.

**Step 2:** Complete [`profiles/AAC_Implementation_Profile_L1_v2.0.md`](profiles/AAC_Implementation_Profile_L1_v2.0.md). Seven governance concern groups with a financial services worked example filling every field.

**Step 3:** If declaring L2 or L3, complete [`profiles/AAC_Implementation_Profile_L2L3_v2.0.md`](profiles/AAC_Implementation_Profile_L2L3_v2.0.md) as a companion.

**Step 4:** Instantiate the governance configuration using [`schema/aac_v2.0_schema.json`](schema/aac_v2.0_schema.json). The FSI reference instance at [`schema/aac_v2.0_instance_fsi.json`](schema/aac_v2.0_instance_fsi.json) demonstrates a complete L1 deployment.

**Step 5:** Get the Implementation Profile signed by the OG-28 authority declared in the Authority Registry. The governance control plane may not initialize against an unsigned profile.

### Path 3 — Map to your existing frameworks

**Governance alignment** — [`crosswalk/AAC_Framework_Crosswalk_v1.0.docx`](crosswalk/AAC_Framework_Crosswalk_v1.0.docx):

| Framework | Coverage |
|---|---|
| CSA Agentic Trust Framework (ATF) | 27 Full · 18 Partial · 11 Gap |
| OWASP Agentic Top 10 (2026) | 9/10 Full · 1 Partial |
| NIST AI RMF 1.0 | 18 Full · 5 Partial · 1 Gap |

**Threat modeling** — [`crosswalk/AAC_ATLAS_Crosswalk_v1.0.docx`](crosswalk/AAC_ATLAS_Crosswalk_v1.0.docx): AAC controls mapped to MITRE ATLAS v5.4.0 adversarial techniques across all 16 tactics.

---

## Control Identifier Format

Every principle carries a stable identifier: `AAC-[DOMAIN]-[NUMBER]`

| Prefix | Domain | Tier |
|---|---|---|
| `AAC-DNH-xx` | Do No Harm | T1 + T2 |
| `AAC-DA-xx` | Decision Arbitration | T1 + T3 |
| `AAC-ZT-xx` | Zero-Trust Security | T1 + T2 + T3 |
| `AAC-AI-xx` | AI & Intelligent Automation | T1 + T3 |
| `AAC-AO-xx` | Autonomous Operations | T1 + T2 |
| `AAC-OG-xx` | Operational Governance | T1 + T2 + T3 |
| `AAC-RS-xx` | Resiliency | T1 + T3 |
| `AAC-TS-xx` | Trust & Safety | T2 |
| `AAC-DP-xx` | Data & Privacy | T1 |
| `AAC-TB-xx` | Testability | T2 + T3 |
| `AAC-SM-xx` | Self-Maintenance | T3 |
| `AAC-AE-xx` | Architecture & Engineering | T3 |
| `AAC-LL-xx` | Low Latency | T3 |

Control identifiers are stable within a major version. Every v1.3 identifier that survives into v2.0 retains its original ID. The 6-identifier delta between 67 principles and 73 control identifiers reflects absorbed and retired v1.3 identifiers preserved as stable migration references.

---

## Key Design Decisions

**Why DNH is an architectural invariant, not a priority**
The Do No Harm domain operates as an override constraint. Any principle in any other domain that would produce a DNH violation is automatically subordinated regardless of operational pressure or business justification. No optimization objective — revenue, cost, performance, or throughput — may override a harm tier classification.

**Why the framework is stateless**
The governance control plane evaluates each action against pre-declared governance artifacts and returns a deterministic decision. No session state between evaluations. This makes it horizontally scalable, reproducible, and auditable — and why the arbitration layer can be implemented in any deterministic policy engine.

**Why there are three enforcement tiers**
The primary reason is the separation of runtime enforcement from governance declaration. What must be enforced per-action belongs in Tier 1. What must be declared before the control plane initializes belongs in Tier 2. What guides implementation without constituting enforcement belongs in Tier 3.

**Why the Decision Arbitration domain exists**
Most governance frameworks specify what is prohibited. The DA domain specifies what to do when prohibitions conflict. DA-59 defines the harm tier taxonomy; DA-60 defines tiered evaluation paths by harm tier; DA-61 provides the liveness guarantee that governance cannot produce deadlock.

**Why an Implementation Profile is required**
Several AAC principles are intentionally abstract at the framework level — harm tier definitions, arbitration time bounds, agent trust tier criteria — because these must be context-specific. A deploying team that has not completed and signed a profile has not meaningfully adopted the framework.

**Why the maturity levels exist**
L1 — Foundational gives any organization a governable posture achievable in weeks without requiring full control plane infrastructure. L2 — Mature targets regulated industry deployments. L3 — Optimizing targets EU AI Act high-risk compliance. The maturity levels reduce the barrier to adoption without weakening any principle.

---

## Novel Contributions

The following AAC principles have no direct equivalent in CSA ATF, OWASP Agentic Top 10, or NIST AI RMF 1.0:

- **AAC-DA-59** — Harm classification taxonomy with pre-classification registry for O(1) runtime lookup and explicit tradeoff resolution rule
- **AAC-DA-60** — Tiered deterministic arbitration: evaluation depth determined by harm tier (T3=ZT+Audit; T2=Confidence+Override+Policy+ZT+Audit; T1=Full five-step sequence)
- **AAC-DA-61** — Liveness guarantee as a safety requirement — governance that produces deadlock is a design defect, not a safety feature
- **AAC-DA-63** — Non-bypassable enforcement boundary as an architectural requirement with integrity violation logging
- **AAC-OG-25** — Policy enforcement integrity: runtime continuous validation against declared governance artifacts
- **AAC-OG-28** — Authority Registry: non-circular accountability chain declared before system initialization
- **AAC-OG-29** — Implementation Profile: parameterization boundary between specification and governed system
- **AAC-RS-39** — System Safe Mode as a designed operating posture with distinct entry/recovery thresholds and hard shutdown capability
- **AAC-AO-60** — Recursive Governance Covenant: sub-agent spawning with signed lineage chain; agents operate at or below creator trust tier
- **AAC-TB-29** — Agent Behavioral Envelope Verification: envelope-only declaration replacing benchmark accuracy model

---

## Framework Acknowledgements

| Framework | Relationship |
|---|---|
| MITRE ATLAS v5.4.0 | Direct dependency — specific principles close named ATLAS technique gaps |
| OWASP Agentic Top 10 (2026) | Direct dependency — ZT-77 closes ASI04; RS-36 maps to ASI-09 |
| EU AI Act (Regulation (EU) 2024/1689) | Regulatory dependency — ZT-76 (Art. 52), ZT-78 (Arts. 10, 53), DP-06 (Art. 10) |
| NIST AI RMF 1.0 | Alignment — 18 Full, 5 Partial, 1 Gap |
| CSA Agentic Trust Framework | Alignment — 27 Full, 18 Partial, 11 Gap |
| STRIDE | Methodological — DA-64 uses STRIDE for harm taxonomy construction guidance |

---

## Citation

> Thakuri, R. (2026). *The Autonomous Agentic Covenant: A Governance Control Plane Specification for Autonomous and AI-Driven Systems* (Version 2.0). Apache License 2.0. https://github.com/raj-thakuri/autonomous-agentic-covenant

> Version 2.0 · April 2026 · 67 principles · Three enforcement tiers · 14 domains · 73 control identifiers

> Evolved from: Thakuri, R. (2026). *The Autonomous Agentic Covenant* (Version 1.3). Apache 2.0. Version 1.3 remains the reference for the framework's ethical philosophy and governance vision.

---

## License

Licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0). See [LICENSE](LICENSE) for full terms.

Contributed code (policy gate scripts, validators, test harnesses) is licensed under Apache 2.0. The specification, profiles, schema, and crosswalk documents remain Apache 2.0.

---

## Author

**Raj Thakuri** — CISO, independent researcher, and practitioner at the intersection of AI security, privacy-first architecture, and AI governance. Developed from operational experience designing governance structures for agentic AI systems in regulated enterprise environments. All views are my own.

*Questions, citations, and implementation reports welcome via GitHub Issues.*
