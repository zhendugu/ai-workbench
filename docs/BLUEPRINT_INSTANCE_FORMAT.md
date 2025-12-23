# BLUEPRINT INSTANCE FORMAT (ENGINE v1)

This document defines the ONLY valid instance format for a Blueprint
loaded by ENGINE v1.

A Blueprint defines the allowed conceptual world of a concrete project.
It is NOT an implementation plan and MUST NOT contain execution details.

This format is frozen for ENGINE v1.
Future versions may extend this format but must not break v1 compatibility.

--------------------------------------------------------------------

GENERAL PRINCIPLES

- Blueprint defines WHAT is allowed, not HOW to implement it
- Blueprint is an ENGINE input, not a documentation artifact
- Blueprint does not trigger execution
- Blueprint does not bind a technical stack
- Blueprint does not grant implementation permission
- Absence of instruction is NOT permission

Any Blueprint that violates these principles is INVALID.

--------------------------------------------------------------------

FILE LOCATION AND NAMING

Location (mandatory):
/blueprints/<blueprint_name>/BLUEPRINT.md

Rules:
- <blueprint_name> must use kebab-case
- Multiple blueprints may exist in a repository
- Only one blueprint may be activated at a time
- Activation is defined elsewhere and is NOT part of this format

--------------------------------------------------------------------

SECTION 0. BLUEPRINT META

Purpose:
Identify the blueprint and bind it to ENGINE v1 without activating it.

Required fields:

- blueprint_id: string
- blueprint_version: 1.0
- target_engine_version: v1

- status: draft | reviewed | approved
- created_by: human | cursor
- created_at: YYYY-MM-DD

- description: one-paragraph summary of the project intent

Rules:
- blueprint_version refers to the blueprint format version
- target_engine_version MUST match the ENGINE major version
- status does NOT imply permission to execute

--------------------------------------------------------------------

SECTION 1. PROJECT INTENT

Purpose:
Define why the project exists, without describing implementation.

1.1 Problem Statement
- What problem does this project exist to solve?
- Who is the target user?

1.2 Success Definition
- What observable outcome defines success?
- Success must be described without metrics tied to implementation

1.3 Non-Goals
- Explicitly list what this project will NOT attempt to do

Forbidden in this section:
- Technical solutions
- Frameworks or tools
- Architectural decisions

--------------------------------------------------------------------

SECTION 2. SCOPE AND BOUNDARIES

Purpose:
Define the allowed and forbidden conceptual scope.

2.1 In Scope
- Capabilities and behaviors explicitly allowed

2.2 Out of Scope
- Capabilities explicitly forbidden

2.3 Hard Boundaries
- Things that must never happen, even if convenient

Rules:
- This section is used to prevent scope creep
- Ambiguity MUST be resolved by human clarification

--------------------------------------------------------------------

SECTION 3. CONCEPTUAL SYSTEM SHAPE

Purpose:
Describe the logical shape of the system without architecture.

3.1 Core Concepts
- List core domain concepts and their meaning

3.2 Major Logical Components
- Describe major parts of the system at a conceptual level

3.3 High-Level Interaction
- Describe how components interact in natural language

Allowed:
- "User interacts with X"
- "A communicates with B"

Forbidden:
- APIs
- Databases
- Message queues
- Deployment models

--------------------------------------------------------------------

SECTION 4. CAPABILITY DECLARATION

Purpose:
Declare high-level capabilities that may affect ENGINE stages.

4.1 Required ENGINE Stage
- required_stage: 4 | 5 | 6

4.2 Persistence
- requires_persistence: yes | no

4.3 External Interaction
- requires_external_api: yes | no

4.4 Background Execution
- requires_background_jobs: yes | no

Rules:
- This section is declarative only
- Declaring a capability does NOT authorize its implementation
- Enforcement is handled by ENGINE CI and stage controls

--------------------------------------------------------------------

SECTION 5. EXPLICIT PROHIBITIONS

Purpose:
Provide hard brakes for AI and human behavior.

Content:
- Forbidden behaviors
- Forbidden shortcuts
- Forbidden assumptions

Recommended examples:
- No inference of missing requirements
- No silent scope expansion
- No implementation without explicit approval

--------------------------------------------------------------------

SECTION 6. MILESTONES

Purpose:
Describe progress checkpoints without task breakdown.

Format:
- Milestone name
  - Description
  - Completion criteria

Rules:
- Milestones describe outcomes, not tasks
- No TODO lists
- No implementation steps

--------------------------------------------------------------------

SECTION 7. OPEN QUESTIONS

Purpose:
List unresolved questions that block activation.

Rules:
- If this section is non-empty, the Blueprint MUST NOT be activated
- Questions must be resolved explicitly by a human

--------------------------------------------------------------------

FORBIDDEN CONTENT (GLOBAL)

A Blueprint MUST NOT contain:
- Programming languages
- Frameworks or libraries
- Cloud providers
- Database types
- File paths
- API endpoints
- Algorithms
- Implementation strategies

Violation of this rule invalidates the Blueprint.

--------------------------------------------------------------------

CURSOR BEHAVIOR CONSTRAINTS

Allowed:
- Ask clarification questions
- Rewrite human intent for precision
- Propose multiple blueprint drafts
- Highlight ambiguity and risk

Forbidden:
- Inferring unstated requirements
- Expanding scope implicitly
- Suggesting implementation paths
- Starting construction

--------------------------------------------------------------------

END OF BLUEPRINT INSTANCE FORMAT