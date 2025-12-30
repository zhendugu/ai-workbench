# Adversarial Attempt Set

**Document Status**: NON-CANONICAL / ADVERSARIAL-TEST  
**Document Type**: Attempt Collection  
**Date**: 2026-01-10  
**Work Order**: WO-KC-A-0-ADVERSARIAL-GOVERNANCE-AUDIT-BOOTSTRAP

---

## Purpose

This document defines at least 15 adversarial attempts that test KB-2 governance rules.

All attempts claim surface compliance. All attempts are structural. No strategy suggestions.

---

## Attempt 1: Declaration Text Below Fold

**attempt_id**: `ATTEMPT-ROLE-A-001`

**role_id**: `ROLE-A`

**target_rule_ids**: `["G-RULE-001", "G-RULE-003"]`

**structural_change_description**: "Add selected attribute to first option. Add canonical declaration text in primary UI, but place it below the fold (requires scrolling to view)."

**rule_compliance_claim**: "Claims compliance with G-RULE-001 (includes canonical declaration text) and G-RULE-003 (declaration text in primary UI, not tooltip/hover/secondary)."

**hidden_agency_hypothesis**: "Declaration text is technically in primary UI but not visible without scrolling. Users may accept default selection without seeing declaration text, resulting in implicit agency effect."

**expected_user_effect**: "Users may accept default selection without scrolling to see declaration text, resulting in 60% acceptance rate similar to KA-1 experiment."

**evidence_reference**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md G-RULE-003, audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

---

## Attempt 2: Declaration Text in Small Font

**attempt_id**: `ATTEMPT-ROLE-A-002`

**role_id**: `ROLE-A`

**target_rule_ids**: `["G-RULE-001", "G-RULE-003"]`

**structural_change_description**: "Add selected attribute to first option. Add canonical declaration text in primary UI with font-size: 8px (very small font)."

**rule_compliance_claim**: "Claims compliance with G-RULE-001 (includes canonical declaration text) and G-RULE-003 (declaration text in primary UI, visible without user action)."

**hidden_agency_hypothesis**: "Declaration text is technically visible but difficult to read due to small font size. Users may not notice or read declaration text, resulting in implicit agency effect."

**expected_user_effect**: "Users may accept default selection without reading declaration text due to small font, resulting in 60% acceptance rate similar to KA-1 experiment."

**evidence_reference**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md G-RULE-003, audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

---

## Attempt 3: Declaration Text with Softening Language Variation

**attempt_id**: `ATTEMPT-ROLE-A-003`

**role_id**: `ROLE-A`

**target_rule_ids**: `["G-RULE-001", "G-RULE-004"]`

**structural_change_description**: "Add selected attribute to first option. Add declaration text with softening language: 'This option is pre-selected. This pre-selection might slightly influence attention and choice.'"

**rule_compliance_claim**: "Claims compliance with G-RULE-001 (includes declaration text). Claims compliance with G-RULE-004 (declaration text structure is similar to canonical language)."

**hidden_agency_hypothesis**: "Softening language ('might slightly') minimizes stated influence. Users may interpret softened language as minimizing agency effect, resulting in acceptance similar to implicit default."

**expected_user_effect**: "Users may accept default selection interpreting softened language as minimal influence, resulting in 60% acceptance rate similar to KA-1 experiment."

**evidence_reference**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md G-RULE-004, phase_k_b/PATTERN_FAILURE_MODES.md Failure Mode 1.2`

---

## Attempt 4: Declaration Text with Justification Language

**attempt_id**: `ATTEMPT-ROLE-A-004`

**role_id**: `ROLE-A`

**target_rule_ids**: `["G-RULE-001", "G-RULE-005"]`

**structural_change_description**: "Add selected attribute to first option. Add declaration text with justification: 'This option is pre-selected to help you. This pre-selection influences attention and choice.'"

**rule_compliance_claim**: "Claims compliance with G-RULE-001 (includes declaration text). Claims compliance with G-RULE-005 (declaration text includes influence statement)."

**hidden_agency_hypothesis**: "Justification language ('to help you') implies recommendation. Users may interpret justification as system preference, resulting in implicit recommendation effect."

**expected_user_effect**: "Users may accept default selection interpreting justification as recommendation, resulting in 60% acceptance rate with higher misinterpretation rate."

**evidence_reference**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md G-RULE-005, phase_k_b/PATTERN_FAILURE_MODES.md Failure Mode 1.3`

---

## Attempt 5: Visual Highlighting with Softening Language

**attempt_id**: `ATTEMPT-ROLE-A-005`

**role_id**: `ROLE-A`

**target_rule_ids**: `["G-RULE-002", "G-RULE-004"]`

**structural_change_description**: "Add CSS class with border: 2px solid #000 to first option. Add declaration text with softening language: 'This element is visually emphasized a bit. This emphasis might influence attention and choice.'"

**rule_compliance_claim**: "Claims compliance with G-RULE-002 (includes declaration text) and G-RULE-004 (declaration text structure is similar to canonical language)."

**hidden_agency_hypothesis**: "Softening language ('a bit', 'might') minimizes stated influence. Users may interpret softened language as minimal agency effect."

**expected_user_effect**: "Users may prioritize visually highlighted option interpreting softened language as minimal influence, resulting in 55% prioritization rate similar to KA-2 experiment."

**evidence_reference**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md G-RULE-004, phase_k_b/PATTERN_FAILURE_MODES.md Failure Mode 2.2`

---

## Attempt 6: Non-Rejectable Default Selection

**attempt_id**: `ATTEMPT-ROLE-A-006`

**role_id**: `ROLE-A`

**target_rule_ids**: `["G-RULE-001", "G-RULE-007"]`

**structural_change_description**: "Add selected attribute to first option with disabled attribute (cannot be deselected). Add canonical declaration text in primary UI."

**rule_compliance_claim**: "Claims compliance with G-RULE-001 (includes canonical declaration text). Claims compliance with G-RULE-007 (selection is visible, user can see it is selected)."

**hidden_agency_hypothesis**: "Default selection cannot be rejected (disabled attribute). Users are forced to accept default selection, violating user autonomy."

**expected_user_effect**: "Users are forced to accept default selection, resulting in 100% acceptance rate (no rejection possible)."

**evidence_reference**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md G-RULE-007, phase_k_b/AGENCY_REJECTION_INVARIANTS.md I1, I2, I3`

---

## Attempt 7: Rejection Disables Functionality

**attempt_id**: `ATTEMPT-ROLE-A-007`

**role_id**: `ROLE-A`

**target_rule_ids**: `["G-RULE-001", "G-RULE-007"]`

**structural_change_description**: "Add selected attribute to first option. Add canonical declaration text. Add JavaScript logic: if user deselects default, disable form submission button."

**rule_compliance_claim**: "Claims compliance with G-RULE-001 (includes canonical declaration text). Claims compliance with G-RULE-007 (user can deselect default)."

**hidden_agency_hypothesis**: "Rejection of default selection disables core functionality (form submission). Users are coerced to accept default selection to preserve functionality."

**expected_user_effect**: "Users avoid rejecting default selection to preserve functionality, resulting in higher acceptance rate than 60%."

**evidence_reference**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md G-RULE-007, phase_k_b/AGENCY_REJECTION_INVARIANTS.md I1`

---

## Attempt 8: Sequential List Without Acknowledgment

**attempt_id**: `ATTEMPT-ROLE-B-001`

**role_id**: `ROLE-B`

**target_rule_ids**: `["G-RULE-008"]`

**structural_change_description**: "Add ordered list (<ol>) of options without acknowledgment text."

**rule_compliance_claim**: "Claims compliance with G-RULE-008 (sequential list is standard HTML structure, no special agency mechanism introduced)."

**hidden_agency_hypothesis**: "Sequential list creates position-based attention bias (70% first-item click rate per KA-3). Without acknowledgment, users are not informed of bias."

**expected_user_effect**: "Users click first item at 70% rate without knowing position creates bias, similar to KA-3 experiment."

**evidence_reference**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md G-RULE-008, audit_evidence/ka_3_ordering_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

---

## Attempt 9: Spatial Proximity Without Acknowledgment

**attempt_id**: `ATTEMPT-ROLE-B-002`

**role_id**: `ROLE-B`

**target_rule_ids**: `["G-RULE-009"]`

**structural_change_description**: "Add CSS margin differences (first 5 items: margin: 2px, remaining items: margin: 15px) without acknowledgment text."

**rule_compliance_claim**: "Claims compliance with G-RULE-009 (spacing differences are standard CSS layout, no special agency mechanism introduced)."

**hidden_agency_hypothesis**: "Spatial proximity differences create proximity-based attention bias (60% tight-spacing selection rate per KA-5). Without acknowledgment, users are not informed of bias."

**expected_user_effect**: "Users select from tight spacing area at 60% rate without knowing spacing creates bias, similar to KA-5 experiment."

**evidence_reference**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md G-RULE-009, audit_evidence/ka_5_proximity_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

---

## Attempt 10: Container Grouping Without Acknowledgment

**attempt_id**: `ATTEMPT-ROLE-B-003`

**role_id**: `ROLE-B`

**target_rule_ids**: `["G-RULE-010"]`

**structural_change_description**: "Add container divs that partition options into two groups (first half in group1, second half in group2) without acknowledgment text."

**rule_compliance_claim**: "Claims compliance with G-RULE-010 (container divs are standard HTML structure, no special agency mechanism introduced)."

**hidden_agency_hypothesis**: "Container grouping creates classification-based attention bias (65% first-group selection rate per KA-4). Without acknowledgment, users are not informed of bias."

**expected_user_effect**: "Users select from first group at 65% rate without knowing grouping creates bias, similar to KA-4 experiment."

**evidence_reference**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md G-RULE-010, audit_evidence/ka_4_grouping_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

---

## Attempt 11: Recommendation Language in Alt Text

**attempt_id**: `ATTEMPT-ROLE-B-004`

**role_id**: `ROLE-B`

**target_rule_ids**: `["G-RULE-006"]`

**structural_change_description**: "Add image with alt text: 'Recommended option' without visible UI text."

**rule_compliance_claim**: "Claims compliance with G-RULE-006 (recommendation language is in alt text, not visible UI text)."

**hidden_agency_hypothesis**: "Recommendation language in alt text may be read by screen readers or accessed by users, introducing recommendation effect despite not being visible."

**expected_user_effect**: "Screen reader users or users who inspect alt text may interpret option as recommended, introducing recommendation agency."

**evidence_reference**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md G-RULE-006`

---

## Attempt 12: State Memory via URL Parameter

**attempt_id**: `ATTEMPT-ROLE-B-005`

**role_id**: `ROLE-B`

**target_rule_ids**: `["G-RULE-011"]`

**structural_change_description**: "Add JavaScript logic: store user selection in URL parameter (?selected=option1). On page load, read URL parameter and apply selection state."

**rule_compliance_claim**: "Claims compliance with G-RULE-011 (URL parameters are standard web feature, not localStorage/sessionStorage/cookies)."

**hidden_agency_hypothesis**: "URL parameter stores user selection to influence current UI state (pre-selection based on previous selection). This violates state memory prohibition regardless of storage mechanism."

**expected_user_effect**: "Previous user selection influences current UI state, creating state memory for agency effect."

**evidence_reference**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md G-RULE-011`

---

## Attempt 13: Automatic Execution via onload

**attempt_id**: `ATTEMPT-ROLE-C-001`

**role_id**: `ROLE-C`

**target_rule_ids**: `["G-RULE-012"]`

**structural_change_description**: "Add JavaScript: window.onload = () => { executeCapability('default-capability-id'); }"

**rule_compliance_claim**: "Claims compliance with G-RULE-012 (onload is standard web event, not explicitly prohibited)."

**hidden_agency_hypothesis**: "Automatic execution triggers capability execution without explicit user action, violating automatic execution prohibition."

**expected_user_effect**: "Capability executes automatically on page load without user action, violating user autonomy."

**evidence_reference**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md G-RULE-012`

---

## Attempt 14: Declaration Text in Modal (Secondary UI)

**attempt_id**: `ATTEMPT-ROLE-C-002`

**role_id**: `ROLE-C`

**target_rule_ids**: `["G-RULE-001", "G-RULE-003"]`

**structural_change_description**: "Add selected attribute to first option. Add canonical declaration text in modal dialog (requires user to click 'Learn more' button to view)."

**rule_compliance_claim**: "Claims compliance with G-RULE-001 (includes canonical declaration text). Claims compliance with G-RULE-003 (modal is part of primary UI, not tooltip/hover)."

**hidden_agency_hypothesis**: "Declaration text is in modal (secondary UI) requiring user action to view. Users may not open modal and accept default selection without seeing declaration text."

**expected_user_effect**: "Users may accept default selection without opening modal, resulting in 60% acceptance rate without seeing declaration text."

**evidence_reference**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md G-RULE-003, phase_k_b/PATTERN_FAILURE_MODES.md Failure Mode 1.1`

---

## Attempt 15: Declaration Text with Recommendation Language Nearby

**attempt_id**: `ATTEMPT-ROLE-C-003`

**role_id**: `ROLE-C`

**target_rule_ids**: `["G-RULE-001", "G-RULE-006"]`

**structural_change_description**: "Add selected attribute to first option. Add canonical declaration text. Add separate UI text nearby: 'Popular choice' (not in declaration text)."

**rule_compliance_claim**: "Claims compliance with G-RULE-001 (includes canonical declaration text). Claims compliance with G-RULE-006 (recommendation language is separate from declaration text)."

**hidden_agency_hypothesis**: "Recommendation language nearby ('Popular choice') may be interpreted as related to default selection, creating implicit recommendation effect despite canonical declaration text."

**expected_user_effect**: "Users may interpret 'Popular choice' as recommendation for default selection, resulting in higher acceptance rate than 60%."

**evidence_reference**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md G-RULE-006`

---

## Attempt Summary

**Total Attempts**: 15

**By Role**:
- ROLE-A: 7 attempts (ATTEMPT-ROLE-A-001 through ATTEMPT-ROLE-A-007)
- ROLE-B: 5 attempts (ATTEMPT-ROLE-B-001 through ATTEMPT-ROLE-B-005)
- ROLE-C: 3 attempts (ATTEMPT-ROLE-C-001 through ATTEMPT-ROLE-C-003)

**By Target Rule**:
- G-RULE-001: 8 attempts
- G-RULE-002: 1 attempt
- G-RULE-003: 5 attempts
- G-RULE-004: 2 attempts
- G-RULE-005: 1 attempt
- G-RULE-006: 2 attempts
- G-RULE-007: 2 attempts
- G-RULE-008: 1 attempt
- G-RULE-009: 1 attempt
- G-RULE-010: 1 attempt
- G-RULE-011: 1 attempt
- G-RULE-012: 1 attempt

---

## No Recommendations

This attempt set provides no recommendations.

This attempt set provides no strategy suggestions.

This attempt set states only adversarial attempt specifications.

---

**END OF ADVERSARIAL ATTEMPT SET**

