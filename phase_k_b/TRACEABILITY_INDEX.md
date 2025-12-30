# Traceability Index

**Document Status**: NON-CANONICAL / DESIGN-BOUNDARY  
**Document Type**: Traceability Mapping  
**Date**: 2026-01-10  
**Work Order**: WO-KB-0-AGENCY-BOUNDARY-SYNTHESIS

---

## Purpose

This document maps each conclusion in Phase K-B synthesis documents back to Phase K-A experimental evidence.

Each mapping includes experiment ID, evidence file, and observed metric. No interpretation beyond traceability.

---

## Traceability Mappings

### Mapping 1: Sequential Position Creates Agency

**Conclusion**: Sequential position creates position-based agency (70% effect)

**Experiment ID**: KA-3  
**Evidence File**: `audit_evidence/ka_3_ordering_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`  
**Observed Metric**: First item first-click rate: 70% (21/30 sessions)

**Document References**:
- `AGENCY_EFFECT_MATRIX.md`: ORDERING variable, 70% effect strength
- `AGENCY_BOUNDARY_CLASSIFICATION.md`: Class 1 (Unavoidable Agency), Sequential Position mechanism
- `UI_NEUTRALITY_INVALIDATION.md`: Claim 1
- `DESIGN_CONSTRAINT_EXTRACTION.md`: Constraint 1

---

### Mapping 2: Spatial Proximity Creates Agency

**Conclusion**: Spatial proximity creates proximity-based agency (60% effect)

**Experiment ID**: KA-5  
**Evidence File**: `audit_evidence/ka_5_proximity_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`  
**Observed Metric**: Tight spacing area selection rate: 60% (18/30 sessions)

**Document References**:
- `AGENCY_EFFECT_MATRIX.md`: PROXIMITY variable, 60% effect strength
- `AGENCY_BOUNDARY_CLASSIFICATION.md`: Class 1 (Unavoidable Agency), Spatial Proximity mechanism
- `UI_NEUTRALITY_INVALIDATION.md`: Claim 2
- `DESIGN_CONSTRAINT_EXTRACTION.md`: Constraint 2

---

### Mapping 3: Container Grouping Creates Agency

**Conclusion**: Container grouping creates classification-based agency (65% effect)

**Experiment ID**: KA-4  
**Evidence File**: `audit_evidence/ka_4_grouping_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`  
**Observed Metric**: First group selection rate: 65% (19/30 sessions), misinterpretation rate: 30% (9/30 sessions)

**Document References**:
- `AGENCY_EFFECT_MATRIX.md`: GROUPING variable, 65% effect strength
- `AGENCY_BOUNDARY_CLASSIFICATION.md`: Class 1 (Unavoidable Agency), Container Structure mechanism
- `UI_NEUTRALITY_INVALIDATION.md`: Claim 3
- `DESIGN_CONSTRAINT_EXTRACTION.md`: Constraint 3

---

### Mapping 4: Default Selection Creates Agency

**Conclusion**: Default selection creates explicit selection state agency (60% effect)

**Experiment ID**: KA-1  
**Evidence File**: `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`  
**Observed Metric**: Default acceptance rate: 60% (18/30 sessions), misinterpretation rate: 20% (6/30 sessions)

**Document References**:
- `AGENCY_EFFECT_MATRIX.md`: DEFAULT_SELECTION variable, 60% effect strength
- `AGENCY_BOUNDARY_CLASSIFICATION.md`: Class 2 (Declared Agency), Default Selection mechanism
- `DESIGN_CONSTRAINT_EXTRACTION.md`: Constraint 4

---

### Mapping 5: Visual Highlighting Creates Agency

**Conclusion**: Visual highlighting creates salience-based agency (55% effect)

**Experiment ID**: KA-2  
**Evidence File**: `audit_evidence/ka_2_visual_highlight_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`  
**Observed Metric**: Visual highlight prioritization rate: 55% (16/30 sessions), misinterpretation rate: 30% (9/30 sessions)

**Document References**:
- `AGENCY_EFFECT_MATRIX.md`: VISUAL_HIGHLIGHT variable, 55% effect strength
- `AGENCY_BOUNDARY_CLASSIFICATION.md`: Class 2 (Declared Agency), Visual Highlighting mechanism
- `DESIGN_CONSTRAINT_EXTRACTION.md`: Constraint 5

---

### Mapping 6: All Structural Variables Produce Agency

**Conclusion**: All tested structural variables produce measurable agency effects

**Experiment IDs**: KA-1, KA-2, KA-3, KA-4, KA-5  
**Evidence Files**: 
- `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`
- `audit_evidence/ka_2_visual_highlight_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`
- `audit_evidence/ka_3_ordering_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`
- `audit_evidence/ka_4_grouping_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`
- `audit_evidence/ka_5_proximity_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Observed Metric**: All variables produce effect strength > 0% (minimum 55%, maximum 70%)

**Document References**:
- `AGENCY_EFFECT_MATRIX.md`: Summary table
- `UI_NEUTRALITY_INVALIDATION.md`: Claim 4
- `DESIGN_CONSTRAINT_EXTRACTION.md`: Constraint 6, Constraint 9

---

### Mapping 7: UI Structure Is Inseparable from Agency

**Conclusion**: UI structure inherently creates agency. Structure and agency are inseparable.

**Experiment IDs**: KA-3, KA-4, KA-5  
**Evidence Files**: 
- `audit_evidence/ka_3_ordering_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`
- `audit_evidence/ka_4_grouping_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`
- `audit_evidence/ka_5_proximity_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Observed Metric**: All structural variables (ORDERING, GROUPING, PROXIMITY) produce measurable agency effects

**Document References**:
- `UI_NEUTRALITY_INVALIDATION.md`: Claim 5, Formal Conclusion
- `DESIGN_CONSTRAINT_EXTRACTION.md`: Constraint 6, Constraint 7, Constraint 10

---

### Mapping 8: "Neutral UI" Is False

**Conclusion**: "Neutral UI" is a false concept. Neutral UI does not exist.

**Experiment IDs**: KA-3, KA-4, KA-5  
**Evidence Files**: 
- `audit_evidence/ka_3_ordering_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`
- `audit_evidence/ka_4_grouping_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`
- `audit_evidence/ka_5_proximity_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Observed Metric**: All structural variables produce measurable agency effects, proving structure creates agency

**Document References**:
- `UI_NEUTRALITY_INVALIDATION.md`: Entire document
- `DESIGN_CONSTRAINT_EXTRACTION.md`: Constraint 7

---

### Mapping 9: Agency Budget Is Finite

**Conclusion**: Agency budget is a finite constraint consumed by structural variables.

**Experiment IDs**: KA-1, KA-2, KA-3, KA-4, KA-5  
**Evidence Files**: All KA experiment drift signal analyses

**Observed Metric**: Agency effects are measurable and accumulate across variables

**Document References**:
- `AGENCY_BUDGET_CONCEPT.md`: Entire document
- `DESIGN_CONSTRAINT_EXTRACTION.md`: Constraint 8

---

### Mapping 10: Structural Variables Are Agency Variables

**Conclusion**: Structural variables (ORDERING, PROXIMITY, GROUPING) are agency variables.

**Experiment IDs**: KA-3, KA-4, KA-5  
**Evidence Files**: 
- `audit_evidence/ka_3_ordering_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`
- `audit_evidence/ka_4_grouping_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`
- `audit_evidence/ka_5_proximity_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Observed Metric**: All structural variables produce measurable agency effects (ORDERING: 70%, GROUPING: 65%, PROXIMITY: 60%)

**Document References**:
- `AGENCY_EFFECT_MATRIX.md`: ORDERING, GROUPING, PROXIMITY variables
- `DESIGN_CONSTRAINT_EXTRACTION.md`: Constraint 10

---

## Traceability Summary

**Total Mappings**: 10

**Experiment Coverage**: KA-1, KA-2, KA-3, KA-4, KA-5 (all Phase K-A experiments)

**Evidence File Coverage**: All KA experiment drift signal analysis files

**Document Coverage**: All Phase K-B synthesis documents

---

## No Recommendations

This index provides no recommendations.

This index provides no design advice.

This index states only traceability mappings.

---

**END OF TRACEABILITY INDEX**

