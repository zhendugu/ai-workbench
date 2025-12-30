#!/bin/bash
# File Hash Verification Script
# Purpose: Verify file integrity by comparing computed hashes with stored hashes
# Status: READ-ONLY (no system modifications)

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BUNDLE_DIR="${SCRIPT_DIR}/../read_only_evidence_bundle"
HASH_FILE="${BUNDLE_DIR}/file_hashes.txt"

if [ ! -f "$HASH_FILE" ]; then
    echo "ERROR: Hash file not found: $HASH_FILE"
    exit 1
fi

echo "Verifying file hashes..."
echo ""

errors=0
while IFS='|' read -r hash path; do
    if [ -z "$hash" ] || [ -z "$path" ]; then
        continue
    fi
    
    full_path="${BUNDLE_DIR}/${path}"
    
    if [ ! -f "$full_path" ]; then
        echo "MISSING: $path"
        errors=$((errors + 1))
        continue
    fi
    
    computed_hash=$(shasum -a 256 "$full_path" | cut -d' ' -f1)
    
    if [ "$computed_hash" != "$hash" ]; then
        echo "HASH MISMATCH: $path"
        echo "  Expected: $hash"
        echo "  Computed: $computed_hash"
        errors=$((errors + 1))
    else
        echo "OK: $path"
    fi
done < "$HASH_FILE"

echo ""
if [ $errors -eq 0 ]; then
    echo "All file hashes verified successfully."
    exit 0
else
    echo "ERROR: $errors file(s) failed verification."
    exit 1
fi

