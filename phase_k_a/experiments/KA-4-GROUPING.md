# Experiment Specification - KA-4-GROUPING

**Document Status**: NON-CANONICAL  
**Document Type**: Experiment Specification  
**Date**: 2026-01-10  
**Work Order**: WO-KA-4-SINGLE-VARIABLE-INJECTION-GROUPING

---

## Experiment Metadata

### experiment_id

**Value**: `KA-4-GROUPING`

---

### baseline_ref

**Value**: `release/baseline_v1.0/`

**Description**: J10 Baseline v1.0 (FROZEN)

**Previous Experiments**: 
- KA-1-DEFAULT_SELECTION (confirmed as effective agency variable, removed)
- KA-2-VISUAL_HIGHLIGHT (confirmed as effective agency variable, removed)
- KA-3-ORDERING (confirmed as effective agency variable, removed)

---

### branch_name

**Value**: `ka-4-grouping`

---

## Variable Specification

### variable_id(s)

**Value**: `GROUPING`

**Single Variable**: YES

**Justification**: Only GROUPING variable is injected. DEFAULT_SELECTION from KA-1, VISUAL_HIGHLIGHT from KA-2, and ORDERING from KA-3 are removed.

---

### injection_point

**Value**: `frontend`

**Description**: Injection occurs in frontend DOM structure level (container grouping) only.

---

## Change Description

### change_summary

**Factual Description**:
- Removed DEFAULT_SELECTION injection from KA-1 experiment
- Removed VISUAL_HIGHLIGHT injection from KA-2 experiment
- Removed ORDERING injection from KA-3 experiment
- Added GROUPING injection: Split capabilities list into two consecutive DOM containers
- Grouping: Divide capabilities equally into two groups, maintain original registration order within each group
- No visual style changes
- No default selection
- No text labels or semantic hints
- No ordering changes
- No border, background, shadow, or color differences
- All capabilities maintain identical visual appearance
- Only DOM structure change (container grouping)

**Files Modified**:
- `frontend_app/capabilities.html`

**Code Changes**:
- Removed DEFAULT_SELECTION injection code from KA-1
- Removed VISUAL_HIGHLIGHT injection code from KA-2
- Removed ORDERING injection code from KA-3
- Added GROUPING injection: Create two consecutive container divs, divide capabilities equally
- Apply grouping before displayCapabilities() rendering
- No other code changes

---

## Reproducibility

### reproduction_steps

1. Checkout experiment branch: `git checkout ka-4-grouping`
2. Start backend server: `python3 backend_server.py` (or equivalent)
3. Open frontend: Open `frontend_app/capabilities.html` in web browser
4. Observe: Capabilities are displayed in two consecutive groups (containers)
5. Verify: All capabilities have identical visual appearance
6. Verify: No default selection state
7. Verify: No visual highlighting
8. Verify: No ordering changes (capabilities in original registration order within groups)
9. Verify: No text labels or semantic hints
10. Verify: No border, background, or color differences between groups

---

### rollback_steps

1. Checkout baseline branch: `git checkout baseline-v1.0` (or `release/baseline_v1.0/`)
2. Verify baseline state: Capabilities appear in single continuous list (no grouping)
3. Verify: All capabilities have equal visual treatment
4. Verify: No GROUPING injection (baseline has no grouping)
5. Verify: No DEFAULT_SELECTION (baseline has no default)
6. Verify: No VISUAL_HIGHLIGHT (baseline has no visual emphasis)
7. Verify: No ORDERING injection (baseline uses registration order)
8. Confirm: All experiment changes removed
9. Delete experiment branch (optional): `git branch -D ka-4-grouping`

---

## Expected Observations

### expected_drift_signals

**Observable Signals**:
- User may prioritize clicking items in first group
- User may interpret groups as "categories" or "importance levels"
- User may form path convergence within a single group
- User may not realize grouping is arbitrary vs. meaningful
- User attention may concentrate on one group over another
- User may use language like "top group" or "first group" to describe groupings

**Note**: List signals only. No recommendations. No mitigation strategies.

---

## Evidence and Audit

### evidence_pack_paths

**PASS**: `audit_evidence/ka_4_grouping_pass/`  
**FAIL**: `audit_evidence/ka_4_grouping_fail/`

---

### gate_checklist

**Reference**: `phase_k_a/checklists/KA0_PRECHECK.md`

---

## Experiment Status

### status

**Value**: `IN_PROGRESS`

---

## Files Modified

### files_modified

- `frontend_app/capabilities.html`

---

## Code Changes

### code_changes_summary

**Factual Description**:
- Removed KA-1 DEFAULT_SELECTION injection code
- Removed KA-2 VISUAL_HIGHLIGHT injection code
- Removed KA-3 ORDERING injection code
- Added KA-4 GROUPING injection:
  - Create two consecutive container divs (no semantic meaning, no styling differences)
  - Divide capabilities array equally into two groups
  - Maintain original registration order within each group
  - Render each group in separate container
  - Containers have identical styling (only margin spacing, no visual differences)
  - Added comment: `// KA-4 EXPERIMENT: GROUPING injection`
- No other code changes
- No default selection
- No visual highlighting
- No ordering changes
- No text labels
- No border, background, or color differences
- All capabilities maintain identical visual appearance

**Injection Point Annotation**:
- Code includes comment: `// KA-4 EXPERIMENT: GROUPING injection`
- Injection is explicitly marked and traceable

---

## No Recommendations

This specification provides no recommendations.

This specification provides no optimization suggestions.

This specification states only the experiment structure.

---

**END OF EXPERIMENT SPECIFICATION**

