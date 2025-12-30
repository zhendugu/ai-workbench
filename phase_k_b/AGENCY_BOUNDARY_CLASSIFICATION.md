# Agency Boundary Classification

**Document Status**: NON-CANONICAL / DESIGN-BOUNDARY  
**Document Type**: Agency Classification System  
**Date**: 2026-01-10  
**Work Order**: WO-KB-0-AGENCY-BOUNDARY-SYNTHESIS

---

## Purpose

This document defines three classes of agency in UI systems based on Phase K-A experimental results.

All classifications are derived from empirical observations. Each mechanism cites at least one KA experiment. No design advice. No mitigation strategies.

---

## Classification System

### Class 1: Unavoidable Agency

**Definition**: Agency effects that occur when any UI element is displayed in any structure.

**Evidence**: KA experiments demonstrate that all tested structural variables (ORDERING, GROUPING, PROXIMITY) produce measurable agency effects.

**Mechanisms**:

**1. Sequential Position (ORDERING)**
- **Evidence**: KA-3
- **Observation**: First item receives 70% first-click rate, 87% attention on first 3 items
- **Mechanism**: Any sequential list creates position-based attention bias
- **Citation**: `audit_evidence/ka_3_ordering_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**2. Spatial Proximity (PROXIMITY)**
- **Evidence**: KA-5
- **Observation**: Tight spacing area receives 60% selection rate
- **Mechanism**: Any spacing difference creates proximity-based bias
- **Citation**: `audit_evidence/ka_5_proximity_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**3. Container Structure (GROUPING)**
- **Evidence**: KA-4
- **Observation**: First group receives 65% selection rate, 30% misinterpretation as categories
- **Mechanism**: Any container grouping creates spatial classification perception
- **Citation**: `audit_evidence/ka_4_grouping_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Characteristic**: Unavoidable agency cannot be eliminated. It can only be managed through declaration.

---

### Class 2: Declared Agency

**Definition**: Agency effects that are explicitly declared to the user as intentional system behavior.

**Evidence**: KA experiments demonstrate that agency variables (DEFAULT_SELECTION, VISUAL_HIGHLIGHT) produce measurable effects that can be declared.

**Mechanisms**:

**1. Default Selection (DEFAULT_SELECTION)**
- **Evidence**: KA-1
- **Observation**: Default acceptance rate 60%, misinterpretation rate 20%
- **Mechanism**: Pre-selected option influences user behavior
- **Citation**: `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`
- **Declaration Requirement**: Must explicitly state "This option is pre-selected" or equivalent

**2. Visual Highlighting (VISUAL_HIGHLIGHT)**
- **Evidence**: KA-2
- **Observation**: Visual highlight prioritization rate 55%, misinterpretation rate 30%
- **Mechanism**: Visual difference influences user behavior
- **Citation**: `audit_evidence/ka_2_visual_highlight_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`
- **Declaration Requirement**: Must explicitly state "This item is visually emphasized" or equivalent

**Characteristic**: Declared agency is intentional and must be explicitly communicated to the user.

---

### Class 3: Prohibited Agency

**Definition**: Agency effects that are not measurable through Phase K-A experiments but are structurally prohibited by existing constitutional boundaries.

**Evidence**: Not directly tested in KA-1 through KA-5, but structurally prohibited by existing constraints.

**Mechanisms**:

**1. Implicit Recommendation Language**
- **Evidence**: Constitutional boundaries (J-series)
- **Prohibition**: System cannot use language that implies recommendation (recommended, suggested, best, optimal)
- **Structural Basis**: Existing constitutional boundaries prohibit recommendation language
- **Citation**: Constitutional boundaries established in Phase J

**2. Automatic Execution**
- **Evidence**: Constitutional boundaries (J-series)
- **Prohibition**: System cannot automatically execute capabilities without explicit human action
- **Structural Basis**: Existing constitutional boundaries prohibit automation
- **Citation**: Constitutional boundaries established in Phase J

**3. State Memory (History-Based Agency)**
- **Evidence**: Constitutional boundaries (J-series)
- **Prohibition**: System cannot use user history to influence current options
- **Structural Basis**: Existing constitutional boundaries prohibit state memory
- **Citation**: Constitutional boundaries established in Phase J

**Characteristic**: Prohibited agency is structurally impossible under existing constraints.

---

## Classification Summary

| Class | Definition | Mechanisms | Count |
|-------|------------|------------|-------|
| Unavoidable Agency | Structural agency that occurs in any UI | ORDERING, PROXIMITY, GROUPING | 3 |
| Declared Agency | Intentional agency that must be declared | DEFAULT_SELECTION, VISUAL_HIGHLIGHT | 2 |
| Prohibited Agency | Structurally prohibited agency | Implicit recommendation, automatic execution, state memory | 3 |

**Total Mechanisms Classified**: 8

---

## No Recommendations

This classification provides no recommendations.

This classification provides no design advice.

This classification states only observed and structural boundaries.

---

**END OF AGENCY BOUNDARY CLASSIFICATION**

