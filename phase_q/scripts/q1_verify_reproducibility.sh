#!/bin/bash
# Verify reproducibility of simulation runs.

# This script verifies that two simulation runs with the same input set and seed
# produce identical log files (same hash).

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Parse arguments
LOG1=""
LOG2=""

while [[ $# -gt 0 ]]; do
    case $1 in
        --log1)
            LOG1="$2"
            shift 2
            ;;
        --log2)
            LOG2="$2"
            shift 2
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

if [ -z "$LOG1" ] || [ -z "$LOG2" ]; then
    echo "Usage: $0 --log1 <log_file_1> --log2 <log_file_2>"
    exit 1
fi

if [ ! -f "$LOG1" ]; then
    echo "Error: Log file 1 not found: $LOG1"
    exit 1
fi

if [ ! -f "$LOG2" ]; then
    echo "Error: Log file 2 not found: $LOG2"
    exit 1
fi

# Compute hashes
HASH1=$(shasum -a 256 "$LOG1" | cut -d' ' -f1)
HASH2=$(shasum -a 256 "$LOG2" | cut -d' ' -f1)

echo "Log file 1: $LOG1"
echo "Hash 1: $HASH1"
echo ""
echo "Log file 2: $LOG2"
echo "Hash 2: $HASH2"
echo ""

if [ "$HASH1" = "$HASH2" ]; then
    echo "✅ Reproducibility verified: Log files are identical"
    exit 0
else
    echo "❌ Reproducibility failed: Log files differ"
    exit 1
fi

