# Authority Schema: Company 001 (Frozen)

**Document ID**: AUTH-COMPANY-SCHEMA-FROZEN-001

**Status**: FROZEN

**Frozen at**: 2025-12-28

**Frozen by**: Human Owner

**Authority Hierarchy**:
1. docs/frontend/DT_FE_DECISION_RECORD_001.md (HIGHEST - 最高语义裁决)
2. This document (AUTH_COMPANY_SCHEMA_FROZEN_001.md)
3. All other Authority Layer documents

**Note**: If any ambiguity or conflict exists, DT_FE_DECISION_RECORD_001.md takes precedence.

**No New Semantics Clause**:
- This document is FROZEN. Any future changes must be in a new version file (e.g., AUTH_COMPANY_SCHEMA_FROZEN_002.md), never by editing this document.
- Semantic changes require explicit human approval and a new versioned schema document.
- This document serves as the immutable baseline for Company authority schema.

---

# Authority Schema: Company 001

**Document ID**: AUTH-COMPANY-SCHEMA-001

**Status**: DRAFT

**Date**: 2025-12-28

**Authority**: This document defines the authoritative fact model for Company entities.

**Scope**: Static fact schema only. No state machines, no execution semantics, no lifecycle management.

---

## 1. What Is Company

**Factual Definition**:

Company is the semantic anchor point for a structural declaration of an AI virtual company.

Company is a **frozen structural fact** that exists after a human decision to freeze a design.

Company provides answers to the question: "What is the declared structure of this virtual company?"

---

## 2. Authority Field Schema

### 2.1 Identity Fields

These fields are **identity declarations**. They identify which Company fact is being declared.

#### company_identifier

- **Type**: String
- **Format**: `COMP-{UUID}` (for Draft) or `FROZEN-COMP-{UUID}` (for Frozen)
- **Authority**: System-generated, immutable
- **Meaning**: Unique identifier that distinguishes this Company from all other Company facts
- **Identity Declaration**: Yes

#### company_name

- **Type**: String
- **Format**: Human-readable text
- **Authority**: Human-declared
- **Meaning**: Name given to this Company structural declaration
- **Identity Declaration**: Yes

### 2.2 Descriptive Fields

These fields are **descriptive text**. They describe what this Company structural declaration represents.

#### company_description

- **Type**: String (multi-line text)
- **Format**: Human-readable text
- **Authority**: Human-declared
- **Meaning**: Human-readable description of what this Company structural declaration represents
- **Identity Declaration**: No
- **Descriptive Text**: Yes

### 2.3 Provenance Fields

These fields record **when and by whom** this Company fact was frozen.

#### frozen_at

- **Type**: Timestamp (ISO 8601, precision to seconds)
- **Format**: `YYYY-MM-DDTHH:MM:SSZ`
- **Authority**: System-recorded at freeze moment
- **Meaning**: Point in time when this Company was frozen
- **Static Fact**: Yes - this timestamp never changes
- **Note**: This is NOT "last updated" or "current time". It is the immutable freeze timestamp.

#### frozen_by

- **Type**: String (identifier)
- **Format**: Human identifier (name, username, or ID)
- **Authority**: Human-declared at freeze moment
- **Meaning**: Who declared this Company to be frozen
- **Static Fact**: Yes - this identifier never changes

---

## 3. What Company Does NOT Contain

### 3.1 State Machine Fields

Company **does NOT contain**:

- Execution state
- Running status
- Active/inactive flags
- Status indicators
- State transitions
- Status history

### 3.2 Execution Fields

Company **does NOT contain**:

- Runtime flags
- Execution indicators
- Process identifiers
- Activity markers
- Performance metrics

### 3.3 Lifecycle Fields

Company **does NOT contain**:

- Lifecycle state
- Maturity indicators
- Progress markers
- Completion status
- Evolution stages

### 3.4 Dynamic Fields

Company **does NOT contain**:

- "Current" anything
- "Latest" anything
- "Recent" anything
- "Active" anything
- Time-based change indicators

---

## 4. Company Facts Are Produced Only Through Freeze

### 4.1 Freeze As Authority Source

**Rule**: Company authoritative facts are produced **only** through the Freeze operation.

**Meaning**:
- Draft state is not an authoritative fact
- Only Frozen Company represents an authoritative structural fact
- Freeze is the human declaration that transforms a draft into a fact

### 4.2 Draft vs Frozen

**Draft Company**:
- Exists in Design-Time mode
- Is mutable and editable
- Is NOT an authoritative fact
- Does NOT have frozen_at or frozen_by fields

**Frozen Company**:
- Exists in Run-Time mode
- Is immutable and read-only
- IS an authoritative fact
- Has frozen_at and frozen_by fields
- Can be read and referenced but never modified

### 4.3 Authority Boundary

**Authority Layer Rule**:
- Only Frozen Company facts are authoritative
- Draft Company is outside the Authority Layer scope
- Frontend may read Draft data, but only Frozen Company is "fact"

---

## 5. Field Type Definitions

### 5.1 String Type

- Plain text
- No formatting requirements beyond encoding (UTF-8)
- No length limits defined in authority schema
- No validation rules beyond "string"

### 5.2 Timestamp Type

- ISO 8601 format
- Precision: seconds
- Timezone: UTC (Z suffix)
- Format: `YYYY-MM-DDTHH:MM:SSZ`
- Example: `2025-12-28T14:30:00Z`

### 5.3 Identifier Type

- Opaque string
- System-generated format: `{PREFIX}-{UUID}`
- Must be unique within the system
- Immutable once assigned

---

## 6. Authority Enforcement

### 6.1 No Interpretation

Frontend, Backend, and Storage layers **cannot**:

- Interpret Company fields to mean something not declared here
- Add semantic meaning to fields beyond what is stated
- Infer additional fields or properties
- Create derived facts from Company facts

### 6.2 Fact Boundaries

Company facts are **complete** as defined. No additional facts may be inferred or added without extending this schema.

### 6.3 Read-Only After Freeze

Once Company is frozen:

- All fields are immutable
- No fields may be modified
- No fields may be added
- No fields may be removed
- The fact is complete and permanent

---

## 7. Schema Summary

**Company Authority Schema**:

- **Identity Fields**: company_identifier, company_name
- **Descriptive Fields**: company_description
- **Provenance Fields**: frozen_at, frozen_by

**Total Fields**: 5

**Authority Source**: Freeze operation only

**State**: Frozen (immutable fact)

---

## END OF COMPANY AUTHORITY SCHEMA

**Note**: This schema defines facts only. Implementation details, storage formats, API designs, and UI presentations are outside this schema's scope.

