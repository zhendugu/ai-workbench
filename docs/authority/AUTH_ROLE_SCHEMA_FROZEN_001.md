# Authority Schema: Role 001 (Frozen)

**Document ID**: AUTH-ROLE-SCHEMA-FROZEN-001

**Status**: FROZEN

**Frozen at**: 2025-12-28

**Frozen by**: Human Owner

**Authority Hierarchy**:
1. docs/frontend/DT_FE_DECISION_RECORD_001.md (HIGHEST - 最高语义裁决)
2. This document (AUTH_ROLE_SCHEMA_FROZEN_001.md)
3. All other Authority Layer documents

**Note**: If any ambiguity or conflict exists, DT_FE_DECISION_RECORD_001.md takes precedence.

**No New Semantics Clause**:
- This document is FROZEN. Any future changes must be in a new version file (e.g., AUTH_ROLE_SCHEMA_FROZEN_002.md), never by editing this document.
- Semantic changes require explicit human approval and a new versioned schema document.
- This document serves as the immutable baseline for Role authority schema.

---

# Authority Schema: Role 001

**Document ID**: AUTH-ROLE-SCHEMA-001

**Status**: DRAFT

**Date**: 2025-12-28

**Authority**: This document defines the authoritative fact model for Role entities (as Cell constraints).

**Scope**: Static fact schema only. Role as attached constraint to Cell. No independent existence. No execution semantics.

---

## 1. What Is Role

**Factual Definition**:

Role is a **constraint attached to a Cell**.

Role is NOT an independent entity. Role cannot exist without being attached to a Cell.

Role declares constraint conditions that apply to the Cell it is attached to.

Role is a **declarative constraint**, not an executor, not an actor, not a role assignment.

---

## 2. Authority Field Schema

### 2.1 Identity Fields

These fields identify which Role constraint fact is being declared.

#### role_identifier

- **Type**: String
- **Format**: `ROLE-{UUID}`
- **Authority**: System-generated, immutable
- **Meaning**: Unique identifier that distinguishes this Role constraint from all other Role constraint facts
- **Identity Declaration**: Yes

#### role_name

- **Type**: String
- **Format**: Human-readable text
- **Authority**: Human-declared
- **Meaning**: Name of this Role constraint
- **Identity Declaration**: Yes

### 2.2 Constraint Type

This field declares the type of constraint.

#### constraint_type

- **Type**: Enumeration (string, constrained values)
- **Allowed Values**:
  - `allow` (允许) - This constraint allows something
  - `forbid` (禁止) - This constraint forbids something
  - `condition` (条件) - This constraint provides a condition
- **Authority**: Human-declared
- **Meaning**: Type of constraint being declared
- **Semantic Constraint**: Constraint type is a declaration, not an enforcement mechanism

### 2.3 Constraint Description

This field describes what this constraint declares.

#### constraint_description

- **Type**: String (multi-line text)
- **Format**: Human-readable text
- **Authority**: Human-declared
- **Meaning**: Description of what this constraint declares
- **Purpose**: Explains what the constraint means for the attached Cell
- **Declarative Text**: Yes

### 2.4 Cell Attachment Reference

This field references the Cell this Role constraint is attached to.

#### attached_to_cell_identifier

- **Type**: String (Cell identifier reference)
- **Format**: `CELL-{UUID}`
- **Authority**: System-assigned (Role cannot exist without Cell attachment)
- **Meaning**: Identifier of the Cell this Role constraint is attached to
- **Reference**: Must reference an existing Cell fact within the same Company
- **Required**: Yes - Role cannot exist without Cell attachment

---

## 3. What Role Is NOT

### 3.1 Independent Entity

Role **is NOT**:

- An independent entity
- A standalone fact
- A top-level concept
- A primary entity
- An entity that can exist without Cell attachment

### 3.2 Execution Entity

Role **is NOT**:

- An executor
- An actor
- A performer
- A worker
- An agent
- An instance

### 3.3 Assignment Entity

Role **is NOT**:

- A role assignment
- A job assignment
- A task assignment
- A responsibility assignment
- A person-to-role mapping
- An AI-to-role mapping

### 3.4 Operational Entity

Role **is NOT**:

- An operational constraint
- An enforcement mechanism
- A validation rule
- A business rule (beyond declarative constraint)
- An execution constraint

---

## 4. What Role Does NOT Contain

### 4.1 Lifecycle Fields

Role **does NOT contain**:

- Lifecycle state
- Activation status
- Active/inactive flags
- Status indicators

### 4.2 Execution Fields

Role **does NOT contain**:

- Execution status
- Running status
- Activity indicators
- Performance metrics

### 4.3 Assignment Fields

Role **does NOT contain**:

- Assigned to (person/AI)
- Assignment history
- Current assignments
- Assignment status

### 4.4 Dynamic Fields

Role **does NOT contain**:

- "Current" anything
- "Latest" anything
- "Recent" anything
- "Active" anything
- Time-based change indicators

---

## 5. Role Facts Are Attached Constraints

### 5.1 Attachment Nature

**Rule**: Role facts are **attached constraints** to Cell facts.

**Meaning**:
- Role cannot exist without Cell attachment
- Role is always attached to exactly one Cell
- Role cannot be moved to another Cell (must delete and recreate)
- Role is part of the Cell's constraint declaration
- Role is not an independent fact

### 5.2 Declarative Constraint

**Rule**: Role facts are **declarative constraints**, not enforcement mechanisms.

**Meaning**:
- Role declares what constraints apply to the Cell
- Role does not enforce constraints
- Role does not validate constraints
- Role does not execute constraints
- Role is a structural declaration, not an operational mechanism

### 5.3 Immutable After Freeze

Once the Company containing the Cell (and its attached Role constraints) is frozen:

- Role facts are immutable
- No Role fields may be modified
- No Role fields may be added
- No Role fields may be removed
- The constraint declarations are complete and permanent

---

## 6. Field Type Definitions

### 6.1 String Type

- Plain text
- No formatting requirements beyond encoding (UTF-8)
- No length limits defined in authority schema
- No validation rules beyond "string"

### 6.2 Identifier Type

- Opaque string
- System-generated format: `{PREFIX}-{UUID}`
- Must be unique within the Company
- Immutable once assigned

### 6.3 Cell Identifier Reference Type

- String that references an existing Cell identifier
- Format: `CELL-{UUID}`
- Must reference a Cell fact that exists in the same Company
- Reference integrity is required (Cell must exist)
- Required: Role cannot exist without Cell attachment

### 6.4 Constraint Type Enumeration

- String constrained to allowed values
- Allowed values: `allow`, `forbid`, `condition`
- Case-sensitive
- No additional values allowed without schema extension

### 6.5 Multi-line Text Type

- Plain text that may contain line breaks
- UTF-8 encoding
- No formatting requirements
- No length limits defined in authority schema

---

## 7. Authority Enforcement

### 7.1 No Interpretation

Frontend, Backend, and Storage layers **cannot**:

- Interpret Role as an independent entity
- Treat Role as an executor or actor
- Assign Role to persons or AI
- Use Role for operational enforcement
- Create operational entities from Role facts

### 7.2 Fact Boundaries

Role facts are **complete** as defined. No additional facts may be inferred or added without extending this schema.

### 7.3 Attachment Requirement

**Rule**: Role facts MUST be attached to a Cell fact.

**Enforcement**:
- Role cannot be created without Cell attachment
- Role cannot exist without Cell attachment
- Role attachment cannot be null or empty
- Role attachment must reference an existing Cell

### 7.4 Read-Only After Freeze

Once Company is frozen:

- All Role facts within that Company are immutable
- No Role fields may be modified
- No Role fields may be added
- No Role fields may be removed
- The constraint declarations are complete and permanent

---

## 8. Schema Summary

**Role Authority Schema**:

- **Identity Fields**: role_identifier, role_name
- **Constraint Fields**: constraint_type (enumeration), constraint_description
- **Attachment Field**: attached_to_cell_identifier (required reference)

**Total Fields**: 5

**Nature**: Attached constraint declaration (not independent entity, not executor)

**Attachment**: Required - must be attached to a Cell fact

**State**: Frozen (immutable fact) when contained in frozen Company

---

## END OF ROLE AUTHORITY SCHEMA

**Note**: This schema defines facts only. Implementation details, storage formats, API designs, and UI presentations are outside this schema's scope.

