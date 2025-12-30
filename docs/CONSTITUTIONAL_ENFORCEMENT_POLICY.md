# Constitutional Enforcement Policy

**Document Status**: **CANONICAL**  
**Document Type**: Constitutional-Level Enforcement Policy  
**Effective Date**: 2025-12-26  
**Purpose**: Defines repository-level enforcement mechanisms for constitutional file changes

---

## Purpose

This document describes what D-2 enforces at the repository level and clarifies that enforcement is a repo-level gate, not recommendation, workflow, or automation inside the app.

**This document exists to:**
- Describe repository-level enforcement mechanisms
- Define required environment variables for constitutional changes
- Clarify that enforcement is a repo-level gate only
- Ensure any change to constitutional files is explicitly human-authorized and auditable

**This document does NOT:**
- Provide implementation solutions
- Give specific business examples
- Authorize new capabilities or features
- Modify existing CANONICAL documents
- Introduce new semantics
- Add runtime product behavior
- Add workflow orchestration to the app
- Add recommendation logic
- Auto-select patterns/capabilities

---

## What D-2 Enforces

### Repository-Level Enforcement

**D-2 enforces at the repository level:**
- Detection of constitutional file changes in git diffs
- Requirement for explicit human authorization before constitutional changes
- Validation of evidence pack directory structure
- Prevention of silent or accidental changes to CANONICAL documents

**This means:**
- ✅ Git repository enforcement (pre-commit, CI, PR checks)
- ✅ CANONICAL document change detection
- ✅ Evidence pack integrity validation (structure only)
- ✅ No runtime behavior changes

**This does NOT mean:**
- ❌ Runtime product behavior changes
- ❌ Workflow orchestration in the app
- ❌ Recommendation logic in the app
- ❌ Auto-selection of patterns/capabilities
- ❌ Modification of semantics of existing CANONICAL documents

---

## Required Environment Variables

### For Constitutional File Changes

**The following environment variables are REQUIRED for any constitutional file change:**

1. **CONSTITUTIONAL_CHANGE_AUTH**
   - Value: MUST be exactly "YES"
   - Purpose: Explicit human authorization token
   - Format: Literal string "YES"

2. **CONSTITUTIONAL_CHANGE_SCOPE**
   - Value: Free text describing the scope of changes
   - Purpose: Explicit change scope description
   - Format: Free text (no format restrictions)

3. **CONSTITUTIONAL_CHANGE_RATIONALE**
   - Value: Free text describing the rationale for changes
   - Purpose: Explicit rationale for constitutional changes
   - Format: Free text (no format restrictions)

**All three variables MUST be set for any constitutional file change to proceed.**

---

## Enforcement Mechanisms

### Mechanism 1: Pre-Commit Hook

**Pre-commit hook runs constitutional_diff_detect.py on staged changes.**

**Behavior:**
- Checks staged changes for constitutional file modifications
- If constitutional files are staged and no auth env vars are set → block commit
- If constitutional files are staged and auth env vars are set → allow commit

**Location:**
- Example hook: `tools/git-hooks/pre-commit.example`
- To enable: Copy to `.git/hooks/pre-commit`

**Enforcement:**
- Blocks commits with unauthorized constitutional changes
- Requires explicit human authorization via environment variables

---

### Mechanism 2: CI / PR Gate

**CI check runs constitutional_diff_detect.py against PR diff.**

**Behavior:**
- Checks PR diff for constitutional file modifications
- If constitutional files are changed and no auth env vars are set → fail CI
- If constitutional files are changed and auth env vars are set → pass CI

**Location:**
- CI configuration: `.github/workflows/constitutional-enforcement.yml`

**Enforcement:**
- Fails CI for unauthorized constitutional changes
- Requires explicit human authorization via environment variables
- Default is "deny" (no secrets that auto-authorize)

---

### Mechanism 3: Evidence Pack Structure Validator

**Validator checks evidence pack directory structure.**

**Behavior:**
- Validates only directory structure and required filenames
- Does NOT judge content, quality, or completeness
- Outputs exit non-zero on structural violations

**Location:**
- Script: `scripts/evidence_pack_validate.py`
- Integrated into CI when audit_evidence changes are present

**Enforcement:**
- Validates evidence pack structure matches COMPLIANCE_EVIDENCE_PACK_GUIDE.md
- Does NOT validate content or quality
- Only checks structure and required paths

---

## Explicit Clarifications

### Enforcement Is NOT Recommendation

**Enforcement is a repo-level gate, NOT a recommendation system.**

**This means:**
- ✅ Enforcement blocks unauthorized changes
- ✅ Enforcement requires explicit authorization
- ✅ Enforcement does NOT recommend changes
- ✅ Enforcement does NOT suggest changes

**This does NOT mean:**
- ❌ Enforcement recommends changes
- ❌ Enforcement suggests changes
- ❌ Enforcement infers authorization
- ❌ Enforcement auto-authorizes

---

### Enforcement Is NOT Workflow

**Enforcement is a repo-level gate, NOT workflow orchestration.**

**This means:**
- ✅ Enforcement blocks unauthorized changes
- ✅ Enforcement requires explicit authorization
- ✅ Enforcement does NOT orchestrate workflows
- ✅ Enforcement does NOT coordinate processes

**This does NOT mean:**
- ❌ Enforcement orchestrates workflows
- ❌ Enforcement coordinates processes
- ❌ Enforcement manages execution flow
- ❌ Enforcement schedules operations

---

### Enforcement Is NOT Automation Inside the App

**Enforcement is a repo-level gate, NOT automation inside the app.**

**This means:**
- ✅ Enforcement is repository-level only
- ✅ Enforcement does NOT affect runtime behavior
- ✅ Enforcement does NOT add product features
- ✅ Enforcement does NOT add app automation

**This does NOT mean:**
- ❌ Enforcement affects runtime behavior
- ❌ Enforcement adds product features
- ❌ Enforcement adds app automation
- ❌ Enforcement modifies app semantics

---

## Constitutional Fileset

### Source of Truth

**Constitutional fileset is defined in CONSTITUTIONAL_FILESET.md.**

**This means:**
- ✅ All constitutional files are explicitly listed
- ✅ Any diff touching this fileset is a "constitutional change"
- ✅ Machine-readable file patterns are provided

**This does NOT mean:**
- ❌ Constitutional fileset may be inferred
- ❌ Constitutional fileset may be auto-derived
- ❌ Constitutional fileset may have exceptions

---

## Explicit Prohibitions

**The following are explicitly prohibited (MUST NOT):**

1. **MUST NOT auto-authorize constitutional changes**
   - No automatic authorization mechanisms
   - No inferred authorization
   - No heuristics for authorization

2. **MUST NOT infer human intent**
   - No inference of authorization from context
   - No inference of authorization from state
   - No inference of authorization from patterns

3. **MUST NOT add runtime product behavior**
   - No runtime behavior changes
   - No product feature additions
   - No app automation additions

4. **MUST NOT introduce recommendations or defaults**
   - No recommendation logic
   - No default selection
   - No auto-selection

---

## Compatibility with Existing Documents

**This document is fully compatible with:**
- `docs/CONSTITUTIONAL_FREEZE_POLICY.md` (defines freeze policy)
- `docs/CONSTITUTIONAL_MODIFICATION_GATE.md` (defines modification gate)
- `docs/CONSTITUTIONAL_FULL_AUDIT_REQUIREMENT.md` (defines full audit requirement)
- `docs/CONSTITUTIONAL_FILESET.md` (defines constitutional fileset)
- `docs/COMPLIANCE_EVIDENCE_PACK_GUIDE.md` (defines evidence pack structure)

**This document constrains:**
- All repository-level enforcement mechanisms
- All CI/PR gate configurations
- All pre-commit hook implementations

---

## Relationship to Existing Phases and Gates

**This document constrains all existing and future phases and gates:**
- **Phase-1**: Must comply with this enforcement policy
- **Phase-2**: Must comply with this enforcement policy
- **Phase-3**: Must comply with this enforcement policy
- **Phase-4**: Must comply with this enforcement policy
- **Future Phases**: Must comply with this enforcement policy

- **Gate A**: Must comply with this enforcement policy
- **Future Gates**: Must comply with this enforcement policy

**This document does NOT:**
- ❌ Override phase-specific constraints
- ❌ Override gate-specific constraints
- ❌ Override capability-specific constraints
- ❌ Provide implementation guidance

**This document DOES:**
- ✅ Provide repository-level enforcement mechanisms
- ✅ Ensure constitutional changes are explicitly human-authorized
- ✅ Prevent silent or accidental changes to constitutional files

---

## Summary

**This document establishes repository-level enforcement for constitutional file changes.**

**Key Mechanisms:**
1. Pre-commit hook for local enforcement
2. CI/PR gate for remote enforcement
3. Evidence pack structure validator

**Key Requirements:**
- CONSTITUTIONAL_CHANGE_AUTH=YES
- CONSTITUTIONAL_CHANGE_SCOPE (free text)
- CONSTITUTIONAL_CHANGE_RATIONALE (free text)

**Key Clarifications:**
- Enforcement is NOT recommendation
- Enforcement is NOT workflow
- Enforcement is NOT automation inside the app
- Enforcement is ONLY a repo-level gate

**Enforcement:**
- All constitutional changes MUST be detected
- All constitutional changes MUST require explicit human authorization
- All constitutional changes MUST be auditable

---

**END OF CONSTITUTIONAL ENFORCEMENT POLICY**

**This document is CANONICAL and IMMUTABLE.**
**No repository-level enforcement mechanism may bypass explicit human authorization requirements.**


