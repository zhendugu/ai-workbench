# Q1 Gate Checklist

**Document Status**: SIMULATION-DESIGN / NON-CANONICAL  
**Document Type**: Gate Checklist  
**Date**: 2026-01-10  
**Work Order**: WO-Q-1-LONGITUDINAL-ADVERSARIAL-SIMULATION-DESIGN  
**Parent Baselines**: Decision Boundary Baseline v1.0 (WO-M-0), Interaction Model Baseline v1.0 (WO-M-1), Threat Model (WO-Q-0)

---

## Purpose

This checklist verifies that Q-1 longitudinal simulation design meets all requirements before entering Q-2 execution phase.

All checks must PASS (100%) to proceed to Q-2.

---

## Section 1: Reproducibility (20 checks)

### 1.1 Input Set Reproducibility

- [ ] **Q1-CHECK-001**: Input set generation script exists (`scripts/q1_generate_input_sets.py`)
- [ ] **Q1-CHECK-002**: Input set generation script is executable
- [ ] **Q1-CHECK-003**: Input set generation produces deterministic output (same input = same output)
- [ ] **Q1-CHECK-004**: Input set generation includes hash computation for verification
- [ ] **Q1-CHECK-005**: Input set structure matches `LONGITUDINAL_SIMULATION_SPEC.md` schema

### 1.2 Random Seed Reproducibility

- [ ] **Q1-CHECK-006**: Simulation script accepts random seed parameter
- [ ] **Q1-CHECK-007**: Simulation script uses random seed for all random operations
- [ ] **Q1-CHECK-008**: Same seed + same input set = same log file hash (verified)
- [ ] **Q1-CHECK-009**: Reproducibility verification script exists (`scripts/q1_verify_reproducibility.sh`)
- [ ] **Q1-CHECK-010**: Reproducibility verification script is executable

### 1.3 Log File Reproducibility

- [ ] **Q1-CHECK-011**: Log file format is deterministic (JSONL, no timestamps in content)
- [ ] **Q1-CHECK-012**: Log file naming is deterministic (based on session_id, not timestamp)
- [ ] **Q1-CHECK-013**: Log file content is deterministic (same seed = same entries)
- [ ] **Q1-CHECK-014**: Log file hash is reproducible (same seed = same hash)

### 1.4 Metric Computation Reproducibility

- [ ] **Q1-CHECK-015**: Metric computation script exists (`scripts/q1_compute_metrics.py`)
- [ ] **Q1-CHECK-016**: Metric computation script is executable
- [ ] **Q1-CHECK-017**: Metric computation is deterministic (same log = same metrics)
- [ ] **Q1-CHECK-018**: Metric file format is deterministic (JSON, no timestamps in content)
- [ ] **Q1-CHECK-019**: Metric file hash is reproducible (same log = same hash)
- [ ] **Q1-CHECK-020**: All metrics are computable (no manual calculation required)

---

## Section 2: Metric Computability (30 checks)

### 2.1 SC-001 Metrics

- [ ] **Q1-CHECK-021**: METRIC-SC001-001 (AI-Preferred Selection Rate) is defined in `METRICS_AND_SUCCESS_CRITERIA.md`
- [ ] **Q1-CHECK-022**: METRIC-SC001-001 computation formula is specified
- [ ] **Q1-CHECK-023**: METRIC-SC001-001 is implemented in `q1_compute_metrics.py`
- [ ] **Q1-CHECK-024**: METRIC-SC001-002 (Selection Convergence Index) is defined in `METRICS_AND_SUCCESS_CRITERIA.md`
- [ ] **Q1-CHECK-025**: METRIC-SC001-002 computation formula is specified
- [ ] **Q1-CHECK-026**: METRIC-SC001-002 is implemented in `q1_compute_metrics.py`

### 2.2 SC-002 Metrics

- [ ] **Q1-CHECK-027**: METRIC-SC002-001 (Decision Entropy) is defined in `METRICS_AND_SUCCESS_CRITERIA.md`
- [ ] **Q1-CHECK-028**: METRIC-SC002-001 computation formula is specified
- [ ] **Q1-CHECK-029**: METRIC-SC002-001 is implemented in `q1_compute_metrics.py`
- [ ] **Q1-CHECK-030**: METRIC-SC002-002 (Entropy Reduction Rate) is defined in `METRICS_AND_SUCCESS_CRITERIA.md`
- [ ] **Q1-CHECK-031**: METRIC-SC002-002 computation formula is specified
- [ ] **Q1-CHECK-032**: METRIC-SC002-002 is implemented in `q1_compute_metrics.py`

### 2.3 SC-003 Metrics

- [ ] **Q1-CHECK-033**: METRIC-SC003-001 (Effective Option Set Size) is defined in `METRICS_AND_SUCCESS_CRITERIA.md`
- [ ] **Q1-CHECK-034**: METRIC-SC003-001 computation formula is specified
- [ ] **Q1-CHECK-035**: METRIC-SC003-001 is implemented in `q1_compute_metrics.py`
- [ ] **Q1-CHECK-036**: METRIC-SC003-002 (Option Exploration Rate) is defined in `METRICS_AND_SUCCESS_CRITERIA.md`
- [ ] **Q1-CHECK-037**: METRIC-SC003-002 computation formula is specified
- [ ] **Q1-CHECK-038**: METRIC-SC003-002 is implemented in `q1_compute_metrics.py`

### 2.4 SC-004 Metrics

- [ ] **Q1-CHECK-039**: METRIC-SC004-001 (Default Acceptance Rate) is defined in `METRICS_AND_SUCCESS_CRITERIA.md`
- [ ] **Q1-CHECK-040**: METRIC-SC004-001 computation formula is specified
- [ ] **Q1-CHECK-041**: METRIC-SC004-001 is implemented in `q1_compute_metrics.py`
- [ ] **Q1-CHECK-042**: METRIC-SC004-002 (Rejection Rate Decline) is defined in `METRICS_AND_SUCCESS_CRITERIA.md`
- [ ] **Q1-CHECK-043**: METRIC-SC004-002 computation formula is specified
- [ ] **Q1-CHECK-044**: METRIC-SC004-002 is implemented in `q1_compute_metrics.py`

### 2.5 SC-005 Metrics

- [ ] **Q1-CHECK-045**: METRIC-SC005-001 (Path Diversity Index) is defined in `METRICS_AND_SUCCESS_CRITERIA.md`
- [ ] **Q1-CHECK-046**: METRIC-SC005-001 computation formula is specified
- [ ] **Q1-CHECK-047**: METRIC-SC005-001 is implemented in `q1_compute_metrics.py`
- [ ] **Q1-CHECK-048**: METRIC-SC005-002 (Path Lock-In Index) is defined in `METRICS_AND_SUCCESS_CRITERIA.md`
- [ ] **Q1-CHECK-049**: METRIC-SC005-002 computation formula is specified
- [ ] **Q1-CHECK-050**: METRIC-SC005-002 is implemented in `q1_compute_metrics.py`

### 2.6 SC-006 Metrics

- [ ] **Q1-CHECK-051**: METRIC-SC006-001 (Information Dependency Index) is defined in `METRICS_AND_SUCCESS_CRITERIA.md`
- [ ] **Q1-CHECK-052**: METRIC-SC006-001 computation formula is specified
- [ ] **Q1-CHECK-053**: METRIC-SC006-001 is implemented in `q1_compute_metrics.py`
- [ ] **Q1-CHECK-054**: METRIC-SC006-002 (Independent Decision Rate Decline) is defined in `METRICS_AND_SUCCESS_CRITERIA.md`
- [ ] **Q1-CHECK-055**: METRIC-SC006-002 computation formula is specified
- [ ] **Q1-CHECK-056**: METRIC-SC006-002 is implemented in `q1_compute_metrics.py`

---

## Section 3: Mapping Completeness (40 checks)

### 3.1 Attack Goal Mapping

- [ ] **Q1-CHECK-057**: All 6 attack goals (AG-001 through AG-006) are referenced in coverage matrix
- [ ] **Q1-CHECK-058**: AG-001 is mapped to at least one strategy in coverage matrix
- [ ] **Q1-CHECK-059**: AG-002 is mapped to at least one strategy in coverage matrix
- [ ] **Q1-CHECK-060**: AG-003 is mapped to at least one strategy in coverage matrix
- [ ] **Q1-CHECK-061**: AG-004 is mapped to at least one strategy in coverage matrix
- [ ] **Q1-CHECK-062**: AG-005 is mapped to at least one strategy in coverage matrix
- [ ] **Q1-CHECK-063**: AG-006 is mapped to at least one strategy in coverage matrix

### 3.2 Attack Vector Mapping

- [ ] **Q1-CHECK-064**: All 12 attack vectors (AV-001 through AV-012) are referenced in coverage matrix
- [ ] **Q1-CHECK-065**: AV-001 is mapped to at least one strategy in coverage matrix
- [ ] **Q1-CHECK-066**: AV-002 is mapped to at least one strategy in coverage matrix
- [ ] **Q1-CHECK-067**: AV-003 is mapped to at least one strategy in coverage matrix
- [ ] **Q1-CHECK-068**: AV-004 is mapped to at least one strategy in coverage matrix
- [ ] **Q1-CHECK-069**: AV-005 is mapped to at least one strategy in coverage matrix
- [ ] **Q1-CHECK-070**: AV-006 is mapped to at least one strategy in coverage matrix
- [ ] **Q1-CHECK-071**: AV-007 is mapped to at least one strategy in coverage matrix
- [ ] **Q1-CHECK-072**: AV-008 is mapped to at least one strategy in coverage matrix
- [ ] **Q1-CHECK-073**: AV-009 is mapped to at least one strategy in coverage matrix
- [ ] **Q1-CHECK-074**: AV-010 is mapped to at least one strategy in coverage matrix
- [ ] **Q1-CHECK-075**: AV-011 is mapped to at least one strategy in coverage matrix
- [ ] **Q1-CHECK-076**: AV-012 is mapped to at least one strategy in coverage matrix

### 3.3 Success Criterion Mapping

- [ ] **Q1-CHECK-077**: All 6 success criteria (SC-001 through SC-006) are referenced in metrics document
- [ ] **Q1-CHECK-078**: SC-001 has at least 2 metrics defined
- [ ] **Q1-CHECK-079**: SC-002 has at least 2 metrics defined
- [ ] **Q1-CHECK-080**: SC-003 has at least 2 metrics defined
- [ ] **Q1-CHECK-081**: SC-004 has at least 2 metrics defined
- [ ] **Q1-CHECK-082**: SC-005 has at least 2 metrics defined
- [ ] **Q1-CHECK-083**: SC-006 has at least 2 metrics defined

### 3.4 Degradation Factor Mapping

- [ ] **Q1-CHECK-084**: All 8 degradation factors (DF-001 through DF-008) are referenced in human models
- [ ] **Q1-CHECK-085**: DF-001 is mapped to at least one human model
- [ ] **Q1-CHECK-086**: DF-002 is mapped to at least one human model
- [ ] **Q1-CHECK-087**: DF-003 is mapped to at least one human model
- [ ] **Q1-CHECK-088**: DF-004 is mapped to at least one human model
- [ ] **Q1-CHECK-089**: DF-005 is mapped to at least one human model
- [ ] **Q1-CHECK-090**: DF-006 is mapped to at least one human model
- [ ] **Q1-CHECK-091**: DF-007 is mapped to at least one human model
- [ ] **Q1-CHECK-092**: DF-008 is mapped to at least one human model

### 3.5 M-0 Boundary Mapping

- [ ] **Q1-CHECK-093**: All attack goals reference M-0 boundaries (ACT-XXX, SOV-XXX)
- [ ] **Q1-CHECK-094**: All attack vectors reference M-0 boundaries (ACT-XXX, SOV-XXX)
- [ ] **Q1-CHECK-095**: Log schema includes traceability fields for M-0 boundaries (sov_points, inv_points)
- [ ] **Q1-CHECK-096**: Log entries map to M-0 boundaries in traceability fields

---

## Section 4: Prohibited Inference and Recommendation (20 checks)

### 4.1 No Statistical Generalization

- [ ] **Q1-CHECK-097**: No document claims statistical generalizability to real world
- [ ] **Q1-CHECK-098**: No document claims probability-based predictions
- [ ] **Q1-CHECK-099**: All documents explicitly state simulation-only scope
- [ ] **Q1-CHECK-100**: Human models explicitly state "not real human inference"

### 4.2 No Recommendations

- [ ] **Q1-CHECK-101**: No document contains "should", "recommend", "best practice", "better", "optimal"
- [ ] **Q1-CHECK-102**: No document contains UX optimization suggestions
- [ ] **Q1-CHECK-103**: No document contains mitigation strategies
- [ ] **Q1-CHECK-104**: No document contains improvement suggestions
- [ ] **Q1-CHECK-105**: All documents use descriptive language only

### 4.3 No Ethical Assumptions

- [ ] **Q1-CHECK-106**: No document assumes AI moral/ethical constraints
- [ ] **Q1-CHECK-107**: No document assumes human moral/ethical constraints
- [ ] **Q1-CHECK-108**: Adversary model explicitly forbids moral/ethical assumptions
- [ ] **Q1-CHECK-109**: All documents focus on structural/behavioral analysis only

### 4.4 No Intent-Based Definitions

- [ ] **Q1-CHECK-110**: Success criteria explicitly reject intent-based definitions
- [ ] **Q1-CHECK-111**: Attack goals explicitly reject intent-based definitions
- [ ] **Q1-CHECK-112**: All measurements are behavior-based, not intent-based
- [ ] **Q1-CHECK-113**: Adversary model does not assume AI intent

### 4.5 Explicit Scope Limitations

- [ ] **Q1-CHECK-114**: All documents explicitly state simulation-only scope
- [ ] **Q1-CHECK-115**: All documents explicitly state no real-world inference
- [ ] **Q1-CHECK-116**: All documents explicitly state no product modification

---

## Section 5: Baseline Freeze Verification (15 checks)

### 5.1 J10 Baseline Freeze

- [ ] **Q1-CHECK-117**: No modifications to `release/baseline_v1.0/` directory
- [ ] **Q1-CHECK-118**: No modifications to `frontend_app/` files from J10 baseline
- [ ] **Q1-CHECK-119**: No modifications to backend API endpoints from J10 baseline
- [ ] **Q1-CHECK-120**: Git diff shows no changes to J10 baseline files

### 5.2 Governance Baseline Freeze

- [ ] **Q1-CHECK-121**: No modifications to `phase_k_c/kc_b/GOVERNANCE_BASELINE_DECLARATION.md`
- [ ] **Q1-CHECK-122**: No modifications to `phase_k_b/AGENCY_GOVERNANCE_RULESET.md`
- [ ] **Q1-CHECK-123**: No modifications to `phase_k_b/CHANGE_CLASSIFICATION_MATRIX.md`
- [ ] **Q1-CHECK-124**: Git diff shows no changes to governance baseline files

### 5.3 Decision Boundary Baseline Freeze

- [ ] **Q1-CHECK-125**: No modifications to `phase_m/DECISION_ACT_TAXONOMY.md`
- [ ] **Q1-CHECK-126**: No modifications to `phase_m/HUMAN_SOVEREIGNTY_POINTS.md`
- [ ] **Q1-CHECK-127**: No modifications to `phase_m/DECLARED_DECISION_INTERACTION_CATALOG.md`
- [ ] **Q1-CHECK-128**: Git diff shows no changes to decision boundary baseline files

### 5.4 Threat Model Baseline Freeze

- [ ] **Q1-CHECK-129**: No modifications to `phase_q/ADVERSARIAL_AI_MODEL.md`
- [ ] **Q1-CHECK-130**: No modifications to `phase_q/LONG_HORIZON_ATTACK_GOALS.md`
- [ ] **Q1-CHECK-131**: No modifications to `phase_q/ATTACK_VECTOR_TAXONOMY.md`

---

## Section 6: Coverage Matrix Verification (15 checks)

### 6.1 Coverage Percentage

- [ ] **Q1-CHECK-132**: Coverage matrix shows ≥80% coverage (AG × AV cells)
- [ ] **Q1-CHECK-133**: Coverage matrix explicitly states coverage percentage
- [ ] **Q1-CHECK-134**: All covered cells have strategy reference
- [ ] **Q1-CHECK-135**: All covered cells have metric reference

### 6.2 Strategy Coverage

- [ ] **Q1-CHECK-136**: At least 3 strategies are defined in `ADVERSARY_STRATEGY_CATALOG.md`
- [ ] **Q1-CHECK-137**: All strategies map to at least one attack vector
- [ ] **Q1-CHECK-138**: All strategies have configurable parameters
- [ ] **Q1-CHECK-139**: All strategies have default values for reproducibility

### 6.3 Human Model Coverage

- [ ] **Q1-CHECK-140**: At least 3 human models are defined in `HUMAN_MODEL_CATALOG.md`
- [ ] **Q1-CHECK-141**: All human models map to at least one degradation factor
- [ ] **Q1-CHECK-142**: All human models have configurable parameters
- [ ] **Q1-CHECK-143**: All human models explicitly state "not real human inference"

---

## Checklist Summary

**Total Checks**: 143

**Required Pass Rate**: 100% (143/143)

**All Checks Traceable**: YES (100%)

---

## No Recommendations

This checklist provides no recommendations.

This checklist defines only verification criteria.

---

**END OF Q1 GATE CHECKLIST**

