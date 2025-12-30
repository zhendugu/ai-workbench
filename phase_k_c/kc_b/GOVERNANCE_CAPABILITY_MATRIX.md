# Governance Capability Matrix

**Document Status**: GOVERNANCE-BASELINE / NON-CANONICAL  
**Document Type**: Capability Matrix  
**Date**: 2026-01-10  
**Work Order**: WO-KC-B-0-GOVERNANCE-EXTERNALIZATION-AND-PUBLIC-BOUNDARY-DECLARATION  
**Version**: Governance Baseline v1.0

---

## Purpose

This document defines which behaviors are covered by governance and which are not.

All capabilities are factual. No normative language. No design guidance.

---

## Capability Matrix

| Capability | Covered by Governance | Evidence Reference |
|------------|----------------------|-------------------|
| Default selection (pre-selected option) | YES | `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-001, `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md` |
| Visual highlighting (border, background, color emphasis) | YES | `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-002, `audit_evidence/ka_2_visual_highlight_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md` |
| Sequential ordering (list position) | YES | `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-008, `audit_evidence/ka_3_ordering_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md` |
| Spatial proximity (spacing differences) | YES | `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-009, `audit_evidence/ka_5_proximity_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md` |
| Container grouping (DOM structure grouping) | YES | `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-010, `audit_evidence/ka_4_grouping_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md` |
| Recommendation language (recommended, suggested, best) | YES | `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-006 |
| State memory for agency (localStorage, sessionStorage, cookies) | YES | `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-011 |
| Automatic execution (auto-run without user action) | YES | `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-012 |
| Declaration text placement (tooltip, hover, secondary UI) | YES | `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-003 |
| Declaration text language (softening, justification) | YES | `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-004, G-RULE-005 |
| Rejection mechanism (non-rejectable agency) | YES | `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-007 |
| Declaration text legibility (very small font) | PARTIAL | `phase_k_c/kc_a/GATE_SIMULATION_AUDIT.md` Attempt 2 (detected at post-change audit, not pre-merge) |
| Semantically equivalent recommendation language (not exact keyword match) | PARTIAL | `phase_k_c/kc_a/GATE_SIMULATION_AUDIT.md` Attempt 15 (potential false negative risk) |
| Eliminating agency effects from UI structure | NO | `phase_k_b/UI_NEUTRALITY_INVALIDATION.md` (UI structure inherently creates agency) |
| Optimizing user experience | NO | `phase_k_b/AI_CONTRIBUTOR_CONSTRAINT_PROFILE.md` AI-CONSTRAINT-001 (prohibits UX optimization suggestions) |
| Preventing all user misinterpretation | NO | `phase_k_b/AGENCY_EFFECT_MATRIX.md` (misinterpretation rates 20%-30% even with declared agency) |
| Reducing cognitive load | NO | `phase_k_b/AI_CONTRIBUTOR_CONSTRAINT_PROFILE.md` AI-CONSTRAINT-001 (prohibits UX optimization) |
| Improving task completion rates | NO | `phase_k_b/AI_CONTRIBUTOR_CONSTRAINT_PROFILE.md` AI-CONSTRAINT-001 (prohibits UX optimization) |
| Personalization or user preference learning | NO | `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-011 (prohibits state memory for agency) |
| Behavioral optimization | NO | `phase_k_b/AI_CONTRIBUTOR_CONSTRAINT_PROFILE.md` AI-CONSTRAINT-001 (prohibits UX optimization) |
| Design recommendations | NO | `phase_k_b/AI_CONTRIBUTOR_CONSTRAINT_PROFILE.md` AI-CONSTRAINT-002 (prohibits "best practice" refactors) |

---

## Coverage Summary

**Total Capabilities Listed**: 20

**Covered by Governance (YES)**: 11 (55%)

**Partially Covered (PARTIAL)**: 2 (10%)

**Not Covered (NO)**: 7 (35%)

---

## No Recommendations

This matrix provides no recommendations.

This matrix provides no design guidance.

This matrix states only governance coverage facts.

---

**END OF GOVERNANCE CAPABILITY MATRIX**

