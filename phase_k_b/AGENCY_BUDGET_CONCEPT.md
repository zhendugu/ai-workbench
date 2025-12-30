# Agency Budget Concept

**Document Status**: NON-CANONICAL / DESIGN-BOUNDARY  
**Document Type**: Constraint Model Definition  
**Date**: 2026-01-10  
**Work Order**: WO-KB-0-AGENCY-BOUNDARY-SYNTHESIS

---

## Purpose

This document defines the concept of an "agency budget" as a constraint model for UI design.

This document defines only the constraint model. It provides no guidance on how to spend the budget. It provides no recommendations. It provides no design advice.

---

## Definition

### Agency Budget

**Concept**: Agency budget is a finite constraint that represents the total agency effects that a UI system can produce.

**Structural Basis**: 
- UI structure inherently creates agency (see `UI_NEUTRALITY_INVALIDATION.md`)
- Agency effects are measurable (see `AGENCY_EFFECT_MATRIX.md`)
- Agency effects accumulate across structural variables

**Constraint Model**: Agency budget is consumed by structural variables. Each structural variable consumes agency budget proportional to its measured effect strength.

---

## Agency Budget Consumption

### Mechanism 1: Sequential Position (ORDERING)

**Effect Strength**: 70%  
**Evidence**: KA-3  
**Citation**: `audit_evidence/ka_3_ordering_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Budget Consumption**: Sequential position consumes agency budget proportional to 70% effect strength.

**Structural Implication**: Any sequential list consumes agency budget through position-based bias.

---

### Mechanism 2: Spatial Proximity (PROXIMITY)

**Effect Strength**: 60%  
**Evidence**: KA-5  
**Citation**: `audit_evidence/ka_5_proximity_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Budget Consumption**: Spatial proximity consumes agency budget proportional to 60% effect strength.

**Structural Implication**: Any spacing difference consumes agency budget through proximity-based bias.

---

### Mechanism 3: Container Grouping (GROUPING)

**Effect Strength**: 65%  
**Evidence**: KA-4  
**Citation**: `audit_evidence/ka_4_grouping_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Budget Consumption**: Container grouping consumes agency budget proportional to 65% effect strength.

**Structural Implication**: Any container structure consumes agency budget through classification-based bias.

---

### Mechanism 4: Default Selection (DEFAULT_SELECTION)

**Effect Strength**: 60%  
**Evidence**: KA-1  
**Citation**: `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Budget Consumption**: Default selection consumes agency budget proportional to 60% effect strength.

**Structural Implication**: Any pre-selected option consumes agency budget through explicit selection state.

---

### Mechanism 5: Visual Highlighting (VISUAL_HIGHLIGHT)

**Effect Strength**: 55%  
**Evidence**: KA-2  
**Citation**: `audit_evidence/ka_2_visual_highlight_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Budget Consumption**: Visual highlighting consumes agency budget proportional to 55% effect strength.

**Structural Implication**: Any visual difference consumes agency budget through salience-based bias.

---

## Budget Constraint Model

**Principle**: Agency budget is finite and consumed by structural variables.

**Constraint**: Agency effects accumulate. Multiple structural variables increase total agency consumption.

**Structural Implication**: UI design decisions consume agency budget. Budget consumption is measurable through effect strength.

---

## No Recommendations

This concept provides no recommendations.

This concept provides no guidance on how to spend the budget.

This concept provides no design advice.

This concept defines only the constraint model.

---

**END OF AGENCY BUDGET CONCEPT**

