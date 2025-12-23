# BLUEPRINT INTERFACE

## Purpose

This document defines the formal interface for BLUEPRINTS in the ENGINE.

A BLUEPRINT is a concrete project definition that is loaded into the ENGINE.
The ENGINE provides governance, workflow, and execution boundaries.
The BLUEPRINT provides domain-specific intent and structure.

This interface is ENGINE-level and domain-agnostic.

---

## What is a Blueprint

A BLUEPRINT is a declarative document that defines:

- A concrete project's domain model
- Product goals and objectives
- Architecture intent
- Implementation milestones
- Project-specific constraints

A BLUEPRINT is replaceable.
Only one BLUEPRINT is active at a time.

The ENGINE remains stable across BLUEPRINT changes.

---

## Required Sections

A valid BLUEPRINT MUST contain the following sections:

### 1. Blueprint Identity
- Unique identifier for the blueprint
- Version or revision marker
- Brief description of the project domain

### 2. Domain Model
- Core entities and their relationships
- Domain vocabulary and terminology
- Conceptual boundaries

### 3. Product Goals
- Primary objectives
- Success criteria
- Scope boundaries

### 4. Architecture Intent
- High-level system structure
- Component responsibilities
- Integration points

### 5. Implementation Milestones
- Ordered sequence of implementation phases
- Dependencies between phases
- Completion criteria for each phase

### 6. Project-Specific Constraints
- Domain-specific rules
- Business logic constraints
- Non-functional requirements specific to this project

---

## What a Blueprint MAY Define

A BLUEPRINT is allowed to define:

- Domain concepts and entities
- Business logic intent and rules
- API surface requirements (endpoints, data structures)
- Data models and schemas
- Workflow definitions
- User interaction patterns
- Integration requirements
- Project-specific validation rules
- Domain-specific error conditions

---

## What a Blueprint MUST NOT Define

A BLUEPRINT is forbidden from defining:

- Governance rules (these are ENGINE-level)
- CI enforcement rules (these are ENGINE-level)
- Technology stack choices (these are ENGINE-level, defined in TECH STACK)
- Stage progression rules (these are ENGINE-level)
- Human-AI collaboration protocols (these are ENGINE-level)
- Execution boundaries (these are ENGINE-level)
- Registry enforcement mechanisms (these are ENGINE-level)

A BLUEPRINT must not attempt to override ENGINE constraints.

---

## Blueprint Activation Process

A BLUEPRINT becomes "active" through the following process:

### Step 1: Blueprint Declaration
- Human provides a BLUEPRINT document
- BLUEPRINT MUST be placed at: `/blueprints/<blueprint_name>/BLUEPRINT.md`
- This is the ONLY valid location for BLUEPRINT files
- BLUEPRINT is validated against this interface

### Step 2: State Update (ACTIVATION)
- `CURRENT_STATE_SNAPSHOT.md` is updated to declare the active BLUEPRINT
- The field `ACTIVE_BLUEPRINT: <blueprint_name>` is set in `CURRENT_STATE_SNAPSHOT.md`
- This is the ONLY mechanism that activates a BLUEPRINT
- Directory existence does NOT activate a BLUEPRINT
- Previous BLUEPRINT (if any) is deactivated by setting `ACTIVE_BLUEPRINT: none`

### Step 3: Registry Alignment
- Endpoint registry is reviewed against BLUEPRINT requirements
- New endpoints required by BLUEPRINT are added to registry (with human approval)
- Existing endpoints are validated against BLUEPRINT intent

### Step 4: Stage Progression
- Current STAGE is evaluated against BLUEPRINT requirements
- If BLUEPRINT requires capabilities beyond current STAGE:
  - Human approval is required for STAGE advancement
  - STAGE advancement follows ENGINE governance rules
- If current STAGE is sufficient:
  - Implementation may proceed within STAGE constraints

### Step 5: Human Approval Gate
- Before any implementation begins:
  - Human must explicitly approve BLUEPRINT activation
  - Human must confirm registry updates
  - Human must confirm STAGE authorization

---

## Relationship to Stage

A BLUEPRINT interacts with STAGE as follows:

- **STAGE defines execution constraints**: What implementation patterns are allowed
- **BLUEPRINT defines domain intent**: What needs to be built
- **STAGE constraints apply regardless of BLUEPRINT**: A BLUEPRINT cannot override STAGE rules
- **BLUEPRINT may require STAGE advancement**: If BLUEPRINT requires capabilities beyond current STAGE, STAGE must advance first (with human approval)

Example:
- If STAGE 4 only allows constant endpoints, a BLUEPRINT requiring database access must wait for STAGE advancement
- If BLUEPRINT only requires constant endpoints, STAGE 4 is sufficient

---

## Relationship to Registry

A BLUEPRINT interacts with REGISTRY as follows:

- **REGISTRY authorizes executable endpoints**: Only registered endpoints may be implemented
- **BLUEPRINT declares required endpoints**: BLUEPRINT specifies what endpoints are needed
- **Registry update requires human approval**: Adding BLUEPRINT-required endpoints to registry requires explicit approval
- **Registry enforcement is ENGINE-level**: CI enforces registry compliance regardless of BLUEPRINT

Process:
1. BLUEPRINT declares endpoint requirements
2. Human reviews requirements against current STAGE constraints
3. If STAGE allows, endpoints are added to registry (with human approval)
4. Implementation proceeds only for registered endpoints

---

## Relationship to Human Approval

A BLUEPRINT requires human approval at multiple points:

1. **Blueprint Activation**: Human must explicitly activate the BLUEPRINT
2. **Registry Updates**: Human must approve endpoint additions to registry
3. **Stage Advancement**: If required, human must approve STAGE progression
4. **Implementation Authorization**: Human must explicitly authorize implementation work

A BLUEPRINT does not automatically authorize implementation.
Human approval is always required.

---

## Blueprint Replacement

A BLUEPRINT may be replaced by another BLUEPRINT:

1. New BLUEPRINT is provided
2. Previous BLUEPRINT is deactivated
3. `CURRENT_STATE_SNAPSHOT.md` is updated
4. Registry is reviewed and updated as needed
5. Implementation state is evaluated against new BLUEPRINT

Previous implementation may become invalid if new BLUEPRINT has different requirements.

---

## Validation Rules

A BLUEPRINT must satisfy:

- Contains all required sections
- Does not define ENGINE-level concerns
- Does not conflict with active TECH STACK
- Does not require capabilities beyond current STAGE (unless STAGE advancement is approved)
- Is internally consistent

Validation is performed by human review.
CI does not validate BLUEPRINT structure (this is a documentation concern).

---

## Implementation Authorization

A BLUEPRINT does not automatically authorize implementation.

**Activation vs Authorization:**
- **Activation**: Only `ACTIVE_BLUEPRINT` field in `CURRENT_STATE_SNAPSHOT.md` determines if a BLUEPRINT is active
- **Directory existence ≠ Activation**: A BLUEPRINT directory may exist but remain inactive
- **Inactive BLUEPRINT cannot drive implementation**: Only the active BLUEPRINT (declared in `CURRENT_STATE_SNAPSHOT.md`) may be used for project reasoning

Implementation requires:
1. Active BLUEPRINT declared in `CURRENT_STATE_SNAPSHOT.md` (field: `ACTIVE_BLUEPRINT: <blueprint_name>`)
2. Endpoints registered in appropriate registry
3. Current STAGE allows required implementation patterns
4. Explicit human approval for implementation work

**If `ACTIVE_BLUEPRINT: none`:**
- No BLUEPRINT is active
- No project-specific implementation is authorized
- ENGINE operates as a construction base only

Absence of a BLUEPRINT means no implementation is authorized.

---

## Blueprint File Location (MANDATORY)

The ONLY valid location for BLUEPRINT files is:

**`/blueprints/<blueprint_name>/BLUEPRINT.md`**

Where:
- `/blueprints/` is the root-level directory (repository root)
- `<blueprint_name>` is the blueprint identifier (must use kebab-case)
- `BLUEPRINT.md` is the mandatory filename (case-sensitive)

**Rules:**
- Any BLUEPRINT file placed outside `/blueprints/` is INVALID and will NOT be recognized by ENGINE
- Any BLUEPRINT file not following the `/blueprints/<name>/BLUEPRINT.md` pattern is INVALID
- Directory existence does NOT imply activation
- Multiple blueprints may exist in `/blueprints/`, but only one may be active at a time

**Invalid locations (explicitly forbidden):**
- `docs/blueprints/` - NOT recognized by ENGINE
- Any other directory - NOT recognized by ENGINE
- Root-level `BLUEPRINT.md` - NOT recognized by ENGINE

---

## Notes

- This interface is ENGINE-level and does not assume any business domain
- A BLUEPRINT is a specification document, not executable code
- BLUEPRINT activation does not modify ENGINE governance rules
- BLUEPRINT replacement does not modify ENGINE structure
- All BLUEPRINT-related changes require human approval

END OF BLUEPRINT INTERFACE

