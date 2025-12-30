# Run-Time Frontend Snapshot Directory

**Purpose**: Static JSON files for Run-Time Frontend to load and validate frozen Authority snapshots.

**Location**: `public/snapshots/authority/{frozenCompanyIdentifier}/`

**Contract**:
- Each snapshot directory contains exactly 6 JSON files:
  1. `company.json` - Company fact (single object)
  2. `cells.json` - Array of Cell facts
  3. `roles.json` - Array of Role facts
  4. `topology.json` - Array of Relationship facts (Topology)
  5. `methodology.json` - Methodology fact (single object)
  6. `freeze_record.json` - FreezeRecord fact (single object)

**Loading Path**:
- Base URL: `/snapshots/authority` (served from `public/` directory)
- Full path: `/snapshots/authority/{frozenCompanyIdentifier}/{file}.json`
- Example: `/snapshots/authority/FROZEN-COMP-DEFAULT/company.json`

**Validation**:
- All JSON files MUST conform to Authority Layer schemas
- `validateFrozenSnapshot()` is called on the assembled snapshot
- Invalid snapshots are rejected and display "Invalid Snapshot" page

**Test Fixture**:
- `FROZEN-COMP-DEFAULT/` - Minimal valid snapshot for UI testing
- This fixture passes all Authority validation checks
- Used as default when no frozenId is provided in URL

**Note**: This is a read-only contract. No execution, state mutation, or backend services involved.

