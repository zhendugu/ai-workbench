# Authority Schema: Cell 001

**Document ID**: AUTH-CELL-SCHEMA-001

**Status**: DRAFT

**Date**: 2025-12-28

**Authority**: This document defines the authoritative fact model for Cell entities.

**Scope**: Static fact schema only. No execution semantics, no lifecycle, no state changes, no actors.

---

## 1. What Is Cell

**Factual Definition**:

Cell is a **responsibility declaration unit**.

Cell declares "what is responsible" and "what is not responsible" within a Company structural declaration.

Cell is a **declarative existence** - it exists as a structural fact, not as an executor.

---

## 2. Authority Field Schema

### 2.1 Identity Fields

These fields are **identity declarations**. They identify which Cell fact is being declared.

#### cell_identifier

- **Type**: String
- **Format**: `CELL-{UUID}`
- **Authority**: System-generated, immutable
- **Meaning**: Unique identifier that distinguishes this Cell from all other Cell facts
- **Identity Declaration**: Yes

#### cell_name

- **Type**: String
- **Format**: Human-readable text
- **Authority**: Human-declared
- **Meaning**: Short identifying name for this Cell responsibility declaration
- **Identity Declaration**: Yes

### 2.2 Responsibility Declaration Fields

These fields are **responsibility declarations**. They declare what this Cell is responsible for and what it is not responsible for.

#### responsibility_what

- **Type**: String (multi-line text)
- **Format**: Human-readable text
- **Authority**: Human-declared
- **Meaning**: Declaration of what this Cell is responsible for
- **Purpose**: Answers the question "What does this Cell declare itself responsible for?"
- **Declarative Text**: Yes

#### responsibility_what_not

- **Type**: String (multi-line text)
- **Format**: Human-readable text
- **Authority**: Human-declared
- **Meaning**: Declaration of what this Cell explicitly declares it is NOT responsible for
- **Purpose**: Answers the question "What does this Cell explicitly declare it is not responsible for?"
- **Declarative Text**: Yes

### 2.3 Constraint Attachment

Cell facts include references to Role constraints that are attached to this Cell.

#### role_constraints

- **Type**: Array of Role constraint references
- **Format**: References to Role facts (see AUTH_ROLE_SCHEMA_001.md for Role structure)
- **Authority**: Human-declared
- **Meaning**: List of Role constraints attached to this Cell
- **Relationship**: Role constraints are **attached to** Cell, not independent entities
- **Note**: Role constraints are defined in AUTH_ROLE_SCHEMA_001.md

---

## 3. What Cell Is NOT

### 3.1 Execution Entity

Cell **is NOT**:

- An Actor
- An Agent
- An executor
- A process runner
- An automation unit
- A worker
- An instance

### 3.2 Operational Entity

Cell **is NOT**:

- An execution unit
- A runtime component
- A service
- A system process
- A running entity

### 3.3 Personified Entity

Cell **is NOT**:

- A person
- A team member
- An employee
- A worker
- A staff member
- A human or AI instance

---

## 4. What Cell Does NOT Contain

### 4.1 Lifecycle Fields

Cell **does NOT contain**:

- Lifecycle state
- Birth date
- Death date
- Activation date
- Deactivation date
- Lifecycle transitions

### 4.2 State Change Fields

Cell **does NOT contain**:

- Current state
- Previous state
- State transitions
- State history
- Status indicators
- State changes

### 4.3 Task Fields

Cell **does NOT contain**:

- Current tasks
- Task queue
- Task history
- Pending work
- Active assignments
- Work in progress

### 4.4 Execution Fields

Cell **does NOT contain**:

- Execution status
- Running status
- Activity indicators
- Performance metrics
- Execution logs
- Runtime information

### 4.5 Dynamic Fields

Cell **does NOT contain**:

- "Current" anything
- "Latest" anything
- "Recent" anything
- "Active" anything
- Time-based change indicators
- Temporal state markers

---

## 5. Cell Facts Are Declarative Existence

### 5.1 Declarative Nature

**Rule**: Cell facts are **declarative existence** statements.

**Meaning**:
- Cell declares that a responsibility exists
- Cell does not execute anything
- Cell does not run
- Cell does not perform actions
- Cell is a structural declaration, not an operational entity

### 5.2 Immutable After Freeze

Once the Company containing this Cell is frozen:

- Cell facts are immutable
- No fields may be modified
- No fields may be added
- No fields may be removed
- The responsibility declaration is complete and permanent

### 5.3 Authority Boundary

**Authority Layer Rule**:
- Cell facts exist as structural declarations
- Cell facts are read-only after freeze
- Frontend may read Cell facts, but cannot modify them
- Cell facts are complete as declared

---

## 6. Field Type Definitions

### 6.1 String Type

- Plain text
- No formatting requirements beyond encoding (UTF-8)
- No length limits defined in authority schema
- No validation rules beyond "string"

### 6.2 Multi-line Text Type

- Plain text that may contain line breaks
- UTF-8 encoding
- No formatting requirements
- No length limits defined in authority schema

### 6.3 Identifier Type

- Opaque string
- System-generated format: `{PREFIX}-{UUID}`
- Must be unique within the Company
- Immutable once assigned

### 6.4 Array of References Type

- Ordered list of references to other authority facts
- References are identifiers (strings)
- Order is significant (declarative ordering)
- Empty array is valid (Cell with no Role constraints)

---

## 7. Authority Enforcement

### 7.1 No Interpretation

Frontend, Backend, and Storage layers **cannot**:

- Interpret Cell as an executor or actor
- Add execution semantics to Cell
- Infer that Cell "runs" or "performs" actions
- Create operational entities from Cell facts
- Assign tasks or work to Cell facts

### 7.2 Fact Boundaries

Cell facts are **complete** as defined. No additional facts may be inferred or added without extending this schema.

### 7.3 Read-Only After Freeze

Once Company is frozen:

- All Cell facts within that Company are immutable
- No Cell fields may be modified
- No Cell fields may be added
- No Cell fields may be removed
- The Cell responsibility declarations are complete and permanent

---

## 8. Schema Summary

**Cell Authority Schema**:

- **Identity Fields**: cell_identifier, cell_name
- **Responsibility Declaration Fields**: responsibility_what, responsibility_what_not
- **Constraint Attachment**: role_constraints (array of Role references)

**Total Fields**: 5 (cell_identifier, cell_name, responsibility_what, responsibility_what_not, role_constraints)

**Nature**: Declarative existence (not execution entity)

**State**: Frozen (immutable fact) when contained in frozen Company

---

## END OF CELL AUTHORITY SCHEMA

**Note**: This schema defines facts only. Implementation details, storage formats, API designs, and UI presentations are outside this schema's scope.

