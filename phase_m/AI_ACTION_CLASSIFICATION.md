# AI Action Classification

**Document Status**: DESIGN-BASELINE / NON-CANONICAL  
**Document Type**: Action Classification  
**Date**: 2026-01-10  
**Work Order**: WO-M-0-HUMAN-AI-DECISION-BOUNDARY-ARCHITECTURE-BOOTSTRAP  
**Version**: Decision Boundary Baseline v1.0

---

## Purpose

This document classifies AI actions into three categories: Non-Decision Action, Advisory Action, Prohibited Action.

This classification is structural, not evaluative. This classification defines only what AI can and cannot do structurally.

---

## Classification 1: Non-Decision Action

**Definition**: AI actions that do not involve decision-making or state changes requiring human authority.

**Structural Characteristics**:
- No human decision required
- No irreversible state change
- No agency effect on human choices
- No implicit recommendation

**Instances**:

### Instance 1: Data Retrieval

**Action**: Fetching data from backend or external source.

**Classification**: Non-Decision Action

**Justification**: Data retrieval does not require human decision. Data retrieval does not change system state in irreversible way. Data retrieval does not create agency effect.

**Traceability**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` (no rule prohibits data retrieval)

---

### Instance 2: Data Transformation

**Action**: Transforming data format (parsing, formatting, validation).

**Classification**: Non-Decision Action

**Justification**: Data transformation does not require human decision. Data transformation does not change system state in irreversible way. Data transformation does not create agency effect.

**Traceability**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` (no rule prohibits data transformation)

---

### Instance 3: Display Rendering

**Action**: Rendering data for display (HTML generation, UI component rendering).

**Classification**: Non-Decision Action

**Justification**: Display rendering does not require human decision. Display rendering does not change system state in irreversible way. Display rendering does not create agency effect if no defaults, highlighting, or ordering are applied.

**Traceability**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-001, G-RULE-002, G-RULE-008 (prohibits defaults, highlighting, ordering in rendering)

---

### Instance 4: Error Reporting

**Action**: Reporting errors or validation failures to human.

**Classification**: Non-Decision Action

**Justification**: Error reporting does not require human decision. Error reporting does not change system state in irreversible way. Error reporting does not create agency effect if no recommendation language is used.

**Traceability**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-006 (prohibits recommendation language in error messages)

---

## Classification 2: Advisory Action

**Definition**: AI actions that provide information or suggestions but require explicit human decision to act upon.

**Structural Characteristics**:
- Requires explicit human decision to act
- Cannot be auto-executed
- Must be explicitly declared as advisory
- Can be rejected, overridden, or ignored without penalty

**Instances**:

### Instance 1: Declared Default Selection

**Action**: Pre-selecting an option with explicit declaration that it is a default and can be changed.

**Classification**: Advisory Action

**Justification**: Default selection is advisory if explicitly declared and rejectable. Human retains authority to change selection. Declaration removes deception.

**Traceability**: `phase_k_b/DECLARED_AGENCY_PATTERN_CATALOG.md` PATTERN-DECLARED-DEFAULT-SELECTION, `phase_k_b/AGENCY_REJECTION_INVARIANTS.md` INVARIANT-001 (rejection has no penalty)

---

### Instance 2: Declared Visual Highlight

**Action**: Visually highlighting an option with explicit declaration that it is highlighted and can be ignored.

**Classification**: Advisory Action

**Justification**: Visual highlight is advisory if explicitly declared and rejectable. Human retains authority to select non-highlighted option. Declaration removes deception.

**Traceability**: `phase_k_b/DECLARED_AGENCY_PATTERN_CATALOG.md` PATTERN-DECLARED-VISUAL-HIGHLIGHT, `phase_k_b/AGENCY_REJECTION_INVARIANTS.md` INVARIANT-001 (rejection has no penalty)

---

### Instance 3: Information Display

**Action**: Displaying information about options (descriptions, metadata, context).

**Classification**: Advisory Action

**Justification**: Information display is advisory. Human retains authority to make decision regardless of information provided. Information does not create agency effect if no recommendation language is used.

**Traceability**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-006 (prohibits recommendation language), `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-005 (prohibits justification language)

---

### Instance 4: Validation Feedback

**Action**: Providing validation feedback on human input (format errors, constraint violations).

**Classification**: Advisory Action

**Justification**: Validation feedback is advisory. Human retains authority to proceed or correct. Validation feedback does not create agency effect if no recommendation language is used.

**Traceability**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-006 (prohibits recommendation language)

---

## Classification 3: Prohibited Action

**Definition**: AI actions that violate human sovereignty or create agency effects without declaration.

**Structural Characteristics**:
- Requires human decision but AI attempts to make decision
- Creates irreversible state change without human confirmation
- Creates agency effect without declaration
- Cannot be rejected, overridden, or ignored

**Instances**:

### Instance 1: Undeclared Default Selection

**Action**: Pre-selecting an option without explicit declaration that it is a default.

**Classification**: Prohibited Action

**Justification**: Undeclared default selection creates agency effect (60% path convergence, 20% misinterpretation). Violates human sovereignty point SOV-001.

**Traceability**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-001 (prohibits undeclared default selection), `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

---

### Instance 2: Automatic Execution

**Action**: Executing an action without explicit human confirmation.

**Classification**: Prohibited Action

**Justification**: Automatic execution removes human control over irreversible state changes. Violates human sovereignty point SOV-002.

**Traceability**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-012 (prohibits automatic execution)

---

### Instance 3: Recommendation Language

**Action**: Using language that implies recommendation (recommended, suggested, best, optimal).

**Classification**: Prohibited Action

**Justification**: Recommendation language creates agency effect and implies system preference. Violates human sovereignty point SOV-007.

**Traceability**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-006 (prohibits recommendation language)

---

### Instance 4: State Memory for Agency

**Action**: Remembering user preferences or history to pre-fill or pre-select options.

**Classification**: Prohibited Action

**Justification**: State memory for agency creates agency effect and removes human control. Violates human sovereignty point SOV-003.

**Traceability**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-011 (prohibits state memory for agency)

---

## Classification Summary

**Total Classifications**: 3

**Non-Decision Actions**: 4 instances

**Advisory Actions**: 4 instances

**Prohibited Actions**: 4 instances

**Total Instances**: 12

---

## No Recommendations

This classification provides no recommendations.

This classification defines only structural action types.

---

**END OF AI ACTION CLASSIFICATION**

