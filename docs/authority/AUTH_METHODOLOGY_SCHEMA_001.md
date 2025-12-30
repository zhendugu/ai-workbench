# Authority Schema: Methodology 001

**Document ID**: AUTH-METHODOLOGY-SCHEMA-001

**Status**: DRAFT

**Date**: 2025-12-28

**Authority**: This document defines the authoritative fact model for Methodology entities.

**Scope**: Static fact schema only. Perspective metadata for human understanding. Does not change facts. Does not affect freeze validity.

---

## 1. What Is Methodology

**Factual Definition**:

Methodology is **perspective metadata** for human understanding of a Company structural declaration.

Methodology is a "reading perspective" that helps humans organize and understand Company structure, but it does not change any facts.

Methodology does not affect the validity of Freeze operations.

Methodology exists solely for human comprehension purposes.

---

## 2. Authority Field Schema

### 2.1 Identity Fields

These fields identify which Methodology fact is being declared.

#### methodology_identifier

- **Type**: String
- **Format**: `METH-{UUID}`
- **Authority**: System-generated, immutable
- **Meaning**: Unique identifier that distinguishes this Methodology from all other Methodology facts
- **Identity Declaration**: Yes

#### methodology_name

- **Type**: String
- **Format**: Human-readable text
- **Authority**: Human-declared
- **Meaning**: Name of this Methodology perspective
- **Examples**: "DevOps", "Agile", "Functional", "Custom Methodology Name"
- **Identity Declaration**: Yes

### 2.2 Descriptive Fields

These fields describe what this Methodology perspective represents.

#### methodology_description

- **Type**: String (multi-line text, optional)
- **Format**: Human-readable text
- **Authority**: Human-declared
- **Meaning**: Description of what this Methodology perspective represents and how it organizes understanding
- **Purpose**: Helps humans understand how to interpret Company structure through this Methodology lens
- **Optional**: Yes (may be empty)
- **Descriptive Text**: Yes

---

## 3. What Methodology Does NOT Do

### 3.1 Does Not Change Facts

Methodology **does NOT**:

- Change any Company facts
- Change any Cell facts
- Change any Topology facts
- Change any Role facts
- Modify structural declarations
- Alter relationship definitions

### 3.2 Does Not Create Conflicts

Methodology **does NOT**:

- Create conflicts between facts
- Require conflict resolution
- Affect freeze validity
- Prevent freezing
- Cause validation failures
- Require reconciliation

### 3.3 Does Not Affect Freeze Validity

Methodology **does NOT**:

- Affect whether a Company can be frozen
- Affect freeze legality
- Require Methodology approval for freeze
- Prevent freeze based on Methodology
- Enforce Methodology constraints on freeze

### 3.4 Does Not Trigger Behavior

Methodology **does NOT**:

- Trigger system behavior
- Trigger backend actions
- Change system operations
- Affect execution (if any exists outside Authority Layer)
- Modify presentation logic beyond organization

### 3.5 Does Not Enforce Constraints

Methodology **does NOT**:

- Enforce structural constraints
- Require specific Cell arrangements
- Mandate relationship patterns
- Force organizational rules
- Apply business logic

---

## 4. Methodology Is Perspective Metadata Only

### 4.1 Perspective Nature

**Rule**: Methodology facts are **perspective metadata** only.

**Meaning**:
- Methodology helps humans understand Company structure
- Methodology may affect how structure is organized for viewing
- Methodology does not change the underlying facts
- Methodology is a lens, not a fact modifier
- Methodology exists for human comprehension

### 4.2 Organization Purpose

**Rule**: Methodology may affect organization and presentation, but not facts.

**Allowed Effects**:
- How Cells are grouped for display
- How Topology is laid out visually
- Which relationships are highlighted
- How information is organized in UI

**Forbidden Effects**:
- Changing actual Cell facts
- Changing actual Topology facts
- Creating new facts
- Deleting facts
- Modifying fact values

### 4.3 Immutable After Freeze

Once the Company containing this Methodology is frozen:

- Methodology facts are immutable
- No Methodology fields may be modified
- No Methodology fields may be added
- No Methodology fields may be removed
- The Methodology perspective is complete and permanent

---

## 5. Field Type Definitions

### 5.1 String Type

- Plain text
- No formatting requirements beyond encoding (UTF-8)
- No length limits defined in authority schema
- No validation rules beyond "string"

### 5.2 Identifier Type

- Opaque string
- System-generated format: `{PREFIX}-{UUID}`
- Must be unique within the Company
- Immutable once assigned

### 5.3 Multi-line Text Type (Optional)

- Plain text that may contain line breaks
- UTF-8 encoding
- No formatting requirements
- May be empty (optional field)

---

## 6. Authority Enforcement

### 6.1 No Fact Modification

Frontend, Backend, and Storage layers **cannot**:

- Use Methodology to modify facts
- Infer that Methodology changes structural declarations
- Treat Methodology as a fact modifier
- Apply Methodology constraints to facts
- Use Methodology to validate or reject facts

### 6.2 Presentation Only

Methodology may be used for:

- Organizing display of facts
- Grouping facts for presentation
- Arranging facts visually
- Highlighting certain facts
- Providing context for reading facts

Methodology must NOT be used for:

- Modifying facts
- Creating facts
- Deleting facts
- Validating facts
- Constraining facts

### 6.3 Fact Boundaries

Methodology facts are **complete** as defined. No additional facts may be inferred or added without extending this schema.

### 6.4 Read-Only After Freeze

Once Company is frozen:

- All Methodology facts within that Company are immutable
- No Methodology fields may be modified
- No Methodology fields may be added
- No Methodology fields may be removed
- The Methodology perspective is complete and permanent

---

## 7. Schema Summary

**Methodology Authority Schema**:

- **Identity Fields**: methodology_identifier, methodology_name
- **Descriptive Fields**: methodology_description (optional)

**Total Fields**: 3 (2 required, 1 optional)

**Nature**: Perspective metadata for human understanding (not fact modifier)

**State**: Frozen (immutable fact) when contained in frozen Company

**Purpose**: Human comprehension only

---

## END OF METHODOLOGY AUTHORITY SCHEMA

**Note**: This schema defines facts only. Implementation details, storage formats, API designs, and UI presentations are outside this schema's scope.

