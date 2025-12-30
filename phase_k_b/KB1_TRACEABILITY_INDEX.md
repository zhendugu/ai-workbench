# KB-1 Traceability Index

**Document Status**: NON-CANONICAL / DESIGN-BOUNDARY  
**Document Type**: Traceability Mapping  
**Date**: 2026-01-10  
**Work Order**: WO-KB-1-DECLARED-AGENCY-PATTERN-DESIGN

---

## Purpose

This document maps each pattern, claim, and invariant in Phase K-B work order KB-1 back to Phase K-A experimental evidence and KB-0 constraints.

Each mapping includes experiment ID, evidence file, observed metric, and constraint reference. No interpretation beyond traceability.

---

## Pattern Traceability

### Pattern 1: Declared Default Selection

**Pattern ID**: PATTERN-DECLARED-DEFAULT-SELECTION

**Base Mechanism**: DEFAULT_SELECTION (Class 2: Declared Agency)

**KA Evidence**:
- **Experiment ID**: KA-1
- **Evidence File**: `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`
- **Observed Metrics**: Default acceptance rate 60%, misinterpretation rate 20%, path convergence rate 60%

**KB-0 Constraint References**:
- **Constraint 4**: Prohibition of Undeclared Default Selection → `phase_k_b/DESIGN_CONSTRAINT_EXTRACTION.md`
- **Class 2 (Declared Agency)**: Default Selection mechanism → `phase_k_b/AGENCY_BOUNDARY_CLASSIFICATION.md`

**Document References**:
- `DECLARED_AGENCY_PATTERN_CATALOG.md`: Pattern 1 specification
- `AGENCY_DISCLOSURE_LANGUAGE.md`: Template 1 (Pre-Selection Disclosure)
- `PATTERN_FAILURE_MODES.md`: Failure Modes 1.1-1.4
- `DECLARATION_VS_IMPLICIT_COMPARISON.md`: Comparison 1
- `AGENCY_REJECTION_INVARIANTS.md`: Invariants I1, I3, I4, I5

---

### Pattern 2: Declared Visual Highlight

**Pattern ID**: PATTERN-DECLARED-VISUAL-HIGHLIGHT

**Base Mechanism**: VISUAL_HIGHLIGHT (Class 2: Declared Agency)

**KA Evidence**:
- **Experiment ID**: KA-2
- **Evidence File**: `audit_evidence/ka_2_visual_highlight_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`
- **Observed Metrics**: Visual highlight prioritization rate 55%, misinterpretation rate 30%, path convergence rate 55%

**KB-0 Constraint References**:
- **Constraint 5**: Prohibition of Undeclared Visual Highlighting → `phase_k_b/DESIGN_CONSTRAINT_EXTRACTION.md`
- **Class 2 (Declared Agency)**: Visual Highlighting mechanism → `phase_k_b/AGENCY_BOUNDARY_CLASSIFICATION.md`

**Document References**:
- `DECLARED_AGENCY_PATTERN_CATALOG.md`: Pattern 2 specification
- `AGENCY_DISCLOSURE_LANGUAGE.md`: Template 2 (Visual Emphasis Disclosure)
- `PATTERN_FAILURE_MODES.md`: Failure Modes 2.1-2.4
- `DECLARATION_VS_IMPLICIT_COMPARISON.md`: Comparison 2
- `AGENCY_REJECTION_INVARIANTS.md`: Invariants I1, I2, I5

---

### Pattern 3: Declared Pre-Selection with Rejection

**Pattern ID**: PATTERN-DECLARED-PRE-SELECTION-REJECTION

**Base Mechanism**: DEFAULT_SELECTION (Class 2: Declared Agency) with explicit rejection

**KA Evidence**:
- **Experiment ID**: KA-1
- **Evidence File**: `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`
- **Observed Metrics**: Default acceptance rate 60%, path offset rate 40%, misinterpretation rate 20%

**KB-0 Constraint References**:
- **Constraint 4**: Prohibition of Undeclared Default Selection → `phase_k_b/DESIGN_CONSTRAINT_EXTRACTION.md`
- **Class 2 (Declared Agency)**: Default Selection mechanism → `phase_k_b/AGENCY_BOUNDARY_CLASSIFICATION.md`

**Document References**:
- `DECLARED_AGENCY_PATTERN_CATALOG.md`: Pattern 3 specification
- `AGENCY_DISCLOSURE_LANGUAGE.md`: Template 3 (Pre-Selection with Change Ability Disclosure)
- `PATTERN_FAILURE_MODES.md`: Failure Modes 3.1-3.3
- `DECLARATION_VS_IMPLICIT_COMPARISON.md`: Comparison 3
- `AGENCY_REJECTION_INVARIANTS.md`: Invariants I1, I3, I4, I5

---

## Disclosure Language Traceability

### Template 1: Pre-Selection Disclosure

**Exact Text**: "This option is pre-selected. This pre-selection influences attention and choice."

**KA Evidence Reference**: KA-1 DEFAULT_SELECTION  
**Misinterpretation Rate**: 20% (without declaration)  
**Citation**: `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Design Justification**: Declaration explicitly states pre-selection state and influence to reduce misinterpretation risk.

---

### Template 2: Visual Emphasis Disclosure

**Exact Text**: "This element is visually emphasized. This emphasis influences attention and choice."

**KA Evidence Reference**: KA-2 VISUAL_HIGHLIGHT  
**Misinterpretation Rate**: 30% (without declaration)  
**Citation**: `audit_evidence/ka_2_visual_highlight_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Design Justification**: Declaration explicitly states visual emphasis and influence to reduce misinterpretation risk.

---

### Template 3: Pre-Selection with Change Ability Disclosure

**Exact Text**: "This option is pre-selected. You can change it. This pre-selection influences attention and choice."

**KA Evidence Reference**: KA-1 DEFAULT_SELECTION  
**Path Offset Rate**: 40% (users who change default)  
**Citation**: `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Design Justification**: Declaration explicitly states change ability to support 40% of users who change defaults.

---

## Failure Mode Traceability

**Total Failure Modes**: 11

**Failure Mode Categories**:
- Hidden Declaration: 3 failure modes (Patterns 1, 2, 3)
- Softening Language: 3 failure modes (Patterns 1, 2, 3)
- Justification Language: 2 failure modes (Patterns 1, 2)
- Non-Rejectable Implementation: 3 failure modes (Patterns 1, 2, 3)

**KA Evidence Coverage**: All failure modes cite KA-1 or KA-2 experimental results

**Citation**: `PATTERN_FAILURE_MODES.md`

---

## Invariant Traceability

**Total Invariants**: 5

**Invariant 1 (Core Functionality Preservation)**:
- **KA Evidence**: KA-1 (40% path offset rate)
- **Citation**: `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Invariant 2 (Option Availability Preservation)**:
- **KA Evidence**: KA-2 (45% change rate)
- **Citation**: `audit_evidence/ka_2_visual_highlight_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Invariant 3 (User Selection Equivalence)**:
- **KA Evidence**: KA-1 (40% path offset rate)
- **Citation**: `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Invariant 4 (Rejection Reversibility)**:
- **KA Evidence**: KA-1 (60% acceptance rate)
- **Citation**: `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Invariant 5 (Rejection Visibility)**:
- **KA Evidence**: KA-1 (40% path offset rate)
- **Citation**: `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

---

## Comparison Traceability

**Total Comparisons**: 3

**Comparison 1 (DEFAULT_SELECTION)**:
- **KA Evidence**: KA-1 (all metrics)
- **Citation**: `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Comparison 2 (VISUAL_HIGHLIGHT)**:
- **KA Evidence**: KA-2 (all metrics)
- **Citation**: `audit_evidence/ka_2_visual_highlight_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Comparison 3 (DEFAULT_SELECTION with Rejection)**:
- **KA Evidence**: KA-1 (all metrics)
- **Citation**: `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

---

## Traceability Summary

**Patterns Mapped**: 3  
**Disclosure Templates Mapped**: 3  
**Failure Modes Mapped**: 11  
**Invariants Mapped**: 5  
**Comparisons Mapped**: 3

**KA Experiment Coverage**: KA-1, KA-2 (Class 2: Declared Agency mechanisms)

**KB-0 Constraint Coverage**: Constraints 4, 5 (DEFAULT_SELECTION, VISUAL_HIGHLIGHT prohibitions)

**Evidence File Coverage**: 
- `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`
- `audit_evidence/ka_2_visual_highlight_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

---

## No Recommendations

This traceability index provides no recommendations.

This traceability index provides no design advice.

This traceability index states only traceability mappings.

---

**END OF KB-1 TRACEABILITY INDEX**

