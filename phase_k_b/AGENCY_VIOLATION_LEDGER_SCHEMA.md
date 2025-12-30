# Agency Violation Ledger Schema

**Document Status**: NON-CANONICAL / DESIGN-BOUNDARY  
**Document Type**: Schema Specification  
**Date**: 2026-01-10  
**Work Order**: WO-KB-2-AGENCY-GOVERNANCE-ENFORCEMENT-RULES

---

## Purpose

This document defines the immutable log schema for agency violations.

All fields are structural. No narrative explanation fields. No discretionary fields.

---

## Schema Definition

### Field 1: violation_id

**Type**: String (unique identifier)

**Format**: `VIOLATION-YYYYMMDD-HHMMSS-{HASH}`

**Example**: `VIOLATION-20260110-143022-A1B2C3`

**Required**: YES

**Immutable**: YES (cannot be modified after creation)

---

### Field 2: timestamp

**Type**: ISO 8601 timestamp (UTC)

**Format**: `YYYY-MM-DDTHH:MM:SSZ`

**Example**: `2026-01-10T14:30:22Z`

**Required**: YES

**Immutable**: YES

---

### Field 3: change_reference

**Type**: String (git commit hash, PR number, or equivalent)

**Format**: Commit hash (40 characters) or PR number format

**Example**: `a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0`

**Required**: YES

**Immutable**: YES

---

### Field 4: violated_rule_id

**Type**: String (rule ID from AGENCY_GOVERNANCE_RULESET.md)

**Format**: Rule ID format (e.g., `G-RULE-001`)

**Example**: `G-RULE-001`

**Required**: YES

**Immutable**: YES

**Allowed Values**: G-RULE-001 through G-RULE-012

---

### Field 5: structural_evidence

**Type**: String (code snippet, file path, line number)

**Format**: JSON string with structure: `{"file": "path/to/file", "line": 123, "snippet": "code snippet"}`

**Example**: `{"file": "frontend_app/capabilities.html", "line": 42, "snippet": "<input type=\"checkbox\" checked>"}`

**Required**: YES

**Immutable**: YES

---

### Field 6: classification_category

**Type**: String (category from CHANGE_CLASSIFICATION_MATRIX.md)

**Format**: Category name

**Example**: `Prohibited Agency`

**Required**: YES

**Immutable**: YES

**Allowed Values**: `Non-Agency`, `Declared Agency`, `Prohibited Agency`

---

### Field 7: gate_id

**Type**: String (gate ID from REVIEW_GATE_DEFINITION.md)

**Format**: Gate ID format (e.g., `GATE-PRE-MERGE`)

**Example**: `GATE-PRE-MERGE`

**Required**: YES

**Immutable**: YES

**Allowed Values**: `GATE-PRE-MERGE`, `GATE-PRE-RELEASE`, `GATE-POST-CHANGE-AUDIT`

---

### Field 8: resolution

**Type**: String (resolution action)

**Format**: Resolution action name

**Example**: `rollback`

**Required**: YES

**Immutable**: NO (can be updated when resolution is applied)

**Allowed Values**: `rollback`, `accept`, `freeze`, `pending`

**Initial Value**: `pending`

---

### Field 9: resolution_timestamp

**Type**: ISO 8601 timestamp (UTC) or null

**Format**: `YYYY-MM-DDTHH:MM:SSZ` or `null`

**Example**: `2026-01-10T14:35:00Z`

**Required**: NO (null if resolution is pending)

**Immutable**: NO (can be updated when resolution is applied)

---

### Field 10: resolution_reference

**Type**: String (git commit hash, PR number, or equivalent) or null

**Format**: Commit hash or PR number format or `null`

**Example**: `b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1`

**Required**: NO (null if resolution is pending)

**Immutable**: NO (can be updated when resolution is applied)

---

## Schema JSON Example

```json
{
  "violation_id": "VIOLATION-20260110-143022-A1B2C3",
  "timestamp": "2026-01-10T14:30:22Z",
  "change_reference": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0",
  "violated_rule_id": "G-RULE-001",
  "structural_evidence": "{\"file\": \"frontend_app/capabilities.html\", \"line\": 42, \"snippet\": \"<input type=\\\"checkbox\\\" checked>\"}",
  "classification_category": "Prohibited Agency",
  "gate_id": "GATE-PRE-MERGE",
  "resolution": "rollback",
  "resolution_timestamp": "2026-01-10T14:35:00Z",
  "resolution_reference": "b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1"
}
```

---

## Schema Constraints

**Immutable Fields**: violation_id, timestamp, change_reference, violated_rule_id, structural_evidence, classification_category, gate_id

**Mutable Fields**: resolution, resolution_timestamp, resolution_reference

**Required Fields**: All fields except resolution_timestamp and resolution_reference (required after resolution is set)

**Validation Rules**:
- violated_rule_id must be valid rule ID (G-RULE-001 through G-RULE-012)
- classification_category must be valid category (Non-Agency, Declared Agency, Prohibited Agency)
- gate_id must be valid gate ID (GATE-PRE-MERGE, GATE-PRE-RELEASE, GATE-POST-CHANGE-AUDIT)
- resolution must be valid resolution action (rollback, accept, freeze, pending)

---

## No Recommendations

This schema provides no recommendations.

This schema provides no design advice.

This schema states only schema specification.

---

**END OF AGENCY VIOLATION LEDGER SCHEMA**

