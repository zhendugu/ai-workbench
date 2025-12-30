# Constitutional Audit Runbook

**Document Status**: **GOVERNANCE-RUNBOOK**  
**Document Type**: Governance Process Definition  
**Effective Date**: 2025-12-26  
**Purpose**: Defines how to execute CONSTITUTIONAL_COMPLIANCE_CHECKLIST.md

---

## Critical Declaration

**This document does NOT introduce new semantics.**

**This document:**
- Defines how to execute the audit process
- Specifies audit trigger conditions
- Defines audit scope selection rules
- Defines PASS/FAIL recording rules
- Defines remediation procedures
- Does NOT add new constraints or requirements

**This document references:**
- `docs/CONSTITUTIONAL_COMPLIANCE_CHECKLIST.md` (source of all check items)
- All CANONICAL constitutional documents listed in the checklist

---

## Purpose

This document defines the executable process for conducting constitutional compliance audits using the CONSTITUTIONAL_COMPLIANCE_CHECKLIST.md.

**This document exists to:**
- Define when audits must be conducted
- Define what must be audited
- Define how to record audit results
- Define how to handle audit failures
- Define evidence collection structure

**This document does NOT:**
- Add new compliance requirements
- Modify existing constraints
- Provide implementation solutions
- Give business examples
- Enable automatic decision-making from audit results

---

## Referenced CANONICAL Documents

**This runbook executes checks derived from the following CANONICAL documents:**

1. `docs/IMMUTABLE_DESIGN_CONSTRAINTS.md`
2. `docs/PATTERN_METHODOLOGY_ONTOLOGY.md`
3. `docs/CAPABILITY_ONTOLOGY.md`
4. `docs/AUDIT_EVIDENCE_ONTOLOGY.md`
5. `docs/AUTHORIZATION_GOVERNANCE_ONTOLOGY.md`
6. `docs/PATTERN_INSTANCE_SCHEMA.md`
7. `docs/PATTERN_REGISTRY_ONTOLOGY.md`
8. `docs/PATTERN_REGISTRY_LIFECYCLE_RULES.md`
9. `docs/PATTERN_CAPABILITY_USAGE_CONSTRAINTS.md`
10. `docs/PATTERN_REGISTRY_AUDIT_TRACEABILITY.md`
11. `docs/HUMAN_DECISION_SELECTION_BOUNDARY.md`

**All check items in CONSTITUTIONAL_COMPLIANCE_CHECKLIST.md are derived from these documents.**

---

## Audit Trigger Conditions

**Constitutional compliance audits MUST be conducted in the following situations:**

### Trigger 1: Pre-Merge Audit

**When:** Before merging any code changes into main/master branch

**Scope:**
- All code changes in the merge request
- All documentation changes in the merge request
- All design decisions documented in the merge request

**Required:**
- Complete audit of all changed files
- Complete audit of all new capabilities
- Complete audit of all modified capabilities

---

### Trigger 2: Pre-Release Audit

**When:** Before any system release or deployment

**Scope:**
- All code in the release
- All documentation in the release
- All system behavior changes

**Required:**
- Full system-wide audit
- All sections of CONSTITUTIONAL_COMPLIANCE_CHECKLIST.md
- Complete evidence package

---

### Trigger 3: Post-Architecture-Change Audit

**When:** After any architectural change or refactoring

**Scope:**
- All affected subsystems
- All affected capabilities
- All affected documentation
- All affected design decisions

**Required:**
- Audit of all affected areas
- Verification of no constraint violations
- Complete evidence package

---

### Trigger 4: Periodic Compliance Audit

**When:** On a regular schedule (e.g., monthly, quarterly)

**Scope:**
- Entire codebase
- All documentation
- All design decisions
- All system behavior

**Required:**
- Full system-wide audit
- All sections of CONSTITUTIONAL_COMPLIANCE_CHECKLIST.md
- Complete evidence package

---

### Trigger 5: On-Demand Audit

**When:** Requested by human authority

**Scope:**
- As specified by the requesting authority
- May be full system or targeted scope

**Required:**
- Audit of specified scope
- Relevant sections of CONSTITUTIONAL_COMPLIANCE_CHECKLIST.md
- Evidence package as specified

---

## Audit Scope Selection Rules

### Rule 1: Code Changes

**If code changes exist:**
- Audit all modified files
- Audit all new files
- Audit all deleted files
- Audit all affected capabilities
- Audit all affected subsystems

**Selection Criteria:**
- All `.py` files in modified directories
- All test files related to modified code
- All configuration files related to modified code

---

### Rule 2: Documentation Changes

**If documentation changes exist:**
- Audit all modified documentation files
- Audit all new documentation files
- Verify documentation does NOT violate constraints
- Verify documentation does NOT introduce new semantics

**Selection Criteria:**
- All `.md` files in modified directories
- All documentation referenced by modified code
- All design documents related to changes

---

### Rule 3: Design Decision Changes

**If design decisions change:**
- Audit all affected subsystems
- Audit all affected capabilities
- Audit all affected patterns
- Verify design decisions comply with constraints

**Selection Criteria:**
- All design documents related to changes
- All architecture documents related to changes
- All subsystem definitions related to changes

---

### Rule 4: System Behavior Changes

**If system behavior changes:**
- Audit all affected capabilities
- Audit all affected subsystems
- Audit all affected patterns
- Verify behavior changes comply with constraints

**Selection Criteria:**
- All capabilities that exhibit changed behavior
- All subsystems that exhibit changed behavior
- All patterns that exhibit changed behavior

---

## PASS/FAIL Recording Rules

### Rule 1: Evidence Must Be Locatable

**For each check item, evidence MUST be locatable:**

**Required Information:**
- File path (absolute or relative to repository root)
- Line number(s) (if applicable)
- Commit hash (if applicable)
- Section/paragraph reference (for documentation)

**Format:**
```
Check X.Y.Z: ✅ PASS
Evidence: File: backend/subsystems/knowledge_management/storage.py, Lines: 45-52
Commit: abc123def456
```

**OR**

```
Check X.Y.Z: ❌ FAIL
Evidence: File: backend/subsystems/pattern_registry/registry.py, Line: 78
Violation: Automatic version judgment logic detected
Commit: xyz789ghi012
```

---

### Rule 2: PASS Evidence Requirements

**For PASS results, evidence MUST show:**
- The constraint is satisfied
- No violation exists
- Code/documentation/design complies with the constraint

**Minimum Evidence:**
- File path where compliance is demonstrated
- Line number(s) or section reference
- Brief description of how compliance is demonstrated

---

### Rule 3: FAIL Evidence Requirements

**For FAIL results, evidence MUST show:**
- The specific violation
- Where the violation occurs (file path, line number)
- What constraint is violated
- Reference to source CANONICAL document

**Required Information:**
- File path
- Line number(s) or section reference
- Specific violation description
- Source CANONICAL document reference
- Commit hash (if applicable)

---

### Rule 4: Partial Scope Audits

**If audit scope is partial (not full system):**
- Record which sections of checklist were audited
- Record which sections were NOT audited
- Record reason for partial scope
- Record when full audit will be conducted (if applicable)

**Format:**
```
Audit Scope: Partial
Sections Audited: 1.1, 1.2, 2.1, 2.2
Sections NOT Audited: 3.1-3.5, 4.1-4.3
Reason: Pre-merge audit of specific subsystem changes
Full Audit Scheduled: 2025-12-31
```

---

## Remediation Procedures

### Step 1: Document Violation

**When a check item fails:**
1. Record the failure in the audit report
2. Provide specific evidence of violation
3. Reference the source CANONICAL document
4. Document the impact of the violation

**Required Information:**
- Check item identifier (e.g., Check 1.1.1)
- Violation description
- Evidence location (file path, line number)
- Source CANONICAL document
- Impact assessment

---

### Step 2: Propose Remediation

**For each violation:**
1. Propose specific remediation steps
2. Identify files that must be modified
3. Identify constraints that must be satisfied
4. Document remediation approach

**Required Information:**
- Remediation steps (specific, actionable)
- Files to be modified
- Constraints to be satisfied
- Expected outcome

---

### Step 3: Implement Remediation

**After remediation is approved:**
1. Implement the remediation
2. Verify the remediation addresses the violation
3. Re-audit the remediated code/documentation/design
4. Record remediation completion

**Required Information:**
- Remediation implementation details
- Verification results
- Re-audit results
- Remediation completion date

---

### Step 4: Remediation Review

**Before closing a violation:**
1. Human reviewer must verify remediation
2. Re-audit must show PASS for the check item
3. Evidence must show violation is resolved
4. Remediation must be documented

**Required Information:**
- Reviewer identifier
- Review date
- Re-audit results
- Remediation verification

---

## Evidence Package Structure

### Directory Structure

**Evidence packages MUST follow this structure:**

```
audit_evidence/
├── audit_report.md
├── evidence/
│   ├── code/
│   │   ├── file_path_1.py
│   │   └── file_path_2.py
│   ├── documentation/
│   │   ├── doc_path_1.md
│   │   └── doc_path_2.md
│   └── design/
│       ├── design_doc_1.md
│       └── design_doc_2.md
├── checklist_results/
│   └── checklist_results.md
└── remediation/
    └── remediation_log.md
```

---

### Evidence File Requirements

**Each evidence file MUST contain:**
- File path (relative to repository root)
- Line number(s) or section reference
- Check item identifier(s) that reference this evidence
- Brief description of evidence
- Commit hash (if applicable)

**Format:**
```markdown
# Evidence File: backend/subsystems/knowledge_management/storage.py

## Check Items Referenced
- Check 1.1.1: All system capabilities are defined within A2 scope
- Check 1.1.2: No capability exists outside A2

## Evidence Location
- Lines: 10-25
- Commit: abc123def456

## Evidence Description
This file implements C-KM-1 (Store Document) within the Knowledge Management subsystem (A2 scope).
No capabilities are defined outside A2 scope.
```

---

## Audit Report Requirements

**Audit reports MUST use the template:**
- `docs/COMPLIANCE_AUDIT_REPORT_TEMPLATE.md`

**Audit reports MUST include:**
- Audit metadata (date, auditor, scope)
- Checklist results (all checked items)
- Evidence references (file paths, line numbers)
- Violation documentation (if any)
- Remediation records (if any)
- Overall compliance status

---

## Evidence Package Requirements

**Evidence packages MUST follow the guide:**
- `docs/COMPLIANCE_EVIDENCE_PACK_GUIDE.md`

**Evidence packages MUST include:**
- All evidence files referenced in audit report
- Checklist results
- Remediation records (if any)
- Directory structure as specified

---

## Compliance with HUMAN_DECISION_SELECTION_BOUNDARY.md

**This runbook complies with HUMAN_DECISION_SELECTION_BOUNDARY.md:**

**Compliance Points:**
- Audit results do NOT automatically trigger decisions
- Audit results do NOT automatically recommend actions
- Audit results do NOT automatically select remediation approaches
- All remediation decisions are human-explicit
- All audit scope selection is human-explicit (or follows human-defined rules)

**Explicit Constraints:**
- Audit results MUST NOT be used for automatic decision-making
- Audit results MUST NOT be used for automatic recommendation
- Audit results MUST NOT be used for automatic selection
- All remediation decisions MUST be human-explicit

---

## Audit Execution Workflow

### Phase 1: Preparation

1. Identify audit trigger condition
2. Determine audit scope
3. Select relevant checklist sections
4. Prepare evidence collection structure

---

### Phase 2: Execution

1. Execute each check item in selected sections
2. Record PASS/FAIL for each check item
3. Collect evidence for each check item
4. Document violations (if any)

---

### Phase 3: Documentation

1. Complete audit report using template
2. Organize evidence package
3. Document violations (if any)
4. Propose remediation (if violations exist)

---

### Phase 4: Remediation (If Needed)

1. Review violations with human authority
2. Implement approved remediation
3. Re-audit remediated areas
4. Verify remediation completion

---

### Phase 5: Completion

1. Finalize audit report
2. Finalize evidence package
3. Record audit completion
4. Archive audit artifacts

---

## Summary

**This runbook defines the executable process for constitutional compliance audits.**

**Key Components:**
1. Audit trigger conditions (5 triggers)
2. Audit scope selection rules (4 rules)
3. PASS/FAIL recording rules (4 rules)
4. Remediation procedures (4 steps)
5. Evidence package structure (directory tree)
6. Audit execution workflow (5 phases)

**Compliance:**
- Fully compatible with CONSTITUTIONAL_COMPLIANCE_CHECKLIST.md
- Fully compatible with HUMAN_DECISION_SELECTION_BOUNDARY.md
- Does NOT introduce new semantics
- Does NOT enable automatic decision-making from audit results

**Enforcement:**
- All audits MUST follow this runbook
- All audit reports MUST use the template
- All evidence packages MUST follow the guide
- All remediation MUST be human-explicit

---

**END OF CONSTITUTIONAL AUDIT RUNBOOK**

**This document is GOVERNANCE-RUNBOOK.**
**This document does NOT introduce new semantics.**
**This document defines how to execute CONSTITUTIONAL_COMPLIANCE_CHECKLIST.md.**

