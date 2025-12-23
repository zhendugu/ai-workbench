# ENGINE REPOSITORY INITIALIZATION CHECKLIST

## Purpose

This document defines what it means for an ENGINE repository to be "initialized."

An ENGINE repository is initialized when all mandatory ENGINE artifacts exist, CI can enforce governance rules, and the repository is ready to accept a BLUEPRINT.

CI enforcement requires repository-level setup because:
- CI must verify ENGINE identity before enforcing rules
- CI must have access to governance documents to determine constraints
- CI must be able to validate stage/registry alignment
- CI must fail gracefully when initialization is incomplete

This checklist is ENGINE-level and applies to all ENGINE repositories, regardless of the BLUEPRINT loaded.

---

## Initialization Phases

### Phase 0: Repository Creation

**Status**: Repository exists (copy or template)

**Checklist**:
- [ ] Repository created (new repository or copied from ENGINE template)
- [ ] Repository has a default branch (typically `main` or `master`)
- [ ] Repository is accessible (GitHub, GitLab, or equivalent)

**Notes**:
- Repository may be empty at this phase
- No ENGINE artifacts required yet
- No CI configuration required yet

---

### Phase 1: Mandatory File Presence (ENGINE Artifacts)

**Status**: All required ENGINE documentation files exist

**Checklist**:
- [ ] `CURRENT_STATE_SNAPSHOT.md` exists at repository root
- [ ] `docs/ENGINE_HANDOFF_PROMPT.md` exists
- [ ] `docs/BLUEPRINT_INTERFACE.md` exists
- [ ] `docs/ENGINE_CI_BOOTSTRAP.md` exists
- [ ] `docs/stage_status.md` exists and is parseable
- [ ] `docs/STAGE_{N}_CONTROLLED_IMPLEMENTATION.md` exists for current stage N
- [ ] `docs/registry/stage_{N}_endpoints.yaml` exists for current stage N

**Validation**:
- All files must be readable
- `stage_status.md` must contain parseable stage declaration
- Stage rule document must match current stage
- Registry file must be valid YAML

**Failure Condition**:
- If any file is missing: ENGINE is not initialized
- If any file is unparseable: ENGINE is not initialized

---

### Phase 2: GitHub Settings Initialization

**Status**: GitHub repository settings configured for CI

**Checklist**:
- [ ] GitHub Actions enabled (Settings → Actions → Allow all actions)
- [ ] Default branch defined (Settings → Branches → Default branch)
- [ ] CI workflow file exists (`.github/workflows/ci-enforcement.yml`)
- [ ] CI scripts directory exists (`.github/scripts/`)

**Notes**:
- GitHub Actions may be enabled by default on new repositories
- Default branch is typically `main` or `master`
- CI workflow may fail until Phase 1 is complete (this is expected)
- No branch protection rules are assumed by default

**Human Responsibility**:
- Human must enable GitHub Actions (if not enabled by default)
- Human must verify default branch is set
- Human may configure branch protection (optional, not required)

**Cursor Pro Responsibility**:
- Cursor Pro can verify file existence
- Cursor Pro can verify workflow syntax
- Cursor Pro CANNOT enable GitHub Actions (requires human)
- Cursor Pro CANNOT change default branch (requires human)

---

### Phase 3: CI First-Run Verification

**Status**: CI runs and performs bootstrap checks

**Checklist**:
- [ ] CI workflow triggers on push to default branch
- [ ] CI workflow triggers on pull requests
- [ ] CI bootstrap checks execute
- [ ] CI bootstrap checks pass (all Phase 1 files verified)
- [ ] CI reports initialization status

**Expected CI Behavior**:
- **Before Phase 1 complete**: CI MUST fail with bootstrap failure messages
- **After Phase 1 complete**: CI MUST pass bootstrap checks
- **After Phase 1 complete**: CI MUST proceed to stage/registry enforcement

**CI Failure Messages (Before Initialization)**:
- `ENGINE bootstrap failure: CURRENT_STATE_SNAPSHOT.md missing at repository root`
- `ENGINE bootstrap failure: docs/ENGINE_HANDOFF_PROMPT.md missing`
- `ENGINE bootstrap failure: docs/BLUEPRINT_INTERFACE.md missing`
- `ENGINE bootstrap failure: docs/stage_status.md missing or current stage unparseable`
- `ENGINE bootstrap failure: docs/STAGE_{N}_CONTROLLED_IMPLEMENTATION.md missing for current stage {N}`
- `ENGINE bootstrap failure: docs/registry/stage_{N}_endpoints.yaml missing or unreadable for current stage {N}`

**CI Success Signal (After Initialization)**:
- All bootstrap checks pass
- Stage/registry alignment checks pass
- CI reports: `ENGINE initialized: all bootstrap checks passed`

---

### Phase 4: Ready-for-Blueprint State

**Status**: ENGINE is initialized and ready to accept a BLUEPRINT

**Checklist**:
- [ ] All Phase 1 files exist and are valid
- [ ] All Phase 2 GitHub settings are configured
- [ ] All Phase 3 CI checks pass
- [ ] `CURRENT_STATE_SNAPSHOT.md` declares: `Active blueprint: NONE`
- [ ] Repository is ready to accept BLUEPRINT loading

**Completion Criteria**:
- All mandatory files present
- CI bootstrap checks pass
- CI stage/registry enforcement active
- No BLUEPRINT loaded (ready for loading)

**Next Steps**:
- Human may load a BLUEPRINT
- Human may update `CURRENT_STATE_SNAPSHOT.md` to declare active BLUEPRINT
- Implementation work remains forbidden until BLUEPRINT is loaded and authorized

---

## Mandatory GitHub-Level Checks

These checks must be explicit and verifiable:

### 1. GitHub Actions Enabled
- **Check**: GitHub Actions is enabled for the repository
- **Location**: Settings → Actions → Allow all actions
- **Required**: Yes (mandatory)
- **Human Action**: Human must enable if not enabled by default
- **Cursor Pro Action**: Cursor Pro can verify but cannot enable

### 2. Default Branch Defined
- **Check**: Repository has a default branch
- **Location**: Settings → Branches → Default branch
- **Required**: Yes (mandatory, typically `main` or `master`)
- **Human Action**: Human must set if not set
- **Cursor Pro Action**: Cursor Pro can verify but cannot change

### 3. CI Workflow Present
- **Check**: `.github/workflows/ci-enforcement.yml` exists
- **Required**: Yes (mandatory)
- **Human Action**: None (file should be copied with ENGINE)
- **Cursor Pro Action**: Cursor Pro can verify file existence and syntax

### 4. CI Allowed to Fail Until Initialization Complete
- **Check**: CI workflow may fail during Phase 1 (expected behavior)
- **Required**: Yes (CI must fail if initialization incomplete)
- **Human Action**: None (expected behavior)
- **Cursor Pro Action**: Cursor Pro must not treat Phase 1 CI failures as errors

### 5. No Branch Protection Assumed by Default
- **Check**: Branch protection rules are not required for initialization
- **Required**: No (optional, not mandatory)
- **Human Action**: Human may configure branch protection (optional)
- **Cursor Pro Action**: Cursor Pro must not assume branch protection exists

---

## Explicit Non-Requirements

The following are NOT required for ENGINE initialization:

### Secrets
- **Not Required**: GitHub Secrets
- **Not Required**: Repository Secrets
- **Not Required**: Environment Secrets
- **Reason**: ENGINE governance does not require external authentication

### Cloud Credentials
- **Not Required**: AWS credentials
- **Not Required**: Azure credentials
- **Not Required**: GCP credentials
- **Reason**: ENGINE governance is repository-local

### Environment Variables
- **Not Required**: Repository-level environment variables
- **Not Required**: Workflow-level environment variables
- **Reason**: ENGINE bootstrap checks are file-existence checks, not runtime checks

### External Services
- **Not Required**: External CI services (Travis, CircleCI, etc.)
- **Not Required**: External monitoring services
- **Not Required**: External deployment services
- **Reason**: ENGINE governance is enforced by GitHub Actions only

**Note**: A BLUEPRINT may require these, but they are not ENGINE initialization requirements.

---

## CI Interaction Rules

### Before Initialization (Phase 0-1)

**CI Behavior**:
- CI MUST run bootstrap checks first
- CI MUST fail if any Phase 1 file is missing
- CI MUST emit specific bootstrap failure messages
- CI MUST NOT proceed to other checks if bootstrap fails
- CI MUST block all implementation-related checks

**CI Failure Messages**:
- Exact messages defined in `ENGINE_CI_BOOTSTRAP.md`
- Messages must identify which file is missing
- Messages must be human-readable

**Expected State**:
- CI failures are expected and normal
- CI failures indicate incomplete initialization
- CI failures do not indicate errors in ENGINE design

---

### During Initialization (Phase 2-3)

**CI Behavior**:
- CI MUST continue to run bootstrap checks
- CI MUST verify GitHub Actions is enabled (if detectable)
- CI MUST verify workflow file exists
- CI MUST proceed to stage/registry checks after bootstrap passes
- CI MUST report initialization progress

**CI Success Signal**:
- All bootstrap checks pass
- CI reports: `ENGINE initialized: all bootstrap checks passed`
- CI proceeds to stage/registry enforcement

**CI Failure Signal**:
- Bootstrap checks fail (expected until Phase 1 complete)
- CI reports specific missing files
- CI blocks further checks

---

### After Initialization (Phase 4)

**CI Behavior**:
- CI MUST pass bootstrap checks (hard requirement)
- CI MUST enforce stage/registry alignment
- CI MUST enforce implementation bans
- CI MUST enforce technology stack locks
- CI MUST enforce SSOT locks
- CI MUST report all violations

**CI Success Signal**:
- All checks pass
- CI reports: `ENGINE governance enforcement active`

**CI Failure Signal**:
- Any governance violation detected
- CI reports specific violation type
- CI blocks merge/merge

---

## Human vs Cursor Responsibility Split

### Human Must Do Manually (GitHub UI)

**GitHub Settings**:
- Enable GitHub Actions (if not enabled by default)
- Set default branch (if not set)
- Configure branch protection (optional)
- Manage repository settings

**BLUEPRINT Loading**:
- Provide BLUEPRINT document
- Activate BLUEPRINT in `CURRENT_STATE_SNAPSHOT.md`
- Approve registry updates
- Approve stage advancement

**CI Modifications**:
- Approve changes to `.github/workflows/*`
- Approve changes to `.github/scripts/*`
- Review CI enforcement changes

**Reason**: These actions require repository-level permissions that Cursor Pro does not have.

---

### Cursor Pro Can Verify Automatically

**File Existence**:
- Verify all Phase 1 files exist
- Verify file readability
- Verify file parseability

**File Content**:
- Verify `stage_status.md` is parseable
- Verify stage rule document matches current stage
- Verify registry file is valid YAML
- Verify `CURRENT_STATE_SNAPSHOT.md` structure

**CI Workflow**:
- Verify workflow file syntax
- Verify workflow triggers
- Verify script file existence

**Consistency**:
- Verify stage declarations match between files
- Verify registry alignment with stage
- Verify no conflicts in documentation

**Reason**: These are read-only verification operations that do not require special permissions.

---

### Cursor Pro Must Never Assume

**Cursor Pro MUST NOT assume**:
- GitHub Actions is enabled
- Default branch is set
- Branch protection exists
- Secrets are configured
- External services are available
- BLUEPRINT is loaded
- Implementation is authorized

**Cursor Pro MUST**:
- Verify file existence before reading
- Verify parseability before parsing
- Verify initialization before proceeding
- Ask human if uncertain

**Reason**: Assumptions lead to failures. Verification is required.

---

## Completion Definition

### Exact Conditions: ENGINE Initialized

An ENGINE repository is considered "initialized" when ALL of the following conditions are met:

1. **Phase 1 Complete**: All mandatory files exist and are valid
   - `CURRENT_STATE_SNAPSHOT.md` exists at repository root
   - `docs/ENGINE_HANDOFF_PROMPT.md` exists
   - `docs/BLUEPRINT_INTERFACE.md` exists
   - `docs/ENGINE_CI_BOOTSTRAP.md` exists
   - `docs/stage_status.md` exists and is parseable
   - `docs/STAGE_{N}_CONTROLLED_IMPLEMENTATION.md` exists for current stage N
   - `docs/registry/stage_{N}_endpoints.yaml` exists for current stage N

2. **Phase 2 Complete**: GitHub settings configured
   - GitHub Actions enabled
   - Default branch defined
   - CI workflow file exists

3. **Phase 3 Complete**: CI bootstrap checks pass
   - CI runs successfully
   - All bootstrap checks pass
   - CI reports: `ENGINE initialized: all bootstrap checks passed`

4. **Phase 4 Complete**: Ready for BLUEPRINT
   - All above conditions met
   - `CURRENT_STATE_SNAPSHOT.md` declares: `Active blueprint: NONE`
   - Repository ready to accept BLUEPRINT

### Files and Signals That Must Exist

**Required Files**:
- `CURRENT_STATE_SNAPSHOT.md` (repository root)
- `docs/ENGINE_HANDOFF_PROMPT.md`
- `docs/BLUEPRINT_INTERFACE.md`
- `docs/ENGINE_CI_BOOTSTRAP.md`
- `docs/stage_status.md`
- `docs/STAGE_{N}_CONTROLLED_IMPLEMENTATION.md` (for current stage N)
- `docs/registry/stage_{N}_endpoints.yaml` (for current stage N)
- `.github/workflows/ci-enforcement.yml`
- `.github/scripts/*.py` (CI enforcement scripts)

**Required Signals**:
- CI bootstrap checks pass
- CI reports initialization success
- No bootstrap failure messages

### CI Signal Indicating Readiness

**CI Success Signal**:
```
ENGINE initialized: all bootstrap checks passed
ENGINE governance enforcement active
```

**CI Failure Signal** (Before Initialization):
```
ENGINE bootstrap failure: [specific file missing]
ENGINE not initialized: bootstrap checks failed. Implementation work is forbidden until ENGINE is initialized.
```

---

## Non-Goals

This document does NOT define:

- **Project/business logic**: This document defines ENGINE initialization, not project requirements
- **Blueprint content**: Blueprint content is defined in BLUEPRINT documents, not here
- **Tech stack**: Technology stack is defined in STACK_DECISION.md, not here
- **Implementation authorization**: Implementation authorization requires BLUEPRINT loading and human approval, not just initialization
- **CI implementation details**: This document defines what must exist, not how CI implements checks

This document defines ENGINE repository initialization, not project execution.

---

## Verification Checklist

Use this checklist to verify ENGINE initialization:

### Phase 1: Mandatory Files
- [ ] `CURRENT_STATE_SNAPSHOT.md` exists at repository root
- [ ] `docs/ENGINE_HANDOFF_PROMPT.md` exists
- [ ] `docs/BLUEPRINT_INTERFACE.md` exists
- [ ] `docs/ENGINE_CI_BOOTSTRAP.md` exists
- [ ] `docs/stage_status.md` exists and is parseable
- [ ] `docs/STAGE_{N}_CONTROLLED_IMPLEMENTATION.md` exists for current stage N
- [ ] `docs/registry/stage_{N}_endpoints.yaml` exists for current stage N

### Phase 2: GitHub Settings
- [ ] GitHub Actions enabled
- [ ] Default branch defined
- [ ] `.github/workflows/ci-enforcement.yml` exists
- [ ] `.github/scripts/` directory exists with scripts

### Phase 3: CI Verification
- [ ] CI workflow triggers on push
- [ ] CI workflow triggers on pull requests
- [ ] CI bootstrap checks execute
- [ ] CI bootstrap checks pass
- [ ] CI reports initialization success

### Phase 4: Ready State
- [ ] All Phase 1-3 checks pass
- [ ] `CURRENT_STATE_SNAPSHOT.md` declares: `Active blueprint: NONE`
- [ ] Repository ready to accept BLUEPRINT

**If all checks pass: ENGINE is initialized.**

---

END OF ENGINE REPOSITORY INITIALIZATION CHECKLIST

