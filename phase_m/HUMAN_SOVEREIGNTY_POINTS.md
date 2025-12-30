# Human Sovereignty Points

**Document Status**: DESIGN-BASELINE / NON-CANONICAL  
**Document Type**: Sovereignty Definition  
**Date**: 2026-01-10  
**Work Order**: WO-M-0-HUMAN-AI-DECISION-BOUNDARY-ARCHITECTURE-BOOTSTRAP  
**Version**: Decision Boundary Baseline v1.0

---

## Purpose

This document defines points in system interaction where human authority is structurally required and cannot be automated or bypassed.

Each sovereignty point includes: structural requirement, non-automatable reason, non-bypassable condition.

---

## Sovereignty Point 1: Initial Selection

**Point ID**: SOV-001

**Definition**: The first selection of an option from a set of available options.

**Structural Requirement**: Human must explicitly select an option. System cannot pre-select.

**Non-Automatable Reason**: Pre-selection creates agency effect (60% path convergence, 20% misinterpretation as system recommendation). Evidence: `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Non-Bypassable Condition**: No option can be selected by system before human explicit action. No default selection allowed.

**Traceability**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-001, `phase_k_b/AGENCY_EFFECT_MATRIX.md` DEFAULT_SELECTION

---

## Sovereignty Point 2: Confirmation

**Point ID**: SOV-002

**Definition**: Explicit confirmation of a selection before irreversible state change.

**Structural Requirement**: Human must explicitly confirm selection. System cannot auto-confirm.

**Non-Automatable Reason**: Auto-confirmation removes human control over irreversible state changes. Confirmation must be separate action from selection.

**Non-Bypassable Condition**: No state change can occur without explicit human confirmation. No timeout-based confirmation. No inactivity-based confirmation.

**Traceability**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-012 (prohibits automatic execution)

---

## Sovereignty Point 3: Parameter Value Provision

**Point ID**: SOV-003

**Definition**: Providing values for decision parameters (text, numbers, dates, selections).

**Structural Requirement**: Human must explicitly provide parameter values. System cannot pre-fill (except empty placeholder).

**Non-Automatable Reason**: Pre-filled values create agency effect (default selection). System cannot infer human intent from history or context.

**Non-Bypassable Condition**: No parameter can be pre-filled with non-empty value. No history-based auto-fill. No context-based inference.

**Traceability**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-001 (prohibits default selection), `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-011 (prohibits state memory for agency)

---

## Sovereignty Point 4: Rejection

**Point ID**: SOV-004

**Definition**: Explicit rejection of AI-provided option, suggestion, or action.

**Structural Requirement**: Human must be able to reject any AI-provided option without penalty.

**Non-Automatable Reason**: Rejection is human decision. System cannot reject on behalf of human. Rejection must be explicit action, not inferred from inaction.

**Non-Bypassable Condition**: Rejection must always be available. Rejection cannot trigger system punishment, degradation, or path locking. Rejection is reversible.

**Traceability**: `phase_k_b/AGENCY_REJECTION_INVARIANTS.md` INVARIANT-001 (rejection has no penalty), INVARIANT-002 (rejection is reversible)

---

## Sovereignty Point 5: Override

**Point ID**: SOV-005

**Definition**: Explicit replacement of AI-provided value with human-provided alternative.

**Structural Requirement**: Human must be able to override any AI-provided value without penalty.

**Non-Automatable Reason**: Override is human decision. System cannot override on behalf of human. Override must be explicit action.

**Non-Bypassable Condition**: Override must always be available. Override cannot trigger system punishment or degradation. Override is reversible.

**Traceability**: `phase_k_b/AGENCY_REJECTION_INVARIANTS.md` INVARIANT-002 (override has no penalty), INVARIANT-003 (override is reversible)

---

## Sovereignty Point 6: Path Selection

**Point ID**: SOV-006

**Definition**: Choosing which sequence of actions to take (workflow path, navigation path).

**Structural Requirement**: Human must explicitly select path. System cannot pre-select or recommend path.

**Non-Automatable Reason**: Path pre-selection creates agency effect (ordering bias: 70% effect, 25% misinterpretation). Evidence: `audit_evidence/ka_3_ordering_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Non-Bypassable Condition**: No path can be pre-selected. No path can be recommended. All paths must be equally accessible.

**Traceability**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-008 (prohibits implicit ordering), `phase_k_b/AGENCY_EFFECT_MATRIX.md` ORDERING

---

## Sovereignty Point 7: Priority Assignment

**Point ID**: SOV-007

**Definition**: Explicitly assigning relative importance or urgency to options or tasks.

**Structural Requirement**: Human must explicitly assign priority. System cannot infer or pre-assign priority.

**Non-Automatable Reason**: Priority inference creates agency effect (visual highlighting: 55% effect, 30% misinterpretation). Evidence: `audit_evidence/ka_2_visual_highlight_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Non-Bypassable Condition**: No priority can be inferred from context, history, or system state. No visual highlighting that implies priority. No recommendation language.

**Traceability**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-002 (prohibits visual highlighting), G-RULE-006 (prohibits recommendation language)

---

## Sovereignty Point 8: Scope Definition

**Point ID**: SOV-008

**Definition**: Explicitly defining boundaries or limits of a decision (what to include, what to exclude).

**Structural Requirement**: Human must explicitly define scope. System cannot infer or pre-define scope.

**Non-Automatable Reason**: Scope inference creates agency effect (grouping: 65% effect, 30% misinterpretation). Evidence: `audit_evidence/ka_4_grouping_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Non-Bypassable Condition**: No scope can be inferred from context or history. No grouping that implies scope. No state memory for scope.

**Traceability**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-010 (prohibits unacknowledged grouping), G-RULE-011 (prohibits state memory for agency)

---

## Sovereignty Point 9: Termination

**Point ID**: SOV-009

**Definition**: Explicitly ending a decision process or canceling an in-progress action.

**Structural Requirement**: Human must be able to terminate any process at any time without penalty.

**Non-Automatable Reason**: Termination is human decision. System cannot terminate on behalf of human. Termination must be explicit action.

**Non-Bypassable Condition**: Termination must always be available. Termination cannot trigger system punishment. No process can be non-terminable.

**Traceability**: `phase_k_b/AGENCY_REJECTION_INVARIANTS.md` INVARIANT-005 (termination is always available)

---

## Sovereignty Point 10: Revocation

**Point ID**: SOV-010

**Definition**: Explicitly undoing a previously confirmed or submitted decision.

**Structural Requirement**: Human must be able to revoke any decision at any time (no time limit or condition).

**Non-Automatable Reason**: Revocation is human decision. System cannot revoke on behalf of human. Revocation must be explicit action.

**Non-Bypassable Condition**: Revocation must always be available. Revocation cannot trigger system punishment. No decision can be non-revocable.

**Traceability**: `phase_k_b/AGENCY_REJECTION_INVARIANTS.md` INVARIANT-004 (revocation is always available)

---

## Sovereignty Summary

**Total Sovereignty Points**: 10

**Human Authority Required**: 10/10 (100%)

**Non-Automatable**: 10/10 (100%)

**Non-Bypassable**: 10/10 (100%)

**Traceability**: All points traceable to Phase K evidence

---

## No Recommendations

This document provides no recommendations.

This document defines only structural sovereignty requirements.

---

**END OF HUMAN SOVEREIGNTY POINTS**

