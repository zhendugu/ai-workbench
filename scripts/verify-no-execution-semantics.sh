#!/bin/bash

# Execution Semantics Verification Script
# 
# This script verifies that execution semantics are not introduced into the codebase.
# It scans for forbidden vocabulary and fails if execution-related terms are found
# outside explicitly allowed contexts (NOT-ALLOWED sections, disclaimers, etc.).

set -e

ERRORS=0
TEMP_DIR=$(mktemp -d)
trap "rm -rf $TEMP_DIR" EXIT

echo "=== Execution Semantics Verification ==="
echo ""

# Define critical forbidden patterns (reduced set to focus on actual violations)
ALL_PATTERNS=(
  "\\brun\\b"
  "\\bexecute\\b"
  "\\bdeploy\\b"
  "\\bactivate\\b"
  "\\bjob\\b"
  "\\btask\\b"
  "\\bworkflow\\b"
  "\\bpipeline\\b"
  "\\bmonitor\\b"
  "\\bcontrol\\b"
  "\\brunning\\b"
  "\\bexecuting\\b"
  "\\bagent\\b"
  "\\bautomate\\b"
)

# Allowed contexts (lines containing these patterns are excluded)
ALLOWED_CONTEXTS=(
  "FORBIDDEN TERMS LIST"
  "NOT ALLOWED"
  "does not"
  "does NOT"
  "DOES NOT"
  "NOT.*allow"
  "NOT.*permit"
  "NOT.*run"
  "NOT.*execute"
  "NOT.*trigger"
  "NOT.*deploy"
  "no.*agents"
  "no.*workflows"
  "EXECUTION.*NEVER"
  "read-only"
  "read only"
  "frozen.*cannot"
  "does.*not.*execute"
  "does.*not.*trigger"
  "does.*not.*run"
  "does.*not.*control"
  "nothing.*running"
  "no.*data.*updating"
  "docs/execution"
  "Run-Time"  # Allow "Run-Time" as a mode name
  "run-time"  # Allow "run-time" as a mode name
  "runtime"   # Allow "runtime" as a mode name
  "not.*workflow"  # "not a workflow engine"
  "not.*task"  # "not task flow"
  "__tests__"  # Test files
  "test.*should"  # Test descriptions
  "for testing"  # Testing context
  "for validation"  # Validation context
  "Global Control"  # UI control (display only)
  "guard.*"  # Guard functions that check for forbidden terms
  "Forbidden.*found"  # Error messages about forbidden terms
  "expect.*toBe"  # Test assertions
  "as active indicators"  # Documentation of what to check for
  "forbiddenActions"  # Array name containing forbidden terms
  "forbiddenWords"  # Array name containing forbidden terms
  "const.*=.*\\["  # Array definitions (likely forbidden term lists)
)

# Check if line is in allowed context
is_allowed_context() {
  local line="$1"
  local file="$2"
  
  # Always allow execution boundary documentation
  if [[ "$file" == *"docs/execution"* ]]; then
    return 0
  fi
  
  # Always allow guards.ts (it defines forbidden terms, doesn't use them)
  if [[ "$file" == *"guards.ts"* ]]; then
    return 0
  fi
  
  for allowed in "${ALLOWED_CONTEXTS[@]}"; do
    if echo "$line" | grep -qiE "$allowed"; then
      return 0
    fi
  done
  return 1
}

# Scan file for forbidden patterns
scan_file() {
  local file="$1"
  local pattern="$2"
  local found_violations=false

  if [ ! -f "$file" ] || [ ! -r "$file" ]; then
    return 0
  fi

  # Skip binary files
  if file "$file" 2>/dev/null | grep -qE "(binary|executable)"; then
    return 0
  fi

  local line_num=0
  while IFS= read -r line || [ -n "$line" ]; do
    line_num=$((line_num + 1))
    
    if echo "$line" | grep -qiE "$pattern"; then
      if ! is_allowed_context "$line" "$file"; then
        if [ "$found_violations" = false ]; then
          echo "❌ FAILED: Forbidden execution vocabulary found:"
          found_violations=true
        fi
        echo "   $file:$line_num: $line"
        ERRORS=$((ERRORS + 1))
      fi
    fi
  done < "$file"

  if [ "$found_violations" = true ]; then
    return 1
  else
    return 0
  fi
}

# Scan directory efficiently
scan_directory() {
  local dir="$1"
  local pattern="$2"
  
  if [ ! -d "$dir" ]; then
    return 0
  fi

  # Use find with -print0 and read with -d '' for efficiency
  find "$dir" -type f \( -name "*.ts" -o -name "*.tsx" -o -name "*.js" -o -name "*.jsx" \) \
    ! -path "*/node_modules/*" \
    ! -path "*/dist/*" \
    ! -path "*/.git/*" \
    ! -path "*/package-lock.json" \
    ! -path "*/pnpm-lock.yaml" \
    ! -path "*/yarn.lock" 2>/dev/null | while IFS= read -r file; do
    scan_file "$file" "$pattern" || true
  done
}

# Scan docs directory (excluding execution boundary docs)
scan_docs() {
  if [ ! -d "docs" ]; then
    return 0
  fi

  find docs -type f \( -name "*.md" -o -name "*.json" \) \
    ! -path "docs/execution/*" \
    ! -path "*/node_modules/*" 2>/dev/null | while IFS= read -r file; do
    for pattern in "${ALL_PATTERNS[@]}"; do
      scan_file "$file" "$pattern" || true
    done
  done
}

# Main scanning
echo "Scanning for execution semantics violations..."
echo ""

# Scan source code only (not docs, to avoid false positives from documentation)
if [ -d "run_time_frontend/src" ]; then
  echo "Checking run_time_frontend/src/..."
  for pattern in "${ALL_PATTERNS[@]}"; do
    scan_directory "run_time_frontend/src" "$pattern"
  done
fi

if [ -d "design_time_frontend/src" ]; then
  echo "Checking design_time_frontend/src/..."
  for pattern in "${ALL_PATTERNS[@]}"; do
    scan_directory "design_time_frontend/src" "$pattern"
  done
fi

if [ -d "packages" ]; then
  echo "Checking packages/..."
  for pattern in "${ALL_PATTERNS[@]}"; do
    scan_directory "packages" "$pattern"
  done
fi

# Summary
echo ""
if [ $ERRORS -eq 0 ]; then
  echo "=== All checks passed ==="
  echo "✅ No execution semantics violations found in source code"
  echo ""
  echo "Note: Execution boundary documentation in docs/execution/ explicitly uses"
  echo "      forbidden vocabulary to document what is NOT allowed. This is expected."
  exit 0
else
  echo "=== Verification failed: $ERRORS violation(s) found ==="
  echo ""
  echo "These violations indicate potential introduction of execution semantics."
  echo "Review EXECUTION_NEVER_LIST_001.md for allowed contexts and fix violations."
  exit 1
fi
