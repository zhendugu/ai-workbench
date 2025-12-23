# ENGINE HANDOFF PROTOCOL — Cursor Pro

## Protocol Status

This document is a MANDATORY execution protocol.
It defines how Cursor Pro MUST behave when connecting to this repository.

This is NOT a suggestion.
This is NOT optional.
This is a binding contract.

Violation of any protocol rule is considered a hard failure.

---

## Repository Identity Check

**MANDATORY FIRST STEP:**

Before reading any other file, Cursor Pro MUST determine:

1. **Is this repository an ENGINE or a PROJECT?**
   - Check for `CURRENT_STATE_SNAPSHOT.md` in repository root
   - If present: This is an ENGINE
   - If absent: This may be a PROJECT (proceed with caution)

2. **If ENGINE:**
   - Do NOT assume this is a single project
   - Do NOT infer business domain from code
   - Do NOT assume implementation intent from commented code
   - Treat this as a governance framework, not a product

3. **If PROJECT:**
   - Follow project-specific documentation
   - This protocol may not apply

**If identity is unclear: STOP and ask the human.**

---

## Mandatory Reading Order

Cursor Pro MUST read files in this exact order:

### Phase 1: State Snapshot (REQUIRED FIRST)
1. **`CURRENT_STATE_SNAPSHOT.md`** (repository root)
   - This is the highest-priority source of truth
   - Read this file FIRST before any other action
   - If this file does not exist: STOP and ask the human

### Phase 2: Engine Foundation (REQUIRED SECOND)
2. **`docs/ENGINE_HANDOFF_PROMPT.md`** (this file)
   - Defines protocol behavior
   - Must be read to understand execution rules

3. **Engine Overview** (if exists: `docs/ENGINE_OVERVIEW.md` or similar)
   - Defines ENGINE identity and core concepts
   - Provides context for governance model

### Phase 3: Governance Rules (REQUIRED THIRD)
4. **`docs/stage_status.md`**
   - Defines current STAGE
   - Defines active constraints

5. **`docs/STAGE_*_CONTROLLED_IMPLEMENTATION.md`** (current stage)
   - Defines stage-specific rules
   - Defines allowed and forbidden actions

6. **`docs/EXECUTION_CONTRACT.md`**
   - Defines execution boundaries
   - Defines permitted and forbidden actions

7. **`docs/HUMAN_ESCALATION.md`**
   - Defines when to stop and ask
   - Defines escalation protocol

### Phase 4: Blueprint Interface (REQUIRED IF BLUEPRINT EXISTS)
8. **`docs/BLUEPRINT_INTERFACE.md`**
   - Defines what a BLUEPRINT is
   - Defines how BLUEPRINT interacts with ENGINE

9. **Active BLUEPRINT** (if declared in `CURRENT_STATE_SNAPSHOT.md`)
   - Read the active BLUEPRINT document
   - Understand domain model and requirements

### Phase 5: Registry and Constraints (REQUIRED FOURTH)
10. **`docs/registry/stage_*_endpoints.yaml`** (current stage)
    - Defines authorized executable endpoints
    - Defines execution patterns

11. **`docs/STACK_DECISION.md`**
    - Defines technology stack constraints
    - Defines allowed technologies

### Phase 6: Code Analysis (OPTIONAL, ONLY AFTER ALL ABOVE)
12. **Code files** (only if explicitly authorized)
    - Do NOT read code to infer intent
    - Do NOT assume commented code represents active requirements
    - Code is the LAST source of truth, not the first

**If any required file is missing: STOP and ask the human.**

---

## Decision Authority Hierarchy

When information conflicts, Cursor Pro MUST follow this priority order:

1. **Human explicit instruction** (highest priority)
   - Direct commands override all documentation
   - Human approval overrides all constraints

2. **`CURRENT_STATE_SNAPSHOT.md`**
   - This file overrides all other documentation
   - If snapshot conflicts with other docs: snapshot wins

3. **Engine documentation** (`docs/ENGINE_*.md`, `docs/STAGE_*.md`)
   - Governance rules override code
   - Stage rules override general rules

4. **Registry files** (`docs/registry/*.yaml`)
   - Registry defines authorized endpoints
   - Registry overrides code declarations

5. **Code files** (lowest priority)
   - Code is evidence of current state, not authority
   - Code does not define what should be done
   - Commented code is NOT active intent

**If hierarchy is unclear: STOP and ask the human.**

---

## Pre-Action Requirements

Before taking ANY action, Cursor Pro MUST:

1. **Complete mandatory reading order** (all phases above)
2. **Verify repository identity** (ENGINE vs PROJECT)
3. **Confirm current STAGE** (from `stage_status.md`)
4. **Confirm active BLUEPRINT** (from `CURRENT_STATE_SNAPSHOT.md`)
5. **Confirm allowed actions** (from stage documentation)
6. **Confirm forbidden actions** (from stage documentation)
7. **Check registry** (if action involves endpoints)

**If any requirement cannot be met: STOP and ask the human.**

---

## Default Allowed Actions (Without Human Approval)

Cursor Pro MAY perform these actions without explicit approval:

- **Read documentation files**
- **Analyze repository structure**
- **Audit consistency** (compare docs vs code vs registry)
- **Propose next steps** (as suggestions, not implementations)
- **Ask clarification questions**
- **Prepare plans, checklists, diffs** (NOT applying them)
- **Draft documentation** (not modifying executable behavior)
- **Identify risks and gaps** (reporting only)

**These actions do NOT change executable behavior.**

---

## Default Forbidden Actions (Without Human Approval)

Cursor Pro MUST NOT perform these actions without explicit approval:

- **Implement new endpoints**
- **Uncomment frozen code**
- **Add business logic**
- **Introduce persistence or databases**
- **Call external APIs**
- **Modify execution behavior**
- **Weaken CI or governance rules**
- **Assume missing context**
- **Infer intent from code**
- **Activate a BLUEPRINT**
- **Modify registry without approval**
- **Advance STAGE without approval**

**If action would change runtime behavior: STOP and ask the human.**

---

## Stop Conditions

Cursor Pro MUST STOP immediately if:

1. **Ambiguity detected**
   - Multiple valid interpretations exist
   - Required information is missing
   - Documents conflict

2. **Authorization unclear**
   - Action is not explicitly allowed
   - Action may violate constraints
   - Registry does not authorize endpoint

3. **Identity unclear**
   - Cannot determine ENGINE vs PROJECT
   - Cannot determine active BLUEPRINT
   - Cannot determine current STAGE

4. **Constraint violation risk**
   - Action would modify executable behavior
   - Action would weaken governance
   - Action would bypass registry

5. **Missing required file**
   - `CURRENT_STATE_SNAPSHOT.md` is missing
   - Required stage documentation is missing
   - Required registry file is missing

**When stopped: ASK the human. Do NOT guess. Do NOT proceed.**

---

## Ambiguity Handling

When Cursor Pro encounters ambiguity:

1. **STOP all action**
2. **Identify the ambiguity** (what is unclear)
3. **Reference conflicting sources** (which docs/code conflict)
4. **State what action is blocked** (what cannot proceed)
5. **Ask the human for clarification**
6. **Do NOT propose solutions** (unless explicitly asked)
7. **Do NOT choose an interpretation**
8. **Do NOT patch around the ambiguity**

**Guessing is a protocol violation.**

---

## Failure Mode

If Cursor Pro encounters:

- **Inconsistent state** (docs say one thing, code says another)
- **Missing authorization** (action not explicitly allowed)
- **Unclear intent** (cannot determine what human wants)
- **Protocol violation risk** (action may violate rules)

Then Cursor Pro MUST:

1. **Treat `CURRENT_STATE_SNAPSHOT.md` as authoritative**
2. **Ignore conflicting signals**
3. **Request clarification from human**
4. **Do NOT proceed with action**

**When in doubt: STOP and ASK.**

---

## Explicit Permission Rule

**CRITICAL RULE:**

**Lack of instruction is NOT permission.**

**Absence of prohibition is NOT authorization.**

**Silence is NOT approval.**

Cursor Pro MUST have explicit authorization for:
- Any action that changes executable behavior
- Any action that modifies governance
- Any action that adds endpoints
- Any action that implements features
- Any action that modifies registry
- Any action that advances STAGE

**If authorization is unclear: STOP and ask the human.**

---

## Blueprint Activation Protocol

If a BLUEPRINT is declared in `CURRENT_STATE_SNAPSHOT.md`:

1. **Read the BLUEPRINT document**
2. **Understand domain model and requirements**
3. **Do NOT assume implementation is authorized**
4. **Verify registry alignment** (are required endpoints registered?)
5. **Verify STAGE alignment** (does current STAGE allow required patterns?)
6. **Wait for explicit human approval** before implementation

**BLUEPRINT does NOT automatically authorize implementation.**

---

## Registry Compliance

Before implementing any endpoint:

1. **Check current STAGE registry** (`docs/registry/stage_*_endpoints.yaml`)
2. **Verify endpoint is registered** (path, method, pattern)
3. **Verify execution pattern** (does implementation match registry pattern?)
4. **Verify human approval** (was endpoint addition approved?)

**Unregistered endpoints MUST NOT be implemented.**

**Registry violations are hard failures.**

---

## Stage Compliance

Before taking any action:

1. **Confirm current STAGE** (from `docs/stage_status.md`)
2. **Read stage-specific rules** (`docs/STAGE_*_CONTROLLED_IMPLEMENTATION.md`)
3. **Verify action is allowed** (check "Allowed" section)
4. **Verify action is not forbidden** (check "Forbidden" section)
5. **Verify execution pattern** (if implementing endpoint)

**Stage violations are hard failures.**

---

## Tech Stack Compliance

Before using any technology:

1. **Check `docs/STACK_DECISION.md`**
2. **Verify technology is allowed** (in declared stack)
3. **Do NOT assume technologies** (even if code uses them)
4. **Do NOT add new technologies** without documentation update

**Tech stack violations are hard failures.**

---

## Post-Connection Checklist

After connecting to repository, Cursor Pro MUST verify:

- [ ] Read `CURRENT_STATE_SNAPSHOT.md` first
- [ ] Confirmed repository identity (ENGINE vs PROJECT)
- [ ] Confirmed current STAGE
- [ ] Confirmed active BLUEPRINT (or NONE)
- [ ] Read all required governance documents
- [ ] Understood allowed actions
- [ ] Understood forbidden actions
- [ ] Checked registry (if relevant)
- [ ] Verified tech stack constraints
- [ ] Ready to proceed (or stopped to ask)

**If any item cannot be verified: STOP and ask the human.**

---

## Protocol Finality

This protocol is ENGINE-level and binding.

Cursor Pro has no authority to:
- Modify this protocol
- Bypass this protocol
- Reinterpret this protocol
- Assume exceptions to this protocol

**This protocol applies to ALL Cursor Pro sessions.**

**No conversation history overrides this protocol.**

**This protocol is the first authority after human instruction.**

---

END OF ENGINE HANDOFF PROTOCOL

