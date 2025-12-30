# Longitudinal Simulation Specification

**Document Status**: SIMULATION-DESIGN / NON-CANONICAL  
**Document Type**: Simulation Framework Definition  
**Date**: 2026-01-10  
**Work Order**: WO-Q-1-LONGITUDINAL-ADVERSARIAL-SIMULATION-DESIGN  
**Parent Baselines**: Decision Boundary Baseline v1.0 (WO-M-0), Interaction Model Baseline v1.0 (WO-M-1), Threat Model (WO-Q-0)

---

## Purpose

This document defines the overall framework for longitudinal adversarial simulation experiments.

This framework is for simulation only, not product implementation.

---

## Simulation Framework

### Session

**Definition**: A sequence of interactions between human model and AI adversary over time.

**Properties**:
- Session ID: Unique identifier (e.g., `session_001`)
- Start time: Simulation timestamp (e.g., `t=0`)
- End time: Simulation timestamp (e.g., `t=100`)
- Duration: Number of turns (e.g., 100 turns)
- Random seed: Fixed seed for reproducibility (e.g., `seed=42`)

**Traceability**: `phase_q/ADVERSARIAL_AI_MODEL.md` (planning horizon assumption)

---

### Turn

**Definition**: A single interaction cycle where AI presents options and human model responds.

**Properties**:
- Turn ID: Unique identifier within session (e.g., `turn_001`)
- Session ID: Parent session identifier
- Timestamp: Relative time within session (e.g., `t=1`)
- AI action: Action taken by AI adversary (e.g., `DIM-004`, `DIM-005`)
- Human action: Action taken by human model (e.g., `ACT-001`, `ACT-004`)
- Options presented: List of options presented by AI
- Option selected: Option selected by human (if any)

**Traceability**: `phase_m/DECLARED_DECISION_INTERACTION_CATALOG.md` (DIM models), `phase_m/DECISION_ACT_TAXONOMY.md` (ACT types)

---

### Event

**Definition**: A discrete occurrence within a turn (e.g., option presentation, human selection, rejection, override).

**Properties**:
- Event ID: Unique identifier within turn (e.g., `event_001`)
- Turn ID: Parent turn identifier
- Event type: Type of event (e.g., `OPTION_PRESENTED`, `HUMAN_SELECTED`, `HUMAN_REJECTED`)
- Event data: Event-specific data (e.g., option ID, selection reason)

**Traceability**: `phase_m/ACCEPT_REJECT_IGNORE_STATE_MACHINE.md` (state transitions)

---

### Action

**Definition**: A specific action taken by AI or human model.

**AI Actions**:
- DIM-001: Preview-Only Presentation
- DIM-002: Declared Default Selection
- DIM-003: Declared Visual Highlight
- DIM-004: Information Display
- DIM-005: Validation Feedback
- DIM-006: Comparative Presentation
- DIM-007: Option Expansion
- DIM-008: Confirmation Request

**Human Actions**:
- ACT-001: Selection
- ACT-002: Confirmation
- ACT-004: Rejection
- ACT-005: Override
- ACT-006: Ignore
- ACT-012: Termination

**Traceability**: `phase_m/DECLARED_DECISION_INTERACTION_CATALOG.md` (DIM models), `phase_m/DECISION_ACT_TAXONOMY.md` (ACT types)

---

### Observation

**Definition**: A measurable state or outcome observed during simulation.

**Properties**:
- Observation ID: Unique identifier (e.g., `obs_001`)
- Turn ID: Turn where observation occurred
- Observation type: Type of observation (e.g., `OPTION_ENTROPY`, `REJECTION_RATE`, `PATH_DIVERSITY`)
- Observation value: Numerical value (e.g., `entropy=2.5`, `rejection_rate=0.3`)

**Traceability**: `phase_q/METRICS_AND_SUCCESS_CRITERIA.md` (metric definitions)

---

### State (Simulation State, Not Product State)

**Definition**: Simulation state variables used for tracking simulation progress.

**Properties**:
- Session state: Current session identifier, turn count, timestamp
- AI state: Current AI strategy, strategy parameters, accumulated influence
- Human state: Current human model, degradation factors, accumulated fatigue
- Option state: Available options, option presentation history, option selection history

**Note**: This is simulation state only, not product system state. Simulation state is used for tracking and measurement, not for product behavior.

**Traceability**: `phase_q/ADVERSARIAL_AI_MODEL.md` (memory assumption), `phase_q/HUMAN-DEGRADATION-FACTORS.md` (degradation factors)

---

## Input Specification

### Input Set

**Definition**: Fixed set of scenarios, options, and parameters used for simulation.

**Properties**:
- Input set ID: Unique identifier (e.g., `input_set_001`)
- Scenarios: List of decision scenarios (e.g., configuration type selection, parameter input)
- Options: List of available options for each scenario
- Option properties: Properties of each option (e.g., feature support, resource requirements)
- Fixed parameters: Fixed simulation parameters (e.g., session duration, turn count)

**Format**: JSON file (e.g., `input_sets/input_set_001.json`)

**Traceability**: `phase_n/PRODUCT_SCENARIO_DEFINITION.md` (product scenario)

---

### Random Seed

**Definition**: Fixed random seed for reproducibility.

**Properties**:
- Seed value: Integer value (e.g., `42`)
- Seed source: Source of seed (e.g., `FIXED`, `CONFIGURED`)
- Reproducibility guarantee: Same seed + same input set = same simulation trajectory

**Format**: Configuration parameter (e.g., `--seed 42`)

**Traceability**: N/A (simulation requirement, not derived from Phase K/M/N)

---

### Strategy Configuration

**Definition**: Configuration parameters for AI adversary strategy.

**Properties**:
- Strategy ID: Strategy identifier (e.g., `STRATEGY-SLOW-DRIFT`)
- Strategy parameters: Strategy-specific parameters (e.g., drift rate, burst intensity)
- Default values: Default parameter values for reproducibility

**Format**: JSON file (e.g., `strategies/strategy_slow_drift.json`)

**Traceability**: `phase_q/ADVERSARY_STRATEGY_CATALOG.md` (strategy definitions)

---

### Human Model Configuration

**Definition**: Configuration parameters for human model.

**Properties**:
- Model ID: Model identifier (e.g., `MODEL-STRICT-SOVEREIGN`)
- Model parameters: Model-specific parameters (e.g., fatigue rate, trust accumulation rate)
- Default values: Default parameter values for reproducibility

**Format**: JSON file (e.g., `human_models/model_strict_sovereign.json`)

**Traceability**: `phase_q/HUMAN_MODEL_CATALOG.md` (model definitions)

---

## Output Specification

### Log Files

**Definition**: Detailed logs of simulation execution.

**Properties**:
- Log format: JSONL (one JSON object per line)
- Log fields: session_id, turn_id, event_type, event_data, timestamp, traceability_fields
- Log location: `simulation_logs/session_{session_id}.jsonl`

**Traceability**: `phase_q/LOGGING_SCHEMA_AND_TRACE_FORMAT.md` (logging schema)

---

### Metric Files

**Definition**: Computed metrics from simulation logs.

**Properties**:
- Metric format: JSON (structured metric data)
- Metric fields: metric_id, metric_value, turn_id, session_id, traceability_fields
- Metric location: `simulation_metrics/session_{session_id}_metrics.json`

**Traceability**: `phase_q/METRICS_AND_SUCCESS_CRITERIA.md` (metric definitions)

---

### Summary Files

**Definition**: Summary statistics across sessions.

**Properties**:
- Summary format: JSON (aggregated statistics)
- Summary fields: session_count, average_metrics, success_criteria_status, traceability_fields
- Summary location: `simulation_summaries/summary_{experiment_id}.json`

**Traceability**: `phase_q/METRICS_AND_SUCCESS_CRITERIA.md` (success criteria)

---

## Minimal Reproduction Flow

### Step 1: Generate Input Sets

**Command**: `python3 scripts/q1_generate_input_sets.py --output input_sets/`

**Output**: Fixed input set files (e.g., `input_sets/input_set_001.json`)

**Reproducibility**: Same command produces same input sets.

---

### Step 2: Run Simulation

**Command**: `python3 scripts/q1_run_simulation.py --input input_sets/input_set_001.json --seed 42 --strategy strategies/strategy_slow_drift.json --human_model human_models/model_strict_sovereign.json --output simulation_logs/`

**Output**: Simulation log files (e.g., `simulation_logs/session_001.jsonl`)

**Reproducibility**: Same input set + same seed + same strategy + same human model = same log files.

---

### Step 3: Compute Metrics

**Command**: `python3 scripts/q1_compute_metrics.py --log simulation_logs/session_001.jsonl --output simulation_metrics/`

**Output**: Metric files (e.g., `simulation_metrics/session_001_metrics.json`)

**Reproducibility**: Same log file = same metric file.

---

### Step 4: Verify Reproducibility

**Command**: `bash scripts/q1_verify_reproducibility.sh --log1 simulation_logs/session_001.jsonl --log2 simulation_logs/session_001_rerun.jsonl`

**Output**: Reproducibility status (PASS/FAIL)

**Reproducibility**: Same input set + same seed = same hash.

---

## Framework Summary

**Simulation Components**: Session, Turn, Event, Action, Observation, State

**Input Components**: Input Set, Random Seed, Strategy Configuration, Human Model Configuration

**Output Components**: Log Files, Metric Files, Summary Files

**Reproducibility**: Fixed seed + fixed input set = fixed trajectory

**All Components Traceable**: YES (100%)

---

## No Recommendations

This specification provides no recommendations.

This specification defines only simulation framework.

---

**END OF LONGITUDINAL SIMULATION SPECIFICATION**

