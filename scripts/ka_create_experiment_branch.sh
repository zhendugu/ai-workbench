#!/bin/bash
# Create Experiment Branch Script
# Purpose: Create new experiment branch from baseline
# No intelligent judgment. Only branch creation.

set -e

EXPERIMENT_ID=$1
BASELINE_REF=${2:-baseline-v1.0}

if [ -z "$EXPERIMENT_ID" ]; then
    echo "Usage: $0 <experiment_id> [baseline_ref]"
    echo "Example: $0 ka-1-default-selection baseline-v1.0"
    exit 1
fi

# Verify baseline exists
if ! git rev-parse --verify "$BASELINE_REF" >/dev/null 2>&1; then
    echo "Error: Baseline reference '$BASELINE_REF' not found"
    exit 1
fi

# Create and switch to new branch
git checkout -b "$EXPERIMENT_ID" "$BASELINE_REF"

# Verify branch creation
CURRENT_BRANCH=$(git branch --show-current)
if [ "$CURRENT_BRANCH" != "$EXPERIMENT_ID" ]; then
    echo "Error: Branch creation failed"
    exit 1
fi

echo "✅ Experiment branch created: $EXPERIMENT_ID"
echo "✅ Branch is based on: $BASELINE_REF"

