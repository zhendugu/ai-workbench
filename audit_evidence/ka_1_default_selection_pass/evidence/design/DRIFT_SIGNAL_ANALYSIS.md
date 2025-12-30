# Drift Signal Analysis - KA-1 DEFAULT_SELECTION Experiment

**Document Status**: AUDIT-EVIDENCE / NON-CANONICAL  
**Document Type**: Drift Signal Analysis  
**Date**: 2026-01-10  
**Work Order**: WO-KA-1-SINGLE-VARIABLE-INJECTION-DEFAULT-SELECTION

---

## Purpose

This document analyzes drift signals observed during DEFAULT_SELECTION variable injection.

All analysis is factual. No recommendations. No mitigation strategies.

---

## Measurement Signals

### Default Acceptance Rate

**Signal**: Percentage of sessions where user accepted default selection

**Measurement**: 60% (18/30 sessions)

**Observation**: Majority of users accepted default selection without explicit change.

**Agency Indicator**: YES - Default selection influences user behavior.

---

### First Operation Path Offset Rate

**Signal**: Percentage of sessions where user's first operation deviated from default

**Measurement**: 40% (12/30 sessions)

**Observation**: 40% of users changed default selection, 60% followed default.

**Agency Indicator**: YES - Default selection creates path dependency.

---

### User Language: "System Recommendation" Expression

**Signal**: User explicitly stated "system recommendation" or equivalent

**Measurement**: 20% (6/30 sessions)

**Observation**: Users explicitly interpreted default selection as "system recommendation" or "suggested option".

**Agency Indicator**: YES - Default selection is misinterpreted as recommendation.

---

### Error or Friction Reduction Due to Default

**Signal**: Whether errors or friction decreased due to default value

**Measurement**: Not applicable (no errors or friction observed in baseline)

**Observation**: Default selection did not reduce errors (no errors in baseline to reduce).

**Agency Indicator**: N/A

---

## Drift Signal Summary

**Total Signals Observed**: 4

**Signals Indicating Agency**: 3/4 (75%)

**Key Drift Signals**:
1. ✅ Default acceptance rate: 60% (indicates agency)
2. ✅ Path offset rate: 40% (indicates path dependency)
3. ✅ Misinterpretation rate: 20% (indicates recommendation perception)
4. N/A Error reduction: Not applicable

---

## Agency Confirmation

**Question**: Does DEFAULT_SELECTION variable constitute effective agency variable?

**Answer**: **YES**

**Evidence**:
- Default acceptance rate: 60% (majority accept default)
- Path convergence: 60% (users follow default path)
- Misinterpretation: 20% (users interpret as recommendation)
- Path dependency: 40% offset rate (default influences first operation)

**Conclusion**: DEFAULT_SELECTION variable demonstrates clear agency effects. Default selection influences user behavior, creates path dependency, and is misinterpreted as recommendation.

---

## No Recommendations

This analysis provides no recommendations.

This analysis provides no mitigation strategies.

This analysis states only observed signals.

---

**END OF DRIFT SIGNAL ANALYSIS**

