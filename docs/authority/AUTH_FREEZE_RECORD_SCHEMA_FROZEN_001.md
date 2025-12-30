# Authority Schema: Freeze Record 001 (Frozen)

**Document ID**: AUTH-FREEZE-RECORD-SCHEMA-FROZEN-001

**Status**: FROZEN

**Frozen at**: 2025-12-28

**Frozen by**: Human Owner

**Authority Hierarchy**:
1. docs/frontend/DT_FE_DECISION_RECORD_001.md (HIGHEST - 最高语义裁决)
2. This document (AUTH_FREEZE_RECORD_SCHEMA_FROZEN_001.md)
3. All other Authority Layer documents

**Note**: If any ambiguity or conflict exists, DT_FE_DECISION_RECORD_001.md takes precedence.

**No New Semantics Clause**:
- This document is FROZEN. Any future changes must be in a new version file (e.g., AUTH_FREEZE_RECORD_SCHEMA_FROZEN_002.md), never by editing this document.
- Semantic changes require explicit human approval and a new versioned schema document.
- This document serves as the immutable baseline for Freeze Record authority schema.

---

# Authority Schema: Freeze Record 001

**Document ID**: AUTH-FREEZE-RECORD-SCHEMA-001

**Status**: DRAFT

**Date**: 2025-12-28

**Authority**: This document defines the authoritative fact model for Freeze Record entities.

**Scope**: Static fact schema only. Immutable record of freeze operation. No event semantics, no activation semantics.

---

## 1. What Is Freeze Record

**Factual Definition**:

Freeze Record is an **immutable record** of a freeze operation performed on a Company structural declaration.

Freeze Record documents **when** and **by whom** a Company was frozen.

Freeze Record is a **provenance fact** that provides audit trail and traceability.

---

## 2. Freeze Record Trigger Condition

### 2.1 Trigger Context

**Rule**: Freeze Record can only be created when:

- A Company exists in Design-Time mode (Draft state)
- A human explicitly performs the Freeze operation
- The Freeze operation completes successfully

**Forbidden Contexts**:
- Freeze Record cannot be created in Run-Time mode
- Freeze Record cannot be created for already-frozen Company
- Freeze Record cannot be created automatically
- Freeze Record cannot be created without human action

### 2.2 Single Source

**Rule**: Freeze Record is created **only** through the Design-Time Freeze operation.

**Meaning**:
- There is exactly one Freeze Record per frozen Company
- Freeze Record is created at the moment of freeze
- Freeze Record is immutable after creation
- Freeze Record cannot be created through any other mechanism

---

## 3. Authority Field Schema

### 3.1 Identity Fields

These fields identify which Freeze Record fact is being declared.

#### freeze_record_identifier

- **Type**: String
- **Format**: `FREEZE-{UUID}`
- **Authority**: System-generated, immutable
- **Meaning**: Unique identifier that distinguishes this Freeze Record from all other Freeze Record facts
- **Identity Declaration**: Yes

### 3.2 Frozen Object Reference

This field references what was frozen.

#### frozen_company_identifier

- **Type**: String (Company identifier reference)
- **Format**: `FROZEN-COMP-{UUID}`
- **Authority**: System-assigned at freeze moment
- **Meaning**: Identifier of the Company that was frozen
- **Reference**: References the frozen Company fact
- **Note**: This identifier is assigned at freeze and differs from the Draft identifier

### 3.3 Freeze Timestamp

This field records when the freeze occurred.

#### frozen_at

- **Type**: Timestamp (ISO 8601, precision to seconds)
- **Format**: `YYYY-MM-DDTHH:MM:SSZ`
- **Authority**: System-recorded at freeze moment
- **Meaning**: Point in time when the freeze operation occurred
- **Static Fact**: Yes - this timestamp never changes
- **Labeling**: Must be labeled as "Frozen at [timestamp]" in presentations
- **Forbidden Labels**: Must NOT use "Last updated", "Updated at", "Current", "Latest", "Recent", or any label implying activity or change
- **Nature**: This is a static timestamp representing when freeze occurred, not an active or changing time

### 3.4 Freeze Declarer

This field records who performed the freeze.

#### frozen_by

- **Type**: String (identifier)
- **Format**: Human identifier (name, username, or ID)
- **Authority**: Human-declared at freeze moment
- **Meaning**: Who declared this Company to be frozen
- **Static Fact**: Yes - this identifier never changes

### 3.5 Freeze Summary (Optional)

This field may contain human-provided summary or notes about the freeze.

#### freeze_summary

- **Type**: String (multi-line text, optional)
- **Format**: Human-readable text
- **Authority**: Human-declared (optional)
- **Meaning**: Optional human-provided summary or notes about why or how this freeze occurred
- **Optional**: Yes (may be empty)
- **Note**: This is for human documentation, not system use

### 3.6 Draft Reference (Optional)

This field may reference the Draft that was frozen.

#### draft_identifier

- **Type**: String (Draft identifier reference, optional)
- **Format**: `COMP-{UUID}` (the original Draft identifier)
- **Authority**: System-recorded at freeze moment (if available)
- **Meaning**: Identifier of the Draft that was frozen (if tracking is maintained)
- **Optional**: Yes (may not be available)
- **Purpose**: For traceability from Draft to Frozen Company

---

## 4. What Freeze Record Is NOT

### 4.1 Event Semantics

Freeze Record **is NOT**:

- A publish event
- An activation event
- A deployment event
- A release event
- A lifecycle event
- A state transition event

### 4.2 Operational Semantics

Freeze Record **is NOT**:

- An activation record
- A deployment record
- A launch record
- A startup record
- An execution trigger

### 4.3 Status Semantics

Freeze Record **is NOT**:

- A status change
- A state update
- An activity marker
- A current state indicator
- A latest status

---

## 5. Minimal Freeze Record Composition

### 5.1 Required Fields

A Freeze Record fact MUST contain:

- freeze_record_identifier (identity)
- frozen_company_identifier (reference to frozen Company)
- frozen_at (timestamp)
- frozen_by (declarer identifier)

**Minimum Fields**: 4

### 5.2 Optional Fields

A Freeze Record fact MAY contain:

- freeze_summary (human notes, optional)
- draft_identifier (Draft reference, optional)

**Note**: Both optional fields may be empty or absent.

---

## 6. Freeze Record Is Immutable

### 6.1 Immutability Rule

**Rule**: Freeze Record facts are **immutable** after creation.

**Meaning**:
- Freeze Record cannot be modified
- Freeze Record cannot be deleted
- Freeze Record cannot be updated
- Freeze Record cannot be changed
- Freeze Record is permanent

### 6.2 Single Version

**Rule**: There is exactly one Freeze Record per frozen Company.

**Meaning**:
- No versioning of Freeze Records
- No updates to Freeze Records
- No corrections to Freeze Records
- No revisions to Freeze Records
- One immutable record per freeze

---

## 7. Field Type Definitions

### 7.1 String Type

- Plain text
- No formatting requirements beyond encoding (UTF-8)
- No length limits defined in authority schema
- No validation rules beyond "string"

### 7.2 Timestamp Type

- ISO 8601 format
- Precision: seconds
- Timezone: UTC (Z suffix)
- Format: `YYYY-MM-DDTHH:MM:SSZ`
- Example: `2025-12-28T14:30:00Z`
- Static: Never changes after assignment

### 7.3 Identifier Type

- Opaque string
- System-generated format: `{PREFIX}-{UUID}`
- Must be unique within the system
- Immutable once assigned

### 7.4 Company Identifier Reference Type

- String that references a frozen Company identifier
- Format: `FROZEN-COMP-{UUID}`
- Must reference a Company fact that exists in frozen state
- Reference integrity is required (Company must exist)

### 7.5 Multi-line Text Type (Optional)

- Plain text that may contain line breaks
- UTF-8 encoding
- No formatting requirements
- May be empty (optional field)

---

## 8. Authority Enforcement

### 8.1 No Interpretation

Frontend, Backend, and Storage layers **cannot**:

- Interpret Freeze Record as an event
- Treat Freeze Record as activation
- Use Freeze Record to trigger actions
- Infer operational semantics from Freeze Record
- Add event semantics to Freeze Record

### 8.2 Fact Boundaries

Freeze Record facts are **complete** as defined. No additional facts may be inferred or added without extending this schema.

### 8.3 Read-Only Forever

Freeze Record:

- Is immutable after creation
- Cannot be modified by any layer
- Cannot be deleted
- Cannot be updated
- Is permanent record

---

## 9. Schema Summary

**Freeze Record Authority Schema**:

- **Identity Fields**: freeze_record_identifier
- **Reference Fields**: frozen_company_identifier, draft_identifier (optional)
- **Timestamp Fields**: frozen_at
- **Declarer Fields**: frozen_by
- **Summary Fields**: freeze_summary (optional)

**Total Fields**: 6 (4 required, 2 optional)

**Nature**: Immutable provenance record (not event, not activation)

**State**: Immutable (permanent fact)

**Trigger**: Design-Time Freeze operation only

---

## END OF FREEZE RECORD AUTHORITY SCHEMA

**Note**: This schema defines facts only. Implementation details, storage formats, API designs, and UI presentations are outside this schema's scope.

