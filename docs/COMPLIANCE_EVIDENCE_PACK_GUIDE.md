# Compliance Evidence Pack Guide

**Document Status**: **TEMPLATE**  
**Document Type**: Evidence Package Structure Guide  
**Effective Date**: 2025-12-26  
**Purpose**: Defines structure and requirements for constitutional compliance audit evidence packages

---

## Purpose

This document defines the required structure and content for constitutional compliance audit evidence packages.

**This document:**
- Defines evidence package directory structure
- Specifies evidence file requirements
- Defines evidence collection rules
- Does NOT introduce new compliance requirements

**This document does NOT:**
- Add new constraints
- Modify existing constraints
- Provide implementation solutions
- Give business examples

---

## Evidence Package Structure

### Required Directory Structure

**All evidence packages MUST follow this structure:**

```
audit_evidence/
├── audit_report.md
├── evidence/
│   ├── code/
│   │   ├── [file_path_1].py
│   │   ├── [file_path_2].py
│   │   └── [additional_code_files]
│   ├── documentation/
│   │   ├── [doc_path_1].md
│   │   ├── [doc_path_2].md
│   │   └── [additional_doc_files]
│   └── design/
│       ├── [design_doc_1].md
│       ├── [design_doc_2].md
│       └── [additional_design_files]
├── checklist_results/
│   └── checklist_results.md
└── remediation/
    └── remediation_log.md
```

---

## Evidence File Requirements

### Code Evidence Files

**Location**: `audit_evidence/evidence/code/`

**Required Content:**
- File path (relative to repository root)
- Line number(s) or section reference
- Check item identifier(s) that reference this evidence
- Brief description of evidence
- Commit hash (if applicable)

**File Naming:**
- Use file path with forward slashes replaced by underscores
- Example: `backend_subsystems_knowledge_management_storage.py`

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

## Code Snippet (if applicable)
[Relevant code section]
```

---

### Documentation Evidence Files

**Location**: `audit_evidence/evidence/documentation/`

**Required Content:**
- File path (relative to repository root)
- Section/paragraph reference
- Check item identifier(s) that reference this evidence
- Brief description of evidence
- Commit hash (if applicable)

**File Naming:**
- Use file path with forward slashes replaced by underscores
- Example: `docs_PATTERN_INSTANCE_SCHEMA.md`

**Format:**
```markdown
# Evidence File: docs/PATTERN_INSTANCE_SCHEMA.md

## Check Items Referenced
- Check 6.1.1: Pattern Instance is a concrete, external, replaceable, versionable representation
- Check 6.1.2: Pattern Instance is purely descriptive

## Evidence Location
- Section: Pattern Instance Identity
- Paragraph: What a Pattern Instance IS

## Evidence Description
This section defines Pattern Instance as purely descriptive and external to A2 core.

## Document Snippet (if applicable)
[Relevant document section]
```

---

### Design Evidence Files

**Location**: `audit_evidence/evidence/design/`

**Required Content:**
- File path (relative to repository root)
- Section/paragraph reference
- Check item identifier(s) that reference this evidence
- Brief description of evidence
- Commit hash (if applicable)

**File Naming:**
- Use file path with forward slashes replaced by underscores
- Example: `docs_PHASE_4_GATE_A_DEFINITION.md`

**Format:**
```markdown
# Evidence File: docs/PHASE_4_GATE_A_DEFINITION.md

## Check Items Referenced
- Check 5.2.1: Gate is a structural boundary definition
- Check 5.2.2: Gate defines semantic constraints

## Evidence Location
- Section: Gate Identity Statement
- Paragraph: What a Gate IS

## Evidence Description
This section defines Gate as a structural boundary, not authorization.

## Design Snippet (if applicable)
[Relevant design section]
```

---

## Checklist Results File

**Location**: `audit_evidence/checklist_results/checklist_results.md`

**Required Content:**
- Complete checklist results (all checked items)
- PASS/FAIL status for each item
- Evidence references for each item
- Violation documentation (if any)

**Format:**
```markdown
# Checklist Results

## Section 1: IMMUTABLE_DESIGN_CONSTRAINTS.md Compliance

### 1.1 A2 (Capability Substrate) is the Only Core

- [x] **Check 1.1.1**: ✅ PASS
  - Evidence: `evidence/code/backend_subsystems_knowledge_management_storage.py`
  - File Path: backend/subsystems/knowledge_management/storage.py
  - Line Number(s): 10-25
  - Commit: abc123def456

- [x] **Check 1.1.2**: ✅ PASS
  - Evidence: `evidence/code/backend_subsystems_knowledge_management_storage.py`
  - File Path: backend/subsystems/knowledge_management/storage.py
  - Line Number(s): 10-25
  - Commit: abc123def456

[Continue for all check items...]
```

---

## Remediation Log File

**Location**: `audit_evidence/remediation/remediation_log.md`

**Required Content:**
- All violation records
- All remediation proposals
- All remediation implementations
- All remediation verifications

**Format:**
```markdown
# Remediation Log

## Violation 1

- **Check Item**: Check X.Y.Z
- **Source Document**: docs/PATTERN_METHODOLOGY_ONTOLOGY.md
- **Violation Description**: Pattern contains execution logic
- **Evidence Location**: 
  - File Path: backend/subsystems/pattern/pattern_instance.py
  - Line Number(s): 45-52
  - Commit: xyz789ghi012

## Remediation 1 (for Violation 1)

- **Remediation Steps**:
  1. Remove execution logic from Pattern Instance
  2. Ensure Pattern Instance is purely descriptive
  3. Verify compliance with PATTERN_METHODOLOGY_ONTOLOGY.md

- **Files to Modify**: backend/subsystems/pattern/pattern_instance.py

- **Constraints to Satisfy**: 
  - Pattern MUST NOT execute anything
  - Pattern MUST NOT trigger actions

- **Expected Outcome**: Pattern Instance is purely descriptive

- **Status**: Completed

- **Remediation Date**: 2025-12-26

- **Remediation Implementer**: [Name]

- **Re-Audit Results**: ✅ PASS

- **Reviewer**: [Name]

- **Review Date**: 2025-12-26

[Continue for all remediations...]
```

---

## Evidence Collection Rules

### Rule 1: All Evidence Must Be Locatable

**Every evidence reference MUST include:**
- File path (absolute or relative to repository root)
- Line number(s) or section reference
- Commit hash (if applicable)

---

### Rule 2: Evidence Must Support Check Item

**Every evidence file MUST:**
- Clearly demonstrate compliance (for PASS)
- Clearly demonstrate violation (for FAIL)
- Reference specific check item(s)
- Be verifiable by human reviewer

---

### Rule 3: Evidence Must Be Complete

**Evidence package MUST include:**
- All evidence files referenced in audit report
- All checklist results
- All remediation records (if any)
- Complete directory structure

---

### Rule 4: Evidence Must Be Organized

**Evidence package MUST:**
- Follow required directory structure
- Use consistent file naming
- Include clear references between files
- Enable easy navigation

---

## Evidence Package Validation

### Validation Checklist

**Before finalizing evidence package, verify:**

- [ ] All required directories exist
- [ ] All evidence files are present
- [ ] All evidence files contain required information
- [ ] All file paths are correct
- [ ] All line numbers are accurate
- [ ] All commit hashes are valid (if applicable)
- [ ] All check items have evidence references
- [ ] All violations have remediation records (if applicable)
- [ ] Directory structure matches specification
- [ ] File naming follows convention

---

## Summary

**This guide defines the structure and requirements for evidence packages.**

**Key Components:**
1. Required directory structure
2. Evidence file requirements (code, documentation, design)
3. Checklist results file requirements
4. Remediation log file requirements
5. Evidence collection rules (4 rules)
6. Evidence package validation checklist

**Compliance:**
- Fully compatible with CONSTITUTIONAL_COMPLIANCE_CHECKLIST.md
- Fully compatible with CONSTITUTIONAL_AUDIT_RUNBOOK.md
- Does NOT introduce new compliance requirements

**Enforcement:**
- All evidence packages MUST follow this structure
- All evidence files MUST contain required information
- All evidence packages MUST be validated before submission

---

**END OF COMPLIANCE EVIDENCE PACK GUIDE**

**This document is a TEMPLATE/GUIDE.**
**All evidence packages MUST follow this structure.**

