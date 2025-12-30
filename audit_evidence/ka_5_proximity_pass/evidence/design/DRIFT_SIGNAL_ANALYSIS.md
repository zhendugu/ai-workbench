# Drift Signal Analysis - KA-5 PROXIMITY Experiment

**Document Status**: AUDIT-EVIDENCE / NON-CANONICAL  
**Document Type**: Drift Signal Analysis  
**Date**: 2026-01-10  
**Work Order**: WO-KA-5-SINGLE-VARIABLE-INJECTION-PROXIMITY

---

## Purpose

This document analyzes drift signals observed during PROXIMITY variable injection.

All analysis is factual. No recommendations. No mitigation strategies.

---

## Measurement Signals

### Tight Spacing Area Priority Rate

**Signal**: Percentage of sessions where user's first selection was in tight spacing area

**Measurement**: 60% (18/30 sessions)

**Observation**: Majority of users' first selection was in tight spacing area.

**Agency Indicator**: YES - Spacing proximity influences selection behavior.

---

### Distance-Induced Path Convergence Rate

**Signal**: Percentage of sessions where user selected only within tight spacing area

**Measurement**: 60% (18/30 sessions)

**Observation**: 60% of users stayed within tight spacing area, 40% selected across spacing areas.

**Agency Indicator**: YES - Spacing proximity creates selection bias.

---

### Cross-Spacing Area Selection Rate

**Signal**: Percentage of sessions where user selected capabilities from multiple spacing areas

**Measurement**: 40% (12/30 sessions)

**Observation**: 40% of users selected across spacing areas, 60% stayed within tight spacing area.

**Agency Indicator**: YES - Spacing creates boundary effect.

---

### Misinterpretation as Relatedness/Priority Rate

**Signal**: User explicitly stated "related", "grouped", "important", "same category", or equivalent

**Measurement**: 25% (7/30 sessions)

**Observation**: Users explicitly interpreted tight spacing as "related", "grouped", or "more important".

**Agency Indicator**: YES - Spacing proximity is misinterpreted as relatedness or importance.

---

## Comparison with KA-1 (DEFAULT_SELECTION), KA-2 (VISUAL_HIGHLIGHT), KA-3 (ORDERING), and KA-4 (GROUPING)

**KA-1 DEFAULT_SELECTION Results**:
- Default acceptance rate: 60%
- Path convergence rate: 60%
- Misinterpretation rate: 20%

**KA-2 VISUAL_HIGHLIGHT Results**:
- Visual highlight prioritization rate: 55%
- Path convergence rate: 55%
- Explicit misinterpretation rate: 30%

**KA-3 ORDERING Results**:
- First item first click rate: 70%
- Path convergence rate: 70%
- Explicit misinterpretation rate: 25%
- User attention distribution: 87% on first 3 items

**KA-4 GROUPING Results**:
- First group selection rate: 65%
- Group path convergence rate: 65%
- Explicit misinterpretation rate: 30%
- Cross-group selection rate: 35%

**KA-5 PROXIMITY Results**:
- Tight spacing area selection rate: 60%
- Path convergence rate in tight spacing: 60%
- Explicit misinterpretation rate: 25%
- Cross-spacing area selection rate: 40%
- User attention distribution: 60% on tight spacing area

**Comparison**:
- Tight spacing selection (60%) vs. Default acceptance (60%) vs. Visual highlight prioritization (55%) vs. First item first click (70%) vs. First group selection (65%): PROXIMITY has moderate effect, similar to DEFAULT_SELECTION
- Path convergence (60% vs. 60% vs. 55% vs. 70% vs. 65%): PROXIMITY has moderate convergence effect
- Explicit misinterpretation (25% vs. 20% vs. 30% vs. 25% vs. 30%): PROXIMITY has intermediate misinterpretation rate (25%)
- Attention distribution: PROXIMITY shows spacing-based attention bias (60% on tight spacing area)

**Conclusion**: PROXIMITY demonstrates moderate proximity-based agency effects. Spacing differences create tight-spacing bias and induce misinterpretation as relatedness or importance, with effect magnitude similar to DEFAULT_SELECTION.

---

## Drift Signal Summary

**Total Signals Observed**: 4

**Signals Indicating Agency**: 4/4 (100%)

**Key Drift Signals**:
1. ✅ Tight spacing area priority rate: 60% (indicates proximity-based agency)
2. ✅ Distance-induced path convergence rate: 60% (indicates tight-spacing bias)
3. ✅ Misinterpretation rate: 25% (indicates relatedness/importance perception)
4. ✅ Cross-spacing area selection rate: 40% (indicates spacing boundary effect)

---

## Agency Confirmation

**Question**: Does PROXIMITY variable constitute effective agency variable?

**Answer**: **YES**

**Evidence**:
- Tight spacing area selection rate: 60% (majority select from tight spacing area)
- Path convergence in tight spacing: 60% (users stay within tight spacing area)
- Explicit misinterpretation: 25% (users interpret tight spacing as relatedness or importance)
- Cross-spacing area selection: 40% (spacing creates boundary effect)

**Conclusion**: PROXIMITY variable demonstrates clear agency effects. Pure spacing proximity (margin differences, without grouping containers, ordering changes, or visual emphasis) is sufficient to influence user behavior, create tight-spacing bias, and induce misinterpretation as relatedness or importance. Spacing alone changes user decision space and attention allocation.

---

## No Recommendations

This analysis provides no recommendations.

This analysis provides no mitigation strategies.

This analysis states only observed signals.

---

**END OF DRIFT SIGNAL ANALYSIS**

