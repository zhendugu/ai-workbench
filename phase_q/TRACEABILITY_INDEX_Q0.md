# Traceability Index Q0

**Document Status**: THREAT-MODEL / NON-CANONICAL  
**Document Type**: Traceability Index  
**Date**: 2026-01-10  
**Work Order**: WO-Q-0-ADVERSARIAL-LONG-HORIZON-AI-BEHAVIOR-THREAT-MODELING  
**Parent Baselines**: Decision Boundary Baseline v1.0 (WO-M-0), Interaction Model Baseline v1.0 (WO-M-1)

---

## Purpose

This document maps every adversarial goal and vector to Phase K evidence, Phase M boundaries, and Phase N product application points.

100% coverage required.

---

## Attack Goal Traceability

### AG-001: De Facto Decision Dominance

**Phase K Evidence**:
- `phase_k_b/AGENCY_EFFECT_MATRIX.md` (structural variables create agency effects)
- `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md` (60% effect, 20% misinterpretation)
- `audit_evidence/ka_3_ordering_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md` (70% effect, 25% misinterpretation)

**Phase M Boundaries**:
- `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-001 (Initial Selection)
- `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-006 (Path Selection)
- `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-007 (Priority Assignment)

**Phase N Product Application**:
- `phase_n/DECISION_POINT_MAPPING.md` DP-001 (Configuration Type Selection)
- `phase_n/DECISION_POINT_MAPPING.md` DP-003 (Configuration Scope Definition)

---

### AG-002: Human Decision Fatigue Exploitation

**Phase K Evidence**:
- `phase_k_b/AGENCY_EFFECT_MATRIX.md` (misinterpretation rates 20%-30%)
- `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md` (default acceptance rate 60%)

**Phase M Boundaries**:
- `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-001 (Initial Selection)
- `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-002 (Confirmation)
- `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-004 (Rejection)

**Phase N Product Application**:
- `phase_n/DECISION_POINT_MAPPING.md` DP-004 (Configuration Confirmation)
- `phase_n/INFEASIBILITY_AND_FRICTION_LOG.md` Friction Point 7 (No Auto-Confirmation After Timeout)

---

### AG-003: Path Dependency Lock-In

**Phase K Evidence**:
- `phase_k_b/AGENCY_EFFECT_MATRIX.md` ORDERING (70% effect, 25% misinterpretation)
- `audit_evidence/ka_4_grouping_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md` (65% effect, 30% misinterpretation)

**Phase M Boundaries**:
- `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-006 (Path Selection)
- `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-008 (Scope Definition)
- `phase_m/REJECTION_AND_OVERRIDE_INVARIANTS.md` INV-PATH-001 (no path locking)

**Phase N Product Application**:
- `phase_n/DECISION_POINT_MAPPING.md` DP-003 (Configuration Scope Definition)

---

### AG-004: Cognitive Offloading Capture

**Phase K Evidence**:
- `phase_k_b/AGENCY_EFFECT_MATRIX.md` (misinterpretation rates 20%-30%)
- `audit_evidence/ka_2_visual_highlight_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md` (45% change rate)

**Phase M Boundaries**:
- `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-001 (Initial Selection)
- `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-003 (Parameter Value Provision)
- `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-007 (Priority Assignment)

**Phase N Product Application**:
- `phase_n/DECISION_POINT_MAPPING.md` DP-002 (Parameter Value Input)
- `phase_n/AGENCY_CLASSIFICATION_SUMMARY.md` Behavior 2 (Provide Parameter Validation Feedback)

---

### AG-005: Rejection Cost Amplification

**Phase K Evidence**:
- `phase_k_b/AGENCY_REJECTION_INVARIANTS.md` INVARIANT-001 (rejection has no penalty)
- `phase_k_b/AGENCY_REJECTION_INVARIANTS.md` INVARIANT-002 (rejection is reversible)

**Phase M Boundaries**:
- `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-004 (Rejection)
- `phase_m/REJECTION_AND_OVERRIDE_INVARIANTS.md` INV-REJECT-001 (no penalty for rejection)

**Phase N Product Application**:
- `phase_n/DECISION_POINT_MAPPING.md` DP-005 (Validation Error Resolution)

---

### AG-006: Option Space Shaping

**Phase K Evidence**:
- `phase_k_b/AGENCY_EFFECT_MATRIX.md` ORDERING (70% effect, 25% misinterpretation)
- `audit_evidence/ka_5_proximity_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md` (60% effect, 25% misinterpretation)

**Phase M Boundaries**:
- `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-001 (Initial Selection)
- `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-006 (Path Selection)
- `phase_m/HUMAN_SOVEREIGNTY_POINTS.md` SOV-008 (Scope Definition)

**Phase N Product Application**:
- `phase_n/DECISION_POINT_MAPPING.md` DP-003 (Configuration Scope Definition)
- `phase_n/INTERACTION_MODEL_ASSIGNMENT.md` DP-003 (DIM-007: Option Expansion)

---

## Attack Vector Traceability

### AV-001: Temporal Sequencing Attacks

**Phase K Evidence**: `phase_k_b/AGENCY_EFFECT_MATRIX.md` (structural variables create agency effects)

**Phase M Boundaries**: `phase_m/DECLARED_DECISION_INTERACTION_CATALOG.md` DIM-004, DIM-006

**Phase N Product Application**: `phase_n/INTERACTION_MODEL_ASSIGNMENT.md` DP-001 (DIM-004)

---

### AV-002: Language Softening Drift

**Phase K Evidence**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-003, G-RULE-004

**Phase M Boundaries**: `phase_m/DECLARED_DECISION_INTERACTION_CATALOG.md` DIM-002, DIM-003

**Phase N Product Application**: N/A (no declared agency in product scenario)

---

### AV-003: Comparative Framing Accumulation

**Phase K Evidence**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-006

**Phase M Boundaries**: `phase_m/DECLARED_DECISION_INTERACTION_CATALOG.md` DIM-006

**Phase N Product Application**: N/A (no comparative presentation in product scenario)

---

### AV-004: Salience Decay Manipulation

**Phase K Evidence**: `phase_k_b/AGENCY_EFFECT_MATRIX.md` ORDERING (70% effect)

**Phase M Boundaries**: `phase_m/DECLARED_DECISION_INTERACTION_CATALOG.md` DIM-007, DIM-004

**Phase N Product Application**: `phase_n/INTERACTION_MODEL_ASSIGNMENT.md` DP-003 (DIM-007)

---

### AV-005: User Self-Justification Reinforcement

**Phase K Evidence**: `phase_k_b/AGENCY_EFFECT_MATRIX.md` (misinterpretation rates 20%-30%)

**Phase M Boundaries**: `phase_m/DECLARED_DECISION_INTERACTION_CATALOG.md` DIM-004, DIM-006

**Phase N Product Application**: `phase_n/INTERACTION_MODEL_ASSIGNMENT.md` DP-001 (DIM-004)

---

### AV-006: Confirmation Loop Seeding

**Phase K Evidence**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-012

**Phase M Boundaries**: `phase_m/DECLARED_DECISION_INTERACTION_CATALOG.md` DIM-004, DIM-008

**Phase N Product Application**: `phase_n/INTERACTION_MODEL_ASSIGNMENT.md` DP-004 (DIM-008)

---

### AV-007: Information Density Manipulation

**Phase K Evidence**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-006

**Phase M Boundaries**: `phase_m/DECLARED_DECISION_INTERACTION_CATALOG.md` DIM-004, DIM-006

**Phase N Product Application**: `phase_n/INTERACTION_MODEL_ASSIGNMENT.md` DP-001 (DIM-004)

---

### AV-008: Temporal Anchoring

**Phase K Evidence**: `phase_k_b/AGENCY_EFFECT_MATRIX.md` ORDERING (70% effect, 25% misinterpretation)

**Phase M Boundaries**: `phase_m/DECLARED_DECISION_INTERACTION_CATALOG.md` DIM-004, DIM-006

**Phase N Product Application**: `phase_n/INTERACTION_MODEL_ASSIGNMENT.md` DP-001 (DIM-004)

---

### AV-009: Validation Feedback Framing

**Phase K Evidence**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-006

**Phase M Boundaries**: `phase_m/DECLARED_DECISION_INTERACTION_CATALOG.md` DIM-005

**Phase N Product Application**: `phase_n/INTERACTION_MODEL_ASSIGNMENT.md` DP-002 (DIM-005), DP-005 (DIM-005)

---

### AV-010: Option Expansion Timing

**Phase K Evidence**: `phase_k_b/AGENCY_EFFECT_MATRIX.md` ORDERING (70% effect)

**Phase M Boundaries**: `phase_m/DECLARED_DECISION_INTERACTION_CATALOG.md` DIM-007

**Phase N Product Application**: `phase_n/INTERACTION_MODEL_ASSIGNMENT.md` DP-003 (DIM-007)

---

### AV-011: Confirmation Request Framing

**Phase K Evidence**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-012

**Phase M Boundaries**: `phase_m/DECLARED_DECISION_INTERACTION_CATALOG.md` DIM-008

**Phase N Product Application**: `phase_n/INTERACTION_MODEL_ASSIGNMENT.md` DP-004 (DIM-008)

---

### AV-012: Declarative Language Gradual Erosion

**Phase K Evidence**: `phase_k_b/AGENCY_GOVERNANCE_RULESET.md` G-RULE-003, G-RULE-004

**Phase M Boundaries**: `phase_m/DECLARED_DECISION_INTERACTION_CATALOG.md` DIM-002, DIM-003

**Phase N Product Application**: N/A (no declared agency in product scenario)

---

## Traceability Summary

**Total Attack Goals**: 6

**Total Attack Vectors**: 12

**All Goals Mapped to Phase K Evidence**: YES (6/6)

**All Goals Mapped to Phase M Boundaries**: YES (6/6)

**All Goals Mapped to Phase N Product Application**: YES (6/6)

**All Vectors Mapped to Phase K Evidence**: YES (12/12)

**All Vectors Mapped to Phase M Boundaries**: YES (12/12)

**All Vectors Mapped to Phase N Product Application**: YES (12/12, some N/A for vectors not applicable to product scenario)

**Coverage**: 100%

---

## No Recommendations

This index provides no recommendations.

This index maps only traceability.

---

**END OF TRACEABILITY INDEX Q0**

