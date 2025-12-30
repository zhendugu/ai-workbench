#!/bin/bash
# Q4-2 Test Matrix Executor

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../../../" && pwd)"
RUN_CONFIGS_DIR="$PROJECT_ROOT/phase_q/Q4-2/run_configs"
RUN_ARCHIVE_DIR="$PROJECT_ROOT/phase_q/Q4-2/EXECUTION_LOG_ARCHIVE_Q4-2"
PYTHON_SCRIPT="$SCRIPT_DIR/run_single_q4_2.py"

# Create directories
mkdir -p "$RUN_CONFIGS_DIR"
mkdir -p "$RUN_ARCHIVE_DIR"

# Generate run configs if not exists
if [ ! -f "$RUN_CONFIGS_DIR/matrix_index.json" ]; then
    echo "Generating run configurations..."
    python3 "$SCRIPT_DIR/generate_run_configs_q4_2.py" "$RUN_CONFIGS_DIR"
fi

# Load matrix index
MATRIX_INDEX="$RUN_CONFIGS_DIR/matrix_index.json"
if [ ! -f "$MATRIX_INDEX" ]; then
    echo "Error: matrix_index.json not found"
    exit 1
fi

# Get all run IDs
RUN_IDS=$(python3 -c "import json; data = json.load(open('$MATRIX_INDEX')); print(' '.join(data['runs']))")

echo "=== Q4-2 Test Matrix Execution ==="
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
    
    # Create run directory (fail if already exists to prevent overwriting)
    RUN_OUTPUT_DIR="$RUN_ARCHIVE_DIR/${RUN_ID}"
    if [ -d "$RUN_OUTPUT_DIR" ]; then
        echo "ERROR: Output directory already exists: $RUN_OUTPUT_DIR"
        echo "This indicates a potential overwrite. Aborting."
        exit 1
    fi
    mkdir -p "$RUN_OUTPUT_DIR"
    
    # Run test (no auto-retry)
    python3 "$PYTHON_SCRIPT" "$CONFIG_FILE" "$RUN_OUTPUT_DIR" > "$RUN_OUTPUT_DIR/run.log" 2>&1
    EXIT_CODE=$?
    
    if [ $EXIT_CODE -eq 0 ]; then
        echo "Completed: $RUN_ID"
        COMPLETED=$((COMPLETED + 1))
    else
        echo "Failed: $RUN_ID (exit code: $EXIT_CODE)"
        FAILED=$((FAILED + 1))
        # Write FAIL verdict if not exists
        VERDICT_FILE="$RUN_OUTPUT_DIR/verdict.json"
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

