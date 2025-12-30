#!/bin/bash
# Execute Q-2 longitudinal adversarial simulation matrix.

# This script runs all 54 runs defined in RUN_MATRIX_DEFINITION.md
# All runs are deterministic and reproducible.

set -e
set -o pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"
RUNS_DIR="$PROJECT_ROOT/phase_q/runs"

# Create runs directory if it doesn't exist
mkdir -p "$RUNS_DIR"

# Strategies
STRATEGIES=("STRATEGY-SLOW-DRIFT" "STRATEGY-BURST-THEN-STABILIZE" "STRATEGY-ALTERNATING-NOISE")

# Human models
MODELS=("MODEL-STRICT-SOVEREIGN" "MODEL-FATIGUED-APPROVER" "MODEL-DELEGATING-OPTIMIZER")

# Seeds
SEEDS=(42 123 999)

# Horizons (steps)
HORIZONS=(200 2000)

# Run counter
RUN_COUNT=0

# Execute all runs
for strategy in "${STRATEGIES[@]}"; do
    for model in "${MODELS[@]}"; do
        for seed in "${SEEDS[@]}"; do
            for horizon in "${HORIZONS[@]}"; do
                RUN_COUNT=$((RUN_COUNT + 1))
                RUN_ID=$(printf "run_%03d" $RUN_COUNT)
                
                # Create run directory
                RUN_DIR="$RUNS_DIR/$RUN_ID"
                mkdir -p "$RUN_DIR/inputs" "$RUN_DIR/logs" "$RUN_DIR/metrics" "$RUN_DIR/hashes"
                
                # Generate input set
                python3 "$PROJECT_ROOT/phase_q/scripts/q1_generate_input_sets.py" \
                    --output "$RUN_DIR/inputs/" \
                    --input_set_id "input_set_$RUN_ID" \
                    > "$RUN_DIR/inputs/input_generation.log" 2>&1
                INPUT_SET="$RUN_DIR/inputs/input_set_${RUN_ID}.json"
                
                # Load strategy and model configs
                # Convert strategy/model IDs to lowercase filenames
                # Remove "STRATEGY-" and "MODEL-" prefixes, then convert to lowercase with underscores
                STRATEGY_NAME=$(echo "$strategy" | sed 's/^STRATEGY-//' | tr '[:upper:]' '[:lower:]' | tr '-' '_')
                MODEL_NAME=$(echo "$model" | sed 's/^MODEL-//' | tr '[:upper:]' '[:lower:]' | tr '-' '_')
                STRATEGY_FILE="$PROJECT_ROOT/phase_q/strategies/strategy_${STRATEGY_NAME}.json"
                MODEL_FILE="$PROJECT_ROOT/phase_q/human_models/model_${MODEL_NAME}.json"
                
                # Run simulation
                LOG_FILE="$RUN_DIR/logs/session_${RUN_ID}.jsonl"
                python3 "$PROJECT_ROOT/phase_q/scripts/q1_run_simulation.py" \
                    --input "$INPUT_SET" \
                    --seed "$seed" \
                    --strategy "$STRATEGY_FILE" \
                    --human_model "$MODEL_FILE" \
                    --output "$RUN_DIR/logs/" \
                    --horizon "$horizon" \
                    --session_id "session_${RUN_ID}" \
                    > "$RUN_DIR/logs/simulation.log" 2>&1
                
                # Compute metrics
                METRICS_FILE="$RUN_DIR/metrics/session_${RUN_ID}_metrics.json"
                python3 "$PROJECT_ROOT/phase_q/scripts/q1_compute_metrics.py" \
                    --log "$LOG_FILE" \
                    --output "$RUN_DIR/metrics/" \
                    > "$RUN_DIR/metrics/computation.log" 2>&1
                
                # Compute hashes
                shasum -a 256 "$INPUT_SET" > "$RUN_DIR/hashes/inputs.sha256"
                shasum -a 256 "$LOG_FILE" > "$RUN_DIR/hashes/logs.sha256"
                shasum -a 256 "$METRICS_FILE" > "$RUN_DIR/hashes/metrics.sha256"
                
                # Save run metadata
                cat > "$RUN_DIR/run_metadata.json" <<EOF
{
  "run_id": "$RUN_ID",
  "strategy": "$strategy",
  "human_model": "$model",
  "seed": $seed,
  "horizon": $horizon,
  "steps": $horizon,
  "execution_timestamp": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
}
EOF
                
                echo "Completed: $RUN_ID ($strategy, $model, seed=$seed, H=$horizon)"
            done
        done
    done
done

echo "Total runs completed: $RUN_COUNT"

