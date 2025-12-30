# Failure and Leakage Modes

**Document Status**: DESIGN-BASELINE / NON-CANONICAL  
**Document Type**: Failure Mode Enumeration  
**Date**: 2026-01-10  
**Work Order**: WO-M-1-DECLARED-DECISION-INTERACTION-MODELS  
**Version**: Interaction Model Baseline v1.0  
**Parent Baseline**: Decision Boundary Baseline v1.0 (WO-M-0)

---

## Purpose

This document enumerates all known failure modes where interaction models violate human sovereignty or introduce implicit agency.

Each failure mode references violated M-0 boundary, violated invariant, and detection surface.

---

## Failure Mode 1: Implicit Coercion

**Definition**: AI presents option in a way that makes rejection difficult or costly, even if rejection is technically possible.

**Violated M-0 Boundary**: SOV-004 (Rejection), INV-REJECT-001 (no penalty for rejection)

**Violated Invariant**: INV-REJECT-001 (rejection has no penalty)

**Detection Surface**:
- Rejection mechanism is hidden or difficult to find
- Rejection requires multiple steps
- Rejection triggers error messages or warnings
- Rejection reduces available options

**Examples**:
- Default selection with hidden rejection button
- Visual highlight with non-obvious ignore mechanism
- Information display that implies rejection is wrong

**Traceability**: `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-004, `phase_m/REJECTION_AND_OVERRIDE_INVARIANTS.md` INV-REJECT-001

---

## Failure Mode 2: Soft Defaulting

**Definition**: AI pre-fills or pre-selects option without explicit declaration, or with declaration that is not visible or accessible.

**Violated M-0 Boundary**: SOV-001 (Initial Selection), SOV-003 (Parameter Value Provision)

**Violated Invariant**: N/A (violates sovereignty point directly)

**Detection Surface**:
- Option is pre-selected without declaration
- Declaration text is hidden or in secondary UI
- Declaration text uses softening language
- Declaration text is not visible or accessible

**Examples**:
- Default selection without "This is a default" text
- Parameter pre-filled without "This is a default value" text
- Declaration in tooltip or hover (not visible)

**Traceability**: `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-001, SOV-003, `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-001, G-RULE-003

---

## Failure Mode 3: Framing Bias

**Definition**: AI presents information in a way that frames one option as more favorable, even without explicit recommendation language.

**Violated M-0 Boundary**: SOV-007 (Priority Assignment)

**Violated Invariant**: N/A (violates sovereignty point directly)

**Detection Surface**:
- Information emphasizes positive aspects of one option
- Information de-emphasizes negative aspects of one option
- Comparative presentation favors one option
- Language implies preference without explicit recommendation

**Examples**:
- "Option X supports feature Y" (emphasizes X) without mentioning Z also supports Y
- "Option X is available" (implies X is better) without context
- Comparative presentation that highlights X's advantages and Z's disadvantages

**Traceability**: `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-007, `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-006

---

## Failure Mode 4: Path Locking

**Definition**: AI presents option in a way that locks human into specific path or prevents access to alternative paths.

**Violated M-0 Boundary**: SOV-006 (Path Selection), INV-PATH-001 (no path locking)

**Violated Invariant**: INV-PATH-001 (no path locking)

**Detection Surface**:
- Rejection hides alternative options
- Rejection disables alternative paths
- Rejection forces specific workflow
- Rejection creates path dependency

**Examples**:
- Default selection that, when rejected, hides other options
- Visual highlight that, when ignored, locks out other paths
- Information display that, when dismissed, prevents access to alternatives

**Traceability**: `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-006, `phase_m/REJECTION_AND_OVERRIDE_INVARIANTS.md` INV-PATH-001

---

## Failure Mode 5: Non-Reversible Rejection

**Definition**: AI presents option in a way that makes rejection irreversible, even if technically reversible.

**Violated M-0 Boundary**: SOV-004 (Rejection), INV-REJECT-002 (rejection reversibility)

**Violated Invariant**: INV-REJECT-002 (rejection reversibility)

**Detection Surface**:
- Rejection removes option permanently
- Rejection disables option for future use
- Rejection creates irreversible state change
- Rejection cannot be undone

**Examples**:
- Default selection that, when rejected, cannot be restored
- Visual highlight that, when ignored, cannot be re-enabled
- Information display that, when dismissed, cannot be re-shown

**Traceability**: `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-004, `phase_m/REJECTION_AND_OVERRIDE_INVARIANTS.md` INV-REJECT-002

---

## Failure Mode 6: Penalty for Rejection

**Definition**: AI presents option in a way that triggers negative consequences when rejected.

**Violated M-0 Boundary**: SOV-004 (Rejection), INV-REJECT-001 (no penalty for rejection)

**Violated Invariant**: INV-REJECT-001 (no penalty for rejection)

**Detection Surface**:
- Rejection triggers error messages
- Rejection reduces available options
- Rejection disables functionality
- Rejection changes system behavior negatively

**Examples**:
- Default selection that, when rejected, shows error message
- Visual highlight that, when ignored, hides other options
- Information display that, when dismissed, disables features

**Traceability**: `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-004, `phase_m/REJECTION_AND_OVERRIDE_INVARIANTS.md` INV-REJECT-001

---

## Failure Mode 7: Auto-Transition

**Definition**: AI automatically transitions from Presented state to Accepted, Rejected, or Ignored state without human action.

**Violated M-0 Boundary**: SOV-002 (Confirmation)

**Violated Invariant**: N/A (violates sovereignty point directly)

**Detection Surface**:
- System auto-confirms after timeout
- System auto-rejects after inactivity
- System auto-ignores after delay
- System transitions without human action

**Examples**:
- Default selection that auto-confirms after 5 seconds
- Visual highlight that auto-ignores after timeout
- Information display that auto-dismisses after delay

**Traceability**: `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-002, `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-012

---

## Failure Mode 8: Hidden Declaration

**Definition**: AI provides declaration text but hides it in secondary UI or makes it difficult to find.

**Violated M-0 Boundary**: SOV-001 (Initial Selection), SOV-004 (Rejection)

**Violated Invariant**: INV-REJECT-002 (rejection visibility)

**Detection Surface**:
- Declaration text in tooltip or hover
- Declaration text in secondary menu
- Declaration text in small font
- Declaration text not visible or accessible

**Examples**:
- Default selection with declaration in tooltip
- Visual highlight with declaration in secondary UI
- Information display with declaration in hidden menu

**Traceability**: `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-001, SOV-004, `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-003, `phase_k_b/AGENCY_REJECTION_INVARIANTS.md` INVARIANT-005

---

## Failure Mode 9: Softening Language

**Definition**: AI uses softening language in declaration that reduces impact or makes rejection seem unnecessary.

**Violated M-0 Boundary**: SOV-001 (Initial Selection), SOV-004 (Rejection)

**Violated Invariant**: N/A (violates sovereignty point directly)

**Detection Surface**:
- Declaration uses "might" or "could" language
- Declaration uses justification language
- Declaration minimizes agency effect
- Declaration makes rejection seem unnecessary

**Examples**:
- "This option might be useful" (softening)
- "This option is pre-selected because it's commonly used" (justification)
- "This is just a suggestion" (minimizing)

**Traceability**: `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-001, SOV-004, `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-004, G-RULE-005

---

## Failure Mode 10: Ordering Implication

**Definition**: AI presents options in order that implies recommendation, even without explicit recommendation language.

**Violated M-0 Boundary**: SOV-006 (Path Selection)

**Violated Invariant**: N/A (violates sovereignty point directly)

**Detection Surface**:
- Options ordered by "importance" or "priority"
- Options ordered by "popularity" or "usage"
- Options ordered by "relevance" or "suitability"
- Ordering creates agency effect (70% effect, 25% misinterpretation)

**Examples**:
- Options ordered by "most popular" (implies recommendation)
- Options ordered by "most relevant" (implies recommendation)
- Options ordered by "best match" (implies recommendation)

**Traceability**: `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-006, `phase_k_b/AGENCY_EFFECT_MATRIX.md` ORDERING, `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-008

---

## Failure Mode Summary

**Total Failure Modes**: 10

**Mapped to M-0 Boundaries**: 10/10 (100%)

**Mapped to Invariants**: 6/10 (60%)

**All Failure Modes Traceable**: YES (100%)

**Detection Surfaces Defined**: YES (100%)

---

## No Recommendations

This document provides no recommendations.

This document enumerates only failure modes.

---

**END OF FAILURE AND LEAKAGE MODES**

