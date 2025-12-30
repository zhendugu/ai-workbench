# Experiment Specification - KA-2-VISUAL_HIGHLIGHT

**Document Status**: NON-CANONICAL  
**Document Type**: Experiment Specification  
**Date**: 2026-01-10  
**Work Order**: WO-KA-2-SINGLE-VARIABLE-INJECTION-VISUAL-HIGHLIGHT

---

## Experiment Metadata

### experiment_id

**Value**: `KA-2-VISUAL_HIGHLIGHT`

---

### baseline_ref

**Value**: `release/baseline_v1.0/`

**Description**: J10 Baseline v1.0 (FROZEN)

**Previous Experiment**: KA-1-DEFAULT_SELECTION (confirmed as effective agency variable)

---

### branch_name

**Value**: `ka-2-visual-highlight`

---

## Variable Specification

### variable_id(s)

**Value**: `VISUAL_HIGHLIGHT`

**Single Variable**: YES

**Justification**: Only VISUAL_HIGHLIGHT variable is injected. DEFAULT_SELECTION from KA-1 is removed.

---

### injection_point

**Value**: `frontend`

**Description**: Injection occurs in frontend UI presentation layer only.

---

## Change Description

### change_summary

**Factual Description**:
- Removed DEFAULT_SELECTION injection from KA-1 experiment
- Added visual highlight to first capability in capabilities.html
- Visual highlight: 2px border (vs. 1px for other capabilities) - minimal visual difference
- No color change, no background change, no text weight change
- No default selection state
- No text labels or semantic hints
- No sorting changes
- No other UI behavior changes

**Files Modified**:
- `frontend_app/capabilities.html`

**Code Changes**:
- Removed DEFAULT_SELECTION injection code from KA-1
- Added CSS class for visual highlight (minimal border difference)
- Applied highlight class to first capability button
- No other code changes

---

## Reproducibility

### reproduction_steps

1. Checkout experiment branch: `git checkout ka-2-visual-highlight`
2. Start backend server: `python3 backend_server.py` (or equivalent)
3. Open frontend: Open `frontend_app/capabilities.html` in web browser
4. Observe: First capability has 2px border (other capabilities have 1px border)
5. Verify: No default selection state
6. Verify: No text labels indicating recommendation
7. Verify: No sorting changes
8. Verify: All capabilities in registration order

---

### rollback_steps

1. Checkout baseline branch: `git checkout baseline-v1.0` (or `release/baseline_v1.0/`)
2. Verify baseline state: No visual highlight on capabilities.html
3. Verify: All capabilities have equal visual treatment
4. Verify: No DEFAULT_SELECTION (baseline has no default)
5. Confirm: All experiment changes removed
6. Delete experiment branch (optional): `git branch -D ka-2-visual-highlight`

---

## Expected Observations

### expected_drift_signals

**Observable Signals**:
- First capability appears visually different (2px border vs. 1px)
- User may prioritize clicking highlighted capability
- User may interpret visual difference as "system recommendation"
- User may assume highlighted option is "more important" or "preferred"
- User may form path convergence to highlighted capability
- User may not realize visual difference is arbitrary vs. meaningful

**Note**: List signals only. No recommendations. No mitigation strategies.

---

## Evidence and Audit

### evidence_pack_paths

**PASS**: `audit_evidence/ka_2_visual_highlight_pass/`  
**FAIL**: `audit_evidence/ka_2_visual_highlight_fail/`

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
  - Removed `selectFirstCapability()` function
  - Removed `.selected` CSS class
  - Removed selection state logic
- Added VISUAL_HIGHLIGHT injection:
  - Added `.visual-highlight` CSS class with 2px border (vs. 1px default)
  - Applied class to first capability button in displayCapabilities()
  - Added comment: `// KA-2 EXPERIMENT: VISUAL_HIGHLIGHT injection`
- No other code changes
- No default selection
- No text labels
- No sorting changes

**Injection Point Annotation**:
- Code includes comment: `// KA-2 EXPERIMENT: VISUAL_HIGHLIGHT injection`
- Injection is explicitly marked and traceable

---

## No Recommendations

This specification provides no recommendations.

This specification provides no optimization suggestions.

This specification states only the experiment structure.

---

**END OF EXPERIMENT SPECIFICATION**

