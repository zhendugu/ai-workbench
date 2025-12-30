# Logging Schema and Trace Format

**Document Status**: SIMULATION-DESIGN / NON-CANONICAL  
**Document Type**: Logging Schema Definition  
**Date**: 2026-01-10  
**Work Order**: WO-Q-1-LONGITUDINAL-ADVERSARIAL-SIMULATION-DESIGN  
**Parent Baselines**: Decision Boundary Baseline v1.0 (WO-M-0), Interaction Model Baseline v1.0 (WO-M-1), Threat Model (WO-Q-0)

---

## Purpose

This document defines unified logging format for longitudinal simulation.

All logs are JSONL format (one JSON object per line). All fields are traceable to AG/AV/SC/DF, ACT/SOV/INV, DIM models.

---

## Log Entry Schema

### Required Fields

**session_id** (string): Unique session identifier (e.g., `"session_001"`)

**turn_id** (string): Unique turn identifier within session (e.g., `"turn_001"`)

**timestamp** (integer): Relative time within session (e.g., `1`)

**event_type** (string): Type of event (e.g., `"OPTION_PRESENTED"`, `"HUMAN_SELECTED"`, `"HUMAN_REJECTED"`)

**event_data** (object): Event-specific data (structure varies by event type)

---

### Event-Specific Fields

#### Event: OPTION_PRESENTED

**event_data structure**:
```json
{
  "presented_options": ["option_001", "option_002", "option_003"],
  "option_order": [0, 1, 2],
  "info_density": {"option_001": 5, "option_002": 3, "option_003": 2},
  "declarations": {"option_001": "This option is pre-selected as a default. You can change it."},
  "dim_model": "DIM-004",
  "ai_strategy": "STRATEGY-SLOW-DRIFT",
  "target_preference": "option_001"
}
```

**Traceability Fields**:
- `dim_model`: Maps to `phase_m/DECLARED_DECISION_INTERACTION_CATALOG.md` DIM-XXX
- `ai_strategy`: Maps to `phase_q/ADVERSARY_STRATEGY_CATALOG.md` STRATEGY-XXX
- `target_preference`: Maps to `phase_q/LONG_HORIZON_ATTACK_GOALS.md` AG-001

---

#### Event: HUMAN_SELECTED

**event_data structure**:
```json
{
  "selected_option": "option_001",
  "action_type": "ACT-001",
  "rejection_count": 0,
  "override_count": 0,
  "time_cost_proxy": 5,
  "human_model": "MODEL-FATIGUED-APPROVER",
  "degradation_factors": {"DF-001": 0.3, "DF-002": 0.5, "DF-003": 0.4}
}
```

**Traceability Fields**:
- `action_type`: Maps to `phase_m/DECISION_ACT_TAXONOMY.md` ACT-XXX
- `human_model`: Maps to `phase_q/HUMAN_MODEL_CATALOG.md` MODEL-XXX
- `degradation_factors`: Maps to `phase_q/HUMAN-DEGRADATION-FACTORS.md` DF-XXX

---

#### Event: HUMAN_REJECTED

**event_data structure**:
```json
{
  "rejected_option": "option_001",
  "action_type": "ACT-004",
  "rejection_count": 1,
  "time_cost_proxy": 8,
  "human_model": "MODEL-STRICT-SOVEREIGN",
  "degradation_factors": {"DF-001": 0.0, "DF-008": 0.0}
}
```

**Traceability Fields**:
- `action_type`: Maps to `phase_m/DECISION_ACT_TAXONOMY.md` ACT-004
- `human_model`: Maps to `phase_q/HUMAN_MODEL_CATALOG.md` MODEL-XXX
- `degradation_factors`: Maps to `phase_q/HUMAN-DEGRADATION-FACTORS.md` DF-XXX

---

#### Event: HUMAN_OVERRIDDEN

**event_data structure**:
```json
{
  "overridden_option": "option_001",
  "override_value": "option_002",
  "action_type": "ACT-005",
  "override_count": 1,
  "time_cost_proxy": 10,
  "human_model": "MODEL-STRICT-SOVEREIGN",
  "degradation_factors": {"DF-001": 0.0}
}
```

**Traceability Fields**:
- `action_type`: Maps to `phase_m/DECISION_ACT_TAXONOMY.md` ACT-005
- `human_model`: Maps to `phase_q/HUMAN_MODEL_CATALOG.md` MODEL-XXX

---

#### Event: HUMAN_IGNORED

**event_data structure**:
```json
{
  "ignored_option": "option_001",
  "action_type": "ACT-006",
  "ignore_count": 1,
  "time_cost_proxy": 2,
  "human_model": "MODEL-DELEGATING-OPTIMIZER",
  "degradation_factors": {"DF-007": 0.6}
}
```

**Traceability Fields**:
- `action_type`: Maps to `phase_m/DECISION_ACT_TAXONOMY.md` ACT-006
- `human_model`: Maps to `phase_q/HUMAN_MODEL_CATALOG.md` MODEL-XXX

---

#### Event: HUMAN_CONFIRMED

**event_data structure**:
```json
{
  "confirmed_option": "option_001",
  "action_type": "ACT-002",
  "confirmation_delay": 3,
  "time_cost_proxy": 5,
  "human_model": "MODEL-FATIGUED-APPROVER",
  "degradation_factors": {"DF-005": 0.4}
}
```

**Traceability Fields**:
- `action_type`: Maps to `phase_m/DECISION_ACT_TAXONOMY.md` ACT-002
- `human_model`: Maps to `phase_q/HUMAN_MODEL_CATALOG.md` MODEL-XXX

---

#### Event: METRIC_OBSERVED

**event_data structure**:
```json
{
  "metric_id": "METRIC-SC001-001",
  "metric_value": 0.75,
  "metric_threshold": 0.8,
  "threshold_exceeded": false,
  "success_criterion": "SC-001",
  "attack_goal": "AG-001",
  "attack_vector": "AV-001"
}
```

**Traceability Fields**:
- `metric_id`: Maps to `phase_q/METRICS_AND_SUCCESS_CRITERIA.md` METRIC-XXX
- `success_criterion`: Maps to `phase_q/ADVERSARIAL-SUCCESS-DEFINITION.md` SC-XXX
- `attack_goal`: Maps to `phase_q/LONG_HORIZON_ATTACK_GOALS.md` AG-XXX
- `attack_vector`: Maps to `phase_q/ATTACK_VECTOR_TAXONOMY.md` AV-XXX

---

### Cumulative Indices

**cumulative_indices** (object): Cumulative metrics across all turns in session

**Structure**:
```json
{
  "ai_preferred_selection_rate": 0.75,
  "decision_entropy": 2.1,
  "effective_option_set_size": 4,
  "default_acceptance_rate": 0.65,
  "rejection_rate": 0.25,
  "path_diversity_index": 1.8,
  "information_dependency_index": 0.55,
  "rejection_cost_proxy": 8.5,
  "confirmation_laziness_index": 0.15,
  "information_density_drift": 0.3,
  "decision_predictability": 0.72
}
```

**Traceability**: All indices map to `phase_q/METRICS_AND_SUCCESS_CRITERIA.md` metrics

---

### Traceability Fields

**sov_points** (array): Human sovereignty points involved (e.g., `["SOV-001", "SOV-004"]`)

**inv_points** (array): Invariants involved (e.g., `["INV-REJECT-001", "INV-OVERRIDE-001"]`)

**dim_models** (array): DIM models used (e.g., `["DIM-004", "DIM-005"]`)

**attack_vectors** (array): Attack vectors active (e.g., `["AV-001", "AV-003"]`)

**attack_goals** (array): Attack goals targeted (e.g., `["AG-001", "AG-002"]`)

**degradation_factors** (object): Degradation factors active (e.g., `{"DF-001": 0.3, "DF-002": 0.5}`)

---

## Log File Format

**Format**: JSONL (one JSON object per line)

**File naming**: `session_{session_id}.jsonl`

**Example entry**:
```json
{"session_id": "session_001", "turn_id": "turn_001", "timestamp": 1, "event_type": "OPTION_PRESENTED", "event_data": {"presented_options": ["option_001", "option_002"], "option_order": [0, 1], "info_density": {"option_001": 5, "option_002": 3}, "declarations": {}, "dim_model": "DIM-004", "ai_strategy": "STRATEGY-SLOW-DRIFT", "target_preference": "option_001"}, "cumulative_indices": {}, "sov_points": ["SOV-001"], "inv_points": [], "dim_models": ["DIM-004"], "attack_vectors": ["AV-001"], "attack_goals": ["AG-001"], "degradation_factors": {}}
```

---

## Schema Summary

**Log Format**: JSONL

**Required Fields**: session_id, turn_id, timestamp, event_type, event_data

**Event Types**: OPTION_PRESENTED, HUMAN_SELECTED, HUMAN_REJECTED, HUMAN_OVERRIDDEN, HUMAN_IGNORED, HUMAN_CONFIRMED, METRIC_OBSERVED

**Traceability Fields**: sov_points, inv_points, dim_models, attack_vectors, attack_goals, degradation_factors

**All Fields Traceable**: YES (100%)

---

## No Recommendations

This schema provides no recommendations.

This schema defines only logging structure.

---

**END OF LOGGING SCHEMA AND TRACE FORMAT**

