# Interaction Model Classification

**Document Status**: DESIGN-BASELINE / NON-CANONICAL  
**Document Type**: Classification System  
**Date**: 2026-01-10  
**Work Order**: WO-M-1-DECLARED-DECISION-INTERACTION-MODELS  
**Version**: Interaction Model Baseline v1.0  
**Parent Baseline**: Decision Boundary Baseline v1.0 (WO-M-0)

---

## Purpose

This document classifies interaction models into four categories: Preview-only, Advisory-with-confirmation, Comparative-presentation, Option-expansion.

Hybrid or ambiguous models are explicitly prohibited.

---

## Classification 1: Preview-Only

**Definition**: AI presents information or data without any selection, highlighting, or ordering that implies preference.

**Characteristics**:
- No AI-provided default selection
- No visual highlighting
- No ordering that implies recommendation
- No parameter pre-filling
- Human makes all decisions

**Interaction Models**:
- DIM-001: Preview-Only Presentation

**AI Action Type**: Non-Decision Action

**Human Action Required**: ACT-001 (Selection), ACT-008 (Parameter Input)

**Prohibited Hybrids**:
- Preview with default selection (becomes Advisory-with-confirmation)
- Preview with visual highlight (becomes Advisory-with-confirmation)
- Preview with ordering (becomes Comparative-presentation)

**Traceability**: `phase_m/DECLARED_DECISION_INTERACTION_CATALOG.md` DIM-001

---

## Classification 2: Advisory-with-confirmation

**Definition**: AI provides advisory input (default selection, visual highlight, information) that requires explicit human confirmation.

**Characteristics**:
- AI provides advisory input with explicit declaration
- Human can accept, reject, override, or ignore
- Rejection/override has no penalty
- Rejection/override is reversible
- Human retains final decision authority

**Interaction Models**:
- DIM-002: Declared Default Selection
- DIM-003: Declared Visual Highlight
- DIM-004: Information Display
- DIM-005: Validation Feedback
- DIM-008: Confirmation Request

**AI Action Type**: Advisory Action

**Human Action Required**: ACT-001 (Selection), ACT-002 (Confirmation), ACT-004 (Rejection), ACT-005 (Override), ACT-006 (Ignore)

**Prohibited Hybrids**:
- Advisory without declaration (becomes Prohibited Action)
- Advisory without rejection mechanism (becomes Prohibited Action)
- Advisory with penalty for rejection (becomes Prohibited Action)
- Advisory with non-reversible rejection (becomes Prohibited Action)

**Traceability**: `phase_m/DECLARED_DECISION_INTERACTION_CATALOG.md` DIM-002, DIM-003, DIM-004, DIM-005, DIM-008

---

## Classification 3: Comparative-presentation

**Definition**: AI presents multiple options side-by-side with factual comparison data, without implying preference.

**Characteristics**:
- Multiple options presented simultaneously
- Factual comparison data provided
- No recommendation language
- No visual highlighting that implies preference
- No ordering that implies recommendation
- Human makes all decisions

**Interaction Models**:
- DIM-006: Comparative Presentation

**AI Action Type**: Advisory Action (Information Display)

**Human Action Required**: ACT-001 (Selection)

**Prohibited Hybrids**:
- Comparative with recommendation language (becomes Prohibited Action)
- Comparative with visual highlighting (becomes Advisory-with-confirmation)
- Comparative with default selection (becomes Advisory-with-confirmation)
- Comparative with ordering (becomes Prohibited Action)

**Traceability**: `phase_m/DECLARED_DECISION_INTERACTION_CATALOG.md` DIM-006

---

## Classification 4: Option-expansion

**Definition**: AI presents additional options or expands option set without implying preference for any option.

**Characteristics**:
- Additional options added to option set
- No option is pre-selected or highlighted
- No ordering that implies recommendation
- No scope inference
- Human makes all decisions

**Interaction Models**:
- DIM-007: Option Expansion

**AI Action Type**: Non-Decision Action (Data Retrieval)

**Human Action Required**: ACT-001 (Selection), ACT-011 (Scope Definition)

**Prohibited Hybrids**:
- Expansion with default selection (becomes Advisory-with-confirmation)
- Expansion with visual highlighting (becomes Advisory-with-confirmation)
- Expansion with ordering (becomes Prohibited Action)
- Expansion with scope inference (becomes Prohibited Action)

**Traceability**: `phase_m/DECLARED_DECISION_INTERACTION_CATALOG.md` DIM-007

---

## Prohibited Hybrid Models

### Prohibited Hybrid 1: Preview with Default

**Definition**: Preview-only presentation combined with default selection.

**Prohibition Reason**: Violates SOV-001 (Initial Selection). Default selection requires explicit declaration and rejection mechanism (Advisory-with-confirmation).

**Traceability**: `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-001

---

### Prohibited Hybrid 2: Advisory without Declaration

**Definition**: Advisory input provided without explicit declaration.

**Prohibition Reason**: Violates SOV-001, SOV-004, SOV-007. Advisory input must be explicitly declared to remove deception.

**Traceability**: `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-001, SOV-004, SOV-007, `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-001, G-RULE-002

---

### Prohibited Hybrid 3: Comparative with Recommendation

**Definition**: Comparative presentation combined with recommendation language.

**Prohibition Reason**: Violates SOV-007 (Priority Assignment). Recommendation language creates agency effect.

**Traceability**: `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-007, `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-006

---

### Prohibited Hybrid 4: Expansion with Ordering

**Definition**: Option expansion combined with ordering that implies recommendation.

**Prohibition Reason**: Violates SOV-006 (Path Selection). Ordering creates agency effect (70% effect, 25% misinterpretation).

**Traceability**: `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-006, `phase_k_b/AGENCY_EFFECT_MATRIX.md` ORDERING

---

## Classification Summary

**Total Classifications**: 4

**Preview-only**: 1 model (DIM-001)

**Advisory-with-confirmation**: 5 models (DIM-002, DIM-003, DIM-004, DIM-005, DIM-008)

**Comparative-presentation**: 1 model (DIM-006)

**Option-expansion**: 1 model (DIM-007)

**Prohibited Hybrids**: 4 (all traceable to M-0 boundaries)

**All Models Classified**: YES (100%)

**No Ambiguous Models**: YES (100%)

---

## No Recommendations

This classification provides no recommendations.

This classification defines only structural categories.

---

**END OF INTERACTION MODEL CLASSIFICATION**

