# Authority Integration Test Fixtures

**Purpose**: Test fixtures for verifying Authority Layer integration and validation.

## Invalid Snapshot Fixtures

### `invalid_snapshot_with_status.json`

**Invalid Field**: `status: "frozen"` in Company object

**Violation**: Company schema (AUTH_COMPANY_SCHEMA_FROZEN_001.md) does not include `status` field. This violates G-3 (no state machine concepts).

**Expected Result**: `validateFrozenSnapshot()` should reject this snapshot with an error identifying the unauthorized `status` field.

**Usage**:
```bash
# Test with validation (requires built Authority package)
node -e "const {validateFrozenSnapshot} = require('../packages/authority/dist/validate.js'); const fs = require('fs'); const invalid = JSON.parse(fs.readFileSync('invalid_snapshot_with_status.json', 'utf8')); const result = validateFrozenSnapshot(invalid); console.log('Valid:', result.valid); result.errors.forEach(e => console.log(e.message));"
```

## Test Scripts

### `test_negative_validation.ts`

**Purpose**: Verify that Authority validation correctly rejects invalid payloads.

**Execution**:
```bash
npx ts-node test_fixtures/test_negative_validation.ts
```

**Expected Output**: Test should pass, confirming that validation rejects the invalid snapshot.

---

**Note**: These fixtures are used for regression testing to ensure Authority boundaries are enforced.

