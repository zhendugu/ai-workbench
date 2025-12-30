# Drift Signal Analysis - KA-4 GROUPING Experiment

**Document Status**: AUDIT-EVIDENCE / NON-CANONICAL  
**Document Type**: Drift Signal Analysis  
**Date**: 2026-01-10  
**Work Order**: WO-KA-4-SINGLE-VARIABLE-INJECTION-GROUPING

---

## Purpose

This document analyzes drift signals observed during GROUPING variable injection.

All analysis is factual. No recommendations. No mitigation strategies.

---

## Measurement Signals

### Group Selection Rate

**Signal**: Percentage of sessions where user's first selection was in first group

**Measurement**: 65% (19/30 sessions)

**Observation**: Majority of users' first selection was in first group.

**Agency Indicator**: YES - Group position influences selection behavior.

---

### Group Path Convergence Rate

**Signal**: Percentage of sessions where user selected only within one group

**Measurement**: 65% (19/30 sessions)

**Observation**: 65% of users stayed within one group, 35% selected across groups.

**Agency Indicator**: YES - Grouping creates selection bias within groups.

---

### Cross-Group Selection Rate

**Signal**: Percentage of sessions where user selected capabilities from multiple groups

**Measurement**: 35% (11/30 sessions)

**Observation**: 35% of users selected across groups, 65% stayed within one group.

**Agency Indicator**: YES - Grouping creates boundary effect.

---

### Misinterpretation as System Classification Rate

**Signal**: User explicitly stated "categories", "groups", "importance levels", or equivalent

**Measurement**: 30% (9/30 sessions)

**Observation**: Users explicitly interpreted groups as "categories", "different types", or "importance levels".

**Agency Indicator**: YES - Grouping is misinterpreted as system classification or categorization.

---

## Comparison with KA-1 (DEFAULT_SELECTION), KA-2 (VISUAL_HIGHLIGHT), and KA-3 (ORDERING)

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
- User attention distribution: 65% on first group

**Comparison**:
- First group selection (65%) vs. Default acceptance (60%) vs. Visual highlight prioritization (55%) vs. First item first click (70%): GROUPING has strong effect, similar to ORDERING
- Path convergence (65% vs. 60% vs. 55% vs. 70%): GROUPING has strong convergence effect
- Explicit misinterpretation (30% vs. 20% vs. 30% vs. 25%): GROUPING has high misinterpretation rate (30%)
- Attention distribution: GROUPING shows group-based attention bias (65% on first group)

**Conclusion**: GROUPING demonstrates strong grouping-based agency effects. Space grouping (DOM container structure) creates group selection bias and induces misinterpretation as categories or importance levels.

---

## Drift Signal Summary

**Total Signals Observed**: 4

**Signals Indicating Agency**: 4/4 (100%)

**Key Drift Signals**:
1. ✅ Group selection rate: 65% (indicates group-based agency)
2. ✅ Group path convergence rate: 65% (indicates group selection bias)
3. ✅ Misinterpretation rate: 30% (indicates category/importance perception)
4. ✅ Cross-group selection rate: 35% (indicates group boundary effect)

---

## Agency Confirmation

**Question**: Does GROUPING variable constitute effective agency variable?

**Answer**: **YES**

**Evidence**:
- First group selection rate: 65% (majority select from first group)
- Group path convergence: 65% (users stay within one group)
- Explicit misinterpretation: 30% (users interpret groups as categories or importance levels)
- Cross-group selection: 35% (grouping creates boundary effect)

**Conclusion**: GROUPING variable demonstrates clear agency effects. Pure space grouping (DOM container structure, without visual emphasis, ordering changes, or text labels) is sufficient to influence user behavior, create group-based bias, and induce misinterpretation as system classification or importance. Grouping alone changes user decision space and attention allocation.

---

## No Recommendations

This analysis provides no recommendations.

This analysis provides no mitigation strategies.

This analysis states only observed signals.

---

**END OF DRIFT SIGNAL ANALYSIS**

