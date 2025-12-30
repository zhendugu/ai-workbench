# Language and Structure Constraint Check

**Document Status**: DESIGN-BASELINE / NON-CANONICAL  
**Document Type**: Constraint Check  
**Date**: 2026-01-10  
**Work Order**: WO-N-0-PRODUCT-LEVEL-AGENCY-APPLICATION  
**Parent Baselines**: Decision Boundary Baseline v1.0 (WO-M-0), Interaction Model Baseline v1.0 (WO-M-1)

---

## Purpose

This document checks whether the product scenario violates DECISION_LANGUAGE_CONSTRAINTS or triggers any Failure/Leakage Mode.

Each violation must be annotated with specific text or structure location.

---

## Language Constraint Check

### Check 1: Imperatives

**Constraint**: AI cannot use imperatives (commands or directives).

**Scenario Check**: AI may display information about configuration types, provide validation feedback, expand option sets, and request confirmation.

**Violation Status**: NO VIOLATION (if AI uses only factual statements and neutral declarative language)

**Required Language**: Factual statements only (e.g., "Configuration type X supports feature Y", "Parameter Z must be between 1 and 100", "Component A is available")

**Traceability**: `phase_m/DECISION_LANGUAGE_CONSTRAINTS.md` Pattern 1

---

### Check 2: Priority Assertions

**Constraint**: AI cannot assert relative importance or urgency.

**Scenario Check**: AI may not state that one configuration type is "more important" or "higher priority" than another.

**Violation Status**: NO VIOLATION (if AI uses only factual statements)

**Required Language**: No priority assertions (e.g., "Configuration type X has property Y" is allowed; "Configuration type X is more important" is prohibited)

**Traceability**: `phase_m/DECISION_LANGUAGE_CONSTRAINTS.md` Pattern 2

---

### Check 3: Optimization Claims

**Constraint**: AI cannot claim one option is better, optimal, or more efficient.

**Scenario Check**: AI may not state that one configuration is "better" or "more efficient" than another.

**Violation Status**: NO VIOLATION (if AI uses only factual statements)

**Required Language**: No optimization claims (e.g., "Configuration X uses resource Y" is allowed; "Configuration X is more efficient" is prohibited)

**Traceability**: `phase_m/DECISION_LANGUAGE_CONSTRAINTS.md` Pattern 3

---

### Check 4: "Best" or "Recommended" Phrasing

**Constraint**: AI cannot use "recommended", "suggested", "best", "optimal" phrasing.

**Scenario Check**: AI may not label any configuration type, parameter value, or scope as "recommended" or "best".

**Violation Status**: NO VIOLATION (if AI uses only factual statements)

**Required Language**: No recommendation language (e.g., "Configuration type X supports feature Y" is allowed; "Configuration type X is recommended" is prohibited)

**Traceability**: `phase_m/DECISION_LANGUAGE_CONSTRAINTS.md` Pattern 4

---

### Check 5: "Should" Phrasing

**Constraint**: AI cannot use "should" phrasing.

**Scenario Check**: AI may not state that human "should" select a specific configuration type, parameter value, or scope.

**Violation Status**: NO VIOLATION (if AI uses only factual statements)

**Required Language**: No "should" phrasing (e.g., "Parameter X must be between 1 and 100" is allowed for validation; "You should set parameter X to 50" is prohibited)

**Traceability**: `phase_m/DECISION_LANGUAGE_CONSTRAINTS.md` Pattern 5

---

### Check 6: Comparative Preference Language

**Constraint**: AI cannot compare options and imply preference.

**Scenario Check**: AI may not state that one configuration is "better than" or "preferred over" another.

**Violation Status**: NO VIOLATION (if AI uses only neutral comparisons)

**Required Language**: Neutral comparisons only (e.g., "Configuration X has property Y, Configuration Z has property W" is allowed; "Configuration X is better than Configuration Z" is prohibited)

**Traceability**: `phase_m/DECISION_LANGUAGE_CONSTRAINTS.md` Pattern 6

---

### Check 7: Future Benefit Claims

**Constraint**: AI cannot claim future benefits or outcomes.

**Scenario Check**: AI may not state that selecting a specific configuration will "improve performance" or "save time".

**Violation Status**: NO VIOLATION (if AI uses only factual statements about current properties)

**Required Language**: No future benefit claims (e.g., "Configuration X uses resource Y" is allowed; "Configuration X will improve performance" is prohibited)

**Traceability**: `phase_m/DECISION_LANGUAGE_CONSTRAINTS.md` Pattern 7

---

### Check 8: Probability Language

**Constraint**: AI cannot use probability or likelihood to imply recommendation.

**Scenario Check**: AI may not state that one configuration is "likely better" or "probably optimal".

**Violation Status**: NO VIOLATION (if AI uses only factual statements)

**Required Language**: No probability language (e.g., "Configuration X has property Y" is allowed; "Configuration X is likely better" is prohibited)

**Traceability**: `phase_m/DECISION_LANGUAGE_CONSTRAINTS.md` Pattern 8

---

## Failure and Leakage Mode Check

### Check 9: Implicit Coercion

**Failure Mode**: AI presents option in a way that makes rejection difficult or costly.

**Scenario Check**: AI must not hide rejection mechanisms or make rejection require multiple steps.

**Violation Status**: NO VIOLATION (if rejection mechanisms are visible and accessible)

**Required Structure**: Rejection mechanisms must be visible in primary UI, accessible without hidden steps, clearly associated with AI-provided options.

**Traceability**: `phase_m/FAILURE_AND_LEAKAGE_MODES.md` Failure Mode 1

---

### Check 10: Soft Defaulting

**Failure Mode**: AI pre-fills or pre-selects option without explicit declaration, or with declaration that is not visible.

**Scenario Check**: AI must not pre-select configuration types, pre-fill parameter values, or pre-define scope.

**Violation Status**: NO VIOLATION (if no pre-selection, pre-filling, or pre-definition occurs)

**Required Structure**: No default selection, no parameter pre-filling (except empty placeholder), no scope pre-definition.

**Traceability**: `phase_m/FAILURE_AND_LEAKAGE_MODES.md` Failure Mode 2

---

### Check 11: Framing Bias

**Failure Mode**: AI presents information in a way that frames one option as more favorable.

**Scenario Check**: AI must not emphasize positive aspects of one configuration type while de-emphasizing negative aspects.

**Violation Status**: NO VIOLATION (if information is presented neutrally for all options)

**Required Structure**: Information must be presented neutrally. All options receive same information treatment.

**Traceability**: `phase_m/FAILURE_AND_LEAKAGE_MODES.md` Failure Mode 3

---

### Check 12: Path Locking

**Failure Mode**: AI presents option in a way that locks human into specific path.

**Scenario Check**: AI must not hide alternative options or disable alternative paths after rejection.

**Violation Status**: NO VIOLATION (if all paths remain accessible after rejection)

**Required Structure**: All paths remain accessible after rejection. Rejection does not hide alternative options.

**Traceability**: `phase_m/FAILURE_AND_LEAKAGE_MODES.md` Failure Mode 4

---

### Check 13: Non-Reversible Rejection

**Failure Mode**: AI presents option in a way that makes rejection irreversible.

**Scenario Check**: AI must not remove options permanently after rejection.

**Violation Status**: NO VIOLATION (if rejection is reversible)

**Required Structure**: Rejection state is reversible. Previously rejected options remain accessible.

**Traceability**: `phase_m/FAILURE_AND_LEAKAGE_MODES.md` Failure Mode 5

---

### Check 14: Penalty for Rejection

**Failure Mode**: AI presents option in a way that triggers negative consequences when rejected.

**Scenario Check**: AI must not trigger error messages, reduce available options, or disable functionality after rejection.

**Violation Status**: NO VIOLATION (if rejection has no penalty)

**Required Structure**: Rejection does not trigger system penalty, degradation, or negative consequence.

**Traceability**: `phase_m/FAILURE_AND_LEAKAGE_MODES.md` Failure Mode 6

---

### Check 15: Auto-Transition

**Failure Mode**: AI automatically transitions from Presented state to Accepted, Rejected, or Ignored state.

**Scenario Check**: AI must not auto-confirm configuration or auto-transition based on timeout or inactivity.

**Violation Status**: NO VIOLATION (if all transitions are human-triggered)

**Required Structure**: All state transitions are human-triggered only. No auto-transitions.

**Traceability**: `phase_m/FAILURE_AND_LEAKAGE_MODES.md` Failure Mode 7

---

### Check 16: Hidden Declaration

**Failure Mode**: AI provides declaration text but hides it in secondary UI.

**Scenario Check**: AI must not hide declaration text in tooltips, hovers, or secondary menus.

**Violation Status**: NO VIOLATION (if declaration text is visible in primary UI)

**Required Structure**: Declaration text must be visible in primary UI, accessible without hidden steps.

**Traceability**: `phase_m/FAILURE_AND_LEAKAGE_MODES.md` Failure Mode 8

---

### Check 17: Softening Language

**Failure Mode**: AI uses softening language in declaration that reduces impact.

**Scenario Check**: AI must not use "might", "could", or justification language in declarations.

**Violation Status**: NO VIOLATION (if declaration uses canonical language without softening)

**Required Structure**: Declaration must use canonical language without softening, justification, or minimizing.

**Traceability**: `phase_m/FAILURE_AND_LEAKAGE_MODES.md` Failure Mode 9

---

### Check 18: Ordering Implication

**Failure Mode**: AI presents options in order that implies recommendation.

**Scenario Check**: AI must not order configuration types, parameter values, or scope options by "importance", "popularity", or "relevance".

**Violation Status**: NO VIOLATION (if ordering does not imply recommendation)

**Required Structure**: Ordering must not imply recommendation. All options must be equally accessible regardless of order.

**Traceability**: `phase_m/FAILURE_AND_LEAKAGE_MODES.md` Failure Mode 10

---

## Constraint Check Summary

**Total Language Constraints Checked**: 8

**Total Failure/Leakage Modes Checked**: 10

**Total Checks**: 18

**Violations Found**: 0 (if all constraints are followed)

**All Checks Traceable**: YES (100%)

---

## No Recommendations

This check provides no recommendations.

This check describes only constraint compliance status.

---

**END OF LANGUAGE AND STRUCTURE CONSTRAINT CHECK**

