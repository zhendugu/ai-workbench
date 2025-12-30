#!/bin/bash
# Rollback to Baseline Script
# Purpose: Rollback experiment branch to baseline state
# No intelligent judgment. Only rollback execution.

set -e

BASELINE_REF=${1:-baseline-v1.0}
DELETE_BRANCH=${2:-no}

echo "Rolling back to baseline: $BASELINE_REF"
echo ""

# Verify baseline exists
if ! git rev-parse --verify "$BASELINE_REF" >/dev/null 2>&1; then
    echo "Error: Baseline reference '$BASELINE_REF' not found"
    exit 1
fi

# Get current branch
CURRENT_BRANCH=$(git branch --show-current)
if [ "$CURRENT_BRANCH" = "$BASELINE_REF" ]; then
    echo "Already on baseline branch"
    exit 0
fi

# Switch to baseline
echo "Switching to baseline branch..."
git checkout "$BASELINE_REF"

# Verify baseline state
echo "Verifying baseline state..."
git status

# Delete experiment branch if requested
if [ "$DELETE_BRANCH" = "yes" ]; then
    echo "Deleting experiment branch: $CURRENT_BRANCH"
    git branch -D "$CURRENT_BRANCH" 2>/dev/null || echo "Branch already deleted or does not exist"
fi

echo ""
echo "✅ Rollback complete. Now on baseline: $BASELINE_REF"

