# The Autonomous Agentic Covenant (AAC)

**A Governance Framework for Autonomous and AI-Driven Systems**

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Version](https://img.shields.io/badge/Version-1.3-blue.svg)](CHANGELOG.md)

---

## What Is the AAC?

The Autonomous Agentic Covenant is an engineering governance framework for teams designing, building, and deploying autonomous and AI-driven systems. It defines 69 principles across 11 domains — from Zero-Trust security and data privacy to agent trust graduation and runtime decision arbitration — providing stable, citable control identifiers that work in design reviews, implementation tickets, CI/CD policy gates, and compliance audits.

The AAC is not a compliance checklist. It is a decision-making framework: when design choices present competing valid options, the relevant AAC domain governs. When domains conflict, **AAC-DNH-0 (Do No Harm)** governs.

The framework was developed by a practitioner for practitioners — grounded in real-world agentic system design, validated against CSA ATF, OWASP Agentic Top 10, and NIST AI RMF 1.0, and published under CC BY 4.0.

---

## Who Is This For?

- **Security architects** designing governance structures for autonomous AI deployments
- **Engineering teams** building agentic systems who need clear, stable design requirements
- **Governance and compliance teams** mapping AI controls to existing frameworks
- **CISOs and risk leaders** establishing organizational standards for agentic AI
- **Researchers and framework builders** looking for a practitioner-authored reference point

---

## What's in This Repository

```
autonomous-agentic-covenant/
├── README.md                          ← this file
├── LICENSE                            ← CC BY 4.0
├── CHANGELOG.md                       ← version history
├── covenant/
│   ├── AAC_v1.3.md                   ← primary specification (Markdown)
│   └── AAC_v1.3.docx                 ← formatted distribution version
├── profiles/
│   └── AAC_Implementation_Profile_v1.0.docx  ← deployment template
├── crosswalk/
│   └── AAC_Framework_Crosswalk_v1.0.docx     ← CSA ATF / OWASP / NIST mapping
└── governance/
    └── CONTRIBUTING.md               ← contribution process
```

**`covenant/`** — The framework specification. Start here. The Markdown version is the canonical reference; the .docx is for distribution and formal citation.

**`profiles/`** — The Implementation Profile template. Every AAC deployment requires a completed profile that declares context-specific parameters: harm tier definitions, agent trust tiers, confidence thresholds, resource boundaries, and safe mode criteria. Without a profile, several AAC principles cannot be verified.

**`crosswalk/`** — Framework alignment document mapping every AAC control to CSA Agentic Trust Framework (ATF), OWASP Agentic Top 10 (2026), and NIST AI RMF 1.0. Use this to justify AAC adoption to teams already operating under these frameworks, or to conduct gap analysis against existing compliance obligations.

**`governance/`** — Contribution process for proposing changes to the framework.

---

## How to Use the AAC

### Path 1 — Read the specification

Start with [`covenant/AAC_v1.3.md`](covenant/AAC_v1.3.md). The domain index at the top links to each domain section. Every principle has a stable anchor — e.g. `#aac-zt-64` — for direct reference in ADRs, tickets, or documentation.

### Path 2 — Deploy a system against it

Download and complete [`profiles/AAC_Implementation_Profile_v1.0.docx`](profiles/AAC_Implementation_Profile_v1.0.docx). The profile has nine sections covering harm classification, agent trust tiers, confidence thresholds, resource boundaries, safe mode behavior, policy enforcement, acceptance criteria, and governance sign-off. A completed profile is a governance artifact under **AAC-OG-24** and must be version-controlled alongside your system.

### Path 3 — Map to your existing frameworks

Open [`crosswalk/AAC_Framework_Crosswalk_v1.0.docx`](crosswalk/AAC_Framework_Crosswalk_v1.0.docx). The crosswalk covers:

| Framework | Coverage |
|---|---|
| CSA Agentic Trust Framework (ATF) | 27 Full · 18 Partial · 11 Gap |
| OWASP Agentic Top 10 (2026) | 9/10 Full · 1 Partial |
| NIST AI RMF 1.0 | 18 Full · 5 Partial · 1 Gap |

---

## Control Identifier Format

Every principle carries a stable identifier: `AAC-[DOMAIN]-[NUMBER]`

| Prefix | Domain |
|---|---|
| `AAC-DNH-0x` | Do No Harm |
| `AAC-AE-xx` | Architecture & Engineering |
| `AAC-TB-xx` | Testability |
| `AAC-AP-xx` | API Design & Extensibility |
| `AAC-LL-xx` | Low Latency |
| `AAC-DP-xx` | Data & Privacy |
| `AAC-AI-xx` | AI & Intelligent Automation |
| `AAC-TS-xx` | Trust & Safety |
| `AAC-OG-xx` | Operational Governance |
| `AAC-RS-xx` | Resiliency |
| `AAC-SM-xx` | Self-Maintenance |
| `AAC-AO-xx` | Autonomous Operations |
| `AAC-DA-xx` | Decision Arbitration |
| `AAC-ZT-xx` | Zero-Trust Security |

Control identifiers are stable across versions within a major release. A control that exists in v1.3 will carry the same identifier in v1.x releases. Breaking changes to identifiers are versioned.

---

## Key Design Decisions

**Why DNH is an architectural invariant, not a priority**
The Do No Harm domain does not sit at the top of a priority stack — it operates as an override constraint. Any principle in any other domain that would produce an outcome violating AAC-DNH-0 is automatically subordinated, regardless of operational pressure or business justification.

**Why the Decision Arbitration domain exists**
Most governance frameworks tell you what is prohibited. The DA domain tells you what to do when prohibitions conflict — when every available action causes some harm. DA-59 defines a harm tier taxonomy; DA-60 defines a sequential arbitration sequence for high-risk actions; DA-61 provides the liveness guarantee that the arbitration layer itself cannot become a deadlock mechanism.

**Why control IDs have gaps**
The numbering sequence reflects the framework's evolution. Numbers that were removed or merged during development are not reused. The gap is a record of the framework's history and prevents citation confusion when earlier versions are referenced.

**Why an Implementation Profile is required**
Several AAC principles are intentionally abstract at the framework level — harm tier thresholds, agent trust tier definitions, safe mode trigger conditions — because these must be context-specific. A deploying team that has not completed a profile has not meaningfully adopted the framework; they have read it.

---

## Novel Contributions

The following AAC principles have no direct equivalent in CSA ATF, OWASP Agentic Top 10, or NIST AI RMF 1.0:

- **AAC-DA-59** — Structured three-tier harm classification taxonomy with explicit tradeoff resolution rule
- **AAC-DA-61** — Liveness guarantee as a safety requirement (a system that cannot make forward progress under its own safety constraints has a design defect, not a safety feature)
- **AAC-DA-63** — Centralized enforcement boundary as a non-bypassable architectural requirement
- **AAC-OG-25** — Policy enforcement integrity: runtime continuous validation of behavior against declared governance artifacts
- **AAC-RS-39** — System Safe Mode as a named, designed operating posture with defined trigger conditions and recovery criteria
- **AAC-DNH-0 suite** — Do No Harm as an absolute override architectural invariant rather than a principle in a priority stack

---

## Citation

> Thakuri, R. (2026). *The Autonomous Agentic Covenant: A Governance Framework for Autonomous and AI-Driven Systems* (Version 1.3). CC BY 4.0. https://github.com/raj-thakuri/autonomous-agentic-covenant

---

## License

This work is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

You are free to share and adapt this material for any purpose, including commercially, provided you give appropriate credit. See [LICENSE](LICENSE) for full terms.

If you contribute code (policy gate scripts, validators, test harnesses) to this repository, contributed code is licensed under Apache 2.0. The specification, profiles, and crosswalk documents remain CC BY 4.0.

---

## Author

**Raj Thakuri** — CISO, independent researcher, and practitioner at the intersection of AI security, privacy-first architecture, and AI governance. This framework was developed from operational experience designing governance structures for agentic AI systems in regulated enterprise environments.

*Questions, citations, and implementation reports welcome via GitHub Issues.*
