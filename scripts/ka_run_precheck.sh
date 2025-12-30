#!/bin/bash
# Run Pre-Check Script
# Purpose: Run pre-check checklist before experiment
# No intelligent judgment. Only check execution.

set -e

EXPERIMENT_ID=$1
BASELINE_REF=${2:-baseline-v1.0}

if [ -z "$EXPERIMENT_ID" ]; then
    echo "Usage: $0 <experiment_id> [baseline_ref]"
    exit 1
fi

echo "Running pre-check for experiment: $EXPERIMENT_ID"
echo "Baseline reference: $BASELINE_REF"
echo ""

# Check 1: Verify baseline reference
echo "Check 1: Verifying baseline reference..."
if ! git rev-parse --verify "$BASELINE_REF" >/dev/null 2>&1; then
    echo "❌ FAIL: Baseline reference '$BASELINE_REF' not found"
    exit 1
fi
echo "✅ PASS: Baseline reference exists"

# Check 2: Verify branch isolation
echo "Check 2: Verifying branch isolation..."
CURRENT_BRANCH=$(git branch --show-current)
if [ "$CURRENT_BRANCH" != "$EXPERIMENT_ID" ]; then
    echo "❌ FAIL: Not on experiment branch. Current: $CURRENT_BRANCH"
    exit 1
fi
echo "✅ PASS: On experiment branch: $CURRENT_BRANCH"

# Check 3: Verify change scope (manual review required)
echo "Check 3: Verifying change scope..."
CHANGED_FILES=$(git diff "$BASELINE_REF"..HEAD --name-only)
if [ -z "$CHANGED_FILES" ]; then
    echo "⚠️  WARNING: No changes detected. Is this intentional?"
else
    echo "✅ PASS: Changes detected in:"
    echo "$CHANGED_FILES"
fi

# Check 4: Run static scan for prohibited keywords
echo "Check 4: Scanning for prohibited keywords..."
PROHIBITED_FOUND=0
for file in $(git diff "$BASELINE_REF"..HEAD --name-only); do
    if git diff "$BASELINE_REF"..HEAD -- "$file" | grep -qiE "should|recommend|best practice"; then
        echo "❌ FAIL: Prohibited keywords found in $file"
        PROHIBITED_FOUND=1
    fi
done

if [ $PROHIBITED_FOUND -eq 1 ]; then
    echo "❌ FAIL: Prohibited keywords detected"
    exit 1
fi
echo "✅ PASS: No prohibited keywords detected"

# Check 5: Verify evidence pack paths exist (manual check required)
echo "Check 5: Verifying evidence pack paths..."
PASS_PATH="audit_evidence/${EXPERIMENT_ID}_pass"
FAIL_PATH="audit_evidence/${EXPERIMENT_ID}_fail"
if [ ! -d "$PASS_PATH" ] || [ ! -d "$FAIL_PATH" ]; then
    echo "⚠️  WARNING: Evidence pack paths may not exist. Create if needed."
else
    echo "✅ PASS: Evidence pack paths exist"
fi

echo ""
echo "Pre-check complete. Manual review of change scope and rollback steps required."

