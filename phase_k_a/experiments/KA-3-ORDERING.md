# Experiment Specification - KA-3-ORDERING

**Document Status**: NON-CANONICAL  
**Document Type**: Experiment Specification  
**Date**: 2026-01-10  
**Work Order**: WO-KA-3-SINGLE-VARIABLE-INJECTION-ORDERING

---

## Experiment Metadata

### experiment_id

**Value**: `KA-3-ORDERING`

---

### baseline_ref

**Value**: `release/baseline_v1.0/`

**Description**: J10 Baseline v1.0 (FROZEN)

**Previous Experiments**: 
- KA-1-DEFAULT_SELECTION (confirmed as effective agency variable, removed)
- KA-2-VISUAL_HIGHLIGHT (confirmed as effective agency variable, removed)

---

### branch_name

**Value**: `ka-3-ordering`

---

## Variable Specification

### variable_id(s)

**Value**: `ORDERING`

**Single Variable**: YES

**Justification**: Only ORDERING variable is injected. DEFAULT_SELECTION from KA-1 and VISUAL_HIGHLIGHT from KA-2 are removed.

---

### injection_point

**Value**: `frontend`

**Description**: Injection occurs in frontend data-to-DOM mapping order only.

---

## Change Description

### change_summary

**Factual Description**:
- Removed DEFAULT_SELECTION injection from KA-1 experiment
- Removed VISUAL_HIGHLIGHT injection from KA-2 experiment
- Added ORDERING injection: Fixed one specific capability to always appear first in list
- Order change: Manually reorder capabilities array before display
- No visual style changes
- No default selection
- No text labels or semantic hints
- No sorting logic changes
- All capabilities maintain identical visual appearance
- DOM order matches visual order

**Files Modified**:
- `frontend_app/capabilities.html`

**Code Changes**:
- Removed DEFAULT_SELECTION injection code from KA-1
- Removed VISUAL_HIGHLIGHT injection code from KA-2
- Added ORDERING injection: Reorder capabilities array to put specific capability first
- Applied reordering before displayCapabilities() call
- No other code changes

---

## Reproducibility

### reproduction_steps

1. Checkout experiment branch: `git checkout ka-3-ordering`
2. Start backend server: `python3 backend_server.py` (or equivalent)
3. Open frontend: Open `frontend_app/capabilities.html` in web browser
4. Observe: Specific capability appears first in list (different from registration order)
5. Verify: All capabilities have identical visual appearance
6. Verify: No default selection state
7. Verify: No visual highlighting
8. Verify: No text labels indicating recommendation
9. Verify: Order is fixed (not dependent on user/time/state)

---

### rollback_steps

1. Checkout baseline branch: `git checkout baseline-v1.0` (or `release/baseline_v1.0/`)
2. Verify baseline state: Capabilities appear in registration order
3. Verify: All capabilities have equal visual treatment
4. Verify: No ORDERING injection (baseline uses registration order)
5. Verify: No DEFAULT_SELECTION (baseline has no default)
6. Verify: No VISUAL_HIGHLIGHT (baseline has no visual emphasis)
7. Confirm: All experiment changes removed
8. Delete experiment branch (optional): `git branch -D ka-3-ordering`

---

## Expected Observations

### expected_drift_signals

**Observable Signals**:
- First capability in list receives first click more frequently
- User may prioritize clicking first item in list
- User may interpret first position as "more important" or "system priority"
- User may form path convergence to first item
- User may not realize order is arbitrary vs. meaningful
- User attention may concentrate on first items

**Note**: List signals only. No recommendations. No mitigation strategies.

---

## Evidence and Audit

### evidence_pack_paths

**PASS**: `audit_evidence/ka_3_ordering_pass/`  
**FAIL**: `audit_evidence/ka_3_ordering_fail/`

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
- Removed KA-1 DEFAULT_SELECTION injection code:
  - Removed `.selected` CSS class
  - Removed `selectFirstCapability()` function
  - Removed selection state logic
- Removed KA-2 VISUAL_HIGHLIGHT injection code:
  - Removed `.visual-highlight` CSS class
  - Removed visual highlight application logic
- Added KA-3 ORDERING injection:
  - Added function to reorder capabilities array
  - Fixed specific capability ID to always appear first
  - Applied reordering before displayCapabilities() call
  - Added comment: `// KA-3 EXPERIMENT: ORDERING injection`
- No other code changes
- No default selection
- No visual highlighting
- No text labels
- No sorting logic changes
- All capabilities maintain identical visual appearance

**Injection Point Annotation**:
- Code includes comment: `// KA-3 EXPERIMENT: ORDERING injection`
- Injection is explicitly marked and traceable

---

## No Recommendations

This specification provides no recommendations.

This specification provides no optimization suggestions.

This specification states only the experiment structure.

---

**END OF EXPERIMENT SPECIFICATION**

