#!/bin/bash
# Structure Integrity Verification Script
# Purpose: Verify evidence bundle structure matches expected format
# Status: READ-ONLY (no system modifications)

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BUNDLE_DIR="${SCRIPT_DIR}/../read_only_evidence_bundle"
STRUCTURE_FILE="${BUNDLE_DIR}/structure_manifest.txt"

if [ ! -f "$STRUCTURE_FILE" ]; then
    echo "ERROR: Structure manifest not found: $STRUCTURE_FILE"
    exit 1
fi

echo "Verifying structure integrity..."
echo ""

errors=0
while IFS='|' read -r path type; do
    if [ -z "$path" ] || [ -z "$type" ]; then
        continue
    fi
    
    full_path="${BUNDLE_DIR}/${path}"
    
    if [ "$type" = "FILE" ]; then
        if [ ! -f "$full_path" ]; then
            echo "MISSING FILE: $path"
            errors=$((errors + 1))
        fi
    elif [ "$type" = "DIR" ]; then
        if [ ! -d "$full_path" ]; then
            echo "MISSING DIRECTORY: $path"
            errors=$((errors + 1))
        fi
    fi
done < "$STRUCTURE_FILE"

echo ""
if [ $errors -eq 0 ]; then
    echo "Structure integrity verified successfully."
    exit 0
else
    echo "ERROR: $errors structure element(s) missing."
    exit 1
fi

