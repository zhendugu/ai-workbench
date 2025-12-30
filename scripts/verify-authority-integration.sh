#!/bin/bash

# Authority Integration Verification Script
# 
# This script verifies that Authority Layer integration is properly enforced:
# 1. Checks for unauthorized fields (status, stage, progress, lifecycle)
# 2. Checks for parallel type definitions outside viewModels
# 3. Checks for direct Authority field access outside authorized boundaries

set -e

ERRORS=0

echo "=== Authority Integration Verification ==="
echo ""

# Check 1: No unauthorized fields in viewModels or component types
echo "Check 1: Scanning for unauthorized fields (status, stage, progress, lifecycle)..."
if grep -r -n -E "(status|stage|progress|lifecycle|readiness|maturity)" \
  --include="*.ts" \
  --include="*.tsx" \
  run_time_frontend/src/types/viewModels.ts \
  run_time_frontend/src/components/ 2>/dev/null | \
  grep -v "//.*status\|//.*stage\|//.*progress\|Status.*ViewModel\|status.*removed\|no.*status" | \
  grep -v "viewModels.ts.*methodologyIdentifier\|viewModels.ts.*freezeRecordIdentifier" > /tmp/auth_check_1.txt; then
  
  echo "❌ FAILED: Unauthorized fields found:"
  cat /tmp/auth_check_1.txt
  ERRORS=$((ERRORS + 1))
else
  echo "✅ PASSED: No unauthorized fields detected"
fi
echo ""

# Check 2: No parallel type definitions (Company, Cell, Role, etc.) outside viewModels
# NOTE: Component Props interfaces (e.g., CompanyIdentityViewProps) are allowed - they're React props, not Authority types
echo "Check 2: Scanning for parallel type definitions..."
if grep -r -n -E "^(export\s+)?(interface|type)\s+(Company|Cell|Role|FreezeRecord|Methodology|Relationship|Topology|FrozenCompany|FrozenSnapshot)\s*[<{]?" \
  --include="*.ts" \
  --include="*.tsx" \
  run_time_frontend/src/ \
  --exclude-dir=node_modules 2>/dev/null | \
  grep -v "viewModels.ts\|authorityTransform.ts\|authorityLoader.ts\|types/index.ts\|ViewModel\|Props\|interface.*Props" > /tmp/auth_check_2.txt; then
  
  echo "❌ FAILED: Parallel type definitions found outside authorized locations:"
  cat /tmp/auth_check_2.txt
  echo ""
  echo "   Authorized locations:"
  echo "   - run_time_frontend/src/types/viewModels.ts"
  echo "   - run_time_frontend/src/services/authorityTransform.ts"
  echo "   - run_time_frontend/src/services/authorityLoader.ts"
  echo "   - run_time_frontend/src/types/index.ts (re-exports only)"
  echo "   - Component Props interfaces are allowed (React props, not Authority types)"
  ERRORS=$((ERRORS + 1))
else
  echo "✅ PASSED: No parallel type definitions found"
fi
echo ""

# Check 3: Components must import from viewModels, not direct Authority types
echo "Check 3: Verifying component imports use viewModels..."
if grep -r -n "import.*Company.*from.*types\|import.*Cell.*from.*types\|import.*Role.*from.*types\|import.*FreezeRecord.*from.*types" \
  --include="*.tsx" \
  run_time_frontend/src/components/ 2>/dev/null | \
  grep -v "viewModels\|authorityTransform\|authorityLoader" > /tmp/auth_check_3.txt; then
  
  echo "❌ FAILED: Components importing Authority types directly (should use viewModels):"
  cat /tmp/auth_check_3.txt
  ERRORS=$((ERRORS + 1))
else
  echo "✅ PASSED: Components correctly use viewModels"
fi
echo ""

# Check 4: authorityLoader must be the only place that imports validateFrozenSnapshot
echo "Check 4: Verifying validation is centralized in authorityLoader..."
VALIDATION_IMPORTS=$(grep -r "import.*validateFrozenSnapshot" \
  --include="*.ts" \
  --include="*.tsx" \
  run_time_frontend/src/ 2>/dev/null | wc -l | tr -d ' ')

if [ "$VALIDATION_IMPORTS" -gt 1 ]; then
  echo "❌ FAILED: validateFrozenSnapshot imported in multiple places:"
  grep -r "import.*validateFrozenSnapshot" --include="*.ts" --include="*.tsx" run_time_frontend/src/
  ERRORS=$((ERRORS + 1))
elif [ "$VALIDATION_IMPORTS" -eq 0 ]; then
  echo "❌ FAILED: validateFrozenSnapshot not imported anywhere"
  ERRORS=$((ERRORS + 1))
else
  echo "✅ PASSED: validateFrozenSnapshot imported only in authorityLoader"
fi
echo ""

# Summary
if [ $ERRORS -eq 0 ]; then
  echo "=== All checks passed ==="
  exit 0
else
  echo "=== Verification failed: $ERRORS error(s) found ==="
  exit 1
fi

