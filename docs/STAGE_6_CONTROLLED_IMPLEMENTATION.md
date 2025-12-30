# Stage 6 – Controlled Implementation

## Purpose

Stage 6 enables controlled implementation of persistent storage, external API interactions, and background task execution under strict registry and CI enforcement. Stage 6 maintains governance boundaries while allowing Blueprint-required capabilities that were forbidden in Stage 4 and Stage 5.

Stage 6 builds upon Stage 4 and Stage 5 foundations:
- Stage 4 baseline remains LOCKED and FROZEN
- Stage 5 registry-based authorization mechanism remains in effect
- Stage 6 adds new capability classes (persistence, external APIs, background tasks) while maintaining governance controls

---

## Current Stage Declaration

Current Stage: Stage 6

Stage 6 is ACTIVE when declared in `CURRENT_STATE_SNAPSHOT.md` and `docs/stage_status.md`.

Stage 4 baseline remains LOCKED and FROZEN.
Stage 5 registry mechanism remains ACTIVE.

---

## Relationship to Previous Stages

### Stage 4 Baseline
- Stage 4 baseline is LOCKED and FROZEN
- Stage 4 execution pattern remains valid for endpoints that do not require Stage 6 capabilities
- Stage 4 constraints apply to all endpoints unless explicitly authorized for Stage 6 capabilities

### Stage 5 Registry Mechanism
- Stage 5 registry-based authorization mechanism remains ACTIVE
- All endpoints MUST be registered in `docs/registry/stage_6_endpoints.yaml` (or appropriate stage-specific registry)
- Registry enforcement continues to apply to all executable endpoints

### Stage 6 Additions
- Stage 6 adds three new capability classes:
  1. **Persistence**: Persistent storage for data, state, and history
  2. **External API Calls**: Interactions with external services (including AI APIs)
  3. **Background Tasks**: Asynchronous execution, scheduled tasks, continuous monitoring

---

## Allowed Actions

### General Allowed Actions

Cursor Pro MAY perform the following actions in Stage 6:

- **Read documentation files**
- **Analyze repository structure**
- **Audit consistency** (compare docs vs code vs registry)
- **Propose next steps** (as suggestions, not implementations)
- **Ask clarification questions**
- **Prepare plans, checklists, diffs** (NOT applying them without approval)
- **Draft documentation** (not modifying executable behavior)
- **Identify risks and gaps** (reporting only)

**These actions do NOT change executable behavior.**

### Stage 6 Specific Allowed Actions

Cursor Pro MAY implement the following **only after** explicit human approval and registry authorization:

1. **Persistent Storage Implementation**
   - Implement data persistence mechanisms
   - Store and retrieve data from persistent storage
   - Manage data lifecycle (create, read, update, delete)
   - Implement data versioning and migration

2. **External API Integration**
   - Implement external API client code
   - Call external services (including AI APIs)
   - Handle external API responses and errors
   - Implement API authentication and authorization

3. **Background Task Implementation**
   - Implement asynchronous task execution
   - Implement scheduled tasks (cron-like, periodic)
   - Implement continuous monitoring and health checks
   - Implement task queues and job processing

### Registry Authorization Requirement

All executable endpoints and capabilities MUST be:
- Registered in `docs/registry/stage_6_endpoints.yaml` (or appropriate stage-specific registry)
- Explicitly authorized by human approval
- Verified by CI before activation
- Conforming to authorized execution patterns

**No implementation may proceed without registry authorization.**

---

## Forbidden Actions

### General Forbidden Actions

Cursor Pro MUST NOT perform the following actions without explicit approval:

- **Implement unregistered endpoints**
- **Uncomment frozen code**
- **Add business logic without authorization**
- **Modify execution behavior without approval**
- **Weaken CI or governance rules**
- **Assume missing context**
- **Infer intent from code**
- **Activate a BLUEPRINT without human instruction**
- **Modify registry without approval**
- **Advance STAGE without approval**

### Stage 6 Specific Forbidden Actions

Cursor Pro MUST NOT:

1. **Implement Persistence Without Authorization**
   - MUST NOT add database connections without registry authorization
   - MUST NOT create persistent storage without explicit approval
   - MUST NOT modify data schemas without Change Control approval (if Blueprint requires Change Control)

2. **Implement External API Calls Without Authorization**
   - MUST NOT call external APIs without registry authorization
   - MUST NOT bypass AI Gateway/Service layer (if Blueprint requires unified AI Gateway)
   - MUST NOT implement API calls that violate Blueprint constraints

3. **Implement Background Tasks Without Authorization**
   - MUST NOT create background tasks without registry authorization
   - MUST NOT implement tasks that violate Blueprint constraints
   - MUST NOT create tasks that bypass governance mechanisms

4. **Bypass Governance Mechanisms**
   - MUST NOT bypass registry enforcement
   - MUST NOT bypass CI verification
   - MUST NOT bypass human approval gates
   - MUST NOT override ENGINE governance rules

5. **Violate Blueprint Boundaries**
   - MUST NOT implement capabilities not declared in active Blueprint
   - MUST NOT override Blueprint constraints
   - MUST NOT implement features beyond Blueprint scope

---

## Implementation Phases

Stage 6 implementation MUST proceed in phases with explicit gates between phases.

### Phase 1: Foundation Infrastructure

**Purpose**: Establish foundational infrastructure required by all other phases.

**Allowed**:
- Implement persistent storage infrastructure
- Implement external API client infrastructure
- Implement background task infrastructure
- Implement observability infrastructure (if required by Blueprint)

**Gate Requirements**:
- All infrastructure components MUST be registered in registry
- All infrastructure components MUST pass CI verification
- Human approval MUST be obtained before proceeding to Phase 2

**Stop Condition**: If infrastructure implementation fails or violates constraints, MUST STOP and escalate.

### Phase 2: Core Subsystems

**Purpose**: Implement core subsystems that depend on Phase 1 infrastructure.

**Allowed**:
- Implement subsystems that require persistence (as declared in Blueprint)
- Implement subsystems that require external APIs (as declared in Blueprint)
- Implement subsystems that require background tasks (as declared in Blueprint)

**Gate Requirements**:
- All Phase 1 infrastructure MUST be functional
- All subsystem implementations MUST be registered in registry
- All subsystem implementations MUST pass CI verification
- Human approval MUST be obtained before proceeding to Phase 3

**Stop Condition**: If core subsystem implementation fails or violates constraints, MUST STOP and escalate.

### Phase 3: Integration and Coordination

**Purpose**: Integrate subsystems and implement coordination mechanisms.

**Allowed**:
- Implement subsystem integration points
- Implement coordination mechanisms (as declared in Blueprint)
- Implement cross-subsystem communication

**Gate Requirements**:
- All Phase 2 core subsystems MUST be functional
- All integration points MUST be registered in registry
- All integration implementations MUST pass CI verification
- Human approval MUST be obtained before proceeding to Phase 4

**Stop Condition**: If integration fails or violates constraints, MUST STOP and escalate.

### Phase 4: Governance and Safety

**Purpose**: Implement governance and safety mechanisms.

**Allowed**:
- Implement change control mechanisms (if required by Blueprint)
- Implement safety and exception handling (if required by Blueprint)
- Implement observability and monitoring (if required by Blueprint)

**Gate Requirements**:
- All Phase 3 integration MUST be functional
- All governance mechanisms MUST be registered in registry
- All governance implementations MUST pass CI verification
- Human approval MUST be obtained before considering Stage 6 complete

**Stop Condition**: If governance implementation fails or violates constraints, MUST STOP and escalate.

### Phase Progression Rules

- Phases MUST be completed in order (1 → 2 → 3 → 4)
- No phase may be skipped
- Each phase MUST pass its gate before proceeding to next phase
- If any phase fails, MUST STOP and escalate (do not proceed to next phase)

---

## Stop & Escalation Rules

### Mandatory Stop Conditions

Cursor Pro MUST STOP immediately and escalate to human if:

1. **Registry Authorization Missing**
   - Endpoint or capability is not registered in registry
   - Registry entry is missing or invalid
   - CI verification fails due to registry mismatch

2. **Blueprint Constraint Violation**
   - Implementation violates active Blueprint constraints
   - Implementation exceeds Blueprint scope
   - Implementation conflicts with Blueprint boundaries

3. **ENGINE Governance Violation**
   - Implementation violates ENGINE governance rules
   - Implementation attempts to override ENGINE constraints
   - Implementation conflicts with ENGINE freeze declarations

4. **Phase Gate Failure**
   - Phase gate requirements are not met
   - Phase implementation fails validation
   - Phase dependencies are not satisfied

5. **Technical Implementation Failure**
   - Implementation cannot proceed due to technical constraints
   - Required capabilities are unavailable
   - Implementation would cause system instability

6. **Ambiguity or Uncertainty**
   - Multiple valid interpretations exist
   - Required information is missing
   - Documents conflict
   - Authorization is unclear

### Escalation Protocol

When STOP condition is triggered:

1. **STOP all implementation work immediately**
2. **Identify the blocking issue** (what is preventing progress)
3. **Reference relevant documents** (which docs/rules are involved)
4. **State what action is blocked** (what cannot proceed)
5. **Ask human for clarification** (do not propose solutions unless explicitly asked)
6. **Do NOT proceed** until human provides explicit authorization

**Guessing is forbidden. Proceeding without authorization is a governance violation.**

### Human Intervention Required

The following situations ALWAYS require human intervention:

- **Stage 6 activation**: Human MUST explicitly approve Stage 6 activation
- **Registry updates**: Human MUST approve all registry additions/modifications
- **Phase gate approvals**: Human MUST approve progression between phases
- **Blueprint constraint changes**: Human MUST approve any changes to Blueprint constraints
- **ENGINE governance changes**: Human MUST approve any changes to ENGINE governance (if allowed)

---

## Relationship to Blueprint & ENGINE

### Authority Hierarchy

When conflicts exist, the following priority order applies:

1. **Explicit human instruction** (highest priority)
   - Direct human commands override all documentation
   - Human approval overrides all constraints

2. **CURRENT_STATE_SNAPSHOT.md**
   - This file is the highest-priority source of truth
   - Must be read first by any AI agent

3. **ENGINE governance documents**
   - ENGINE_V1_FREEZE.md
   - ENGINE_HANDOFF_PROMPT.md
   - ENGINE_CI_BOOTSTRAP.md
   - This document (STAGE_6_CONTROLLED_IMPLEMENTATION.md)

4. **Active Blueprint**
   - Blueprint defines business requirements and constraints
   - Blueprint MUST NOT override ENGINE governance rules
   - Blueprint constraints apply within ENGINE governance boundaries

5. **Registry files**
   - Registry defines authorized endpoints and capabilities
   - Registry enforcement is ENGINE-level
   - Registry overrides code declarations

6. **Code files** (lowest priority)
   - Code is evidence of current state, not source of truth
   - Code does not define what should be done

### Blueprint Interaction Rules

**Blueprint Requirements**:
- Blueprint MAY declare required capabilities (persistence, external APIs, background tasks)
- Blueprint MUST NOT override ENGINE governance rules
- Blueprint constraints apply within Stage 6 allowed actions

**Blueprint Constraints**:
- If Blueprint forbids a capability, that capability MUST NOT be implemented (even if Stage 6 allows it)
- If Blueprint requires a capability, that capability MAY be implemented (if Stage 6 allows it and registry authorizes it)
- Blueprint boundaries (BOUNDARIES.md) MUST be respected

**Blueprint Activation**:
- Blueprint activation does NOT automatically authorize implementation
- Implementation requires: Blueprint activation + Registry authorization + Human approval + CI verification

### ENGINE Governance Rules

**ENGINE Rules Are Immutable**:
- ENGINE governance rules (ENGINE_V1_FREEZE.md) cannot be overridden by Stage 6
- ENGINE CI enforcement (ENGINE_CI_BOOTSTRAP.md) applies to all stages
- ENGINE handoff protocol (ENGINE_HANDOFF_PROMPT.md) applies to all stages

**Stage 6 Within ENGINE Framework**:
- Stage 6 is a capability expansion, not a governance override
- Stage 6 adds new allowed actions but does not remove governance constraints
- Stage 6 implementations MUST comply with all ENGINE governance rules

---

## Registry Enforcement

### Registry Requirement

All executable endpoints and capabilities MUST be registered in:
- `docs/registry/stage_6_endpoints.yaml` (or appropriate stage-specific registry)

**No implementation may proceed without registry entry.**

### Registry Authorization Pattern

Registry entries MUST specify:
- Endpoint/capability identifier
- Stage introduced (must be 6 or later)
- Authorization status
- Required capabilities (persistence, external API, background task)
- Execution constraints

### CI Enforcement

CI MUST enforce:
- All endpoints are registered
- All registered endpoints conform to execution patterns
- No unregistered endpoints are implemented
- Registry structure is valid

**CI violations block merge and deployment.**

---

## Human Approval Gates

### Mandatory Human Approval

The following actions ALWAYS require explicit human approval:

1. **Stage 6 Activation**
   - Human MUST approve Stage 6 activation in `CURRENT_STATE_SNAPSHOT.md`
   - Human MUST approve Stage 6 activation in `docs/stage_status.md`

2. **Registry Updates**
   - Human MUST approve all additions to `docs/registry/stage_6_endpoints.yaml`
   - Human MUST approve all modifications to existing registry entries

3. **Phase Progression**
   - Human MUST approve progression from Phase 1 to Phase 2
   - Human MUST approve progression from Phase 2 to Phase 3
   - Human MUST approve progression from Phase 3 to Phase 4

4. **Blueprint Constraint Changes**
   - Human MUST approve any changes to Blueprint constraints
   - Human MUST approve any Blueprint scope expansions

5. **Implementation Authorization**
   - Human MUST explicitly authorize implementation work
   - Human MUST approve implementation plans before execution

**Absence of approval means the action is unauthorized.**

---

## Document Type Classification

### Design-Time Documents (FROZEN)

**Status**: FROZEN  
**Modification**: Prohibited without explicit human approval

**Document Types**:
- **Blueprint Documents**: `blueprints/*/BLUEPRINT.md` and related Blueprint documents
- **Subsystem README Files**: `backend/subsystems/*/README.md`

**Characteristics**:
- Define "what" and "boundaries" only
- Use design-time/structural verbs only (Define, Specify, Declare, Describe, Represent, Constrain)
- Contain no implementation details, no behavior logic, no algorithms
- Subject to strict semantic freeze rules (see Subsystem README Freeze Rules below)

**Freeze Enforcement**:
- CI MUST enforce freeze rules
- Any violation blocks merge
- Modification requires explicit human approval

### Implementation Surface Documents (Pre-Code)

**Status**: Pre-Code (Implementation Boundary Lock)  
**Modification**: Allowed for scope clarification, prohibited for behavior logic

**Document Types**:
- **MVP Runtime Surface**: `docs/MVP_RUNTIME_SURFACE.md`
- **Implementation Rules**: `docs/IMPLEMENTATION_RULES.md`

**Characteristics**:
- Define implementation scope and structure
- May contain step-by-step execution path descriptions
- May define abstract data structures and capabilities
- Do NOT authorize behavior logic or algorithms
- Do NOT authorize implementation code

**Authorization Boundary**:
- Implementation Surface Documents authorize structure and scope only
- Step descriptions in Implementation Surface Documents do NOT authorize behavior logic
- Implementation Surface Documents do NOT authorize algorithms or decision-making logic
- Actual implementation requires explicit authorization per Implementation Rules

**Warning**: Implementation Surface Documents are pre-code design documents. They define what CAN be implemented, not HOW to implement. Behavior logic and algorithms require separate authorization.

---

## Subsystem README Freeze Rules

### Behavior Semantics Frozen

**Freeze Date**: 2025-12-23  
**Freeze Status**: FROZEN

All `backend/subsystems/*/README.md` files are subject to strict semantic freeze rules.

### Responsibilities Section Rules

**Design-Time Verbs Only**:
- README Responsibilities sections MUST use only design-time/structural verbs
- **Allowed verbs**: Define, Specify, Declare, Describe, Represent, Constrain
- **Forbidden verbs**: Manage, Execute, Implement, Trigger, Detect, Monitor, Handle, Route, Receive, Record, Track, Maintain, Validate, Provide, Recover, Terminate, Restructure, Analyze, Read, Write, Run, Create, Extract

**Violation**: Any use of forbidden verbs in Responsibilities sections is a freeze violation.

### Conditional Logic Prohibition

**Forbidden Patterns**:
- MUST NOT contain conditional logic: `if`, `when`, `then`, `immediately`, `auto-*`
- MUST NOT contain conditional clauses that imply decision-making

**Exception**: Structural condition definitions (e.g., "trigger conditions", "condition structure") are acceptable as they define structures, not conditional logic.

**Violation**: Any conditional logic in Responsibilities sections is a freeze violation.

### Execution Context Prohibition

**Forbidden Terms** (in behavioral sense):
- MUST NOT contain: `runtime`, `execution`, `process`, `lifecycle`, `flow` (when used to describe behavior)

**Exceptions**:
- "No runtime rules" (in Constraints sections) is acceptable
- "review process structure" (structure definition) is acceptable
- State value lists (e.g., "active, idle, executing, dissolved") are acceptable

**Violation**: Any execution context terms in Responsibilities sections (in behavioral sense) is a freeze violation.

### Non-Responsibility Declarations

**Required**:
- All README files MUST contain "What this subsystem does NOT do" section
- This section MUST clearly state boundaries
- This section MAY reference other subsystems to clarify boundaries

**Violation**: Missing or incomplete non-responsibility declarations is a freeze violation.

### Freeze Enforcement

**CI Enforcement**:
- CI MUST scan all `backend/subsystems/*/README.md` files
- CI MUST check for forbidden verbs in Responsibilities sections
- CI MUST check for conditional logic patterns
- CI MUST check for execution context terms (in behavioral sense)
- CI MUST verify presence of "What this subsystem does NOT do" sections

**Violation Handling**:
- Any violation blocks merge
- Violations MUST be fixed before proceeding
- Freeze rules cannot be overridden without explicit human approval

### Freeze Modification

**Modification Requirements**:
- Any changes to README Responsibilities sections MUST maintain design-time/structural semantic level
- Any changes MUST NOT introduce behavioral semantics
- Any changes MUST be reviewed against freeze criteria
- Modification of freeze rules requires explicit human approval

---

## Finality

This document defines Stage 6 governance rules for ENGINE v1.

Stage 6 rules are binding and cannot be overridden except by:
- Explicit human instruction
- ENGINE governance document updates (with proper approval)

Stage 6 implementations MUST comply with all rules defined in this document.

Violation of Stage 6 rules is a governance violation and will be blocked by CI.

---

END OF STAGE 6 CONTROLLED IMPLEMENTATION

