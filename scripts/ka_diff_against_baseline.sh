#!/bin/bash
# Diff Against Baseline Script
# Purpose: Generate diff report comparing experiment to baseline
# No intelligent judgment. Only diff generation.

set -e

EXPERIMENT_ID=$1
BASELINE_REF=${2:-baseline-v1.0}

if [ -z "$EXPERIMENT_ID" ]; then
    echo "Usage: $0 <experiment_id> [baseline_ref]"
    exit 1
fi

OUTPUT_DIR="phase_k_a/reports"
mkdir -p "$OUTPUT_DIR"

DIFF_REPORT="$OUTPUT_DIR/${EXPERIMENT_ID}_diff_report.txt"
FILES_CHANGED="$OUTPUT_DIR/${EXPERIMENT_ID}_files_changed.txt"
KEYWORD_SCAN="$OUTPUT_DIR/${EXPERIMENT_ID}_keyword_scan.txt"

echo "Generating diff report for: $EXPERIMENT_ID"
echo "Baseline reference: $BASELINE_REF"
echo ""

# Generate full diff
echo "Generating full diff..."
git diff "$BASELINE_REF"..HEAD > "$DIFF_REPORT"
echo "✅ Full diff saved to: $DIFF_REPORT"

# Generate file-by-file diff
echo "Generating file-by-file diff..."
git diff "$BASELINE_REF"..HEAD --name-status > "$FILES_CHANGED"
echo "✅ Files changed saved to: $FILES_CHANGED"

# Scan for prohibited keywords
echo "Scanning for prohibited keywords..."
git diff "$BASELINE_REF"..HEAD | grep -iE "should|recommend|best practice" > "$KEYWORD_SCAN" || true
if [ -s "$KEYWORD_SCAN" ]; then
    echo "⚠️  WARNING: Prohibited keywords found. See: $KEYWORD_SCAN"
else
    echo "✅ PASS: No prohibited keywords found"
    rm -f "$KEYWORD_SCAN"
fi

echo ""
echo "Diff report complete. Reports saved to: $OUTPUT_DIR"

