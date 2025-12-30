# Design Constraint Extraction

**Document Status**: NON-CANONICAL / DESIGN-BOUNDARY  
**Document Type**: Constraint Specification  
**Date**: 2026-01-10  
**Work Order**: WO-KB-0-AGENCY-BOUNDARY-SYNTHESIS

---

## Purpose

This document extracts non-negotiable design constraints from Phase K-A experimental results.

Each constraint is written as a prohibition or invariant. Each constraint maps to KA evidence. No design advice. No mitigation strategies.

---

## Constraint List

### Constraint 1: Prohibition of Unacknowledged Sequential Position Bias

**Type**: Prohibition  
**Statement**: UI systems MUST NOT present sequential options without acknowledging that sequential position creates position-based bias.

**Evidence**: KA-3 ORDERING experiment  
**Data**: First item receives 70% first-click rate, 87% attention on first 3 items  
**Citation**: `audit_evidence/ka_3_ordering_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Invariant**: Sequential position bias is unavoidable. Unacknowledged sequential position violates agency transparency.

---

### Constraint 2: Prohibition of Unacknowledged Spatial Proximity Bias

**Type**: Prohibition  
**Statement**: UI systems MUST NOT present spatial layouts without acknowledging that spatial proximity creates proximity-based bias.

**Evidence**: KA-5 PROXIMITY experiment  
**Data**: Tight spacing area receives 60% selection rate, 25% misinterpretation as relatedness  
**Citation**: `audit_evidence/ka_5_proximity_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Invariant**: Spatial proximity bias is unavoidable. Unacknowledged spatial proximity violates agency transparency.

---

### Constraint 3: Prohibition of Unacknowledged Container Grouping Bias

**Type**: Prohibition  
**Statement**: UI systems MUST NOT present container groupings without acknowledging that container grouping creates classification-based bias.

**Evidence**: KA-4 GROUPING experiment  
**Data**: First group receives 65% selection rate, 30% misinterpretation as categories  
**Citation**: `audit_evidence/ka_4_grouping_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Invariant**: Container grouping bias is unavoidable. Unacknowledged container grouping violates agency transparency.

---

### Constraint 4: Prohibition of Undeclared Default Selection

**Type**: Prohibition  
**Statement**: UI systems MUST NOT use default selection without explicit declaration to the user.

**Evidence**: KA-1 DEFAULT_SELECTION experiment  
**Data**: Default acceptance rate 60%, misinterpretation rate 20%  
**Citation**: `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Invariant**: Default selection creates measurable agency effect. Undeclared default selection violates agency transparency.

---

### Constraint 5: Prohibition of Undeclared Visual Highlighting

**Type**: Prohibition  
**Statement**: UI systems MUST NOT use visual highlighting without explicit declaration to the user.

**Evidence**: KA-2 VISUAL_HIGHLIGHT experiment  
**Data**: Visual highlight prioritization rate 55%, misinterpretation rate 30%  
**Citation**: `audit_evidence/ka_2_visual_highlight_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Invariant**: Visual highlighting creates measurable agency effect. Undeclared visual highlighting violates agency transparency.

---

### Constraint 6: Invariant: UI Structure Inherently Creates Agency

**Type**: Invariant  
**Statement**: UI systems MUST acknowledge that UI structure inherently creates agency effects.

**Evidence**: KA-1 through KA-5 experiments  
**Data**: All tested structural variables produce measurable agency effects (> 0%)  
**Citation**: `phase_k_b/AGENCY_EFFECT_MATRIX.md`

**Invariant**: UI structure and agency are inseparable. Neutral UI does not exist.

---

### Constraint 7: Prohibition of "Neutral UI" Claims

**Type**: Prohibition  
**Statement**: UI systems MUST NOT claim to be "neutral" without falsifying KA experimental evidence.

**Evidence**: UI_NEUTRALITY_INVALIDATION.md  
**Data**: All structural variables (ORDERING, PROXIMITY, GROUPING) produce measurable agency  
**Citation**: `phase_k_b/UI_NEUTRALITY_INVALIDATION.md`

**Invariant**: "Neutral UI" is a false concept. Claims of neutrality violate evidence-based constraints.

---

### Constraint 8: Invariant: Agency Budget Is Finite

**Type**: Invariant  
**Statement**: UI systems MUST operate under the constraint that agency budget is finite.

**Evidence**: Agency budget concept  
**Data**: Agency effects accumulate across structural variables  
**Citation**: `phase_k_b/AGENCY_BUDGET_CONCEPT.md`

**Invariant**: Agency budget consumption is measurable. Budget is finite and consumed by structural variables.

---

### Constraint 9: Prohibition of Agency Effect Denial

**Type**: Prohibition  
**Statement**: UI systems MUST NOT deny that structural variables create agency effects.

**Evidence**: KA-1 through KA-5 experiments  
**Data**: All tested variables produce measurable effects (minimum 55%, maximum 70%)  
**Citation**: `phase_k_b/AGENCY_EFFECT_MATRIX.md`

**Invariant**: Agency effects are empirically measurable. Denial of agency effects violates evidence-based constraints.

---

### Constraint 10: Invariant: Structural Variables Are Agency Variables

**Type**: Invariant  
**Statement**: UI systems MUST acknowledge that structural variables (ORDERING, PROXIMITY, GROUPING) are agency variables.

**Evidence**: KA-3, KA-4, KA-5 experiments  
**Data**: ORDERING (70% effect), GROUPING (65% effect), PROXIMITY (60% effect)  
**Citation**: `phase_k_b/AGENCY_EFFECT_MATRIX.md`

**Invariant**: Structural variables produce agency effects. Structural variables are agency variables.

---

## Constraint Summary

| Constraint ID | Type | Mechanism | Evidence |
|---------------|------|-----------|----------|
| C1 | Prohibition | Sequential position bias | KA-3 |
| C2 | Prohibition | Spatial proximity bias | KA-5 |
| C3 | Prohibition | Container grouping bias | KA-4 |
| C4 | Prohibition | Default selection | KA-1 |
| C5 | Prohibition | Visual highlighting | KA-2 |
| C6 | Invariant | UI structure creates agency | KA-1~KA-5 |
| C7 | Prohibition | "Neutral UI" claims | UI_NEUTRALITY_INVALIDATION |
| C8 | Invariant | Agency budget is finite | AGENCY_BUDGET_CONCEPT |
| C9 | Prohibition | Agency effect denial | KA-1~KA-5 |
| C10 | Invariant | Structural variables are agency | KA-3, KA-4, KA-5 |

**Total Constraints**: 10

---

## No Recommendations

This extraction provides no recommendations.

This extraction provides no design advice.

This extraction provides no mitigation strategies.

This extraction states only prohibitions and invariants.

---

**END OF DESIGN CONSTRAINT EXTRACTION**

