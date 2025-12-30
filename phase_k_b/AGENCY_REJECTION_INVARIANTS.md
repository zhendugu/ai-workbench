# Agency Rejection Invariants

**Document Status**: NON-CANONICAL / DESIGN-BOUNDARY  
**Document Type**: Invariant Specification  
**Date**: 2026-01-10  
**Work Order**: WO-KB-1-DECLARED-AGENCY-PATTERN-DESIGN

---

## Purpose

This document defines invariants that must hold when users reject declared agency patterns.

Each invariant describes what must still work if agency is rejected. No design suggestions. No optimization strategies.

---

## Invariant 1: Core Functionality Preservation

**Invariant Statement**: All core system functionality must remain available after rejection of declared agency.

**Rejection Context**: User rejects pre-selection, visual emphasis, or other declared agency mechanism.

**Required State**: 
- All options remain accessible
- All operations remain executable
- No functionality is disabled
- No options are permanently removed
- System continues to function identically to pre-rejection state

**Structural Requirement**: Rejection does not break core system function. Rejection is a UI state change, not a functional change.

**KA Evidence Reference**: KA-1 DEFAULT_SELECTION experiment  
**Observed Metric**: Path offset rate 40% (users who change default)  
**Citation**: `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Justification**: 40% of users reject defaults. System must support rejection without functional degradation.

---

## Invariant 2: Option Availability Preservation

**Invariant Statement**: All options must remain available and accessible after rejection of declared agency.

**Rejection Context**: User rejects pre-selected option or visually emphasized element.

**Required State**:
- All options remain in option set
- All options remain accessible
- No option is permanently disabled
- No option is hidden or removed
- User can select any option that was available before rejection

**Structural Requirement**: Rejection does not modify option set. Option set is invariant to rejection state.

**KA Evidence Reference**: KA-2 VISUAL_HIGHLIGHT experiment  
**Observed Metric**: Visual highlight change rate 45% (users who select non-emphasized options)  
**Citation**: `audit_evidence/ka_2_visual_highlight_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Justification**: 45% of users select non-emphasized options. All options must remain available for selection.

---

## Invariant 3: User Selection Equivalence

**Invariant Statement**: User-selected options must be treated identically to pre-selected or emphasized options.

**Rejection Context**: User rejects pre-selection or visual emphasis and selects alternative option.

**Required State**:
- User-selected option receives same treatment as pre-selected option
- User-selected option executes identically to pre-selected option
- No functional difference between user-selected and pre-selected states
- No performance difference between user-selected and pre-selected states
- No access difference between user-selected and pre-selected states

**Structural Requirement**: Selection state (pre-selected vs. user-selected) does not affect option treatment. Option treatment is invariant to selection source.

**KA Evidence Reference**: KA-1 DEFAULT_SELECTION experiment  
**Observed Metric**: Path offset rate 40% (users who change default)  
**Citation**: `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Justification**: 40% of users change defaults. User-selected options must be functionally equivalent to pre-selected options.

---

## Invariant 4: Rejection Reversibility

**Invariant Statement**: User rejection of declared agency must be reversible without functional penalty.

**Rejection Context**: User rejects pre-selection or visual emphasis, then changes mind.

**Required State**:
- User can restore pre-selected state
- User can restore visual emphasis state
- Restoration does not disable functionality
- Restoration does not remove options
- Restoration does not affect system state beyond UI state

**Structural Requirement**: Rejection state is reversible. Rejection is a UI state change, not an irreversible system change.

**KA Evidence Reference**: KA-1 DEFAULT_SELECTION experiment  
**Observed Metric**: Default acceptance rate 60% (users who accept default)  
**Citation**: `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Justification**: Users may change mind. Rejection must be reversible to support user autonomy.

---

## Invariant 5: Rejection Visibility

**Invariant Statement**: Rejection action must be visible and accessible without hidden steps.

**Rejection Context**: User attempts to reject pre-selection or visual emphasis.

**Required State**:
- Rejection action is visible in primary UI
- Rejection action is accessible without hidden steps
- Rejection action does not require multiple clicks or navigation
- Rejection action is discoverable without instructions
- Rejection action is clearly associated with declared agency mechanism

**Structural Requirement**: Rejection action must be visible and accessible. Rejection cannot be hidden or obfuscated.

**KA Evidence Reference**: KA-1 DEFAULT_SELECTION experiment  
**Observed Metric**: Path offset rate 40% (users who change default)  
**Citation**: `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Justification**: 40% of users reject defaults. Rejection action must be visible and accessible to support this behavior.

---

## Invariant Summary

| Invariant ID | Name | Required State | KA Evidence |
|--------------|------|----------------|-------------|
| I1 | Core Functionality Preservation | All functionality remains available | KA-1 (40% path offset) |
| I2 | Option Availability Preservation | All options remain accessible | KA-2 (45% change rate) |
| I3 | User Selection Equivalence | User-selected = pre-selected treatment | KA-1 (40% path offset) |
| I4 | Rejection Reversibility | Rejection can be reversed | KA-1 (60% acceptance) |
| I5 | Rejection Visibility | Rejection action is visible | KA-1 (40% path offset) |

**Total Invariants**: 5

---

## No Recommendations

This invariant specification provides no recommendations.

This invariant specification provides no design suggestions.

This invariant specification provides no optimization strategies.

This invariant specification states only required invariants.

---

**END OF AGENCY REJECTION INVARIANTS**

