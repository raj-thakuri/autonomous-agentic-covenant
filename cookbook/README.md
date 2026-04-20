# AAC Governance Cookbook

**Companion publication to the Autonomous Agentic Covenant v2.0**

The Cookbook is a practitioner-focused companion to the AAC specification. Where the spec defines *what* governance controls are required, the Cookbook shows *how* to implement them — using concrete failure scenarios, schema-aligned JSON snippets, and AVAL enforcement traces.

---

## What's in Here

| File | Description |
|---|---|
| `AAC_Governance_Cookbook_v1.0.md` | Full text — six governance recipes (Markdown) |
| `AAC_Governance_Cookbook_v1.0.pdf` | Print/share version |

---

## How to Use It

Each recipe follows a consistent structure:

1. **The Scenario** — a real agentic failure mode
2. **The Probabilistic Failure** — why standard guardrails miss it
3. **The AAC Solution** — which controls apply and why
4. **Implementation Profile Snippet** — schema-aligned JSON showing the declaration
5. **AVAL Enforcement Trace** — what the governance plane produces when the scenario fires
6. **The "So What?"** — regulatory and framework mappings (EU AI Act, OWASP, MITRE ATLAS)

Recipes 1–3 address individual action governance. Recipes 4–6 address system-level and multi-agent governance — the territory where most frameworks stop and the AAC begins.

---

## Relationship to the Toolkit

The AVAL enforcement traces in each recipe are produced by [`toolkit/`](../toolkit/) — the reference implementation of AAC v2.0 Decision Arbitration. You can reproduce any trace by running `aval simulate` with the corresponding `covenant.json` and action file. See [`toolkit/GUIDE.md`](../toolkit/GUIDE.md) for setup instructions.

---

*Apache License 2.0 · Preprint: dx.doi.org/10.2139/ssrn.6526238*
