# Agency Governance Ruleset

**Document Status**: NON-CANONICAL / DESIGN-BOUNDARY  
**Document Type**: Governance Rule Specification  
**Date**: 2026-01-10  
**Work Order**: WO-KB-2-AGENCY-GOVERNANCE-ENFORCEMENT-RULES

---

## Purpose

This document defines enforceable governance rules that prevent regression into implicit agency, soft erosion of declared agency, and introduction of prohibited agency.

All rules are structural. All rules are traceable to KB evidence. No intent-based rules. No discretionary enforcement.

---

## Rule 1: Prohibition of Undeclared Default Selection

**Rule ID**: G-RULE-001

**Type**: MUST NOT

**Statement**: Changes MUST NOT introduce default selection (pre-selected option, checkbox, radio button) without explicit declaration.

**Trigger Condition**: Code change introduces: selected attribute, checked attribute, defaultChecked property, or equivalent pre-selection state.

**Required Declaration**: If default selection exists, MUST include canonical disclosure text: "This option is pre-selected. This pre-selection influences attention and choice."

**Failure Consequence**: Block merge. Require rollback or add declaration.

**KB Evidence Reference**: KB-0 Constraint 4, KA-1 DEFAULT_SELECTION experiment (60% effect, 20% misinterpretation)

**Citation**: `phase_k_b/DESIGN_CONSTRAINT_EXTRACTION.md` Constraint 4, `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

---

## Rule 2: Prohibition of Undeclared Visual Highlighting

**Rule ID**: G-RULE-002

**Type**: MUST NOT

**Statement**: Changes MUST NOT introduce visual highlighting (border, background, font weight, color emphasis) without explicit declaration.

**Trigger Condition**: Code change introduces: CSS class or inline style that creates visual emphasis difference (border > 1px, background color, font-weight > normal, color difference) relative to non-emphasized elements.

**Required Declaration**: If visual highlighting exists, MUST include canonical disclosure text: "This element is visually emphasized. This emphasis influences attention and choice."

**Failure Consequence**: Block merge. Require rollback or add declaration.

**KB Evidence Reference**: KB-0 Constraint 5, KA-2 VISUAL_HIGHLIGHT experiment (55% effect, 30% misinterpretation)

**Citation**: `phase_k_b/DESIGN_CONSTRAINT_EXTRACTION.md` Constraint 5, `audit_evidence/ka_2_visual_highlight_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

---

## Rule 3: Prohibition of Hidden Declaration

**Rule ID**: G-RULE-003

**Type**: MUST NOT

**Statement**: Changes MUST NOT place declaration text in hidden locations (tooltip, hover, secondary UI, collapsed section).

**Trigger Condition**: Code change places declaration text in: tooltip, hover state, secondary UI, collapsed section, or requires user action to view.

**Required Declaration**: Declaration text MUST be visible without user action in primary UI.

**Failure Consequence**: Block merge. Require declaration text in primary UI.

**KB Evidence Reference**: KB-1 PATTERN_FAILURE_MODES.md (Failure Mode 1.1, 2.1, 3.1)

**Citation**: `phase_k_b/PATTERN_FAILURE_MODES.md`

---

## Rule 4: Prohibition of Softening Language in Declaration

**Rule ID**: G-RULE-004

**Type**: MUST NOT

**Statement**: Changes MUST NOT use softening words (a bit, slightly, somewhat, might, could) in declaration text.

**Trigger Condition**: Code change contains declaration text with softening words: a bit, slightly, somewhat, might, could, tends to, usually.

**Required Declaration**: Declaration text MUST use exact canonical language from AGENCY_DISCLOSURE_LANGUAGE.md.

**Failure Consequence**: Block merge. Require canonical language.

**KB Evidence Reference**: KB-1 PATTERN_FAILURE_MODES.md (Failure Mode 1.2, 2.2, 3.3)

**Citation**: `phase_k_b/PATTERN_FAILURE_MODES.md`

---

## Rule 5: Prohibition of Justification Language in Declaration

**Rule ID**: G-RULE-005

**Type**: MUST NOT

**Statement**: Changes MUST NOT use justification words (because, to help, for convenience, to guide) in declaration text.

**Trigger Condition**: Code change contains declaration text with justification words: because, since, to help, for convenience, to guide, to make it easier.

**Required Declaration**: Declaration text MUST use exact canonical language from AGENCY_DISCLOSURE_LANGUAGE.md.

**Failure Consequence**: Block merge. Require canonical language.

**KB Evidence Reference**: KB-1 PATTERN_FAILURE_MODES.md (Failure Mode 1.3, 2.3)

**Citation**: `phase_k_b/PATTERN_FAILURE_MODES.md`

---

## Rule 6: Prohibition of Recommendation Language

**Rule ID**: G-RULE-006

**Type**: MUST NOT

**Statement**: Changes MUST NOT use recommendation words (recommended, suggested, best, preferred, optimal) in UI text.

**Trigger Condition**: Code change contains UI text with recommendation words: recommended, suggested, best, preferred, optimal, ideal, should.

**Required Declaration**: N/A (recommendation language is prohibited, not declared)

**Failure Consequence**: Block merge. Require removal of recommendation language.

**KB Evidence Reference**: KB-0 Class 3 (Prohibited Agency), Constitutional boundaries (J-series)

**Citation**: `phase_k_b/AGENCY_BOUNDARY_CLASSIFICATION.md` Class 3

---

## Rule 7: Prohibition of Non-Rejectable Agency

**Rule ID**: G-RULE-007

**Type**: MUST NOT

**Statement**: Changes MUST NOT introduce agency mechanism that cannot be rejected by user.

**Trigger Condition**: Code change introduces: pre-selection that cannot be deselected, visual emphasis that cannot be ignored, or agency mechanism that disables functionality upon rejection.

**Required Declaration**: Agency mechanism MUST be rejectable per AGENCY_REJECTION_INVARIANTS.md.

**Failure Consequence**: Block merge. Require rejection mechanism or remove agency.

**KB Evidence Reference**: KB-1 AGENCY_REJECTION_INVARIANTS.md (I1, I2, I3, I4, I5)

**Citation**: `phase_k_b/AGENCY_REJECTION_INVARIANTS.md`

---

## Rule 8: Prohibition of Unacknowledged Sequential Position Bias

**Rule ID**: G-RULE-008

**Type**: MUST NOT

**Statement**: Changes MUST NOT introduce sequential lists without acknowledging position-based bias.

**Trigger Condition**: Code change introduces: ordered list, menu, or sequential display of options.

**Required Declaration**: Sequential lists MUST include acknowledgment: "This list creates position-based attention bias. Items appear in this order."

**Failure Consequence**: Block merge. Require acknowledgment.

**KB Evidence Reference**: KB-0 Constraint 1, KA-3 ORDERING experiment (70% effect)

**Citation**: `phase_k_b/DESIGN_CONSTRAINT_EXTRACTION.md` Constraint 1, `audit_evidence/ka_3_ordering_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

---

## Rule 9: Prohibition of Unacknowledged Spatial Proximity Bias

**Rule ID**: G-RULE-009

**Type**: MUST NOT

**Statement**: Changes MUST NOT introduce spatial layouts with proximity differences without acknowledging proximity-based bias.

**Trigger Condition**: Code change introduces: spacing differences (margin, padding) between options, or spatial grouping without explicit acknowledgment.

**Required Declaration**: Spatial layouts with proximity differences MUST include acknowledgment: "This layout creates proximity-based attention bias. Spacing differences influence attention."

**Failure Consequence**: Block merge. Require acknowledgment.

**KB Evidence Reference**: KB-0 Constraint 2, KA-5 PROXIMITY experiment (60% effect)

**Citation**: `phase_k_b/DESIGN_CONSTRAINT_EXTRACTION.md` Constraint 2, `audit_evidence/ka_5_proximity_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

---

## Rule 10: Prohibition of Unacknowledged Container Grouping Bias

**Rule ID**: G-RULE-010

**Type**: MUST NOT

**Statement**: Changes MUST NOT introduce container groupings without acknowledging classification-based bias.

**Trigger Condition**: Code change introduces: container divs, sections, or groups that partition options without explicit acknowledgment.

**Required Declaration**: Container groupings MUST include acknowledgment: "This grouping creates classification-based attention bias. Container structure influences perception."

**Failure Consequence**: Block merge. Require acknowledgment.

**KB Evidence Reference**: KB-0 Constraint 3, KA-4 GROUPING experiment (65% effect, 30% misinterpretation)

**Citation**: `phase_k_b/DESIGN_CONSTRAINT_EXTRACTION.md` Constraint 3, `audit_evidence/ka_4_grouping_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

---

## Rule 11: Prohibition of State Memory for Agency

**Rule ID**: G-RULE-011

**Type**: MUST NOT

**Statement**: Changes MUST NOT introduce state memory (localStorage, sessionStorage, cookies, URL parameters) that influences current options or selection behavior.

**Trigger Condition**: Code change introduces: localStorage, sessionStorage, cookie, or URL parameter that stores user selection, preference, or history to influence current UI.

**Required Declaration**: N/A (state memory for agency is prohibited, not declared)

**Failure Consequence**: Block merge. Require removal of state memory.

**KB Evidence Reference**: KB-0 Class 3 (Prohibited Agency), Constitutional boundaries (J-series)

**Citation**: `phase_k_b/AGENCY_BOUNDARY_CLASSIFICATION.md` Class 3

---

## Rule 12: Prohibition of Automatic Execution

**Rule ID**: G-RULE-012

**Type**: MUST NOT

**Statement**: Changes MUST NOT introduce automatic execution of capabilities without explicit user action.

**Trigger Condition**: Code change introduces: automatic capability execution, auto-run, or execution triggered without explicit user click/action.

**Required Declaration**: N/A (automatic execution is prohibited, not declared)

**Failure Consequence**: Block merge. Require explicit user action.

**KB Evidence Reference**: KB-0 Class 3 (Prohibited Agency), Constitutional boundaries (J-series)

**Citation**: `phase_k_b/AGENCY_BOUNDARY_CLASSIFICATION.md` Class 3

---

## Rule Summary

| Rule ID | Type | Mechanism | KB Evidence |
|---------|------|-----------|-------------|
| G-RULE-001 | MUST NOT | Undeclared default selection | KB-0 C4, KA-1 |
| G-RULE-002 | MUST NOT | Undeclared visual highlighting | KB-0 C5, KA-2 |
| G-RULE-003 | MUST NOT | Hidden declaration | KB-1 Failure Modes |
| G-RULE-004 | MUST NOT | Softening language | KB-1 Failure Modes |
| G-RULE-005 | MUST NOT | Justification language | KB-1 Failure Modes |
| G-RULE-006 | MUST NOT | Recommendation language | KB-0 Class 3 |
| G-RULE-007 | MUST NOT | Non-rejectable agency | KB-1 Invariants |
| G-RULE-008 | MUST NOT | Unacknowledged ordering | KB-0 C1, KA-3 |
| G-RULE-009 | MUST NOT | Unacknowledged proximity | KB-0 C2, KA-5 |
| G-RULE-010 | MUST NOT | Unacknowledged grouping | KB-0 C3, KA-4 |
| G-RULE-011 | MUST NOT | State memory for agency | KB-0 Class 3 |
| G-RULE-012 | MUST NOT | Automatic execution | KB-0 Class 3 |

**Total Rules**: 12

---

## No Recommendations

This ruleset provides no recommendations.

This ruleset provides no design advice.

This ruleset states only enforceable governance rules.

---

**END OF AGENCY GOVERNANCE RULESET**

