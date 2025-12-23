# HUMAN STARTUP PRE-AUDIT REPORT

**Audit Date**: 2024-12-19  
**Audit Type**: Read-Only Human Usability Analysis  
**Purpose**: Identify actual startup path, hidden prerequisites, and friction points for first-time human users

---

## AUDIT ASSUMPTIONS

**Human User Profile:**
- Rational developer with standard Git/GitHub knowledge
- No prior knowledge of ENGINE internal design
- Goal: Start from empty directory and reach "ENGINE ready for construction" state
- Expectation: Follow documentation and pass CI without violating rules

**Audit Scope:**
- Starting from empty directory (or fresh git clone)
- Minimum viable startup path
- CI failure/success paths
- Human confusion points
- Hidden prerequisites
- Behavior without active Blueprint

**Not Audited:**
- Internal ENGINE correctness (assumed correct)
- Blueprint creation process (out of scope)
- Implementation work (out of scope)

---

## SECTION 1: MINIMUM STARTUP PATH

### 1.1 Starting from Empty Directory

**Critical Discovery**: A human cannot start from a truly empty directory. The ENGINE requires a complete file structure before first push.

**Minimum File Set Required Before First Push:**

**Phase 1: Core ENGINE Files (7 files)**
1. `CURRENT_STATE_SNAPSHOT.md` (repository root)
   - Must contain: `ENGINE_VERSION: v1`
   - Must contain: `ACTIVE_STAGE: 5` (or matching stage from stage_status.md)
   - Must contain: `ACTIVE_BLUEPRINT: none`
   - **Critical**: Field format matters - CI expects exact patterns

2. `docs/ENGINE_HANDOFF_PROMPT.md`
   - Required by bootstrap check

3. `docs/BLUEPRINT_INTERFACE.md`
   - Required by bootstrap check

4. `docs/stage_status.md`
   - Must contain parseable: `Current Stage: Stage N`
   - Bootstrap reads this to determine which stage files to check

5. `docs/STAGE_{N}_CONTROLLED_IMPLEMENTATION.md`
   - Where {N} is the stage number from stage_status.md
   - Currently: `docs/STAGE_5_CONTROLLED_IMPLEMENTATION.md`

6. `docs/registry/stage_{N}_endpoints.yaml`
   - Where {N} is the stage number from stage_status.md
   - Currently: `docs/registry/stage_5_endpoints.yaml`
   - Must be valid YAML (basic structure check)

7. `.github/workflows/ci-enforcement.yml`
   - CI workflow file (triggers CI runs)

**Phase 2: CI Scripts (10 scripts)**
- `.github/scripts/bootstrap_check.py`
- `.github/scripts/check_ci_sentinel.py`
- `.github/scripts/check_engine_version_presence.py`
- `.github/scripts/check_engine_version_value.py`
- `.github/scripts/check_anti_tamper.py`
- `.github/scripts/check_stage_consistency.py`
- `.github/scripts/check_stage_guard.py`
- `.github/scripts/check_stack_lock.py`
- `.github/scripts/check_ssot_lock.py`
- `.github/scripts/check_implementation_ban.py`

**Total Minimum**: 17 files before first push can succeed

### 1.2 File Order Sensitivity

**Critical Order Dependencies:**

1. **CURRENT_STATE_SNAPSHOT.md must exist before:**
   - bootstrap check (fails if missing)
   - engine-version-gate (fails if missing)
   - engine-version-value-gate (silently passes if missing, but bootstrap already failed)
   - stage-registry-guard (fails if missing or unparseable)

2. **docs/stage_status.md must exist and be parseable before:**
   - bootstrap check can determine which stage files to check
   - stage-registry-guard can compare with CURRENT_STATE_SNAPSHOT.md

3. **Stage-specific files must match stage_status.md:**
   - If stage_status.md says "Stage 5", bootstrap expects:
     - `docs/STAGE_5_CONTROLLED_IMPLEMENTATION.md`
     - `docs/registry/stage_5_endpoints.yaml`
   - Mismatch causes bootstrap failure

**Order-Sensitive Creation Sequence:**
1. Create `docs/stage_status.md` with correct stage number
2. Create `CURRENT_STATE_SNAPSHOT.md` with matching `ACTIVE_STAGE`
3. Create stage-specific files matching the stage number
4. Create all other bootstrap-required files
5. Create CI scripts and workflow

**Human Risk**: If files are created out of order, bootstrap will fail with unclear error messages about missing files.

### 1.3 First Push CI Behavior

**Scenario: Human clones repository and pushes first commit**

**CI Execution Path:**

1. **ci-sentinel** (runs first, no dependencies)
   - Checks: Default branch detectable, git history depth
   - **If fails**: Human-readable diagnostic message printed
   - **If passes**: No output, continues

2. **bootstrap** (depends on ci-sentinel)
   - Checks: 7 mandatory files exist and are readable
   - Checks: stage_status.md is parseable
   - Checks: Stage-specific files exist
   - **If fails**: Specific error message for missing file
   - **If passes**: Prints "ENGINE bootstrap checks passed"

3. **engine-version-gate** (depends on bootstrap)
   - Checks: ENGINE_VERSION field exists in CURRENT_STATE_SNAPSHOT.md
   - **If fails**: "ENGINE_VERSION is not declared in CURRENT_STATE_SNAPSHOT.md"
   - **If passes**: No output

4. **engine-version-value-gate** (depends on engine-version-gate)
   - Checks: ENGINE_VERSION value is "v1" (hardcoded allowlist)
   - **If fails**: "ENGINE_VERSION value is invalid or unsupported: {value}"
   - **If passes**: No output

5. **anti-tamper** (depends on previous gates)
   - Checks: Changes to .github/workflows/* or .github/scripts/*
   - Checks: [CI-APPROVED] token in commit message or PR title
   - **If fails**: "ENGINE anti-tamper violation: CI modification detected without explicit human approval."
   - **If passes**: No output

6. **stage-registry-guard** (depends on previous gates)
   - Checks: Stage number matches between CURRENT_STATE_SNAPSHOT.md and stage_status.md
   - Checks: Registry file exists for active stage
   - Checks: Registry YAML structure is valid
   - **If fails**: Specific error message about mismatch or missing file
   - **If passes**: No output

7. **Remaining jobs** (stage-guard, stack-lock, ssot-lock, implementation-ban)
   - All depend on stage-registry-guard
   - Execute only if all previous gates pass

**First Push Success Criteria:**
- All 7 bootstrap files exist
- CURRENT_STATE_SNAPSHOT.md has correct format (ENGINE_VERSION, ACTIVE_STAGE, ACTIVE_BLUEPRINT)
- stage_status.md matches CURRENT_STATE_SNAPSHOT.md stage number
- Stage-specific files exist
- No CI modifications in first commit (or [CI-APPROVED] token present)

**First Push Failure Scenarios:**
- Missing any bootstrap file → bootstrap fails
- CURRENT_STATE_SNAPSHOT.md missing → bootstrap fails
- ENGINE_VERSION missing → engine-version-gate fails
- ENGINE_VERSION not "v1" → engine-version-value-gate fails
- Stage mismatch → stage-registry-guard fails
- CI files modified without token → anti-tamper fails

### 1.4 Concrete Human-Visible Startup Path

**Step-by-Step Path (from empty directory):**

**Step 1: Repository Setup**
- Create GitHub repository
- Enable GitHub Actions (Settings → Actions → General)
- Set default branch (Settings → Branches → Default branch)
- Clone repository locally

**Step 2: Create Bootstrap Files (Order Matters)**
1. Create `docs/stage_status.md`:
   ```
   Current Stage: Stage 5
   ```
2. Create `CURRENT_STATE_SNAPSHOT.md` (repository root):
   ```
   ENGINE_VERSION: v1
   ACTIVE_STAGE: 5
   ACTIVE_BLUEPRINT: none
   ```
3. Create `docs/STAGE_5_CONTROLLED_IMPLEMENTATION.md`
4. Create `docs/registry/stage_5_endpoints.yaml` (valid YAML)
5. Create `docs/ENGINE_HANDOFF_PROMPT.md`
6. Create `docs/BLUEPRINT_INTERFACE.md`

**Step 3: Create CI Infrastructure**
1. Create `.github/workflows/ci-enforcement.yml`
2. Create all 10 CI scripts in `.github/scripts/`

**Step 4: First Commit and Push**
- Commit all files
- Push to default branch
- **Expected**: CI runs, all gates pass

**Step 5: Verify CI Success**
- Check GitHub Actions tab
- All jobs should pass
- No error messages

**Human Friction Point**: Steps 2-3 require knowledge of exact file names, locations, and formats. No single document provides this complete list.

---

## SECTION 2: CURRENT_STATE_SNAPSHOT REAL AUTHORITY

### 2.1 CI Jobs Directly Dependent on CURRENT_STATE_SNAPSHOT.md

**Direct Dependencies (4 jobs):**

1. **bootstrap**
   - Checks: File existence only
   - Error: "ENGINE bootstrap failure: CURRENT_STATE_SNAPSHOT.md missing at repository root"
   - **Does NOT validate structure or fields**

2. **engine-version-gate**
   - Reads: ENGINE_VERSION field
   - Pattern: `ENGINE_VERSION\s*[:=]\s*v\d+`
   - Error: "ENGINE_VERSION is not declared in CURRENT_STATE_SNAPSHOT.md"
   - **Does NOT validate value, only presence**

3. **engine-version-value-gate**
   - Reads: ENGINE_VERSION value
   - Validates: Must be "v1" (hardcoded allowlist)
   - Error: "ENGINE_VERSION value is invalid or unsupported: {value}"
   - **Silently passes if file missing (bootstrap already failed)**

4. **stage-registry-guard**
   - Reads: "Active stage: STAGE N" or "Active stage: Stage N"
   - Pattern: `Active stage:\s*STAGE\s+(\d+)` or `Active stage:\s*Stage\s+(\d+)`
   - **Critical Mismatch**: CURRENT_STATE_SNAPSHOT.md uses `ACTIVE_STAGE: 5`, but script expects `Active stage: Stage 5`
   - **This will cause stage-registry-guard to fail**

**Indirect Dependencies:**
- All jobs after stage-registry-guard depend on it passing
- If stage-registry-guard fails, all downstream jobs are skipped

### 2.2 Documents Assuming CURRENT_STATE_SNAPSHOT.md Existence

**Documents that reference CURRENT_STATE_SNAPSHOT.md:**

1. **ENGINE_V1_FREEZE.md**
   - Declares: "CURRENT_STATE_SNAPSHOT.md is the highest-priority source of truth"
   - Declares: "Must be read first by any AI agent"

2. **ENGINE_VERSION_DECLARATION_SPEC.md**
   - Declares: "The ONLY authoritative source of ENGINE version"
   - Declares: "ENGINE_VERSION field MUST exist"

3. **BLUEPRINT_ACTIVATION_SPEC.md**
   - Declares: "The active Blueprint is declared ONLY in CURRENT_STATE_SNAPSHOT.md"
   - Declares: "ACTIVE_BLUEPRINT field required"

4. **ENGINE_HANDOFF_PROMPT.md**
   - Declares: "Read this file FIRST before any other action"
   - Declares: "If this file does not exist: STOP and ask the human"

5. **ENGINE_CI_BOOTSTRAP.md**
   - Declares: "CURRENT_STATE_SNAPSHOT.md exists at repository root" as mandatory check
   - Declares: "Stage declaration consistency" requires reading from CURRENT_STATE_SNAPSHOT.md

**Total**: 5 major governance documents assume existence

### 2.3 Failure Behavior When Fields Are Missing or Malformed

**Field: ENGINE_VERSION**

**Missing:**
- engine-version-gate fails: "ENGINE_VERSION is not declared in CURRENT_STATE_SNAPSHOT.md"
- **Human Action**: Add `ENGINE_VERSION: v1` to file

**Malformed (wrong format):**
- Pattern expects: `ENGINE_VERSION\s*[:=]\s*v\d+`
- Examples that fail:
  - `ENGINE_VERSION v1` (no colon/equals)
  - `engine_version: v1` (case-sensitive, but pattern is case-insensitive, so this might pass)
  - `ENGINE_VERSION: 1` (missing 'v' prefix)
- **Human Action**: Fix format to match pattern

**Wrong Value:**
- engine-version-value-gate fails: "ENGINE_VERSION value is invalid or unsupported: {value}"
- Only "v1" is allowed (hardcoded)
- **Human Action**: Change to "v1" or wait for ENGINE v2 support

**Field: ACTIVE_STAGE**

**Missing:**
- stage-registry-guard fails: "Error: Cannot parse stage from CURRENT_STATE_SNAPSHOT.md"
- **Human Action**: Add `ACTIVE_STAGE: 5` (or matching stage)

**Format Mismatch (CRITICAL):**
- CURRENT_STATE_SNAPSHOT.md uses: `ACTIVE_STAGE: 5`
- check_stage_consistency.py expects: `Active stage: STAGE 5` or `Active stage: Stage 5`
- **This is a format mismatch that will cause failure**
- **Human Action**: Either change CURRENT_STATE_SNAPSHOT.md format or update script pattern

**Wrong Value:**
- stage-registry-guard fails: "ENGINE stage conflict: CURRENT_STATE_SNAPSHOT.md declares stage {X}, docs/stage_status.md declares stage {Y}"
- **Human Action**: Update one file to match the other

**Field: ACTIVE_BLUEPRINT**

**Missing:**
- No CI check currently validates this field
- **Documentation declares it required, but CI does not enforce**
- **Human Risk**: Field could be missing without CI catching it

**Malformed:**
- No CI validation of format
- **Human Risk**: Invalid format would not be caught until Blueprint activation attempted

**Wrong Value (blueprint doesn't exist):**
- No CI check validates blueprint directory exists
- **Human Risk**: Could set `ACTIVE_BLUEPRINT: nonexistent` without CI catching it

### 2.4 Error Message Human-Actionability

**Highly Actionable Messages:**
- "ENGINE bootstrap failure: CURRENT_STATE_SNAPSHOT.md missing at repository root"
  - **Action**: Create file at repository root
- "ENGINE_VERSION is not declared in CURRENT_STATE_SNAPSHOT.md"
  - **Action**: Add `ENGINE_VERSION: v1` field
- "ENGINE_VERSION value is invalid or unsupported: {value}"
  - **Action**: Change value to "v1"
- "ENGINE stage conflict: CURRENT_STATE_SNAPSHOT.md declares stage {X}, docs/stage_status.md declares stage {Y}"
  - **Action**: Update one file to match

**Less Actionable Messages:**
- "Error: Cannot parse stage from CURRENT_STATE_SNAPSHOT.md"
  - **Issue**: Doesn't specify expected format
  - **Human Confusion**: What format is expected?
- "ENGINE registry validation failure: docs/registry/stage_{N}_endpoints.yaml is malformed or invalid"
  - **Issue**: Doesn't specify what's wrong with YAML
  - **Human Confusion**: Which line? What syntax error?

**Critical Gap:**
- No error message for "ACTIVE_STAGE format mismatch"
- Script expects "Active stage: Stage 5" but file has "ACTIVE_STAGE: 5"
- **Human Risk**: Will fail with "Cannot parse stage" which doesn't explain format issue

---

## SECTION 3: STAGE AND BLUEPRINT HUMAN CONFUSION POINTS

### 3.1 Blueprint Directory Exists But Cannot Build

**Confusion Scenario:**
- Human creates `/blueprints/my-project/BLUEPRINT.md`
- Human expects: "Blueprint exists, so I can start building"
- **Reality**: Blueprint is NOT active until `ACTIVE_BLUEPRINT: my-project` is set in CURRENT_STATE_SNAPSHOT.md

**Documentation Says:**
- BLUEPRINT_ACTIVATION_SPEC.md: "Directory existence does NOT imply activation"
- BLUEPRINT_INTERFACE.md: "Directory existence does NOT imply activation"

**CI Behavior:**
- No CI check validates ACTIVE_BLUEPRINT field
- No CI check validates blueprint directory exists when ACTIVE_BLUEPRINT is set
- **Gap**: Documentation says CI should check, but no implementation exists

**Human Mental Model Mismatch:**
- **Human Expectation**: "If I create the directory, it's active"
- **ENGINE Reality**: "Only CURRENT_STATE_SNAPSHOT.md activates"
- **Friction**: Human must read BLUEPRINT_ACTIVATION_SPEC.md to understand this

### 3.2 Stage Changed But CI Blocks Progress

**Confusion Scenario:**
- Human updates `docs/stage_status.md` to "Current Stage: Stage 6"
- Human expects: "Stage 6 is now active"
- **Reality**: CI fails because:
  1. CURRENT_STATE_SNAPSHOT.md still says `ACTIVE_STAGE: 5`
  2. `docs/STAGE_6_CONTROLLED_IMPLEMENTATION.md` doesn't exist
  3. `docs/registry/stage_6_endpoints.yaml` doesn't exist

**Documentation Says:**
- ENGINE_CI_BOOTSTRAP.md: "Stage declaration consistency" requires both files to match
- stage-registry-guard enforces this

**Human Mental Model Mismatch:**
- **Human Expectation**: "Update one file to change stage"
- **ENGINE Reality**: "Must update multiple files in sync"
- **Friction**: Human must update:
  1. `docs/stage_status.md`
  2. `CURRENT_STATE_SNAPSHOT.md` (ACTIVE_STAGE field)
  3. Create `docs/STAGE_{N}_CONTROLLED_IMPLEMENTATION.md`
  4. Create `docs/registry/stage_{N}_endpoints.yaml`

### 3.3 Stage 5 vs Stage 4 Confusion

**Current State:**
- `docs/stage_status.md`: "Current Stage: Stage 5"
- `docs/STAGE_5_CONTROLLED_IMPLEMENTATION.md`: "Stage 5 is ACTIVE"
- `CURRENT_STATE_SNAPSHOT.md`: `ACTIVE_STAGE: 5`

**Human Confusion Points:**
- Stage 5 "allows incremental endpoint expansion" but "all Stage 4 constraints remain unchanged"
- **Human Question**: "What's the actual difference?"
- **Answer**: Stage 5 allows more endpoints in registry, but execution pattern is identical

**Documentation Clarity:**
- STAGE_5_CONTROLLED_IMPLEMENTATION.md clearly states: "All Stage 4 execution constraints remain unchanged"
- **But**: Human might not read this carefully and assume Stage 5 is more permissive

### 3.4 Blueprint Location Confusion

**Current State:**
- BLUEPRINT_ACTIVATION_SPEC.md: `/blueprints/<name>/BLUEPRINT.md`
- BLUEPRINT_INSTANCE_FORMAT.md: `/blueprints/<blueprint_name>/BLUEPRINT.md`
- BLUEPRINT_INTERFACE.md: `/blueprints/<blueprint_name>/BLUEPRINT.md` (after recent update)

**All documents now agree**, but:
- **Historical Confusion**: BLUEPRINT_INTERFACE.md previously suggested `docs/blueprints/`
- **Human Risk**: If reading old documentation or cached versions, might use wrong path

---

## SECTION 4: CI HIDDEN PREREQUISITES

### 4.1 CI Conditions Not Obvious from Documentation

**Hidden Prerequisite 1: Git History Depth**
- **Requirement**: `fetch-depth: 0` in checkout action
- **Reason**: anti-tamper check needs git diff
- **Documentation**: Mentioned in check_ci_sentinel.py but not in ENGINE_CI_BOOTSTRAP.md
- **Human Risk**: If workflow doesn't specify fetch-depth: 0, CI might fail silently

**Hidden Prerequisite 2: Default Branch Detection**
- **Requirement**: GITHUB_REF_NAME or GITHUB_REF environment variables
- **Reason**: ci-sentinel checks default branch
- **Documentation**: Not explicitly documented
- **Human Risk**: If GitHub Actions environment is misconfigured, CI fails

**Hidden Prerequisite 3: [CI-APPROVED] Token Format**
- **Requirement**: Exact token `[CI-APPROVED]` in commit message or PR title
- **Reason**: anti-tamper check requires explicit approval
- **Documentation**: Mentioned in check_anti_tamper.py but not prominently
- **Human Risk**: Human might use variations like "[CI APPROVED]" or "CI-APPROVED" which won't work

**Hidden Prerequisite 4: CURRENT_STATE_SNAPSHOT.md Field Format**
- **Requirement**: Exact field names and formats
  - `ENGINE_VERSION: v1` (not `ENGINE_VERSION=v1` or `engine_version: v1`)
  - `ACTIVE_STAGE: 5` (but script expects `Active stage: Stage 5` - **format mismatch**)
  - `ACTIVE_BLUEPRINT: none` (no validation exists)
- **Documentation**: Format not documented in one place
- **Human Risk**: Field format errors cause unclear failures

### 4.2 Actions Humans Think Are Normal But Require Special Tokens

**Action: Modify CI Workflow**
- **Human Expectation**: "I can modify CI like any code"
- **Reality**: Requires `[CI-APPROVED]` token in commit message
- **Failure**: "ENGINE anti-tamper violation: CI modification detected without explicit human approval."
- **Friction**: Human must remember to include token

**Action: Modify CI Scripts**
- **Human Expectation**: "I can fix bugs in CI scripts"
- **Reality**: Requires `[CI-APPROVED]` token
- **Failure**: Same as above
- **Friction**: Human must remember to include token

**Action: First Commit with CI Files**
- **Human Expectation**: "First commit can include CI setup"
- **Reality**: If CI files are in first commit, anti-tamper might fail (depends on git diff logic)
- **Friction**: Unclear if first commit needs token

### 4.3 Startup-Level CI Blockers

**Blocker 1: Missing CURRENT_STATE_SNAPSHOT.md**
- **Blocks**: bootstrap, engine-version-gate, stage-registry-guard, all downstream
- **Error**: Clear and actionable
- **Recovery**: Create file with correct format

**Blocker 2: Missing ENGINE_VERSION Field**
- **Blocks**: engine-version-gate, all downstream
- **Error**: Clear and actionable
- **Recovery**: Add field to CURRENT_STATE_SNAPSHOT.md

**Blocker 3: ENGINE_VERSION Not "v1"**
- **Blocks**: engine-version-value-gate, all downstream
- **Error**: Clear but restrictive (only v1 allowed)
- **Recovery**: Change to "v1" or wait for v2 support

**Blocker 4: Stage Format Mismatch**
- **Blocks**: stage-registry-guard, all downstream
- **Error**: "Error: Cannot parse stage from CURRENT_STATE_SNAPSHOT.md"
- **Recovery**: **Unclear** - error doesn't specify expected format
- **Critical Gap**: Format mismatch between CURRENT_STATE_SNAPSHOT.md (`ACTIVE_STAGE: 5`) and script expectation (`Active stage: Stage 5`)

**Blocker 5: Stage Number Mismatch**
- **Blocks**: stage-registry-guard, all downstream
- **Error**: "ENGINE stage conflict: CURRENT_STATE_SNAPSHOT.md declares stage {X}, docs/stage_status.md declares stage {Y}"
- **Recovery**: Update one file to match

**Blocker 6: Missing Stage-Specific Files**
- **Blocks**: bootstrap, all downstream
- **Error**: "ENGINE bootstrap failure: docs/STAGE_{N}_CONTROLLED_IMPLEMENTATION.md missing for current stage {N}"
- **Recovery**: Create missing file

**Blocker 7: Missing Registry File**
- **Blocks**: bootstrap, all downstream
- **Error**: "ENGINE bootstrap failure: docs/registry/stage_{N}_endpoints.yaml missing or unreadable for current stage {N}"
- **Recovery**: Create missing file

---

## SECTION 5: ENGINE BEHAVIOR WITHOUT ACTIVE BLUEPRINT

### 5.1 Explicitly Allowed (ACTIVE_BLUEPRINT: none)

**From BLUEPRINT_ACTIVATION_SPEC.md:**

**Allowed:**
- Governance work
- ENGINE infrastructure work
- Blueprint drafting

**From ENGINE_HANDOFF_PROMPT.md:**

**Allowed (Default Mode):**
- Read documentation files
- Analyze repository structure
- Audit consistency
- Propose next steps (as suggestions, not implementations)
- Ask clarification questions
- Prepare plans, checklists, diffs (NOT applying them)
- Draft documentation
- Identify risks and gaps

**From STAGE_5_CONTROLLED_IMPLEMENTATION.md:**

**Allowed:**
- Executable endpoints **only if** they conform to "Authorized Execution Pattern"
- Endpoints must be registered in `docs/registry/stage_5_endpoints.yaml`
- No persistence, external API calls, background tasks, state mutation

**CI Behavior:**
- All CI checks run normally
- implementation-ban checks endpoint registry compliance
- No special handling for "no blueprint" state

### 5.2 Explicitly Forbidden (ACTIVE_BLUEPRINT: none)

**From BLUEPRINT_ACTIVATION_SPEC.md:**

**Forbidden:**
- Project-specific implementation
- Project-specific assumptions

**From ENGINE_HANDOFF_PROMPT.md:**

**Forbidden (Default Mode):**
- Implement new endpoints (without registry authorization)
- Uncomment frozen code
- Add business logic
- Introduce persistence or databases
- Call external APIs
- Modify execution behavior
- Weaken CI or governance rules
- Assume missing context

**From STAGE_5_CONTROLLED_IMPLEMENTATION.md:**

**Forbidden:**
- Database integration
- Auth
- Async workflows
- AI calls
- Side effects
- Unregistered endpoints

### 5.3 Gray Zones (Documentation vs CI)

**Gray Zone 1: Blueprint Drafting Location**
- **Documentation**: "Blueprint drafting" is allowed
- **CI**: No check prevents creating files in `/blueprints/`
- **Status**: Allowed, but no guidance on where to draft

**Gray Zone 2: Endpoint Implementation Without Blueprint**
- **Documentation**: "Project-specific implementation" is forbidden
- **Question**: Is `/health` endpoint "project-specific"?
- **CI**: Allows `/health` if registered in stage_5_endpoints.yaml
- **Status**: Ambiguous - endpoint exists but no project is active

**Gray Zone 3: Documentation Updates**
- **Documentation**: "Draft documentation" is allowed
- **Question**: Can human update ENGINE governance docs?
- **CI**: ssot-lock prevents modification of frozen docs (GCD, S1, S2)
- **Status**: Allowed for non-frozen docs, forbidden for frozen docs

**Gray Zone 4: Registry Updates**
- **Documentation**: "Registry update requires human approval"
- **Question**: Can human update registry when ACTIVE_BLUEPRINT: none?
- **CI**: No check prevents registry updates
- **Status**: Allowed, but documentation suggests approval needed

### 5.4 CI Behavior Without Active Blueprint

**Current CI Behavior:**
- No CI job checks ACTIVE_BLUEPRINT field
- No CI job validates blueprint directory exists
- No CI job prevents "project-specific" implementation
- **Gap**: Documentation declares expectations, but CI doesn't enforce

**What CI Actually Enforces:**
- Endpoint registry compliance (stage-aware)
- Technology stack lock
- SSOT lock (frozen docs)
- Implementation bans (database, persistence, etc.)
- Stage/registry alignment

**What CI Does NOT Enforce:**
- ACTIVE_BLUEPRINT field presence
- ACTIVE_BLUEPRINT field format
- Blueprint directory existence when ACTIVE_BLUEPRINT is set
- "Project-specific" vs "infrastructure" distinction

**Human Risk**: Human could set `ACTIVE_BLUEPRINT: invalid-name` and CI would not catch it until Blueprint activation is attempted.

---

## SECTION 6: HIGH-RISK HUMAN ERROR POINTS

### 6.1 Format Mismatch: ACTIVE_STAGE Field

**Risk Level**: CRITICAL

**Issue:**
- CURRENT_STATE_SNAPSHOT.md uses: `ACTIVE_STAGE: 5`
- check_stage_consistency.py expects: `Active stage: STAGE 5` or `Active stage: Stage 5`
- **This is a guaranteed failure**

**Human Experience:**
1. Human creates CURRENT_STATE_SNAPSHOT.md with `ACTIVE_STAGE: 5`
2. Human pushes to GitHub
3. CI fails: "Error: Cannot parse stage from CURRENT_STATE_SNAPSHOT.md"
4. Human confused: "The field exists, why can't it parse?"

**Root Cause**: Format mismatch between file format and script expectation

**Impact**: Blocks all CI after stage-registry-guard

### 6.2 Missing [CI-APPROVED] Token

**Risk Level**: HIGH

**Issue:**
- Human modifies `.github/workflows/ci-enforcement.yml` or `.github/scripts/*`
- Human forgets to include `[CI-APPROVED]` in commit message
- CI fails: "ENGINE anti-tamper violation: CI modification detected without explicit human approval."

**Human Experience:**
1. Human fixes a bug in CI script
2. Human commits with message: "Fix CI script bug"
3. CI fails with anti-tamper error
4. Human confused: "I'm fixing a bug, why do I need approval?"

**Root Cause**: Token requirement not obvious from workflow

**Impact**: Blocks all CI after anti-tamper

### 6.3 Stage Number Mismatch

**Risk Level**: MEDIUM

**Issue:**
- Human updates `docs/stage_status.md` to "Current Stage: Stage 6"
- Human forgets to update `CURRENT_STATE_SNAPSHOT.md`
- CI fails: "ENGINE stage conflict: CURRENT_STATE_SNAPSHOT.md declares stage 5, docs/stage_status.md declares stage 6"

**Human Experience:**
1. Human wants to advance to Stage 6
2. Human updates stage_status.md
3. CI fails with conflict error
4. Human must update both files

**Root Cause**: Two files must be kept in sync manually

**Impact**: Blocks all CI after stage-registry-guard

### 6.4 Missing Stage-Specific Files

**Risk Level**: MEDIUM

**Issue:**
- Human updates stage to Stage 6
- Human forgets to create `docs/STAGE_6_CONTROLLED_IMPLEMENTATION.md`
- CI fails: "ENGINE bootstrap failure: docs/STAGE_6_CONTROLLED_IMPLEMENTATION.md missing for current stage 6"

**Human Experience:**
1. Human advances stage
2. CI fails with missing file error
3. Human must create stage-specific files

**Root Cause**: Stage advancement requires multiple file updates

**Impact**: Blocks bootstrap, all downstream

### 6.5 ENGINE_VERSION Value Restriction

**Risk Level**: LOW (but confusing)

**Issue:**
- Human sets `ENGINE_VERSION: v2` (expecting future support)
- CI fails: "ENGINE_VERSION value is invalid or unsupported: v2"
- Only "v1" is allowed (hardcoded)

**Human Experience:**
1. Human wants to use ENGINE v2
2. Human sets ENGINE_VERSION: v2
3. CI fails
4. Human confused: "How do I upgrade to v2?"

**Root Cause**: Hardcoded allowlist, no upgrade path documented

**Impact**: Blocks all CI after engine-version-value-gate

---

## SECTION 7: DIRECT WRITING INPUTS FOR HUMAN STARTUP MANUAL

### 7.1 Minimum Startup Checklist

**For Human Startup Manual, include:**

1. **Prerequisites:**
   - GitHub repository created
   - GitHub Actions enabled
   - Default branch set
   - Repository cloned locally

2. **Required Files (in order):**
   - `docs/stage_status.md` (with "Current Stage: Stage N")
   - `CURRENT_STATE_SNAPSHOT.md` (with exact format - see below)
   - `docs/STAGE_{N}_CONTROLLED_IMPLEMENTATION.md`
   - `docs/registry/stage_{N}_endpoints.yaml`
   - `docs/ENGINE_HANDOFF_PROMPT.md`
   - `docs/BLUEPRINT_INTERFACE.md`
   - `.github/workflows/ci-enforcement.yml`
   - All 10 CI scripts

3. **CURRENT_STATE_SNAPSHOT.md Exact Format:**
   ```
   ENGINE_VERSION: v1
   ACTIVE_STAGE: 5
   ACTIVE_BLUEPRINT: none
   ```
   **Critical**: Use exact field names and format shown above

4. **First Push:**
   - Commit all files
   - Push to default branch
   - Check GitHub Actions tab
   - All jobs should pass

### 7.2 Common Failure Scenarios and Fixes

**For Human Startup Manual, include troubleshooting:**

1. **"ENGINE_VERSION is not declared"**
   - Fix: Add `ENGINE_VERSION: v1` to CURRENT_STATE_SNAPSHOT.md

2. **"ENGINE_VERSION value is invalid"**
   - Fix: Change value to exactly "v1" (only v1 is supported)

3. **"Cannot parse stage from CURRENT_STATE_SNAPSHOT.md"**
   - Fix: **CRITICAL** - Format mismatch. Script expects "Active stage: Stage 5" but file has "ACTIVE_STAGE: 5"
   - **Either**: Change file to "Active stage: Stage 5"
   - **Or**: Update script pattern (requires [CI-APPROVED] token)

4. **"ENGINE stage conflict"**
   - Fix: Update CURRENT_STATE_SNAPSHOT.md ACTIVE_STAGE to match docs/stage_status.md

5. **"Missing STAGE_{N}_CONTROLLED_IMPLEMENTATION.md"**
   - Fix: Create the file for the current stage number

6. **"Missing stage_{N}_endpoints.yaml"**
   - Fix: Create the registry file for the current stage number

7. **"ENGINE anti-tamper violation"**
   - Fix: Add `[CI-APPROVED]` to commit message or PR title when modifying CI files

### 7.3 Blueprint Activation Process

**For Human Startup Manual, include:**

1. **Create Blueprint:**
   - Create `/blueprints/<name>/BLUEPRINT.md`
   - Follow BLUEPRINT_INSTANCE_FORMAT.md

2. **Activate Blueprint:**
   - Update `CURRENT_STATE_SNAPSHOT.md`:
     - Change `ACTIVE_BLUEPRINT: none` to `ACTIVE_BLUEPRINT: <name>`
   - **Note**: Directory existence does NOT activate - only CURRENT_STATE_SNAPSHOT.md activates

3. **Verify Activation:**
   - **Current Gap**: No CI check validates activation
   - **Manual Check**: Verify ACTIVE_BLUEPRINT field is set correctly

### 7.4 Stage Advancement Process

**For Human Startup Manual, include:**

1. **Update Stage (4 files must change):**
   - `docs/stage_status.md`: "Current Stage: Stage N"
   - `CURRENT_STATE_SNAPSHOT.md`: `ACTIVE_STAGE: N` (or "Active stage: Stage N" if format fixed)
   - Create `docs/STAGE_{N}_CONTROLLED_IMPLEMENTATION.md`
   - Create `docs/registry/stage_{N}_endpoints.yaml`

2. **Verify Consistency:**
   - Stage numbers must match between stage_status.md and CURRENT_STATE_SNAPSHOT.md
   - CI will fail if mismatch

3. **Commit and Push:**
   - Commit all changes together
   - Push to trigger CI
   - Verify all CI checks pass

---

## SECTION 8: CRITICAL FINDINGS SUMMARY

### 8.1 Format Mismatch (CRITICAL)

**Finding**: CURRENT_STATE_SNAPSHOT.md uses `ACTIVE_STAGE: 5` but check_stage_consistency.py expects `Active stage: Stage 5`

**Impact**: stage-registry-guard will always fail with current file format

**Status**: This is a guaranteed failure point

**Recommendation for Manual**: Either document the correct format OR fix the script pattern

### 8.2 Missing CI Enforcement for Blueprint Activation

**Finding**: No CI job checks ACTIVE_BLUEPRINT field or validates blueprint directory exists

**Impact**: Human can set invalid ACTIVE_BLUEPRINT without CI catching it

**Status**: Documentation declares expectations, but CI doesn't enforce

**Recommendation for Manual**: Document that Blueprint activation validation is manual until CI enforcement is added

### 8.3 Hidden Prerequisites

**Finding**: Multiple CI prerequisites not documented:
- Git history depth requirement
- Default branch detection requirement
- [CI-APPROVED] token exact format
- CURRENT_STATE_SNAPSHOT.md field format expectations

**Impact**: Human errors cause unclear failures

**Status**: Prerequisites exist but are not centralized

**Recommendation for Manual**: Create a "CI Prerequisites" section listing all hidden requirements

### 8.4 Two-File Stage Synchronization

**Finding**: Stage must be declared in two files that must match:
- docs/stage_status.md
- CURRENT_STATE_SNAPSHOT.md

**Impact**: Human must remember to update both files

**Status**: This is intentional design but creates friction

**Recommendation for Manual**: Emphasize that both files must be updated together

---

## SECTION 9: AUDIT COMPLETION

**Audit Status**: COMPLETE  
**Files Examined**: 17 governance documents, 10 CI scripts, 1 CI workflow, 1 state snapshot  
**Findings**: 1 critical format mismatch, 3 high-risk error points, 4 gray zones, multiple hidden prerequisites  
**Recommendations**: Documented in Section 7 for Human Startup Manual

**Next Steps**: Human review of findings and creation of Human Startup Manual based on audit results.

---

END OF HUMAN STARTUP PRE-AUDIT REPORT

