# ENGINE V1 FREEZE DECLARATION

## Freeze Status

ENGINE v1 is FROZEN.

This declaration establishes immutable governance boundaries for ENGINE v1.

ENGINE v1 governance rules are now baseline and cannot be retroactively changed.

---

## ENGINE Identity as Immutable

The ENGINE identity is immutable:

- This repository is an ENGINE, not a project
- Concrete projects are loaded as BLUEPRINTS
- The ENGINE provides governance, workflow, boundaries, execution constraints, and AI-human collaboration rules
- The ENGINE does not define business logic

This identity cannot be changed in ENGINE v1.

Future ENGINE versions (v2, v3, etc.) may extend or modify this identity, but v1 remains frozen.

---

## Governance Priority Order

The following priority order is immutable for ENGINE v1:

1. **Explicit human instruction** (highest priority)
   - Direct human commands override all documentation
   - Human approval overrides all constraints

2. **CURRENT_STATE_SNAPSHOT.md** (repository root)
   - This file is the highest-priority source of truth
   - Must be read first by any AI agent

3. **ENGINE_V1_FREEZE.md** (this document)
   - Defines immutable governance boundaries
   - Must be read after CURRENT_STATE_SNAPSHOT.md
   - Cannot be overridden by conversation context

4. **ENGINE governance documents**
   - ENGINE_HANDOFF_PROMPT.md
   - ENGINE_CI_BOOTSTRAP.md
   - ENGINE_REPO_INIT_CHECKLIST.md
   - BLUEPRINT_INTERFACE.md

5. **Stage-specific documents**
   - STAGE_*_CONTROLLED_IMPLEMENTATION.md
   - stage_status.md

6. **Registry files**
   - docs/registry/stage_*_endpoints.yaml

7. **Code files** (lowest priority)
   - Evidence of current state, not source of truth

This priority order cannot be changed in ENGINE v1.

---

## AI / Cursor Behavior Invariants

The following AI/Cursor behavior rules are immutable for ENGINE v1:

### Default Mode
- AI operates in analysis and preparation mode by default
- AI is allowed to read documentation, analyze structure, audit consistency, propose plans, ask questions, prepare diffs (not applied), draft documentation
- AI is NOT allowed to implement features, modify executable behavior, add endpoints, unfreeze frozen code, introduce side effects, change runtime behavior

### Authorization Model
- Any action that changes executable behavior requires: registry authorization, CI verification, explicit human approval
- Absence of instruction does NOT imply permission
- Lack of instruction is NOT permission

### Failure Mode
- When uncertain: STOP, ASK the human, DO NOT guess, DO NOT auto-complete intentions
- Guessing is considered a violation

### Startup Protocol
- Cursor Pro MUST read CURRENT_STATE_SNAPSHOT.md first
- Cursor Pro MUST read ENGINE_V1_FREEZE.md after CURRENT_STATE_SNAPSHOT.md
- Conversation history does NOT override these documents

These behavior invariants cannot be changed in ENGINE v1.

---

## Frozen Core Scope

### Rule Categories That Are Frozen

The following rule categories are frozen in ENGINE v1:

1. **ENGINE Identity Rules**
   - ENGINE vs PROJECT distinction
   - BLUEPRINT loading mechanism
   - ENGINE stability across BLUEPRINT changes

2. **Governance Priority Order**
   - Document authority hierarchy
   - Human instruction supremacy
   - CURRENT_STATE_SNAPSHOT.md as highest-priority source of truth

3. **AI/Cursor Behavior Rules**
   - Default mode (analysis/preparation)
   - Authorization model (explicit approval required)
   - Failure mode (stop and ask)
   - Startup protocol (mandatory reading order)

4. **CI Enforcement Architecture**
   - Bootstrap check requirements
   - Anti-tamper enforcement
   - Stage/Registry alignment enforcement
   - Sentinel checks

5. **Stage Progression Rules**
   - Stage definition structure
   - Stage advancement requirements
   - Registry binding to stages

6. **Blueprint Interface**
   - Blueprint definition structure
   - Blueprint activation process
   - Blueprint replacement rules

### Forbidden Changes Post-v1

The following changes are FORBIDDEN in ENGINE v1:

- Weakening CI enforcement rules
- Removing mandatory checks
- Changing governance priority order
- Modifying AI/Cursor behavior invariants
- Changing ENGINE identity definition
- Retroactively reinterpreting existing rules
- Bypassing explicit approval requirements
- Removing startup protocol requirements
- Changing document authority hierarchy

### Allowed Changes Post-v1

The following changes are ALLOWED post-v1:

- Adding new stages (Stage 6, Stage 7, etc.)
- Adding new registry files for new stages
- Adding new CI checks (additive only)
- Extending Blueprint interface (additive only)
- Adding new governance documents (versioned)
- Updating CURRENT_STATE_SNAPSHOT.md (state changes only, not structure)
- Adding new ENGINE versions (v2, v3, etc.)

All post-v1 changes must be:
- Additive only (no removal of v1 rules)
- Versioned (if creating new ENGINE version)
- Explicitly approved by human

---

## Link to Startup Authority

ENGINE_V1_FREEZE.md is subordinate only to:

1. **Explicit human instruction**
   - Direct human commands override this document
   - Human approval can authorize changes that would otherwise violate freeze

2. **CURRENT_STATE_SNAPSHOT.md**
   - Must be read first
   - ENGINE_V1_FREEZE.md must be read after CURRENT_STATE_SNAPSHOT.md
   - If conflict exists, CURRENT_STATE_SNAPSHOT.md wins (but human instruction wins over both)

ENGINE_V1_FREEZE.md cannot be overridden by:
- Conversation context
- Inferred intent
- Historical patterns
- Code structure
- Other documentation (except CURRENT_STATE_SNAPSHOT.md and explicit human instruction)

---

## No Retroactive Changes

The following rules apply to ENGINE v1:

### Existing Rules Are Baseline
- All ENGINE rules existing at v1 freeze are now baseline
- These rules cannot be removed or weakened
- These rules define the minimum governance standard

### No Re-interpretation
- Past rules cannot be retroactively re-interpreted
- Rules must be understood as written at freeze time
- Ambiguity requires human clarification, not AI interpretation

### Extensions Must Be Versioned
- New ENGINE versions (v2, v3, etc.) must be explicitly declared
- New versions can extend or modify v1 rules
- v1 rules remain frozen even when new versions exist
- Version progression requires explicit human approval

### Version Boundaries
- ENGINE v1 rules apply to all repositories using ENGINE v1
- Upgrading to ENGINE v2 requires explicit human decision
- v1 and v2 can coexist (different repositories)
- v1 freeze is permanent

---

## Future Work Is Additive Only

All future work on ENGINE v1 must be:

- **Additive**: New rules, new checks, new documents
- **Non-destructive**: Cannot remove or weaken existing rules
- **Explicitly approved**: Requires human approval for any change
- **Versioned**: Major changes create new ENGINE versions

Future work cannot:
- Remove existing governance rules
- Weaken existing CI enforcement
- Change immutable identity or behavior rules
- Retroactively modify v1 baseline

---

## Freeze Enforcement

ENGINE v1 freeze is enforced by:

1. **Documentation**: This document declares the freeze
2. **CI Enforcement**: CI checks prevent unauthorized changes
3. **Human Oversight**: Explicit approval required for any governance change
4. **Version Control**: Git history preserves v1 baseline

Violation of ENGINE v1 freeze requires:
- Explicit human approval
- Clear justification
- Version progression (if changing immutable rules)

---

## Authority and Finality

This document is a binding governance declaration.

ENGINE v1 governance rules are frozen as declared.

No AI agent, no conversation context, no code structure can override this freeze except:
- Explicit human instruction
- CURRENT_STATE_SNAPSHOT.md (for state changes only)

This freeze is permanent for ENGINE v1.

---

END OF ENGINE V1 FREEZE DECLARATION

