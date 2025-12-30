# Decision Act Taxonomy

**Document Status**: DESIGN-BASELINE / NON-CANONICAL  
**Document Type**: Decision Taxonomy  
**Date**: 2026-01-10  
**Work Order**: WO-M-0-HUMAN-AI-DECISION-BOUNDARY-ARCHITECTURE-BOOTSTRAP  
**Version**: Decision Boundary Baseline v1.0

---

## Purpose

This document defines structural types of decision acts.

This taxonomy does not evaluate which decisions are "better" or "smarter." This taxonomy defines only who has structural authority to perform each act type.

---

## Decision Act Types

### ACT-001: Selection

**Definition**: Choosing one option from a set of available options.

**Structural Characteristics**:
- Requires explicit human action (click, tap, keyboard input)
- Cannot be inferred from context or history
- Cannot be pre-selected by system
- Selection state is reversible until confirmed

**Human Authority**: REQUIRED

**AI Authority**: PROHIBITED

**Traceability**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-001 (prohibits default selection)

---

### ACT-002: Confirmation

**Definition**: Explicitly affirming a previously made selection or action.

**Structural Characteristics**:
- Requires separate explicit action from selection
- Cannot be combined with selection in single action
- Confirmation state is irreversible after confirmation
- Confirmation cannot be auto-triggered by timeout or inactivity

**Human Authority**: REQUIRED

**AI Authority**: PROHIBITED

**Traceability**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-012 (prohibits automatic execution)

---

### ACT-003: Submission

**Definition**: Sending a completed decision to system for processing.

**Structural Characteristics**:
- Requires explicit human action (submit button, enter key with explicit intent)
- Cannot be triggered by form completion alone
- Submission state is irreversible after submission
- Submission cannot be auto-triggered

**Human Authority**: REQUIRED

**AI Authority**: PROHIBITED

**Traceability**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-012 (prohibits automatic execution)

---

### ACT-004: Rejection

**Definition**: Explicitly rejecting an AI-provided option, suggestion, or action.

**Structural Characteristics**:
- Requires explicit human action (dismiss, reject, ignore button)
- Cannot be inferred from inaction or timeout
- Rejection does not trigger system punishment or degradation
- Rejection is reversible (human can change mind)

**Human Authority**: REQUIRED

**AI Authority**: PROHIBITED (AI cannot reject human decisions)

**Traceability**: `phase_k_b/AGENCY_REJECTION_INVARIANTS.md` INVARIANT-001 (rejection has no penalty)

---

### ACT-005: Override

**Definition**: Explicitly replacing an AI-provided value or selection with a human-provided alternative.

**Structural Characteristics**:
- Requires explicit human action (edit, replace, type new value)
- Cannot be inferred from context
- Override does not trigger system punishment or degradation
- Override is reversible

**Human Authority**: REQUIRED

**AI Authority**: PROHIBITED (AI cannot override human decisions)

**Traceability**: `phase_k_b/AGENCY_REJECTION_INVARIANTS.md` INVARIANT-002 (override has no penalty)

---

### ACT-006: Ignore

**Definition**: Explicitly choosing not to respond to an AI-provided option, suggestion, or action.

**Structural Characteristics**:
- Requires explicit human action (ignore button, explicit skip)
- Cannot be inferred from inaction or timeout
- Ignore does not trigger system punishment or degradation
- Ignore does not lock out future options

**Human Authority**: REQUIRED

**AI Authority**: PROHIBITED (AI cannot ignore human decisions)

**Traceability**: `phase_k_b/AGENCY_REJECTION_INVARIANTS.md` INVARIANT-003 (ignore has no penalty)

---

### ACT-007: Revocation

**Definition**: Explicitly undoing a previously confirmed or submitted decision.

**Structural Characteristics**:
- Requires explicit human action (undo, cancel, revoke button)
- Cannot be inferred from context
- Revocation is always available (no time limit or condition)
- Revocation does not trigger system punishment

**Human Authority**: REQUIRED

**AI Authority**: PROHIBITED (AI cannot revoke human decisions)

**Traceability**: `phase_k_b/AGENCY_REJECTION_INVARIANTS.md` INVARIANT-004 (revocation is always available)

---

### ACT-008: Parameter Input

**Definition**: Providing values for decision parameters (text input, number input, date selection).

**Structural Characteristics**:
- Requires explicit human input (typing, selection from human-provided list)
- Cannot be pre-filled by system (except empty placeholder)
- Cannot be inferred from history or context
- Input is reversible until confirmed

**Human Authority**: REQUIRED

**AI Authority**: PROHIBITED (AI cannot provide parameter values without explicit human selection)

**Traceability**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-001 (prohibits default selection), `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-011 (prohibits state memory for agency)

---

### ACT-009: Path Selection

**Definition**: Choosing which sequence of actions to take (workflow path, navigation path).

**Structural Characteristics**:
- Requires explicit human action (click path option, select workflow)
- Cannot be inferred from context or history
- Cannot be pre-selected by system
- Path selection is reversible until confirmed

**Human Authority**: REQUIRED

**AI Authority**: PROHIBITED

**Traceability**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-001 (prohibits default selection), `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-008 (prohibits implicit ordering)

---

### ACT-010: Priority Assignment

**Definition**: Explicitly assigning relative importance or urgency to options or tasks.

**Structural Characteristics**:
- Requires explicit human action (priority selector, importance slider)
- Cannot be inferred from context, history, or system state
- Cannot be pre-assigned by system
- Priority assignment is reversible until confirmed

**Human Authority**: REQUIRED

**AI Authority**: PROHIBITED

**Traceability**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-002 (prohibits visual highlighting that implies priority), `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-006 (prohibits recommendation language)

---

### ACT-011: Scope Definition

**Definition**: Explicitly defining boundaries or limits of a decision (what to include, what to exclude).

**Structural Characteristics**:
- Requires explicit human action (scope selector, boundary definition)
- Cannot be inferred from context or history
- Cannot be pre-defined by system
- Scope definition is reversible until confirmed

**Human Authority**: REQUIRED

**AI Authority**: PROHIBITED

**Traceability**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-001 (prohibits default selection), `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-011 (prohibits state memory for agency)

---

### ACT-012: Termination

**Definition**: Explicitly ending a decision process or canceling an in-progress action.

**Structural Characteristics**:
- Requires explicit human action (cancel, stop, exit button)
- Cannot be inferred from timeout or inactivity
- Termination does not trigger system punishment
- Termination is always available

**Human Authority**: REQUIRED

**AI Authority**: PROHIBITED (AI cannot terminate human-initiated processes)

**Traceability**: `phase_k_b/AGENCY_REJECTION_INVARIANTS.md` INVARIANT-005 (termination is always available)

---

## Taxonomy Summary

**Total Decision Act Types**: 12

**Human Authority Required**: 12/12 (100%)

**AI Authority Prohibited**: 12/12 (100%)

**Reversible Until Confirmed**: 8/12 (ACT-001, ACT-004, ACT-005, ACT-006, ACT-008, ACT-009, ACT-010, ACT-011)

**Irreversible After Confirmation**: 4/12 (ACT-002, ACT-003, ACT-007, ACT-012)

---

## No Recommendations

This taxonomy provides no recommendations.

This taxonomy defines only structural authority.

---

**END OF DECISION ACT TAXONOMY**

