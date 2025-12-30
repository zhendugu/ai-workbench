# Traceability Matrix M1

**Document Status**: DESIGN-BASELINE / NON-CANONICAL  
**Document Type**: Traceability Matrix  
**Date**: 2026-01-10  
**Work Order**: WO-M-1-DECLARED-DECISION-INTERACTION-MODELS  
**Version**: Interaction Model Baseline v1.0  
**Parent Baseline**: Decision Boundary Baseline v1.0 (WO-M-0)

---

## Purpose

This document maps every interaction model to ACT-XXX, SOV-XXX, INV-XXX, and Phase K evidence where applicable.

No unmapped models allowed.

---

## Mapping Table

| Interaction Model | ACT-XXX | SOV-XXX | INV-XXX | Phase K Evidence |
|-------------------|---------|---------|---------|------------------|
| DIM-001: Preview-Only Presentation | ACT-001, ACT-008 | SOV-001, SOV-003, SOV-006, SOV-007 | N/A | `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-001, G-RULE-002, G-RULE-008 |
| DIM-002: Declared Default Selection | ACT-001, ACT-004, ACT-005 | SOV-001, SOV-004, SOV-005 | INV-REJECT-001, INV-REJECT-002 | `phase_k_b/DECLARED_AGENCY_PATTERN_CATALOG.md` PATTERN-DECLARED-DEFAULT-SELECTION, `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md` |
| DIM-003: Declared Visual Highlight | ACT-001, ACT-004, ACT-006 | SOV-001, SOV-004, SOV-006, SOV-007 | INV-REJECT-001, INV-REJECT-002 | `phase_k_b/DECLARED_AGENCY_PATTERN_CATALOG.md` PATTERN-DECLARED-VISUAL-HIGHLIGHT, `audit_evidence/ka_2_visual_highlight_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md` |
| DIM-004: Information Display | ACT-001, ACT-008 | SOV-001, SOV-003, SOV-007 | N/A | `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-006 |
| DIM-005: Validation Feedback | ACT-008, ACT-005 | SOV-003, SOV-005, SOV-007 | INV-OVERRIDE-001, INV-OVERRIDE-002 | `phase_m/REJECTION_AND_OVERRIDE_INVARIANTS.md` INV-OVERRIDE-001, INV-OVERRIDE-002 |
| DIM-006: Comparative Presentation | ACT-001 | SOV-001, SOV-006, SOV-007 | N/A | `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-006, G-RULE-008 |
| DIM-007: Option Expansion | ACT-001, ACT-011 | SOV-001, SOV-006, SOV-007, SOV-008, SOV-011 | N/A | `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-001, G-RULE-002, G-RULE-008, G-RULE-010, G-RULE-011 |
| DIM-008: Confirmation Request | ACT-002, ACT-004, ACT-012 | SOV-002, SOV-004, SOV-009, SOV-012 | INV-REJECT-001 | `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-012 |

---

## Detailed Mappings

### DIM-001: Preview-Only Presentation

**ACT Mappings**:
- ACT-001: Selection (human must select option)
- ACT-008: Parameter Input (human must provide parameter values)

**SOV Mappings**:
- SOV-001: Initial Selection (no pre-selection)
- SOV-003: Parameter Value Provision (no pre-filling)
- SOV-006: Path Selection (no ordering that implies recommendation)
- SOV-007: Priority Assignment (no visual highlighting that implies priority)

**INV Mappings**: N/A (no rejection/override required)

**Phase K Evidence**:
- `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-001 (prohibits default selection)
- `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-002 (prohibits visual highlighting)
- `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-008 (prohibits implicit ordering)

---

### DIM-002: Declared Default Selection

**ACT Mappings**:
- ACT-001: Selection (human can accept or change default)
- ACT-004: Rejection (human can reject default)
- ACT-005: Override (human can override default)

**SOV Mappings**:
- SOV-001: Initial Selection (default must be declared)
- SOV-004: Rejection (rejection must be available)
- SOV-005: Override (override must be available)

**INV Mappings**:
- INV-REJECT-001: No penalty for rejection
- INV-REJECT-002: Rejection reversibility

**Phase K Evidence**:
- `phase_k_b/DECLARED_AGENCY_PATTERN_CATALOG.md` PATTERN-DECLARED-DEFAULT-SELECTION
- `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md` (60% effect, 20% misinterpretation)

---

### DIM-003: Declared Visual Highlight

**ACT Mappings**:
- ACT-001: Selection (human can select highlighted or non-highlighted option)
- ACT-004: Rejection (human can reject highlight)
- ACT-006: Ignore (human can ignore highlight)

**SOV Mappings**:
- SOV-001: Initial Selection (highlight must be declared)
- SOV-004: Rejection (rejection must be available)
- SOV-006: Path Selection (highlight must not imply path recommendation)
- SOV-007: Priority Assignment (highlight must be declared)

**INV Mappings**:
- INV-REJECT-001: No penalty for rejection
- INV-REJECT-002: Rejection reversibility

**Phase K Evidence**:
- `phase_k_b/DECLARED_AGENCY_PATTERN_CATALOG.md` PATTERN-DECLARED-VISUAL-HIGHLIGHT
- `audit_evidence/ka_2_visual_highlight_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md` (55% effect, 30% misinterpretation)

---

### DIM-004: Information Display

**ACT Mappings**:
- ACT-001: Selection (human must select option)
- ACT-008: Parameter Input (human must provide parameter values)

**SOV Mappings**:
- SOV-001: Initial Selection (information does not imply selection)
- SOV-003: Parameter Value Provision (information does not imply parameter values)
- SOV-007: Priority Assignment (information does not imply priority)

**INV Mappings**: N/A (no rejection/override required)

**Phase K Evidence**:
- `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-006 (prohibits recommendation language)

---

### DIM-005: Validation Feedback

**ACT Mappings**:
- ACT-008: Parameter Input (human can correct input)
- ACT-005: Override (human can override validation)

**SOV Mappings**:
- SOV-003: Parameter Value Provision (validation does not imply parameter values)
- SOV-005: Override (override must be available)
- SOV-007: Priority Assignment (validation does not imply priority)

**INV Mappings**:
- INV-OVERRIDE-001: No penalty for override
- INV-OVERRIDE-002: Override reversibility

**Phase K Evidence**: N/A (M-0 invariant only)

---

### DIM-006: Comparative Presentation

**ACT Mappings**:
- ACT-001: Selection (human must select option)

**SOV Mappings**:
- SOV-001: Initial Selection (comparison does not imply selection)
- SOV-006: Path Selection (comparison does not imply path recommendation)
- SOV-007: Priority Assignment (comparison does not imply priority)

**INV Mappings**: N/A (no rejection/override required)

**Phase K Evidence**:
- `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-006 (prohibits recommendation language)
- `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-008 (prohibits implicit ordering)

---

### DIM-007: Option Expansion

**ACT Mappings**:
- ACT-001: Selection (human must select option)
- ACT-011: Scope Definition (human can define scope)

**SOV Mappings**:
- SOV-001: Initial Selection (expansion does not imply selection)
- SOV-006: Path Selection (expansion does not imply path recommendation)
- SOV-007: Priority Assignment (expansion does not imply priority)
- SOV-008: Scope Definition (expansion does not imply scope)
- SOV-011: Scope Definition (human must define scope)

**INV Mappings**: N/A (no rejection/override required)

**Phase K Evidence**:
- `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-001 (prohibits default selection)
- `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-002 (prohibits visual highlighting)
- `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-008 (prohibits implicit ordering)
- `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-010 (prohibits unacknowledged grouping)
- `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-011 (prohibits state memory for agency)

---

### DIM-008: Confirmation Request

**ACT Mappings**:
- ACT-002: Confirmation (human must confirm)
- ACT-004: Rejection (human can reject)
- ACT-012: Termination (human can terminate)

**SOV Mappings**:
- SOV-002: Confirmation (human must confirm)
- SOV-004: Rejection (rejection must be available)
- SOV-009: Termination (termination must be available)
- SOV-012: Termination (human can terminate)

**INV Mappings**:
- INV-REJECT-001: No penalty for rejection

**Phase K Evidence**:
- `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-012 (prohibits automatic execution)

---

## Traceability Summary

**Total Interaction Models**: 8

**Models Mapped to ACT**: 8/8 (100%)

**Models Mapped to SOV**: 8/8 (100%)

**Models Mapped to INV**: 4/8 (50%) (4 models require rejection/override invariants)

**Models Mapped to Phase K Evidence**: 8/8 (100%)

**Unmapped Models**: 0/8 (0%)

---

## No Recommendations

This matrix provides no recommendations.

This matrix maps only traceability.

---

**END OF TRACEABILITY MATRIX M1**

