# Q2 Gate Checklist

**Document Status**: SIMULATION-EXECUTION / NON-CANONICAL  
**Document Type**: Gate Checklist  
**Date**: 2026-01-10  
**Work Order**: WO-Q-2-LONGITUDINAL-ADVERSARIAL-SIMULATION-EXECUTION-AND-DOMINANCE-DETECTION  
**Parent Baselines**: Q-1 Simulation Design (WO-Q-1)

---

## Purpose

This checklist verifies that Q-2 execution meets all requirements.

All checks must PASS (100%) to proceed to Q-3.

---

## Section 1: Baseline Immutability (20 checks)

### 1.1 J10 Baseline Freeze

- [ ] **Q2-CHECK-001**: No modifications to `release/baseline_v1.0/` directory
- [ ] **Q2-CHECK-002**: No modifications to `frontend_app/` files from J10 baseline
- [ ] **Q2-CHECK-003**: No modifications to backend API endpoints from J10 baseline
- [ ] **Q2-CHECK-004**: Git diff shows no changes to J10 baseline files

### 1.2 Governance Baseline Freeze

- [ ] **Q2-CHECK-005**: No modifications to `phase_k_c/kc_b/GOVERNANCE_BASELINE_DECLARATION.md`
- [ ] **Q2-CHECK-006**: No modifications to `phase_k_b/AGENCY_GOVERNANCE_RULESET.md`
- [ ] **Q2-CHECK-007**: No modifications to `phase_k_b/CHANGE_CLASSIFICATION_MATRIX.md`
- [ ] **Q2-CHECK-008**: Git diff shows no changes to governance baseline files

### 1.3 Decision Boundary Baseline Freeze

- [ ] **Q2-CHECK-009**: No modifications to `phase_m/DECISION_ACT_TAXONOMY.md`
- [ ] **Q2-CHECK-010**: No modifications to `phase_m/HUMAN_SOVEREIGNTY_POINTS.md`
- [ ] **Q2-CHECK-011**: No modifications to `phase_m/DECLARED_DECISION_INTERACTION_CATALOG.md`
- [ ] **Q2-CHECK-012**: Git diff shows no changes to decision boundary baseline files

### 1.4 Threat Model Baseline Freeze

- [ ] **Q2-CHECK-013**: No modifications to `phase_q/ADVERSARIAL_AI_MODEL.md`
- [ ] **Q2-CHECK-014**: No modifications to `phase_q/LONG_HORIZON_ATTACK_GOALS.md`
- [ ] **Q2-CHECK-015**: No modifications to `phase_q/ATTACK_VECTOR_TAXONOMY.md`
- [ ] **Q2-CHECK-016**: No modifications to `phase_q/ADVERSARIAL-SUCCESS-DEFINITION.md`

### 1.5 Q-1 Design Baseline Freeze

- [ ] **Q2-CHECK-017**: No modifications to `phase_q/LONGITUDINAL_SIMULATION_SPEC.md`
- [ ] **Q2-CHECK-018**: No modifications to `phase_q/ADVERSARY_STRATEGY_CATALOG.md`
- [ ] **Q2-CHECK-019**: No modifications to `phase_q/HUMAN_MODEL_CATALOG.md`
- [ ] **Q2-CHECK-020**: No modifications to `phase_q/METRICS_AND_SUCCESS_CRITERIA.md`

---

## Section 2: Reproducibility (15 checks)

### 2.1 Run Reproducibility

- [ ] **Q2-CHECK-021**: All 54 runs completed
- [ ] **Q2-CHECK-022**: Each run has fixed seed documented
- [ ] **Q2-CHECK-023**: Each run has input snapshot saved
- [ ] **Q2-CHECK-024**: Each run has log file saved
- [ ] **Q2-CHECK-025**: Each run has metrics file saved
- [ ] **Q2-CHECK-026**: Each run has hash files saved

### 2.2 Hash Verification

- [ ] **Q2-CHECK-027**: All input hashes are reproducible (same input = same hash)
- [ ] **Q2-CHECK-028**: All log hashes are reproducible (same seed = same hash)
- [ ] **Q2-CHECK-029**: All metric hashes are reproducible (same log = same hash)
- [ ] **Q2-CHECK-030**: Reproducibility verification script exists and is executable

### 2.3 Run Metadata

- [ ] **Q2-CHECK-031**: Each run has `run_metadata.json` with all required fields
- [ ] **Q2-CHECK-032**: All run IDs follow naming convention from RUN_MATRIX_DEFINITION.md
- [ ] **Q2-CHECK-033**: All runs are traceable to strategy, model, seed, horizon
- [ ] **Q2-CHECK-034**: Run execution order is documented
- [ ] **Q2-CHECK-035**: No automatic retry occurred (manual rerun only)

---

## Section 3: Metric Computation (20 checks)

### 3.1 All Metrics Computed

- [ ] **Q2-CHECK-036**: METRIC-SC001-001 computed for all runs
- [ ] **Q2-CHECK-037**: METRIC-SC001-002 computed for all runs
- [ ] **Q2-CHECK-038**: METRIC-SC002-001 computed for all runs
- [ ] **Q2-CHECK-039**: METRIC-SC002-002 computed for all runs
- [ ] **Q2-CHECK-040**: METRIC-SC003-001 computed for all runs
- [ ] **Q2-CHECK-041**: METRIC-SC003-002 computed for all runs
- [ ] **Q2-CHECK-042**: METRIC-SC004-001 computed for all runs
- [ ] **Q2-CHECK-043**: METRIC-SC004-002 computed for all runs
- [ ] **Q2-CHECK-044**: METRIC-SC005-001 computed for all runs
- [ ] **Q2-CHECK-045**: METRIC-SC005-002 computed for all runs
- [ ] **Q2-CHECK-046**: METRIC-SC006-001 computed for all runs
- [ ] **Q2-CHECK-047**: METRIC-SC006-002 computed for all runs
- [ ] **Q2-CHECK-048**: METRIC-REJECT-COST computed for all runs
- [ ] **Q2-CHECK-049**: METRIC-CONFIRM-LAZY computed for all runs
- [ ] **Q2-CHECK-050**: METRIC-INFO-DENSITY computed for all runs
- [ ] **Q2-CHECK-051**: METRIC-PREDICT computed for all runs

### 3.2 Metric Aggregation

- [ ] **Q2-CHECK-052**: METRICS_AGGREGATION_REPORT.md exists
- [ ] **Q2-CHECK-053**: Aggregation report contains all 9 strategy×model groups
- [ ] **Q2-CHECK-054**: Aggregation report contains statistical descriptions only (no interpretations)
- [ ] **Q2-CHECK-055**: All metrics have min/max/median/mean statistics

---

## Section 4: Dominance Detection (15 checks)

### 4.1 Threshold Application

- [ ] **Q2-CHECK-056**: THRESHOLD_AND_DECISION_RULES.md exists
- [ ] **Q2-CHECK-057**: All thresholds are from Source A (Q-1 explicit) or Source B (mathematical boundary)
- [ ] **Q2-CHECK-058**: No thresholds from Source C (prohibited subjective)
- [ ] **Q2-CHECK-059**: All SC-001 through SC-006 have decision rules defined
- [ ] **Q2-CHECK-060**: Decision rules are deterministic (no subjective judgment)

### 4.2 SC Evaluation

- [ ] **Q2-CHECK-061**: SC-001 evaluated for all runs
- [ ] **Q2-CHECK-062**: SC-002 evaluated for all runs
- [ ] **Q2-CHECK-063**: SC-003 evaluated for all runs
- [ ] **Q2-CHECK-064**: SC-004 evaluated for all runs
- [ ] **Q2-CHECK-065**: SC-005 evaluated for all runs
- [ ] **Q2-CHECK-066**: SC-006 evaluated for all runs
- [ ] **Q2-CHECK-067**: Overall PASS/FAIL determined for all runs
- [ ] **Q2-CHECK-068**: Dominance detection results saved to file
- [ ] **Q2-CHECK-069**: All evaluations are traceable to run_id and metrics
- [ ] **Q2-CHECK-070**: No INCONCLUSIVE cases (or INCONCLUSIVE explicitly documented)

---

## Section 5: Case Extraction (10 checks)

### 5.1 FAIL Cases

- [ ] **Q2-CHECK-071**: DOMINANCE_CASEBOOK.md exists
- [ ] **Q2-CHECK-072**: At least 10 FAIL cases extracted (or all if < 10)
- [ ] **Q2-CHECK-073**: All FAIL cases sorted by extreme metric values
- [ ] **Q2-CHECK-074**: Each FAIL case has run_id, triggered SC, triggered metrics
- [ ] **Q2-CHECK-075**: Each FAIL case has log fragment location (event_id, turn_id, line_number)

### 5.2 PASS Cases

- [ ] **Q2-CHECK-076**: At least 10 PASS borderline cases extracted (or all if < 10)
- [ ] **Q2-CHECK-077**: All PASS cases sorted by distance to threshold
- [ ] **Q2-CHECK-078**: Each PASS case has run_id, closest SC, closest metrics
- [ ] **Q2-CHECK-079**: Each PASS case has log fragment location
- [ ] **Q2-CHECK-080**: All cases are traceable to run directories

---

## Section 6: Drift and Accumulation Audit (10 checks)

### 6.1 Failure Mode Coverage

- [ ] **Q2-CHECK-081**: DRIFT_AND_ACCUMULATION_AUDIT.md exists
- [ ] **Q2-CHECK-082**: FM-STATIC-001 audited (temporal accumulation)
- [ ] **Q2-CHECK-083**: FM-STATIC-002 audited (repetition-induced habituation)
- [ ] **Q2-CHECK-084**: FM-STATIC-003 audited (gradual language drift)
- [ ] **Q2-CHECK-085**: FM-STATIC-004 audited (information density manipulation)
- [ ] **Q2-CHECK-086**: FM-STATIC-005 audited (option space shaping)
- [ ] **Q2-CHECK-087**: FM-STATIC-006 audited (comparative framing accumulation)
- [ ] **Q2-CHECK-088**: FM-STATIC-007 audited (user self-justification reinforcement)

### 6.2 Signal Computation

- [ ] **Q2-CHECK-089**: All failure mode signals are computable (no manual calculation)
- [ ] **Q2-CHECK-090**: All signals are traceable to run_ids and metrics

---

## Section 7: Coverage Verification (10 checks)

### 7.1 Coverage Matrix Update

- [ ] **Q2-CHECK-091**: Q2_ATTACK_COVERAGE_MATRIX_UPDATE.md exists
- [ ] **Q2-CHECK-092**: Q-2 execution coverage ≥ Q-1 design coverage (80.6%) or structural reason given
- [ ] **Q2-CHECK-093**: All covered cells have run_id references
- [ ] **Q2-CHECK-094**: Coverage percentage explicitly stated
- [ ] **Q2-CHECK-095**: Structural uncoverable reasons (if any) are factual only

### 7.2 Run Coverage Verification

- [ ] **Q2-CHECK-096**: All 54 runs are mapped to AG×AV combinations
- [ ] **Q2-CHECK-097**: All run_ids are traceable to strategy and model
- [ ] **Q2-CHECK-098**: Coverage verification is deterministic (no subjective judgment)
- [ ] **Q2-CHECK-099**: All run_ids are valid (exist in runs directory)
- [ ] **Q2-CHECK-100**: Coverage matrix update is complete

---

## Section 8: Prohibited Content (10 checks)

### 8.1 No Recommendations

- [ ] **Q2-CHECK-101**: No "should", "recommend", "best practice", "better", "optimal" in deliverables
- [ ] **Q2-CHECK-102**: No UX optimization suggestions
- [ ] **Q2-CHECK-103**: No mitigation strategies
- [ ] **Q2-CHECK-104**: No improvement suggestions
- [ ] **Q2-CHECK-105**: No product/UX recommendations

### 8.2 No Interpretations

- [ ] **Q2-CHECK-106**: METRICS_AGGREGATION_REPORT.md contains statistical descriptions only
- [ ] **Q2-CHECK-107**: DOMINANCE_CASEBOOK.md contains case facts only (no interpretations)
- [ ] **Q2-CHECK-108**: DRIFT_AND_ACCUMULATION_AUDIT.md contains signal facts only
- [ ] **Q2-CHECK-109**: All deliverables use descriptive language only
- [ ] **Q2-CHECK-110**: No statistical generalizations to real world

---

## Checklist Summary

**Total Checks**: 110

**Required Pass Rate**: 100% (110/110)

**All Checks Traceable**: YES (100%)

---

## No Recommendations

This checklist provides no recommendations.

This checklist defines only verification criteria.

---

**END OF Q2 GATE CHECKLIST**

