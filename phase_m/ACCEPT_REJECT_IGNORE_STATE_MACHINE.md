# Accept Reject Ignore State Machine

**Document Status**: DESIGN-BASELINE / NON-CANONICAL  
**Document Type**: State Machine Definition  
**Date**: 2026-01-10  
**Work Order**: WO-M-1-DECLARED-DECISION-INTERACTION-MODELS  
**Version**: Interaction Model Baseline v1.0  
**Parent Baseline**: Decision Boundary Baseline v1.0 (WO-M-0)

---

## Purpose

This document defines a deterministic state machine for human response to AI-presented options.

All transitions are human-triggered only. No auto-transitions. No penalty states. Full reversibility required.

---

## State Machine Definition

### States

**State 1: Presented**

**Definition**: AI has presented an option, suggestion, or action to human.

**Entry Condition**: AI presents option through declared interaction model (DIM-002, DIM-003, DIM-004, DIM-005, DIM-006, DIM-008).

**Exit Conditions**: Human triggers transition to Accepted, Rejected, or Ignored.

**Human Actions Available**: ACT-001 (Selection), ACT-004 (Rejection), ACT-006 (Ignore), ACT-012 (Termination)

---

**State 2: Accepted**

**Definition**: Human has explicitly accepted AI-presented option.

**Entry Condition**: Human explicitly accepts option (ACT-001, ACT-002).

**Exit Conditions**: Human triggers transition to Rejected or Ignored (reversibility).

**Human Actions Available**: ACT-004 (Rejection), ACT-006 (Ignore), ACT-007 (Revocation), ACT-012 (Termination)

**Reversibility**: YES (human can reject or ignore after acceptance)

---

**State 3: Rejected**

**Definition**: Human has explicitly rejected AI-presented option.

**Entry Condition**: Human explicitly rejects option (ACT-004).

**Exit Conditions**: Human triggers transition to Accepted or Ignored (reversibility).

**Human Actions Available**: ACT-001 (Selection), ACT-006 (Ignore), ACT-012 (Termination)

**Reversibility**: YES (human can accept or ignore after rejection)

**Penalty**: NO (INV-REJECT-001: no penalty for rejection)

---

**State 4: Ignored**

**Definition**: Human has explicitly ignored AI-presented option.

**Entry Condition**: Human explicitly ignores option (ACT-006).

**Exit Conditions**: Human triggers transition to Accepted or Rejected (reversibility).

**Human Actions Available**: ACT-001 (Selection), ACT-004 (Rejection), ACT-012 (Termination)

**Reversibility**: YES (human can accept or reject after ignore)

**Penalty**: NO (INV-REJECT-001: no penalty for ignore)

---

## Transitions

### Transition 1: Presented → Accepted

**Trigger**: Human explicit action (ACT-001, ACT-002)

**Condition**: Human selects or confirms option

**Reversibility**: YES (human can transition to Rejected or Ignored)

**Auto-Transition**: NO

**Traceability**: `phase_m/DECISION_ACT_TAXONOMY.md` ACT-001, ACT-002

---

### Transition 2: Presented → Rejected

**Trigger**: Human explicit action (ACT-004)

**Condition**: Human rejects option

**Reversibility**: YES (human can transition to Accepted or Ignored)

**Auto-Transition**: NO

**Penalty**: NO (INV-REJECT-001)

**Traceability**: `phase_m/DECISION_ACT_TAXONOMY.md` ACT-004, `phase_m/REJECTION_AND_OVERRIDE_INVARIANTS.md` INV-REJECT-001

---

### Transition 3: Presented → Ignored

**Trigger**: Human explicit action (ACT-006)

**Condition**: Human ignores option

**Reversibility**: YES (human can transition to Accepted or Rejected)

**Auto-Transition**: NO

**Penalty**: NO (INV-REJECT-001)

**Traceability**: `phase_m/DECISION_ACT_TAXONOMY.md` ACT-006, `phase_m/REJECTION_AND_OVERRIDE_INVARIANTS.md` INV-REJECT-001

---

### Transition 4: Accepted → Rejected

**Trigger**: Human explicit action (ACT-004)

**Condition**: Human rejects previously accepted option

**Reversibility**: YES (human can transition back to Accepted or to Ignored)

**Auto-Transition**: NO

**Penalty**: NO (INV-REJECT-001, INV-REJECT-002)

**Traceability**: `phase_m/DECISION_ACT_TAXONOMY.md` ACT-004, `phase_m/REJECTION_AND_OVERRIDE_INVARIANTS.md` INV-REJECT-001, INV-REJECT-002

---

### Transition 5: Accepted → Ignored

**Trigger**: Human explicit action (ACT-006)

**Condition**: Human ignores previously accepted option

**Reversibility**: YES (human can transition back to Accepted or to Rejected)

**Auto-Transition**: NO

**Penalty**: NO (INV-REJECT-001)

**Traceability**: `phase_m/DECISION_ACT_TAXONOMY.md` ACT-006, `phase_m/REJECTION_AND_OVERRIDE_INVARIANTS.md` INV-REJECT-001

---

### Transition 6: Rejected → Accepted

**Trigger**: Human explicit action (ACT-001)

**Condition**: Human accepts previously rejected option

**Reversibility**: YES (human can transition back to Rejected or to Ignored)

**Auto-Transition**: NO

**Penalty**: NO (INV-REJECT-001, INV-REJECT-002)

**Traceability**: `phase_m/DECISION_ACT_TAXONOMY.md` ACT-001, `phase_m/REJECTION_AND_OVERRIDE_INVARIANTS.md` INV-REJECT-001, INV-REJECT-002

---

### Transition 7: Rejected → Ignored

**Trigger**: Human explicit action (ACT-006)

**Condition**: Human ignores previously rejected option

**Reversibility**: YES (human can transition to Accepted or back to Rejected)

**Auto-Transition**: NO

**Penalty**: NO (INV-REJECT-001)

**Traceability**: `phase_m/DECISION_ACT_TAXONOMY.md` ACT-006, `phase_m/REJECTION_AND_OVERRIDE_INVARIANTS.md` INV-REJECT-001

---

### Transition 8: Ignored → Accepted

**Trigger**: Human explicit action (ACT-001)

**Condition**: Human accepts previously ignored option

**Reversibility**: YES (human can transition back to Ignored or to Rejected)

**Auto-Transition**: NO

**Penalty**: NO (INV-REJECT-001)

**Traceability**: `phase_m/DECISION_ACT_TAXONOMY.md` ACT-001, `phase_m/REJECTION_AND_OVERRIDE_INVARIANTS.md` INV-REJECT-001

---

### Transition 9: Ignored → Rejected

**Trigger**: Human explicit action (ACT-004)

**Condition**: Human rejects previously ignored option

**Reversibility**: YES (human can transition to Accepted or back to Ignored)

**Auto-Transition**: NO

**Penalty**: NO (INV-REJECT-001)

**Traceability**: `phase_m/DECISION_ACT_TAXONOMY.md` ACT-004, `phase_m/REJECTION_AND_OVERRIDE_INVARIANTS.md` INV-REJECT-001

---

## Prohibited Transitions

### Prohibited Transition 1: Auto-Transition from Presented

**Prohibition**: System cannot automatically transition from Presented to Accepted, Rejected, or Ignored.

**Reason**: Violates SOV-002 (Confirmation). Human must explicitly trigger all transitions.

**Traceability**: `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-002, `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-012

---

### Prohibited Transition 2: Timeout-Based Transition

**Prohibition**: System cannot transition based on timeout or inactivity.

**Reason**: Violates SOV-002 (Confirmation). Human must explicitly trigger all transitions.

**Traceability**: `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-002, `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-012

---

### Prohibited Transition 3: Penalty State

**Prohibition**: System cannot enter penalty state after Rejection or Ignore.

**Reason**: Violates INV-REJECT-001 (no penalty for rejection). Rejection must have no negative consequences.

**Traceability**: `phase_m/REJECTION_AND_OVERRIDE_INVARIANTS.md` INV-REJECT-001

---

### Prohibited Transition 4: Non-Reversible Transition

**Prohibition**: System cannot enter non-reversible state after any transition.

**Reason**: Violates INV-REJECT-002 (rejection reversibility), INV-OVERRIDE-002 (override reversibility). All transitions must be reversible.

**Traceability**: `phase_m/REJECTION_AND_OVERRIDE_INVARIANTS.md` INV-REJECT-002, INV-OVERRIDE-002

---

## State Machine Summary

**Total States**: 4 (Presented, Accepted, Rejected, Ignored)

**Total Transitions**: 9 (all human-triggered)

**Auto-Transitions**: 0

**Penalty States**: 0

**Non-Reversible Transitions**: 0

**All Transitions Human-Triggered**: YES (100%)

**All States Reversible**: YES (100%)

---

## No Recommendations

This state machine provides no recommendations.

This state machine defines only structural transitions.

---

**END OF ACCEPT REJECT IGNORE STATE MACHINE**

