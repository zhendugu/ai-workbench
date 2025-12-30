# Authority Schema: Topology 001

**Document ID**: AUTH-TOPOLOGY-SCHEMA-001

**Status**: DRAFT

**Date**: 2025-12-28

**Authority**: This document defines the authoritative fact model for Topology (declarative relationships).

**Scope**: Static fact schema only. No process semantics, no execution order, no time dependencies.

---

## 1. What Is Topology

**Factual Definition**:

Topology is a collection of **declarative relationships** between Cell facts.

Topology declares structural relationships, not execution flows, not processes, not time sequences.

Topology is a **readable structural declaration** that describes how Cell facts relate to each other.

---

## 2. Authority Field Schema

A Topology fact is a **relationship fact** between two Cell facts.

### 2.1 Relationship Identity Fields

These fields identify which relationship fact is being declared.

#### relationship_identifier

- **Type**: String
- **Format**: `REL-{UUID}`
- **Authority**: System-generated, immutable
- **Meaning**: Unique identifier that distinguishes this relationship from all other relationship facts
- **Identity Declaration**: Yes

### 2.2 Relationship Source and Target

These fields identify the Cell facts involved in this relationship.

#### source_cell_identifier

- **Type**: String (Cell identifier reference)
- **Format**: `CELL-{UUID}`
- **Authority**: Human-declared (reference to existing Cell fact)
- **Meaning**: Identifier of the source Cell fact in this relationship
- **Reference**: Must reference an existing Cell fact within the same Company

#### target_cell_identifier

- **Type**: String (Cell identifier reference)
- **Format**: `CELL-{UUID}`
- **Authority**: Human-declared (reference to existing Cell fact)
- **Meaning**: Identifier of the target Cell fact in this relationship
- **Reference**: Must reference an existing Cell fact within the same Company

### 2.3 Relationship Type

This field declares the type of relationship.

#### relationship_type

- **Type**: Enumeration (string, constrained values)
- **Allowed Values**:
  - `dependency` (依赖关系) - Cell A depends on Cell B's output
  - `reference` (参考关系) - Cell A references Cell B's definition
  - `input_output` (输入输出关系) - Cell A's output is Cell B's input
- **Authority**: Human-declared
- **Meaning**: Type of structural relationship being declared
- **Semantic Constraint**: Relationship types are **nouns**, not verbs
- **Note**: No execution semantics are implied by relationship type

### 2.4 Relationship Description

This field provides additional descriptive text about the relationship.

#### relationship_description

- **Type**: String (multi-line text, optional)
- **Format**: Human-readable text
- **Authority**: Human-declared
- **Meaning**: Additional descriptive text explaining this relationship
- **Optional**: Yes (may be empty)
- **Descriptive Text**: Yes

---

## 3. What Topology Does NOT Express

### 3.1 Process Semantics

Topology **does NOT express**:

- Workflow
- Process flow
- Execution sequence
- Step-by-step procedures
- Process definitions

### 3.2 Order Semantics

Topology **does NOT express**:

- Sequence order
- Time order
- Execution order
- Processing order
- Sequential dependencies

### 3.3 Time Semantics

Topology **does NOT express**:

- Temporal relationships
- Time dependencies
- Duration
- Timing
- Scheduling

### 3.4 Execution Dependencies

Topology **does NOT express**:

- Execution dependencies
- Runtime dependencies
- Operational dependencies
- Service dependencies
- Process dependencies

### 3.5 Dynamic Semantics

Topology **does NOT express**:

- Current state of relationships
- Active relationships
- Recent relationships
- Relationship changes
- Relationship lifecycle

---

## 4. Topology Is Readable Structural Declaration

### 4.1 Structural Nature

**Rule**: Topology facts are **structural declarations** only.

**Meaning**:
- Topology declares how Cell facts relate structurally
- Topology does not declare execution flows
- Topology does not declare time sequences
- Topology does not declare processes
- Topology is for human reading and understanding, not for execution

### 4.2 Relationship Type Constraints

**Rule**: Relationship types must be **nouns**, not verbs.

**Allowed Nouns**:
- `dependency` (noun: a dependency relationship)
- `reference` (noun: a reference relationship)
- `input_output` (noun: an input-output relationship)

**Forbidden Verbs**:
- execute, triggers, causes, produces, consumes, etc.
- Any verb that implies action or execution

### 4.3 Immutable After Freeze

Once the Company containing this Topology is frozen:

- Topology facts are immutable
- No relationship facts may be modified
- No relationship facts may be added
- No relationship facts may be removed
- The structural declaration is complete and permanent

---

## 5. Minimal Relationship Composition

### 5.1 Required Fields

A relationship fact MUST contain:

- relationship_identifier (identity)
- source_cell_identifier (source reference)
- target_cell_identifier (target reference)
- relationship_type (type declaration)

**Minimum Fields**: 4

### 5.2 Optional Fields

A relationship fact MAY contain:

- relationship_description (descriptive text)

**Note**: relationship_description is optional and may be empty.

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

### 6.4 Relationship Type Enumeration

- String constrained to allowed values
- Allowed values: `dependency`, `reference`, `input_output`
- Case-sensitive
- No additional values allowed without schema extension

### 6.5 Multi-line Text Type (Optional)

- Plain text that may contain line breaks
- UTF-8 encoding
- No formatting requirements
- May be empty (optional field)

---

## 7. Authority Enforcement

### 7.1 No Interpretation

Frontend, Backend, and Storage layers **cannot**:

- Interpret relationships as execution flows
- Infer execution order from relationships
- Create processes from topology
- Generate workflows from relationships
- Add time semantics to relationships
- Add execution semantics to relationships

### 7.2 Fact Boundaries

Topology facts are **complete** as defined. No additional facts may be inferred or added without extending this schema.

### 7.3 Read-Only After Freeze

Once Company is frozen:

- All Topology facts within that Company are immutable
- No relationship facts may be modified
- No relationship facts may be added
- No relationship facts may be removed
- The structural declaration is complete and permanent

---

## 8. Schema Summary

**Topology Authority Schema** (per relationship fact):

- **Identity Fields**: relationship_identifier
- **Reference Fields**: source_cell_identifier, target_cell_identifier
- **Type Declaration**: relationship_type (enumeration)
- **Descriptive Fields**: relationship_description (optional)

**Total Fields**: 5 (4 required, 1 optional)

**Nature**: Declarative structural relationships (not execution flows)

**State**: Frozen (immutable facts) when contained in frozen Company

**Collection**: Topology is a collection of relationship facts

---

## END OF TOPOLOGY AUTHORITY SCHEMA

**Note**: This schema defines facts only. Implementation details, storage formats, API designs, and UI presentations are outside this schema's scope.

