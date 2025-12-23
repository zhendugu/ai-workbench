# ENGINE CI BOOTSTRAP CONTRACT

## Purpose

This document defines CI as the enforcement layer for ENGINE governance.

CI is required for portability across repositories. When this ENGINE is copied to a new repository, CI must enforce the same governance rules regardless of the specific project (BLUEPRINT) loaded into the ENGINE.

CI is not optional. CI is not a suggestion. CI is law.

This document defines what CI MUST enforce, not what CI MAY enforce.

---

## Mandatory CI Bootstrap Checks

CI MUST fail if any of the following conditions are not met:

### 1. State Snapshot Existence
- **Check**: `CURRENT_STATE_SNAPSHOT.md` exists at repository root
- **Failure Reason**: ENGINE identity cannot be established without state snapshot
- **CI Failure Message**: `ENGINE bootstrap failure: CURRENT_STATE_SNAPSHOT.md missing at repository root`

### 2. Handoff Protocol Existence
- **Check**: `docs/ENGINE_HANDOFF_PROMPT.md` exists
- **Failure Reason**: Cursor Pro startup behavior is undefined without handoff protocol
- **CI Failure Message**: `ENGINE bootstrap failure: docs/ENGINE_HANDOFF_PROMPT.md missing`

### 3. Blueprint Interface Existence
- **Check**: `docs/BLUEPRINT_INTERFACE.md` exists
- **Failure Reason**: BLUEPRINT loading rules are undefined without interface definition
- **CI Failure Message**: `ENGINE bootstrap failure: docs/BLUEPRINT_INTERFACE.md missing`

### 4. Stage Status Existence and Parseability
- **Check**: `docs/stage_status.md` exists and current stage is parseable
- **Failure Reason**: Current stage must be determinable for enforcement
- **CI Failure Message**: `ENGINE bootstrap failure: docs/stage_status.md missing or current stage unparseable`

### 5. Stage Rule Documentation Existence
- **Check**: Required stage rule document exists for current stage
- **Pattern**: `docs/STAGE_{N}_CONTROLLED_IMPLEMENTATION.md` where `{N}` is the current stage number
- **Failure Reason**: Stage-specific rules must be documented
- **CI Failure Message**: `ENGINE bootstrap failure: docs/STAGE_{N}_CONTROLLED_IMPLEMENTATION.md missing for current stage {N}`

### 6. Endpoint Registry Existence
- **Check**: Endpoint registry file(s) required by current stage exist and are readable
- **Pattern**: `docs/registry/stage_{N}_endpoints.yaml` where `{N}` is the current stage number
- **Failure Reason**: Registry enforcement requires registry files
- **CI Failure Message**: `ENGINE bootstrap failure: docs/registry/stage_{N}_endpoints.yaml missing or unreadable for current stage {N}`

**All bootstrap checks must pass before any other CI checks execute.**

---

## Stage/Registry Alignment Rules

CI MUST enforce the following alignment rules:

### 1. Registry Compliance for Active Stage
- CI MUST check all executable endpoints against the registry for the active stage
- CI MUST fail if any endpoint is implemented but not registered
- CI MUST fail if any registered endpoint violates the execution pattern defined in the registry

### 2. Stage Declaration Consistency
- CI MUST read current stage from both:
  - `CURRENT_STATE_SNAPSHOT.md` (authoritative)
  - `docs/stage_status.md` (must match)
- CI MUST fail if stage declarations conflict
- **CI Failure Message**: `ENGINE stage conflict: CURRENT_STATE_SNAPSHOT.md declares stage {X}, docs/stage_status.md declares stage {Y}`

### 3. Stage-Specific Registry Enforcement
- If current stage is Stage 4: CI MUST enforce `docs/registry/stage_4_endpoints.yaml`
- If current stage is Stage 5: CI MUST enforce `docs/registry/stage_5_endpoints.yaml`
- CI MUST NOT silently behave as Stage 4 when stage is Stage 5
- CI MUST NOT silently behave as Stage 5 when stage is Stage 4
- **CI Failure Message**: `ENGINE registry mismatch: current stage {N} requires docs/registry/stage_{N}_endpoints.yaml but enforcement is using wrong registry`

### 4. Registry File Validation
- CI MUST validate registry YAML structure
- CI MUST fail if registry file is malformed
- **CI Failure Message**: `ENGINE registry validation failure: docs/registry/stage_{N}_endpoints.yaml is malformed or invalid`

---

## Engine Initialization Gate

### Definition: ENGINE Initialized

An ENGINE is considered "initialized" when all of the following artifacts exist and are valid:

1. **State Snapshot**: `CURRENT_STATE_SNAPSHOT.md` exists at repository root
2. **Handoff Protocol**: `docs/ENGINE_HANDOFF_PROMPT.md` exists
3. **Blueprint Interface**: `docs/BLUEPRINT_INTERFACE.md` exists
4. **Stage Status**: `docs/stage_status.md` exists and is parseable
5. **Stage Rules**: Stage-specific rule document exists for current stage
6. **Registry**: Endpoint registry file exists for current stage

### Minimal Initialization Artifacts

The minimal set of artifacts that constitute ENGINE initialization:

- `CURRENT_STATE_SNAPSHOT.md` (repository root)
- `docs/ENGINE_HANDOFF_PROMPT.md`
- `docs/BLUEPRINT_INTERFACE.md`
- `docs/stage_status.md`
- `docs/STAGE_{N}_CONTROLLED_IMPLEMENTATION.md` (for current stage N)
- `docs/registry/stage_{N}_endpoints.yaml` (for current stage N)

### Implementation Work Prohibition

**Implementation work is forbidden until initialization checks pass.**

CI MUST:
- Run bootstrap checks before any other checks
- Fail the entire CI run if bootstrap checks fail
- Block all implementation-related checks until bootstrap passes

**CI Failure Message**: `ENGINE not initialized: bootstrap checks failed. Implementation work is forbidden until ENGINE is initialized.`

---

## Anti-Tamper Rules

### Governance-Critical Changes

Any change to the following is considered a governance-critical change:

- `.github/workflows/*` (CI workflow definitions)
- `.github/scripts/*` (CI enforcement scripts)

### Explicit Human Approval Requirement

Changes to governance-critical files MUST require explicit human approval.

**Explicit approval is defined as:**

1. **Human instruction**: Direct human command to modify CI files
2. **Labeled PR**: Pull request with explicit label indicating CI modification approval (e.g., `approved:ci-change`)
3. **Documented approval**: Human comment in PR or commit message explicitly approving CI change

**Absence of explicit approval means the change is unauthorized.**

### CI Weakening Detection

CI MUST fail by default if CI enforcement is weakened.

CI MUST detect:
- Removal of enforcement checks
- Modification of enforcement logic that reduces strictness
- Addition of bypass mechanisms
- Disabling of mandatory checks

**CI Failure Message**: `ENGINE anti-tamper violation: CI enforcement has been weakened. Explicit human approval required for CI modifications.`

### CI Modification Gate

Before allowing CI modifications:

1. CI MUST verify explicit human approval exists
2. CI MUST verify modification does not weaken enforcement
3. CI MUST verify modification maintains bootstrap checks
4. CI MUST verify modification maintains stage/registry alignment

**If any verification fails: CI MUST fail.**

---

## CI Failure Messages

CI MUST emit the following exact error strings for the specified conditions:

### Bootstrap Failures

- `ENGINE bootstrap failure: CURRENT_STATE_SNAPSHOT.md missing at repository root`
- `ENGINE bootstrap failure: docs/ENGINE_HANDOFF_PROMPT.md missing`
- `ENGINE bootstrap failure: docs/BLUEPRINT_INTERFACE.md missing`
- `ENGINE bootstrap failure: docs/stage_status.md missing or current stage unparseable`
- `ENGINE bootstrap failure: docs/STAGE_{N}_CONTROLLED_IMPLEMENTATION.md missing for current stage {N}`
- `ENGINE bootstrap failure: docs/registry/stage_{N}_endpoints.yaml missing or unreadable for current stage {N}`

### Stage/Registry Alignment Failures

- `ENGINE stage conflict: CURRENT_STATE_SNAPSHOT.md declares stage {X}, docs/stage_status.md declares stage {Y}`
- `ENGINE registry mismatch: current stage {N} requires docs/registry/stage_{N}_endpoints.yaml but enforcement is using wrong registry`
- `ENGINE registry validation failure: docs/registry/stage_{N}_endpoints.yaml is malformed or invalid`

### Initialization Failures

- `ENGINE not initialized: bootstrap checks failed. Implementation work is forbidden until ENGINE is initialized.`

### Anti-Tamper Failures

- `ENGINE anti-tamper violation: CI enforcement has been weakened. Explicit human approval required for CI modifications.`
- `ENGINE anti-tamper violation: CI modification detected without explicit human approval.`

---

## Non-Goals

This document does NOT define:

- **Project/business logic**: This document defines ENGINE enforcement expectations, not project requirements
- **Blueprint-specific rules**: Blueprint rules are defined in BLUEPRINT documents, not here
- **Stage-specific implementation patterns**: Stage implementation patterns are defined in STAGE_*_CONTROLLED_IMPLEMENTATION.md, not here
- **Technology stack choices**: Technology stack is defined in STACK_DECISION.md, not here
- **CI implementation details**: This document defines what CI must enforce, not how CI implements enforcement

This document defines ENGINE governance enforcement, not project execution.

---

## Authority Hierarchy

When CI encounters conflicts:

1. **This document** (ENGINE_CI_BOOTSTRAP.md) defines CI enforcement requirements
2. **CURRENT_STATE_SNAPSHOT.md** defines current state (authoritative for stage declaration)
3. **Stage-specific documents** (STAGE_*_CONTROLLED_IMPLEMENTATION.md) define stage rules
4. **Registry files** (stage_*_endpoints.yaml) define authorized endpoints
5. **Code files** are the lowest authority (evidence of current state, not source of truth)

**If conflicts exist: CI MUST fail and report the conflict.**

---

## Portability Requirement

This ENGINE is designed to be copied to new repositories.

When copied:

1. All bootstrap checks MUST still pass
2. All enforcement rules MUST still apply
3. CI MUST enforce the same governance regardless of BLUEPRINT
4. CI MUST not require repository-specific configuration

**If CI requires repository-specific configuration: the ENGINE is not portable.**

---

## Contract Finality

This document is a binding contract for CI behavior.

CI MUST comply with all rules defined in this document.

CI MUST NOT:
- Skip bootstrap checks
- Allow initialization bypass
- Permit unauthorized CI modifications
- Ignore stage/registry alignment
- Weaken enforcement without explicit approval

**Violation of this contract is a hard failure.**

---

END OF ENGINE CI BOOTSTRAP CONTRACT

