#!/bin/bash
# Epoch Stress Run Matrix Executor

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../../../../" && pwd)"
RUN_CONFIGS_DIR="$PROJECT_ROOT/phase_q/Q4-1/run_configs"
RUN_ARCHIVE_DIR="$PROJECT_ROOT/phase_q/Q4-1/RUN_LOG_ARCHIVE_Q4-1"
PYTHON_SCRIPT="$SCRIPT_DIR/run_single_epoch_test.py"

# Create directories
mkdir -p "$RUN_CONFIGS_DIR"
mkdir -p "$RUN_ARCHIVE_DIR"

# Generate run configs if not exists
if [ ! -f "$RUN_CONFIGS_DIR/matrix_index.json" ]; then
    echo "Generating run configurations..."
    python3 "$SCRIPT_DIR/generate_run_configs.py" "$RUN_CONFIGS_DIR"
fi

# Load matrix index
MATRIX_INDEX="$RUN_CONFIGS_DIR/matrix_index.json"
if [ ! -f "$MATRIX_INDEX" ]; then
    echo "Error: matrix_index.json not found"
    exit 1
fi

# Get all run IDs
RUN_IDS=$(python3 -c "import json; data = json.load(open('$MATRIX_INDEX')); print(' '.join(data['runs']))")

echo "=== Epoch Stress Run Matrix Execution ==="
echo "Total runs: $(echo $RUN_IDS | wc -w)"
echo ""

# Execute each run
COMPLETED=0
FAILED=0

for RUN_ID in $RUN_IDS; do
    CONFIG_FILE="$RUN_CONFIGS_DIR/${RUN_ID}.json"
    
    if [ ! -f "$CONFIG_FILE" ]; then
        echo "Warning: Config file not found: $CONFIG_FILE"
        continue
    fi
    
    echo "Running: $RUN_ID"
    
    # Run test (don't exit on failure)
    # Create run directory first
    mkdir -p "$RUN_ARCHIVE_DIR/${RUN_ID}"
    
    # Run test and capture exit code properly
    python3 "$PYTHON_SCRIPT" "$CONFIG_FILE" "$RUN_ARCHIVE_DIR" > "$RUN_ARCHIVE_DIR/${RUN_ID}/run.log" 2>&1
    EXIT_CODE=$?
    
    if [ $EXIT_CODE -eq 0 ]; then
        echo "Completed: $RUN_ID"
        COMPLETED=$((COMPLETED + 1))
    else
        echo "Failed: $RUN_ID (exit code: $EXIT_CODE)"
        FAILED=$((FAILED + 1))
        # Write FAIL verdict if not exists
        VERDICT_FILE="$RUN_ARCHIVE_DIR/${RUN_ID}/verdict.json"
        if [ ! -f "$VERDICT_FILE" ]; then
            python3 -c "
import json
from datetime import datetime
with open('$VERDICT_FILE', 'w') as f:
    json.dump({
        'run_id': '$RUN_ID',
        'verdict': 'FAIL',
        'timestamp': datetime.now().isoformat(),
        'error': 'Test execution failed'
    }, f, indent=2)
"
        fi
    fi
    
    echo ""
done

echo "=== Execution Summary ==="
echo "Completed: $COMPLETED"
echo "Failed: $FAILED"
echo "Total: $((COMPLETED + FAILED))"

