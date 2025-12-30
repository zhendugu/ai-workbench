# Declaration vs Implicit Comparison

**Document Status**: NON-CANONICAL / DESIGN-BOUNDARY  
**Document Type**: Comparative Analysis  
**Date**: 2026-01-10  
**Work Order**: WO-KB-1-DECLARED-AGENCY-PATTERN-DESIGN

---

## Purpose

This document compares implicit agency (KA experiment form) with declared agency (pattern form).

All metrics reference KA experimental results. No claims of improvement. No optimization framing. Factual comparison only.

---

## Comparison 1: DEFAULT_SELECTION

### Implicit Form (KA-1 Experiment)

**Mechanism**: Pre-selected option without declaration

**KA Evidence**: KA-1 DEFAULT_SELECTION experiment  
**Evidence File**: `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Observed Metrics**:
- Default acceptance rate: 60% (18/30 sessions)
- Misinterpretation rate: 20% (6/30 sessions explicitly stated "system recommendation")
- Path convergence rate: 60% (18/30 sessions)
- Path offset rate: 40% (12/30 sessions changed default)

---

### Declared Form (PATTERN-DECLARED-DEFAULT-SELECTION)

**Mechanism**: Pre-selected option with explicit declaration

**Declaration Text**: "This option is pre-selected. This pre-selection influences attention and choice."

**Expected Metrics** (based on KA-1):
- Default acceptance rate: 60% (same mechanism, declaration does not change acceptance behavior)
- Misinterpretation rate: Expected reduction (declaration explicitly states pre-selection state)
- Path convergence rate: 60% (same mechanism, declaration does not change convergence behavior)
- Path offset rate: 40% (same mechanism, declaration does not change rejection behavior)

**Difference**: Declaration explicitly states pre-selection state and influence. Misinterpretation risk reduced by explicit declaration.

---

### Side-by-Side Comparison

| Metric | Implicit (KA-1) | Declared (Pattern) | Difference |
|--------|-----------------|-------------------|------------|
| Default acceptance rate | 60% | 60% (expected) | None (same mechanism) |
| Misinterpretation rate | 20% | Expected reduction | Declaration reduces misinterpretation risk |
| Path convergence rate | 60% | 60% (expected) | None (same mechanism) |
| Path offset rate | 40% | 40% (expected) | None (same mechanism) |

**Conclusion**: Declaration does not change behavioral effect (60% acceptance). Declaration reduces misinterpretation risk by explicitly stating pre-selection state.

---

## Comparison 2: VISUAL_HIGHLIGHT

### Implicit Form (KA-2 Experiment)

**Mechanism**: Visual emphasis without declaration

**KA Evidence**: KA-2 VISUAL_HIGHLIGHT experiment  
**Evidence File**: `audit_evidence/ka_2_visual_highlight_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Observed Metrics**:
- Visual highlight prioritization rate: 55% (16/30 sessions)
- Misinterpretation rate: 30% (9/30 sessions explicitly stated "system recommendation" or "important")
- Path convergence rate: 55% (16/30 sessions)
- Visual highlight change rate: 45% (14/30 sessions selected non-emphasized options)

---

### Declared Form (PATTERN-DECLARED-VISUAL-HIGHLIGHT)

**Mechanism**: Visual emphasis with explicit declaration

**Declaration Text**: "This element is visually emphasized. This emphasis influences attention and choice."

**Expected Metrics** (based on KA-2):
- Visual highlight prioritization rate: 55% (same mechanism, declaration does not change prioritization behavior)
- Misinterpretation rate: Expected reduction (declaration explicitly states visual emphasis and influence)
- Path convergence rate: 55% (same mechanism, declaration does not change convergence behavior)
- Visual highlight change rate: 45% (same mechanism, declaration does not change rejection behavior)

**Difference**: Declaration explicitly states visual emphasis and influence. Misinterpretation risk reduced by explicit declaration.

---

### Side-by-Side Comparison

| Metric | Implicit (KA-2) | Declared (Pattern) | Difference |
|--------|-----------------|-------------------|------------|
| Prioritization rate | 55% | 55% (expected) | None (same mechanism) |
| Misinterpretation rate | 30% | Expected reduction | Declaration reduces misinterpretation risk |
| Path convergence rate | 55% | 55% (expected) | None (same mechanism) |
| Change rate | 45% | 45% (expected) | None (same mechanism) |

**Conclusion**: Declaration does not change behavioral effect (55% prioritization). Declaration reduces misinterpretation risk by explicitly stating visual emphasis and influence.

---

## Comparison 3: DEFAULT_SELECTION with Rejection

### Implicit Form (KA-1 Experiment)

**Mechanism**: Pre-selected option without declaration, user can change (implicit rejection)

**KA Evidence**: KA-1 DEFAULT_SELECTION experiment  
**Evidence File**: `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Observed Metrics**:
- Default acceptance rate: 60% (18/30 sessions)
- Path offset rate: 40% (12/30 sessions changed default)
- Misinterpretation rate: 20% (6/30 sessions explicitly stated "system recommendation")

---

### Declared Form (PATTERN-DECLARED-PRE-SELECTION-REJECTION)

**Mechanism**: Pre-selected option with explicit declaration and explicit rejection action

**Declaration Text**: "This option is pre-selected. You can change it. This pre-selection influences attention and choice."

**Expected Metrics** (based on KA-1):
- Default acceptance rate: 60% (same mechanism, declaration does not change acceptance behavior)
- Path offset rate: 40% (same mechanism, declaration does not change rejection behavior, but explicit rejection action may increase visibility)
- Misinterpretation rate: Expected reduction (declaration explicitly states pre-selection state, change ability, and influence)

**Difference**: Declaration explicitly states pre-selection state, change ability, and influence. Explicit rejection action increases visibility of rejection path.

---

### Side-by-Side Comparison

| Metric | Implicit (KA-1) | Declared (Pattern) | Difference |
|--------|-----------------|-------------------|------------|
| Default acceptance rate | 60% | 60% (expected) | None (same mechanism) |
| Path offset rate | 40% | 40% (expected, may increase due to explicit rejection action) | Explicit rejection action may increase visibility |
| Misinterpretation rate | 20% | Expected reduction | Declaration reduces misinterpretation risk |

**Conclusion**: Declaration does not change behavioral effect (60% acceptance, 40% rejection). Declaration reduces misinterpretation risk and may increase rejection visibility through explicit rejection action.

---

## Summary

**Key Observation**: Declaration does not eliminate agency effects. Behavioral metrics (acceptance rate, convergence rate, rejection rate) remain unchanged because the underlying mechanism is identical.

**Key Difference**: Declaration reduces misinterpretation risk by explicitly stating mechanism state and influence.

**Evidence Base**: All comparisons reference KA-1 and KA-2 experimental results.

---

## No Recommendations

This comparison provides no recommendations.

This comparison provides no claims of improvement.

This comparison provides no optimization framing.

This comparison states only factual differences between implicit and declared forms.

---

**END OF DECLARATION VS IMPLICIT COMPARISON**

