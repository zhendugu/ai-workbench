# KB-2 Traceability and Audit Index

**Document Status**: NON-CANONICAL / DESIGN-BOUNDARY  
**Document Type**: Traceability Mapping  
**Date**: 2026-01-10  
**Work Order**: WO-KB-2-AGENCY-GOVERNANCE-ENFORCEMENT-RULES

---

## Purpose

This document maps every governance rule back to KB-0 boundary, KB-1 pattern, and KA evidence.

No orphan rules allowed. All rules must be traceable.

---

## Rule Traceability Mappings

### G-RULE-001: Prohibition of Undeclared Default Selection

**KB-0 Boundary Reference**: Constraint 4 (Prohibition of Undeclared Default Selection)  
**Citation**: `phase_k_b/DESIGN_CONSTRAINT_EXTRACTION.md` Constraint 4

**KB-1 Pattern Reference**: PATTERN-DECLARED-DEFAULT-SELECTION  
**Citation**: `phase_k_b/DECLARED_AGENCY_PATTERN_CATALOG.md` Pattern 1

**KA Evidence Reference**: KA-1 DEFAULT_SELECTION experiment  
**Evidence File**: `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`  
**Observed Metrics**: Default acceptance rate 60%, misinterpretation rate 20%

---

### G-RULE-002: Prohibition of Undeclared Visual Highlighting

**KB-0 Boundary Reference**: Constraint 5 (Prohibition of Undeclared Visual Highlighting)  
**Citation**: `phase_k_b/DESIGN_CONSTRAINT_EXTRACTION.md` Constraint 5

**KB-1 Pattern Reference**: PATTERN-DECLARED-VISUAL-HIGHLIGHT  
**Citation**: `phase_k_b/DECLARED_AGENCY_PATTERN_CATALOG.md` Pattern 2

**KA Evidence Reference**: KA-2 VISUAL_HIGHLIGHT experiment  
**Evidence File**: `audit_evidence/ka_2_visual_highlight_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`  
**Observed Metrics**: Visual highlight prioritization rate 55%, misinterpretation rate 30%

---

### G-RULE-003: Prohibition of Hidden Declaration

**KB-0 Boundary Reference**: Constraint 4, Constraint 5 (declaration requirements)  
**Citation**: `phase_k_b/DESIGN_CONSTRAINT_EXTRACTION.md`

**KB-1 Pattern Reference**: PATTERN_FAILURE_MODES.md (Failure Modes 1.1, 2.1, 3.1)  
**Citation**: `phase_k_b/PATTERN_FAILURE_MODES.md`

**KA Evidence Reference**: KA-1, KA-2 (misinterpretation rates without visible declaration)  
**Evidence Files**: 
- `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md` (20% misinterpretation)
- `audit_evidence/ka_2_visual_highlight_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md` (30% misinterpretation)

---

### G-RULE-004: Prohibition of Softening Language in Declaration

**KB-0 Boundary Reference**: Constraint 4, Constraint 5 (declaration requirements)  
**Citation**: `phase_k_b/DESIGN_CONSTRAINT_EXTRACTION.md`

**KB-1 Pattern Reference**: PATTERN_FAILURE_MODES.md (Failure Modes 1.2, 2.2, 3.3)  
**Citation**: `phase_k_b/PATTERN_FAILURE_MODES.md`

**KA Evidence Reference**: KA-1, KA-2 (significant effect rates, softening minimizes influence)  
**Evidence Files**: 
- `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md` (60% effect)
- `audit_evidence/ka_2_visual_highlight_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md` (55% effect)

---

### G-RULE-005: Prohibition of Justification Language in Declaration

**KB-0 Boundary Reference**: Constraint 4, Constraint 5 (declaration requirements)  
**Citation**: `phase_k_b/DESIGN_CONSTRAINT_EXTRACTION.md`

**KB-1 Pattern Reference**: PATTERN_FAILURE_MODES.md (Failure Modes 1.3, 2.3)  
**Citation**: `phase_k_b/PATTERN_FAILURE_MODES.md`

**KA Evidence Reference**: KA-1, KA-2 (misinterpretation rates, justification implies recommendation)  
**Evidence Files**: 
- `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md` (20% misinterpretation)
- `audit_evidence/ka_2_visual_highlight_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md` (30% misinterpretation)

---

### G-RULE-006: Prohibition of Recommendation Language

**KB-0 Boundary Reference**: Class 3 (Prohibited Agency), Constraint 7 (Prohibition of "Neutral UI" Claims)  
**Citation**: `phase_k_b/AGENCY_BOUNDARY_CLASSIFICATION.md` Class 3, `phase_k_b/DESIGN_CONSTRAINT_EXTRACTION.md` Constraint 7

**KB-1 Pattern Reference**: N/A (recommendation language is prohibited, not declared)

**KA Evidence Reference**: Constitutional boundaries (J-series), not directly tested in KA experiments

---

### G-RULE-007: Prohibition of Non-Rejectable Agency

**KB-0 Boundary Reference**: Constraint 4, Constraint 5 (declaration requirements imply rejection)  
**Citation**: `phase_k_b/DESIGN_CONSTRAINT_EXTRACTION.md`

**KB-1 Pattern Reference**: AGENCY_REJECTION_INVARIANTS.md (I1, I2, I3, I4, I5)  
**Citation**: `phase_k_b/AGENCY_REJECTION_INVARIANTS.md`

**KA Evidence Reference**: KA-1, KA-2 (path offset rates, change rates indicate rejection behavior)  
**Evidence Files**: 
- `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md` (40% path offset)
- `audit_evidence/ka_2_visual_highlight_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md` (45% change rate)

---

### G-RULE-008: Prohibition of Unacknowledged Sequential Position Bias

**KB-0 Boundary Reference**: Constraint 1 (Prohibition of Unacknowledged Sequential Position Bias)  
**Citation**: `phase_k_b/DESIGN_CONSTRAINT_EXTRACTION.md` Constraint 1

**KB-1 Pattern Reference**: N/A (Class 1: Unavoidable Agency, acknowledgment required but not pattern)

**KA Evidence Reference**: KA-3 ORDERING experiment  
**Evidence File**: `audit_evidence/ka_3_ordering_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`  
**Observed Metrics**: First item first-click rate 70%, 87% attention on first 3 items

---

### G-RULE-009: Prohibition of Unacknowledged Spatial Proximity Bias

**KB-0 Boundary Reference**: Constraint 2 (Prohibition of Unacknowledged Spatial Proximity Bias)  
**Citation**: `phase_k_b/DESIGN_CONSTRAINT_EXTRACTION.md` Constraint 2

**KB-1 Pattern Reference**: N/A (Class 1: Unavoidable Agency, acknowledgment required but not pattern)

**KA Evidence Reference**: KA-5 PROXIMITY experiment  
**Evidence File**: `audit_evidence/ka_5_proximity_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`  
**Observed Metrics**: Tight spacing area selection rate 60%, misinterpretation rate 25%

---

### G-RULE-010: Prohibition of Unacknowledged Container Grouping Bias

**KB-0 Boundary Reference**: Constraint 3 (Prohibition of Unacknowledged Container Grouping Bias)  
**Citation**: `phase_k_b/DESIGN_CONSTRAINT_EXTRACTION.md` Constraint 3

**KB-1 Pattern Reference**: N/A (Class 1: Unavoidable Agency, acknowledgment required but not pattern)

**KA Evidence Reference**: KA-4 GROUPING experiment  
**Evidence File**: `audit_evidence/ka_4_grouping_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`  
**Observed Metrics**: First group selection rate 65%, misinterpretation rate 30%

---

### G-RULE-011: Prohibition of State Memory for Agency

**KB-0 Boundary Reference**: Class 3 (Prohibited Agency)  
**Citation**: `phase_k_b/AGENCY_BOUNDARY_CLASSIFICATION.md` Class 3

**KB-1 Pattern Reference**: N/A (state memory is prohibited, not declared)

**KA Evidence Reference**: Constitutional boundaries (J-series), not directly tested in KA experiments

---

### G-RULE-012: Prohibition of Automatic Execution

**KB-0 Boundary Reference**: Class 3 (Prohibited Agency)  
**Citation**: `phase_k_b/AGENCY_BOUNDARY_CLASSIFICATION.md` Class 3

**KB-1 Pattern Reference**: N/A (automatic execution is prohibited, not declared)

**KA Evidence Reference**: Constitutional boundaries (J-series), not directly tested in KA experiments

---

## Traceability Summary

**Total Rules**: 12

**Rules with KB-0 References**: 12/12 (100%)

**Rules with KB-1 References**: 7/12 (58%) - Rules 1-7 reference KB-1 patterns/failure modes, Rules 8-12 reference KB-0 constraints or Class 3

**Rules with KA Evidence References**: 9/12 (75%) - Rules 1-5, 7-10 reference KA experiments, Rules 6, 11-12 reference constitutional boundaries

**Orphan Rules**: 0/12 (0%)

---

## No Recommendations

This traceability index provides no recommendations.

This traceability index provides no design advice.

This traceability index states only traceability mappings.

---

**END OF KB-2 TRACEABILITY AND AUDIT INDEX**

