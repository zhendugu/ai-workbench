#!/bin/bash
# Collect Evidence Skeleton Script
# Purpose: Generate empty evidence pack structure
# No intelligent judgment. Only structure creation.

set -e

EXPERIMENT_ID=$1

if [ -z "$EXPERIMENT_ID" ]; then
    echo "Usage: $0 <experiment_id>"
    echo "Example: $0 ka-1-default-selection"
    exit 1
fi

PASS_DIR="audit_evidence/${EXPERIMENT_ID}_pass"
FAIL_DIR="audit_evidence/${EXPERIMENT_ID}_fail"

# Create PASS evidence pack structure
echo "Creating PASS evidence pack structure..."
mkdir -p "$PASS_DIR/evidence/design"
mkdir -p "$PASS_DIR/checklist_results"

# Copy PASS templates
if [ -d "phase_k_a/evidence_templates/pass" ]; then
    cp phase_k_a/evidence_templates/pass/* "$PASS_DIR/" 2>/dev/null || true
fi

# Create FAIL evidence pack structure
echo "Creating FAIL evidence pack structure..."
mkdir -p "$FAIL_DIR/evidence/design"
mkdir -p "$FAIL_DIR/checklist_results"
mkdir -p "$FAIL_DIR/remediation"

# Copy FAIL templates
if [ -d "phase_k_a/evidence_templates/fail" ]; then
    cp phase_k_a/evidence_templates/fail/* "$FAIL_DIR/" 2>/dev/null || true
fi

echo "✅ Evidence pack structure created:"
echo "   PASS: $PASS_DIR"
echo "   FAIL: $FAIL_DIR"

