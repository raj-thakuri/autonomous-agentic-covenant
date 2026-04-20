aaa# AVAL — Deployment and Usage Guide

AAC Validator & Logic-checker v0.1.0  
Reference implementation of AAC v2.0 Decision Arbitration (AAC-DA-59 to DA-63)

---

## Prerequisites

- Python 3.10 or higher
- `pip` or `uv` (recommended)

---

## Installation

**1. Navigate to the toolkit directory**

```bash
cd autonomous-agentic-covenant/toolkit
```

**2. Create a virtual environment**

```bash
# Using uv (recommended)
uv venv .venv

# Or using standard Python
python -m venv .venv
```

**3. Activate the environment**

```bash
# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

**4. Install AVAL**

```bash
# Using uv
uv pip install -e .

# Or using pip
pip install -e .
```

**5. Verify the installation**

```bash
aval --help
```

Expected output:

```
Usage: aval [OPTIONS] COMMAND [ARGS]...

  AAC Validator & Logic-checker (AAC v2.0)

Commands:
  lint      Validate syntax and schema compliance of a covenant.json
  profile   Output a Maturity Grade (L1/L2/L3) based on populated AAC controls
  simulate  Run the DA-60 deterministic arbitration sequence for a proposed action
```

---

## Command 1: `aval lint`

Validates a `covenant.json` file against the AAC v2.0 schema. Runs three checks in sequence:

1. JSON syntax — file must be valid JSON
2. Schema validation — all required fields present and correctly typed, maturity-aware conditionals enforced (L2/L3 additional fields)
3. Artifact integrity — `expires_at` checked against the current date (AAC-OG-24), and `revision_authority` verified as a declared principal in `authority_registry` (AAC-OG-28)

**Usage**

```bash
# Using the included test fixtures
aval lint test_suite/valid_l1_covenant.json
aval lint test_suite/invalid_syntax.json

# Using your own file
aval lint path/to/your-covenant.json --json
```

**Example — passing**

```bash
aval lint test_suite/valid_l1_covenant.json
```

```
PASS: schema valid, artifact current
```

Exit code: `0`

**Example — failing**

```bash
aval lint test_suite/invalid_syntax.json
```

```
FAIL: 9 error(s)
  [1] root: 'harm_classification' is a required property
  [2] root: 'authority_registry' is a required property
  [3] root: 'fallback_registry' is a required property
  ...
```

Exit code: `1`

**Machine-readable output**

```bash
aval lint test_suite/valid_l1_covenant.json --json
```

```json
{
  "valid": true,
  "errors": []
}
```

---

## Command 2: `aval profile`

Reads a `covenant.json` and outputs a Maturity Grade showing which AAC governance controls are populated and whether the file satisfies its declared maturity level (L1, L2, or L3).

This command does not require a passing `lint` first, but a schema-invalid file will produce incomplete results.

**Usage**

```bash
# Using the included test fixture
aval profile test_suite/valid_l1_covenant.json

# Using your own file
aval profile path/to/your-covenant.json --json
```

**Example — compliant L1**

```bash
aval profile test_suite/valid_l1_covenant.json
```

```
Maturity Grade: L1 (COMPLIANT)

Populated Controls:
  [PASS] authority_registry.principals (AAC-OG-28)
  [PASS] harm_classification.tier_definitions [declared 3/3] (AAC-DA-59)
  [PASS] harm_classification.pre_classified_actions (AAC-DA-59)
  [PASS] harm_classification.foreseeable_harm_signals [declared 3/3 min] (AAC-DNH-B)
  [PASS] fallback_registry (AAC-DA-61)
  [PASS] enforcement_gates (AAC-DA-60)
  [PASS] system_constraints.escalation_hierarchy (AAC-DA-61)

Missing Required:
  (none)
```

Exit code: `0` (compliant), `1` (non-compliant)

**Example — non-compliant L2 (missing required fields)**

```
Maturity Grade: L2 (NON-COMPLIANT)

Populated Controls:
  [PASS] authority_registry.principals (AAC-OG-28)
  [PASS] harm_classification.tier_definitions [declared 3/3] (AAC-DA-59)
  ...

Missing Required:
  [FAIL] behavioral_envelopes (AAC-TB-29) — required at L2
  [FAIL] harm_classification.taxonomy_review_cadence (AAC-OG-24) — required at L2
  [FAIL] system_constraints.safe_mode (AAC-RS-39) — required at L2
```

Exit code: `1`

---

## Command 3: `aval simulate`

Runs the DA-60 deterministic arbitration sequence against a proposed action. Requires two files:

- A governance configuration file (your deployed `covenant.json`, or use the included `test_suite/valid_l1_covenant.json` to get started)
- An action file you author describing the proposed action (see format below, or use the included `test_suite/failing_simulation_action.json`)

Every simulation produces a **Governance Trace** — a per-step audit record of each check and its outcome, as required by AAC-DP-07.

**Usage**

```bash
# Using the included test fixtures
aval simulate --covenant test_suite/valid_l1_covenant.json \
              --action test_suite/failing_simulation_action.json

# Using your own files
aval simulate --covenant path/to/your-covenant.json \
              --action path/to/your-action.json

# Machine-readable output
aval simulate --covenant test_suite/valid_l1_covenant.json \
              --action test_suite/failing_simulation_action.json --json
```

### Proposed Action File Format

Create a new `.json` file (any name) with the following fields:

```json
{
  "tool_name": "string",
  "action_class": "string",
  "proposed_params": {},
  "reported_confidence": 0.0,
  "reversibility_score": 0.0,
  "agent_id": "string"
}
```

| Field | Description |
|---|---|
| `tool_name` | Name of the tool/integration as declared in `integration_registry` |
| `action_class` | Action class as declared in `enforcement_gates` or `pre_classified_actions` |
| `proposed_params` | Freeform parameters for the action (not evaluated by AVAL) |
| `reported_confidence` | Agent's self-reported confidence score (0.0 – 1.0) |
| `reversibility_score` | How reversible the action is (0.0 = fully irreversible, 1.0 = fully reversible). Used on the T1 path only |
| `agent_id` | Must match an `agent_id` declared in `agent_registry` |

### Evaluation Paths

The arbitration engine selects one of three paths based on the action's harm tier:

| Path | Harm Tier | Steps Run |
|---|---|---|
| `T3_ZT_AUDIT` | FRICTION | Agent auth/authz only |
| `T2_CONFIDENCE_OVERRIDE_POLICY` | MATERIAL | Confidence (DA-62) + override + policy constraints |
| `T1_FULL_SEQUENCE` | IRREVERSIBLE | All 5 steps + DNH-A pre-gate |

### Example — DENY (prohibited action)

```bash
aval simulate --covenant test_suite/valid_l1_covenant.json \
              --action test_suite/failing_simulation_action.json
```

```
[CHECK] Agent Registry (AAC-DA-63): PASS - agent 'did:aac:sandbox-agent-001' declared
[CHECK] Prohibited Action (AAC-DA-63): FAIL - 'EXECUTE_TRANSFER' is in prohibited_action_classes - integrity violation
[DISPOSITION]: DENY
[FALLBACK]: fallback-deny-and-log (AAC-DA-61)
```

Exit code: `1`

### Example — ALLOW (FRICTION action, T3 path)

```json
{
  "tool_name": "Internal Records API",
  "action_class": "READ_DATA",
  "proposed_params": {},
  "reported_confidence": 0.95,
  "reversibility_score": 0.0,
  "agent_id": "did:aac:sandbox-agent-001"
}
```

```
[CHECK] Agent Registry (AAC-DA-63): PASS - agent 'did:aac:sandbox-agent-001' declared
[CHECK] Prohibited Action (AAC-DA-63): PASS - 'READ_DATA' not in prohibited_action_classes
[CHECK] Agent Authorization (AAC-DA-63): PASS - 'READ_DATA' is an authorized action class
[CHECK] Integration Registry (AAC-ZT-77): PASS - tool 'Internal Records API' authorized
[CHECK] Harm Classification (AAC-DA-59): PASS - 'READ_DATA' classified as FRICTION via enforcement_gates
[CHECK] Evaluation Path (AAC-DA-60): PASS - T3_ZT_AUDIT - ZT+Audit baseline satisfied; no arbitration sequence required
[DISPOSITION]: ALLOW
```

Exit code: `0`

### Example — ALLOW (MATERIAL action, T2 path)

```json
{
  "tool_name": "Internal Records API",
  "action_class": "GENERATE_REPORT",
  "proposed_params": {},
  "reported_confidence": 0.92,
  "reversibility_score": 0.0,
  "agent_id": "did:aac:sandbox-agent-001"
}
```

```
[CHECK] Agent Registry (AAC-DA-63): PASS - agent 'did:aac:sandbox-agent-001' declared
[CHECK] Prohibited Action (AAC-DA-63): PASS - 'GENERATE_REPORT' not in prohibited_action_classes
[CHECK] Agent Authorization (AAC-DA-63): PASS - 'GENERATE_REPORT' is an authorized action class
[CHECK] Integration Registry (AAC-ZT-77): PASS - tool 'Internal Records API' authorized
[CHECK] Harm Classification (AAC-DA-59): PASS - 'GENERATE_REPORT' classified as MATERIAL via enforcement_gates
[CHECK] Confidence Verification (AAC-DA-62): PASS - reported_confidence 0.92 >= required 0.8
[CHECK] Sovereignty Override (AAC-OG-28): PASS - action harm_tier MATERIAL within declared harm_tier_max MATERIAL
[CHECK] Policy Constraints (AAC-AO-58): PASS - system_constraints satisfied - no additional bounds declared
[CHECK] Gate Disposition (AAC-DA-60): PASS - all checks passed - gate declares ALLOW
[DISPOSITION]: ALLOW
```

Exit code: `0`

### Example — DENY (MATERIAL action, confidence below threshold)

Same action as above but with `"reported_confidence": 0.5`:

```
[CHECK] Confidence Verification (AAC-DA-62): FAIL - reported_confidence 0.5 < required 0.8
[DISPOSITION]: DENY
[FALLBACK]: fallback-deny-and-log (AAC-DA-61)
```

Exit code: `1`

---

## Dispositions

| Disposition | Meaning |
|---|---|
| `ALLOW` | All checks passed; gate permits execution |
| `DENY` | One or more checks failed; action blocked |
| `ESCALATE` | Action requires human principal review before execution |
| `FALLBACK` | Execution deferred to the declared safe fallback action |

---

## Exit Codes

| Code | Meaning |
|---|---|
| `0` | Pass — `lint` valid, `profile` compliant, `simulate` ALLOW |
| `1` | Fail — validation error, non-compliant grade, or non-ALLOW disposition |

Exit codes are suitable for use in CI/CD pipelines.

---

## Test Fixtures

Three sample files are included in `test_suite/`:

| File | Purpose |
|---|---|
| `valid_l1_covenant.json` | Minimal valid L1 covenant — passes `lint` and `profile` |
| `invalid_syntax.json` | Schema-invalid covenant — fails `lint` with missing required fields |
| `failing_simulation_action.json` | Proposed action for `EXECUTE_TRANSFER` — DENY via prohibited action check |

---

## Governance Trace Reference

Each `[CHECK]` line in the simulation output maps to a specific AAC v2.0 control:

| Check | Control | When Run |
|---|---|---|
| Agent Registry | AAC-DA-63 | All paths |
| Prohibited Action | AAC-DA-63 | All paths |
| Agent Authorization | AAC-DA-63 | All paths |
| Integration Registry | AAC-ZT-77 | All paths |
| Harm Classification | AAC-DA-59 | All paths |
| DNH-A Pre-Gate | AAC-DNH-A | T1 only |
| Confidence Verification | AAC-DA-62 | T1 and T2 |
| Reversibility Scoring | AAC-DA-60 | T1 only |
| Sovereignty Override | AAC-OG-28 | T1 and T2 |
| Policy Constraints | AAC-AO-58 | T1 and T2 |
