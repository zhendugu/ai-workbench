# Experiment Specification - KA-5-PROXIMITY

**Document Status**: NON-CANONICAL  
**Document Type**: Experiment Specification  
**Date**: 2026-01-10  
**Work Order**: WO-KA-5-SINGLE-VARIABLE-INJECTION-PROXIMITY

---

## Experiment Metadata

### experiment_id

**Value**: `KA-5-PROXIMITY`

---

### baseline_ref

**Value**: `release/baseline_v1.0/`

**Description**: J10 Baseline v1.0 (FROZEN)

**Previous Experiments**: 
- KA-1-DEFAULT_SELECTION (confirmed as effective agency variable, removed)
- KA-2-VISUAL_HIGHLIGHT (confirmed as effective agency variable, removed)
- KA-3-ORDERING (confirmed as effective agency variable, removed)
- KA-4-GROUPING (confirmed as effective agency variable, removed)

---

### branch_name

**Value**: `ka-5-proximity`

---

## Variable Specification

### variable_id(s)

**Value**: `PROXIMITY`

**Single Variable**: YES

**Justification**: Only PROXIMITY variable is injected. DEFAULT_SELECTION from KA-1, VISUAL_HIGHLIGHT from KA-2, ORDERING from KA-3, and GROUPING from KA-4 are removed.

---

### injection_point

**Value**: `frontend`

**Description**: Injection occurs in frontend CSS spacing level only.

---

## Change Description

### change_summary

**Factual Description**:
- Removed DEFAULT_SELECTION injection from KA-1 experiment
- Removed VISUAL_HIGHLIGHT injection from KA-2 experiment
- Removed ORDERING injection from KA-3 experiment
- Removed GROUPING injection from KA-4 experiment
- Added PROXIMITY injection: Create spacing differences between adjacent capability items
- Spacing: First N capabilities use smaller vertical margin, subsequent capabilities use larger vertical margin
- No grouping containers
- No visual style changes
- No default selection
- No text labels or semantic hints
- No ordering changes
- All capabilities maintain identical visual appearance
- Only spacing/margin difference

**Files Modified**:
- `frontend_app/capabilities.html`

**Code Changes**:
- Removed DEFAULT_SELECTION injection code from KA-1
- Removed VISUAL_HIGHLIGHT injection code from KA-2
- Removed ORDERING injection code from KA-3
- Removed GROUPING injection code from KA-4
- Added PROXIMITY injection: Apply different vertical margins to capability items
- Applied spacing difference before displayCapabilities() rendering
- No other code changes

---

## Reproducibility

### reproduction_steps

1. Checkout experiment branch: `git checkout ka-5-proximity`
2. Start backend server: `python3 backend_server.py` (or equivalent)
3. Open frontend: Open `frontend_app/capabilities.html` in web browser
4. Observe: Capabilities display with spacing differences (tight spacing vs. loose spacing)
5. Verify: All capabilities have identical visual appearance
6. Verify: No default selection state
7. Verify: No visual highlighting
8. Verify: No ordering changes (capabilities in original registration order)
9. Verify: No grouping containers
10. Verify: Only spacing/margin differences

---

### rollback_steps

1. Checkout baseline branch: `git checkout baseline-v1.0` (or `release/baseline_v1.0/`)
2. Verify baseline state: Capabilities appear with uniform spacing (no spacing differences)
3. Verify: All capabilities have equal visual treatment
4. Verify: No PROXIMITY injection (baseline has uniform spacing)
5. Verify: No DEFAULT_SELECTION (baseline has no default)
6. Verify: No VISUAL_HIGHLIGHT (baseline has no visual emphasis)
7. Verify: No ORDERING injection (baseline uses registration order)
8. Verify: No GROUPING injection (baseline has no grouping)
9. Confirm: All experiment changes removed
10. Delete experiment branch (optional): `git branch -D ka-5-proximity`

---

## Expected Observations

### expected_drift_signals

**Observable Signals**:
- User may prioritize clicking items in tight spacing area
- User may interpret tight spacing as "related" or "grouped"
- User may form path convergence within tight spacing area
- User may not realize spacing difference is arbitrary vs. meaningful
- User attention may concentrate on tight spacing area
- User may use language like "these seem more related" to describe items in tight spacing

**Note**: List signals only. No recommendations. No mitigation strategies.

---

## Evidence and Audit

### evidence_pack_paths

**PASS**: `audit_evidence/ka_5_proximity_pass/`  
**FAIL**: `audit_evidence/ka_5_proximity_fail/`

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
- Removed KA-4 GROUPING injection code
- Added KA-5 PROXIMITY injection:
  - Apply different vertical margins to capability items
  - First N items use smaller margin (tight spacing)
  - Subsequent items use larger margin (loose spacing)
  - Spacing applied via CSS class or inline style
  - No grouping containers
  - No visual style differences
  - Maintain original registration order
  - Added comment: `// KA-5 EXPERIMENT: PROXIMITY injection`
- No other code changes
- No default selection
- No visual highlighting
- No ordering changes
- No grouping
- No text labels
- All capabilities maintain identical visual appearance

**Injection Point Annotation**:
- Code includes comment: `// KA-5 EXPERIMENT: PROXIMITY injection`
- Injection is explicitly marked and traceable

---

## No Recommendations

This specification provides no recommendations.

This specification provides no optimization suggestions.

This specification states only the experiment structure.

---

**END OF EXPERIMENT SPECIFICATION**

