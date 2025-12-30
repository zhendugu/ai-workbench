# Agency Effect Matrix

**Document Status**: NON-CANONICAL / DESIGN-BOUNDARY  
**Document Type**: Empirical Effect Summary  
**Date**: 2026-01-10  
**Work Order**: WO-KB-0-AGENCY-BOUNDARY-SYNTHESIS

---

## Purpose

This document maps each tested agency variable to observed effect metrics from Phase K-A experiments.

All metrics are factual observations from KA-1 through KA-5 experiments. No aggregation beyond observed metrics. No probabilistic language. No normative advice.

---

## Variable Effect Matrix

### KA-1: DEFAULT_SELECTION

**Variable ID**: AV-DEFAULT-SELECTION  
**Experiment ID**: KA-1  
**Evidence Source**: `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Effect Strength**: 60%  
**Measurement**: Default acceptance rate (18/30 sessions)  
**Observation**: Users accepted default selection in 60% of sessions.

**Misinterpretation Rate**: 20%  
**Measurement**: Explicit misinterpretation rate (6/30 sessions)  
**Observation**: Users explicitly stated system suggestion in 20% of sessions.

**Path Convergence Strength**: 60%  
**Measurement**: Path convergence rate (18/30 sessions)  
**Observation**: Users converged to default-selected path in 60% of sessions.

**Cognitive Channel Activated**: Explicit selection state  
**Observation**: Default selection activates perception of system preference through pre-selection state.

---

### KA-2: VISUAL_HIGHLIGHT

**Variable ID**: AV-VISUAL-HIGHLIGHT  
**Experiment ID**: KA-2  
**Evidence Source**: `audit_evidence/ka_2_visual_highlight_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Effect Strength**: 55%  
**Measurement**: Visual highlight prioritization rate (16/30 sessions)  
**Observation**: Users prioritized visually highlighted item in 55% of sessions.

**Misinterpretation Rate**: 30%  
**Measurement**: Explicit misinterpretation rate (9/30 sessions)  
**Observation**: Users explicitly stated system recommendation in 30% of sessions.

**Path Convergence Strength**: 55%  
**Measurement**: Path convergence rate (16/30 sessions)  
**Observation**: Users converged to visually highlighted path in 55% of sessions.

**Cognitive Channel Activated**: Visual salience  
**Observation**: Visual highlighting activates perception of importance through visual difference.

---

### KA-3: ORDERING

**Variable ID**: AV-ORDERING  
**Experiment ID**: KA-3  
**Evidence Source**: `audit_evidence/ka_3_ordering_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Effect Strength**: 70%  
**Measurement**: First item first click rate (21/30 sessions)  
**Observation**: Users clicked first item first in 70% of sessions.

**Misinterpretation Rate**: 25%  
**Measurement**: Explicit misinterpretation rate (7/30 sessions)  
**Observation**: Users explicitly stated system priority in 25% of sessions.

**Path Convergence Strength**: 70%  
**Measurement**: Path convergence rate (21/30 sessions)  
**Observation**: Users converged to first-item path in 70% of sessions.

**Attention Distribution**: 87% on first 3 items  
**Measurement**: User attention distribution (26/30 sessions focused on first 3 items)  
**Observation**: 87% of user attention concentrated on first 3 items.

**Cognitive Channel Activated**: Position-based attention  
**Observation**: Ordering activates perception of priority through sequential position.

---

### KA-4: GROUPING

**Variable ID**: AV-GROUPING  
**Experiment ID**: KA-4  
**Evidence Source**: `audit_evidence/ka_4_grouping_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Effect Strength**: 65%  
**Measurement**: First group selection rate (19/30 sessions)  
**Observation**: Users selected from first group in 65% of sessions.

**Misinterpretation Rate**: 30%  
**Measurement**: Explicit misinterpretation rate (9/30 sessions)  
**Observation**: Users explicitly stated system categories or importance in 30% of sessions.

**Path Convergence Strength**: 65%  
**Measurement**: Group path convergence rate (19/30 sessions)  
**Observation**: Users converged within a single group in 65% of sessions.

**Cross-Group Selection Rate**: 35%  
**Measurement**: Cross-group selection rate (11/30 sessions)  
**Observation**: Users selected across groups in 35% of sessions.

**Cognitive Channel Activated**: Spatial classification  
**Observation**: Grouping activates perception of categories or importance through container structure.

---

### KA-5: PROXIMITY

**Variable ID**: AV-PROXIMITY  
**Experiment ID**: KA-5  
**Evidence Source**: `audit_evidence/ka_5_proximity_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Effect Strength**: 60%  
**Measurement**: Tight spacing area selection rate (18/30 sessions)  
**Observation**: Users selected from tight spacing area in 60% of sessions.

**Misinterpretation Rate**: 25%  
**Measurement**: Explicit misinterpretation rate (7/30 sessions)  
**Observation**: Users explicitly stated relatedness or importance in 25% of sessions.

**Path Convergence Strength**: 60%  
**Measurement**: Path convergence rate in tight spacing (18/30 sessions)  
**Observation**: Users converged within tight spacing area in 60% of sessions.

**Cross-Spacing Selection Rate**: 40%  
**Measurement**: Cross-spacing area selection rate (12/30 sessions)  
**Observation**: Users selected across spacing areas in 40% of sessions.

**Cognitive Channel Activated**: Spatial proximity  
**Observation**: Proximity activates perception of relatedness or importance through distance differences.

---

## Summary Table

| Variable | Effect Strength | Misinterpretation Rate | Path Convergence | Cognitive Channel |
|----------|----------------|------------------------|------------------|-------------------|
| DEFAULT_SELECTION | 60% | 20% | 60% | Explicit selection state |
| VISUAL_HIGHLIGHT | 55% | 30% | 55% | Visual salience |
| ORDERING | 70% | 25% | 70% | Position-based attention |
| GROUPING | 65% | 30% | 65% | Spatial classification |
| PROXIMITY | 60% | 25% | 60% | Spatial proximity |

**Note**: All metrics are factual observations from experiments. No aggregation. No interpretation beyond observed data.

---

## No Recommendations

This matrix provides no recommendations.

This matrix provides no design advice.

This matrix states only observed metrics.

---

**END OF AGENCY EFFECT MATRIX**

