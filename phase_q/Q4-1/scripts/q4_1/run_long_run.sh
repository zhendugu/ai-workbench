#!/bin/bash
# Long Run Test Executor (≥10k Epochs)

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../../../../" && pwd)"
RUN_ARCHIVE_DIR="$PROJECT_ROOT/phase_q/Q4-1/RUN_LOG_ARCHIVE_Q4-1"
PYTHON_SCRIPT="$SCRIPT_DIR/run_single_epoch_test.py"

# Long run configurations
LONG_RUNS=(
    "run_p5_s0"  # P0 baseline, 10k epochs
    "run_p5_s1"  # P3 high concurrency, 10k epochs
)

echo "=== Long Run Test Execution ==="
echo "Total long runs: ${#LONG_RUNS[@]}"
echo ""

# Check if configs exist, if not generate them
RUN_CONFIGS_DIR="$PROJECT_ROOT/phase_q/Q4-1/run_configs"
if [ ! -f "$RUN_CONFIGS_DIR/matrix_index.json" ]; then
    echo "Generating run configurations..."
    python3 "$SCRIPT_DIR/generate_run_configs.py" "$RUN_CONFIGS_DIR"
fi

# Execute long runs
for RUN_ID in "${LONG_RUNS[@]}"; do
    CONFIG_FILE="$RUN_CONFIGS_DIR/${RUN_ID}.json"
    
    if [ ! -f "$CONFIG_FILE" ]; then
        echo "Error: Config file not found: $CONFIG_FILE"
        exit 1
    fi
    
    echo "Running long run: $RUN_ID"
    echo "This may take a while (10k epochs)..."
    
    # Create run directory first
    mkdir -p "$RUN_ARCHIVE_DIR/${RUN_ID}"
    
    # Run test and capture exit code properly
    python3 "$PYTHON_SCRIPT" "$CONFIG_FILE" "$RUN_ARCHIVE_DIR" > "$RUN_ARCHIVE_DIR/${RUN_ID}/run.log" 2>&1
    EXIT_CODE=$?
    
    if [ $EXIT_CODE -eq 0 ]; then
        echo "Completed: $RUN_ID"
    else
        echo "Failed: $RUN_ID (exit code: $EXIT_CODE)"
        exit 1
    fi
    
    echo ""
done

echo "=== Long Run Execution Complete ==="

