# Declared Decision Interaction Catalog

**Document Status**: DESIGN-BASELINE / NON-CANONICAL  
**Document Type**: Interaction Model Catalog  
**Date**: 2026-01-10  
**Work Order**: WO-M-1-DECLARED-DECISION-INTERACTION-MODELS  
**Version**: Interaction Model Baseline v1.0  
**Parent Baseline**: Decision Boundary Baseline v1.0 (WO-M-0)

---

## Purpose

This document defines all permitted declared decision interaction models between Human and AI.

Each model ensures AI participation without crossing Human Sovereignty Points defined in Phase M-0.

---

## Interaction Model 1: Preview-Only Presentation

**Interaction ID**: DIM-001

**Definition**: AI presents information or data without any selection, highlighting, or ordering that implies preference.

**Human Action Required**: ACT-001 (Selection), ACT-008 (Parameter Input)

**AI Action Type**: Non-Decision Action (Display Rendering)

**Explicit Non-Decision Assertion**: "This display does not imply preference, recommendation, or default selection."

**Entry Conditions**:
- Human has initiated decision process
- Human has not yet made selection
- No AI-provided default selection exists

**Exit Conditions**:
- Human makes explicit selection (ACT-001)
- Human provides parameter input (ACT-008)
- Human terminates process (ACT-012)

**Reversibility Guarantees**:
- Human can change selection at any time before confirmation
- Human can modify parameter input at any time before confirmation
- No selection state is locked

**Prohibited Variants**:
- Pre-selected option (violates SOV-001)
- Visual highlighting that implies priority (violates SOV-007)
- Ordering that implies recommendation (violates SOV-006)
- Default parameter values (violates SOV-003)

**Mapped Sovereignty Points**: SOV-001, SOV-003, SOV-006, SOV-007

**Traceability**: `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-001, SOV-003, SOV-006, SOV-007

---

## Interaction Model 2: Declared Default Selection

**Interaction ID**: DIM-002

**Definition**: AI pre-selects an option with explicit declaration that it is a default and can be changed.

**Human Action Required**: ACT-001 (Selection), ACT-004 (Rejection), ACT-005 (Override)

**AI Action Type**: Advisory Action (Declared Default Selection)

**Explicit Non-Decision Assertion**: "This option is pre-selected as a default. You can change it."

**Entry Conditions**:
- Human has initiated decision process
- AI has declared default selection with canonical disclosure language
- Rejection mechanism is visible and accessible

**Exit Conditions**:
- Human accepts default (ACT-001, no change)
- Human rejects default and selects alternative (ACT-004, ACT-001)
- Human overrides default with different value (ACT-005)
- Human terminates process (ACT-012)

**Reversibility Guarantees**:
- Human can reject default at any time before confirmation
- Human can override default at any time before confirmation
- Rejection is reversible (human can restore default)
- Override is reversible (human can revert to default)

**Prohibited Variants**:
- Undeclared default selection (violates SOV-001)
- Non-rejectable default (violates INV-REJECT-001)
- Default with penalty for rejection (violates INV-REJECT-001)
- Hidden rejection mechanism (violates INV-REJECT-002)

**Mapped Sovereignty Points**: SOV-001, SOV-004, SOV-005

**Traceability**: `phase_k_b/DECLARED_AGENCY_PATTERN_CATALOG.md` PATTERN-DECLARED-DEFAULT-SELECTION, `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-001, SOV-004, SOV-005

---

## Interaction Model 3: Declared Visual Highlight

**Interaction ID**: DIM-003

**Definition**: AI visually highlights an option with explicit declaration that it is highlighted and can be ignored.

**Human Action Required**: ACT-001 (Selection), ACT-004 (Rejection), ACT-006 (Ignore)

**AI Action Type**: Advisory Action (Declared Visual Highlight)

**Explicit Non-Decision Assertion**: "This option is visually highlighted. You can ignore it and select any option."

**Entry Conditions**:
- Human has initiated decision process
- AI has declared visual highlight with canonical disclosure language
- Rejection/ignore mechanism is visible and accessible

**Exit Conditions**:
- Human selects highlighted option (ACT-001)
- Human selects non-highlighted option (ACT-001, ACT-006)
- Human rejects highlight (ACT-004)
- Human terminates process (ACT-012)

**Reversibility Guarantees**:
- Human can ignore highlight at any time
- Human can reject highlight at any time
- Ignore is reversible (human can later select highlighted option)
- Rejection is reversible (human can later accept highlight)

**Prohibited Variants**:
- Undeclared visual highlight (violates SOV-007)
- Non-ignorable highlight (violates INV-REJECT-001)
- Highlight with penalty for ignoring (violates INV-REJECT-001)
- Hidden ignore mechanism (violates INV-REJECT-002)

**Mapped Sovereignty Points**: SOV-001, SOV-004, SOV-006, SOV-007

**Traceability**: `phase_k_b/DECLARED_AGENCY_PATTERN_CATALOG.md` PATTERN-DECLARED-VISUAL-HIGHLIGHT, `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-001, SOV-004, SOV-006, SOV-007

---

## Interaction Model 4: Information Display

**Interaction ID**: DIM-004

**Definition**: AI displays information about options (descriptions, metadata, context) without implying preference.

**Human Action Required**: ACT-001 (Selection), ACT-008 (Parameter Input)

**AI Action Type**: Advisory Action (Information Display)

**Explicit Non-Decision Assertion**: "This information does not imply recommendation or preference."

**Entry Conditions**:
- Human has initiated decision process
- Human has not yet made selection
- Information is factually accurate

**Exit Conditions**:
- Human makes explicit selection (ACT-001)
- Human provides parameter input (ACT-008)
- Human terminates process (ACT-012)

**Reversibility Guarantees**:
- Human can change selection at any time before confirmation
- Human can modify parameter input at any time before confirmation
- No selection state is locked

**Prohibited Variants**:
- Recommendation language (violates SOV-007)
- Priority assertions (violates SOV-007)
- Optimization claims (violates SOV-007)
- "Best" or "Recommended" phrasing (violates SOV-007)

**Mapped Sovereignty Points**: SOV-001, SOV-003, SOV-007

**Traceability**: `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-001, SOV-003, SOV-007, `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-006

---

## Interaction Model 5: Validation Feedback

**Interaction ID**: DIM-005

**Definition**: AI provides validation feedback on human input (format errors, constraint violations) without implying recommendation.

**Human Action Required**: ACT-008 (Parameter Input), ACT-005 (Override)

**AI Action Type**: Advisory Action (Validation Feedback)

**Explicit Non-Decision Assertion**: "This validation feedback does not imply recommendation or preference."

**Entry Conditions**:
- Human has provided parameter input
- Input violates format or constraint
- Validation feedback is factually accurate

**Exit Conditions**:
- Human corrects input (ACT-008, ACT-005)
- Human overrides validation (ACT-005, if override allowed)
- Human terminates process (ACT-012)

**Reversibility Guarantees**:
- Human can correct input at any time
- Human can override validation if override is allowed
- Override is reversible (human can revert to validated input)

**Prohibited Variants**:
- Recommendation language in error messages (violates SOV-007)
- Penalty for validation failure (violates INV-OVERRIDE-001)
- Non-overridable validation (violates INV-OVERRIDE-002)
- Hidden override mechanism (violates INV-OVERRIDE-002)

**Mapped Sovereignty Points**: SOV-003, SOV-005, SOV-007

**Traceability**: `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-003, SOV-005, SOV-007, `phase_m/REJECTION_AND_OVERRIDE_INVARIANTS.md` INV-OVERRIDE-001, INV-OVERRIDE-002

---

## Interaction Model 6: Comparative Presentation

**Interaction ID**: DIM-006

**Definition**: AI presents multiple options side-by-side with factual comparison data, without implying preference.

**Human Action Required**: ACT-001 (Selection)

**AI Action Type**: Advisory Action (Information Display)

**Explicit Non-Decision Assertion**: "This comparison does not imply recommendation or preference."

**Entry Conditions**:
- Human has initiated decision process
- Multiple options are available
- Comparison data is factually accurate

**Exit Conditions**:
- Human makes explicit selection (ACT-001)
- Human terminates process (ACT-012)

**Reversibility Guarantees**:
- Human can change selection at any time before confirmation
- No selection state is locked

**Prohibited Variants**:
- Recommendation language (violates SOV-007)
- Priority assertions (violates SOV-007)
- Visual highlighting that implies preference (violates SOV-007)
- Ordering that implies recommendation (violates SOV-006)

**Mapped Sovereignty Points**: SOV-001, SOV-006, SOV-007

**Traceability**: `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-001, SOV-006, SOV-007, `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-006, G-RULE-008

---

## Interaction Model 7: Option Expansion

**Interaction ID**: DIM-007

**Definition**: AI presents additional options or expands option set without implying preference for any option.

**Human Action Required**: ACT-001 (Selection), ACT-011 (Scope Definition)

**AI Action Type**: Non-Decision Action (Data Retrieval)

**Explicit Non-Decision Assertion**: "These additional options do not imply recommendation or preference."

**Entry Conditions**:
- Human has initiated decision process
- Additional options are available
- No option is pre-selected or highlighted

**Exit Conditions**:
- Human makes explicit selection (ACT-001)
- Human defines scope (ACT-011)
- Human terminates process (ACT-012)

**Reversibility Guarantees**:
- Human can change selection at any time before confirmation
- Human can modify scope at any time before confirmation
- No selection state is locked

**Prohibited Variants**:
- Pre-selected option in expanded set (violates SOV-001)
- Visual highlighting that implies preference (violates SOV-007)
- Ordering that implies recommendation (violates SOV-006)
- Scope inference (violates SOV-008)

**Mapped Sovereignty Points**: SOV-001, SOV-006, SOV-007, SOV-008, SOV-011

**Traceability**: `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-001, SOV-006, SOV-007, SOV-008, SOV-011

---

## Interaction Model 8: Confirmation Request

**Interaction ID**: DIM-008

**Definition**: AI requests explicit human confirmation before executing irreversible action.

**Human Action Required**: ACT-002 (Confirmation), ACT-004 (Rejection), ACT-012 (Termination)

**AI Action Type**: Advisory Action (Information Display)

**Explicit Non-Decision Assertion**: "This confirmation request does not imply recommendation. You can confirm, reject, or terminate."

**Entry Conditions**:
- Human has made selection
- Action requires confirmation (irreversible state change)
- Confirmation request is explicit and visible

**Exit Conditions**:
- Human confirms (ACT-002)
- Human rejects (ACT-004)
- Human terminates (ACT-012)

**Reversibility Guarantees**:
- Human can reject confirmation at any time before confirmation
- Human can terminate at any time before confirmation
- Rejection is reversible (human can re-initiate process)
- Termination is reversible (human can restart process)

**Prohibited Variants**:
- Auto-confirmation (violates SOV-002)
- Timeout-based confirmation (violates SOV-002)
- Non-rejectable confirmation (violates INV-REJECT-001)
- Penalty for rejection (violates INV-REJECT-001)

**Mapped Sovereignty Points**: SOV-002, SOV-004, SOV-009, SOV-012

**Traceability**: `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-002, SOV-004, SOV-009, SOV-012, `phase_m/REJECTION_AND_OVERRIDE_INVARIANTS.md` INV-REJECT-001

---

## Catalog Summary

**Total Interaction Models**: 8

**Non-Decision Actions**: 2 (DIM-001, DIM-007)

**Advisory Actions**: 6 (DIM-002, DIM-003, DIM-004, DIM-005, DIM-006, DIM-008)

**Prohibited Actions**: 0

**All Models Mapped to Sovereignty Points**: YES (100%)

**All Models Have Reversibility Guarantees**: YES (100%)

**All Models Have Explicit Non-Decision Assertions**: YES (100%)

---

## No Recommendations

This catalog provides no recommendations.

This catalog defines only structural interaction models.

---

**END OF DECLARED DECISION INTERACTION CATALOG**

