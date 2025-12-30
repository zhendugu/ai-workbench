#!/bin/bash
# R-2E Minimal Red Team Execution Matrix

# Do not exit on error - continue with other runs
# set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../../../" && pwd)"
RUN_CONFIGS_DIR="$PROJECT_ROOT/phase_q/R2/run_configs_r2e"
RUN_ARCHIVE_DIR="$PROJECT_ROOT/phase_q/R2/EXECUTION_LOG_ARCHIVE_R2E"
PYTHON_SCRIPT="$SCRIPT_DIR/run_single_r2e.py"

# Create directories
mkdir -p "$RUN_CONFIGS_DIR"
mkdir -p "$RUN_ARCHIVE_DIR"

# Generate run configs if not exists
if [ ! -f "$RUN_CONFIGS_DIR/r2e_run_index.json" ]; then
    echo "Generating run configurations..."
    python3 "$SCRIPT_DIR/generate_r2e_run_configs.py" "$RUN_CONFIGS_DIR"
fi

# Load run index
RUN_INDEX="$RUN_CONFIGS_DIR/r2e_run_index.json"
if [ ! -f "$RUN_INDEX" ]; then
    echo "Error: r2e_run_index.json not found"
    exit 1
fi

# Get all run IDs
RUN_IDS=$(python3 -c "import json; data = json.load(open('$RUN_INDEX')); print(' '.join(data['runs']))")

echo "=== R-2E Minimal Red Team Execution ==="
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
    
    # Create run output directory (will fail if exists)
    RUN_OUTPUT_DIR="$RUN_ARCHIVE_DIR/${RUN_ID}"
    
    # Check if directory exists (prevent overwriting)
    if [ -d "$RUN_OUTPUT_DIR" ]; then
        echo "ERROR: Output directory already exists: $RUN_OUTPUT_DIR"
        echo "This indicates a potential overwrite. Aborting."
        exit 1
    fi
    
    # Create directory for log file
    mkdir -p "$RUN_OUTPUT_DIR"
    
    # Run attack (no auto-retry)
    python3 "$PYTHON_SCRIPT" "$CONFIG_FILE" "$RUN_OUTPUT_DIR" > "$RUN_OUTPUT_DIR/run.log" 2>&1
    EXIT_CODE=$?
    
    if [ $EXIT_CODE -eq 0 ]; then
        echo "Completed: $RUN_ID"
        COMPLETED=$((COMPLETED + 1))
    else
        echo "Failed: $RUN_ID (exit code: $EXIT_CODE)"
        FAILED=$((FAILED + 1))
        # Write FAIL verdict if not exists
        VERDICT_FILE="$RUN_OUTPUT_DIR/outputs.json"
        if [ ! -f "$VERDICT_FILE" ]; then
            python3 -c "
import json
from datetime import datetime
with open('$VERDICT_FILE', 'w') as f:
    json.dump({
        'run_id': '$RUN_ID',
        'verdict': 'FAIL',
        'timestamp': datetime.now().isoformat(),
        'error': 'Attack execution failed'
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

