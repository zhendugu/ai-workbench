#!/bin/bash
# Reference Consistency Verification Script
# Purpose: Verify all file references in Phase K documents point to existing files
# Status: READ-ONLY (no system modifications)

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BUNDLE_DIR="${SCRIPT_DIR}/../read_only_evidence_bundle"

echo "Verifying reference consistency..."
echo ""

errors=0

# Check Phase K-B synthesis documents for broken references
for doc in "${BUNDLE_DIR}"/phase_k_b/*.md; do
    if [ ! -f "$doc" ]; then
        continue
    fi
    
    doc_name=$(basename "$doc")
    echo "Checking references in: $doc_name"
    
    # Extract file references (patterns like `path/to/file.md` or `audit_evidence/...`)
    while IFS= read -r line; do
        # Match markdown link patterns and backtick file paths
        if echo "$line" | grep -qE '`[^`]+\.(md|json)`|\[.*\]\([^)]+\.(md|json)\)'; then
            ref=$(echo "$line" | sed -E 's/.*`([^`]+\.(md|json))`.*/\1/' | sed -E 's/.*\[.*\]\(([^)]+\.(md|json))\).*/\1/')
            
            if [ -n "$ref" ]; then
                # Check if reference exists (relative to bundle root or absolute)
                if [ ! -f "${BUNDLE_DIR}/${ref}" ] && [ ! -f "${BUNDLE_DIR}/../${ref}" ] && [ ! -f "$ref" ]; then
                    echo "  BROKEN REFERENCE: $ref (in $doc_name)"
                    errors=$((errors + 1))
                fi
            fi
        fi
    done < "$doc"
done

echo ""
if [ $errors -eq 0 ]; then
    echo "Reference consistency verified successfully."
    exit 0
else
    echo "ERROR: $errors broken reference(s) found."
    exit 1
fi

