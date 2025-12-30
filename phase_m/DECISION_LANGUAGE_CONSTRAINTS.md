# Decision Language Constraints

**Document Status**: DESIGN-BASELINE / NON-CANONICAL  
**Document Type**: Language Constraint Definition  
**Date**: 2026-01-10  
**Work Order**: WO-M-1-DECLARED-DECISION-INTERACTION-MODELS  
**Version**: Interaction Model Baseline v1.0  
**Parent Baseline**: Decision Boundary Baseline v1.0 (WO-M-0)

---

## Purpose

This document defines forbidden AI language patterns and required neutral declarative language.

All constraints map to M-0 boundaries. No exceptions.

---

## Forbidden Language Patterns

### Pattern 1: Imperatives

**Forbidden Pattern**: Commands or directives that tell human what to do.

**Examples**:
- "You should select X"
- "Choose Y"
- "Use Z"
- "Select this option"

**Violation**: Violates SOV-001 (Initial Selection). Human must make selection decision, not AI.

**Traceability**: `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-001, `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-006

---

### Pattern 2: Priority Assertions

**Forbidden Pattern**: Language that asserts relative importance or urgency.

**Examples**:
- "X is more important"
- "Y has higher priority"
- "Z is urgent"
- "X should be done first"

**Violation**: Violates SOV-007 (Priority Assignment). Human must assign priority, not AI.

**Traceability**: `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-007, `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-006

---

### Pattern 3: Optimization Claims

**Forbidden Pattern**: Language that claims one option is better, optimal, or more efficient.

**Examples**:
- "X is better"
- "Y is optimal"
- "Z is more efficient"
- "X will save time"

**Violation**: Violates SOV-007 (Priority Assignment). Human must evaluate options, not AI.

**Traceability**: `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-007, `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-006

---

### Pattern 4: "Best" or "Recommended" Phrasing

**Forbidden Pattern**: Language that explicitly recommends or suggests best option.

**Examples**:
- "X is recommended"
- "Y is the best choice"
- "Z is suggested"
- "X is preferred"

**Violation**: Violates SOV-007 (Priority Assignment). Recommendation language creates agency effect.

**Traceability**: `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-007, `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-006, `phase_k_b/AGENCY_EFFECT_MATRIX.md`

---

### Pattern 5: "Should" Phrasing

**Forbidden Pattern**: Language that implies obligation or recommendation.

**Examples**:
- "You should select X"
- "X should be chosen"
- "Y should be used"
- "Z should be preferred"

**Violation**: Violates SOV-001 (Initial Selection), SOV-007 (Priority Assignment). "Should" implies recommendation.

**Traceability**: `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-001, SOV-007, `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-006

---

### Pattern 6: Comparative Preference Language

**Forbidden Pattern**: Language that compares options and implies preference.

**Examples**:
- "X is better than Y"
- "Y is preferred over Z"
- "X is more suitable than Y"
- "Y is the better option"

**Violation**: Violates SOV-007 (Priority Assignment). Comparative preference language creates agency effect.

**Traceability**: `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-007, `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-006

---

### Pattern 7: Future Benefit Claims

**Forbidden Pattern**: Language that claims future benefits or outcomes.

**Examples**:
- "X will improve performance"
- "Y will save time"
- "Z will be more efficient"
- "X will help you"

**Violation**: Violates SOV-007 (Priority Assignment). Future benefit claims imply recommendation.

**Traceability**: `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-007, `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-006

---

### Pattern 8: Probability Language

**Forbidden Pattern**: Language that uses probability or likelihood to imply recommendation.

**Examples**:
- "X is likely better"
- "Y probably works best"
- "Z is most likely optimal"
- "X has a higher chance of success"

**Violation**: Violates SOV-007 (Priority Assignment). Probability language implies recommendation.

**Traceability**: `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-007, `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-006

---

## Required Neutral Declarative Language

### Pattern 1: Factual Statements

**Required Pattern**: Statements that describe facts without implying preference.

**Examples**:
- "Option X has property Y"
- "Option Y has property Z"
- "Option X supports feature Y"
- "Option Y requires parameter Z"

**Justification**: Factual statements do not create agency effect. Human retains decision authority.

**Traceability**: `phase_m/DECLARED_DECISION_INTERACTION_CATALOG.md` DIM-004, DIM-006

---

### Pattern 2: Neutral Comparisons

**Required Pattern**: Comparisons that present facts without implying preference.

**Examples**:
- "Option X has property Y, Option Z has property W"
- "Option X supports feature Y, Option Z supports feature W"
- "Option X requires parameter Y, Option Z requires parameter W"

**Justification**: Neutral comparisons do not create agency effect. Human retains decision authority.

**Traceability**: `phase_m/DECLARED_DECISION_INTERACTION_CATALOG.md` DIM-006

---

### Pattern 3: Explicit Declaration Language

**Required Pattern**: Language that explicitly declares AI action without implying recommendation.

**Examples**:
- "This option is pre-selected as a default. You can change it."
- "This option is visually highlighted. You can ignore it."
- "This information does not imply recommendation."

**Justification**: Explicit declaration removes deception. Human retains decision authority.

**Traceability**: `phase_k_b/DECLARED_AGENCY_PATTERN_CATALOG.md`, `phase_m/DECLARED_DECISION_INTERACTION_CATALOG.md` DIM-002, DIM-003

---

### Pattern 4: Validation Language

**Required Pattern**: Language that reports validation results without implying recommendation.

**Examples**:
- "Input X does not match format Y"
- "Parameter Z violates constraint W"
- "Input X is invalid"

**Justification**: Validation language reports facts. Human retains decision authority to correct or override.

**Traceability**: `phase_m/DECLARED_DECISION_INTERACTION_CATALOG.md` DIM-005

---

## Constraint Summary

**Forbidden Patterns**: 8

**Required Patterns**: 4

**All Constraints Mapped to M-0 Boundaries**: YES (100%)

**All Constraints Traceable**: YES (100%)

---

## No Recommendations

This document provides no recommendations.

This document defines only language constraints.

---

**END OF DECISION LANGUAGE CONSTRAINTS**

