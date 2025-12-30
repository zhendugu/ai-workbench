# Experiment Specification Template

**Document Status**: NON-CANONICAL  
**Document Type**: Experiment Specification Template  
**Date**: 2026-01-10  
**Work Order**: WO-KA-0-AGENCY-VARIABLES-EXPLICITIZATION-AND-EXPERIMENT-HARNESS-BOOTSTRAP

---

## Purpose

This template defines the structure for single-variable agency injection experiments.

Copy this template for each experiment. Fill in all required fields.

**Prohibited Language**: Do not use should/recommend/best practice in this specification.

---

## Experiment Metadata

### experiment_id

**Format**: `KA-<number>-<variable_id>`

**Example**: `KA-1-DEFAULT_SELECTION`

**Required**: YES

---

### baseline_ref

**Description**: Reference to J10 Baseline v1.0

**Format**: 
- Git tag: `baseline-v1.0`
- Commit hash: `<hash>`
- Directory path: `release/baseline_v1.0/`

**Required**: YES

**Example**: `baseline-v1.0` or `release/baseline_v1.0/`

---

### branch_name

**Description**: Git branch name for this experiment

**Format**: `ka-<number>-<variable_id>`

**Example**: `ka-1-default-selection`

**Required**: YES

---

## Variable Specification

### variable_id(s)

**Description**: Agency variable ID(s) being injected

**Format**: Single variable ID or explicit minimal combination

**Required**: YES

**Example**: `DEFAULT_SELECTION`

**Note**: Single variable principle applies. If multiple variables, explicitly justify minimal combination.

---

### injection_point

**Description**: Where variable is injected

**Options**:
- `frontend` - Frontend code only
- `backend` - Backend code only
- `bridge` - Frontend-backend interaction
- `both` - Both frontend and backend (must justify)

**Required**: YES

**Example**: `frontend`

---

## Change Description

### change_summary

**Description**: Factual summary of changes made

**Format**: Factual description only. No recommendations. No optimization language.

**Required**: YES

**Example**:
```
Added pre-selection logic to capabilities.html:
- On page load, first capability in list is pre-selected
- Pre-selected capability has 'selected' CSS class applied
- Pre-selected capability is included in form submission by default
```

**Prohibited Language**: 
- "should"
- "recommend"
- "best practice"
- "better"
- "improve"
- "optimize"

---

## Reproducibility

### reproduction_steps

**Description**: Deterministic steps to reproduce experiment

**Format**: Numbered list of commands and actions

**Required**: YES

**Example**:
```
1. Checkout experiment branch: git checkout ka-1-default-selection
2. Start backend server: python3 backend_server.py
3. Open frontend: open frontend_app/capabilities.html
4. Observe: First capability appears selected on page load
5. Verify: Check browser console for no errors
```

---

### rollback_steps

**Description**: Deterministic steps to rollback to baseline

**Format**: Numbered list of commands and actions

**Required**: YES

**Example**:
```
1. Checkout baseline branch: git checkout baseline-v1.0
2. Verify baseline state: No pre-selection on capabilities.html
3. Confirm: All experiment changes removed
```

---

## Expected Observations

### expected_drift_signals

**Description**: Observable signals that indicate agency drift

**Format**: List of signals only. No recommendations. No mitigation strategies.

**Required**: YES

**Example**:
```
- First capability appears selected on page load
- Pre-selected capability has visual indication (highlighted/checked)
- User may interpret pre-selection as "system recommendation"
- User may assume pre-selected option is "default choice"
```

**Note**: List signals only. Do not provide recommendations or fixes.

---

## Evidence and Audit

### evidence_pack_paths

**Description**: Paths to PASS and FAIL evidence packs

**Format**: 
```
PASS: audit_evidence/ka_<number>_<variable_id>_pass/
FAIL: audit_evidence/ka_<number>_<variable_id>_fail/
```

**Required**: YES

**Example**:
```
PASS: audit_evidence/ka_1_default_selection_pass/
FAIL: audit_evidence/ka_1_default_selection_fail/
```

---

### gate_checklist

**Description**: Checklist used for gate verification

**Format**: Reference to Phase K-A checklist

**Required**: YES

**Example**: `phase_k_a/checklists/KA0_PRECHECK.md`

---

## Experiment Status

### status

**Options**:
- `PLANNED` - Experiment planned but not started
- `IN_PROGRESS` - Experiment in progress
- `COMPLETE` - Experiment completed
- `ROLLED_BACK` - Experiment rolled back to baseline

**Required**: YES

---

## Files Modified

### files_modified

**Description**: List of files modified in this experiment

**Format**: Relative paths from repository root

**Required**: YES

**Example**:
```
- frontend_app/capabilities.html
- frontend_app/capability_run.html
```

---

## Code Changes

### code_changes_summary

**Description**: Factual summary of code changes

**Format**: Factual description only. No recommendations.

**Required**: YES

**Example**:
```
Added JavaScript function selectFirstCapability() in capabilities.html:
- Function called on page load
- Sets 'selected' class on first capability element
- Adds event listener for form submission
```

---

## No Recommendations

This template provides no recommendations.

This template provides no optimization suggestions.

This template states only the specification structure.

---

## Template Usage

1. Copy this template to `phase_k_a/experiments/KA-<number>-<variable_id>.md`
2. Fill in all required fields
3. Use factual language only
4. Avoid prohibited language (should/recommend/best practice)
5. Ensure reproducibility and rollback steps are complete

---

**END OF EXPERIMENT SPECIFICATION TEMPLATE**

