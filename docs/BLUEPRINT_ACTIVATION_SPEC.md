# BLUEPRINT ACTIVATION SPEC (ENGINE v1)

This document defines the ONLY valid mechanism to activate a Blueprint
in ENGINE v1.

Blueprint activation is a governance action.
It does NOT grant implementation permission by itself.

This specification is frozen for ENGINE v1.

--------------------------------------------------------------------

CORE PRINCIPLES

- Only ONE blueprint may be active at any time
- Activation must be explicit and centralized
- Activation must be machine-verifiable
- Absence of activation means NO project exists
- Activation is reversible only by explicit human action

No implicit activation is allowed.

--------------------------------------------------------------------

SOURCE OF TRUTH

The active Blueprint is declared ONLY in:

CURRENT_STATE_SNAPSHOT.md (repository root)

No other file, directory, commit message, or convention
is allowed to declare activation.

--------------------------------------------------------------------

REQUIRED FIELD

CURRENT_STATE_SNAPSHOT.md MUST contain exactly one of the following:

ACTIVE_BLUEPRINT: none
ACTIVE_BLUEPRINT: <blueprint_name>

Rules:
- <blueprint_name> must match an existing directory under `/blueprints/`
- `/blueprints/` is the ONLY valid root directory for BLUEPRINT files
- The blueprint directory MUST contain `BLUEPRINT.md` (case-sensitive)
- The value MUST be exact (case-sensitive)
- Directory existence does NOT imply activation
- Only `ACTIVE_BLUEPRINT` field in `CURRENT_STATE_SNAPSHOT.md` determines activation

Examples:

ACTIVE_BLUEPRINT: none
ACTIVE_BLUEPRINT: user-auth-system

--------------------------------------------------------------------

ACTIVATION STATES

There are only two valid states:

1. INACTIVE STATE
   ACTIVE_BLUEPRINT: none

   Meaning:
   - No project is active
   - ENGINE operates as a construction base only
   - No implementation may proceed
   - CI must reject any project-specific execution

2. ACTIVE STATE
   ACTIVE_BLUEPRINT: <blueprint_name>

   Meaning:
   - Exactly one blueprint is active (determined by `ACTIVE_BLUEPRINT` field)
   - The blueprint directory MUST exist at `/blueprints/<blueprint_name>/BLUEPRINT.md`
   - All project reasoning is scoped to this blueprint
   - CI and Cursor must load and respect this blueprint
   - Implementation is still gated by stage + registry
   - Inactive blueprints (not declared in `ACTIVE_BLUEPRINT`) cannot drive implementation

Any other state is INVALID.

--------------------------------------------------------------------

ACTIVATION REQUIREMENTS

Before a Blueprint may be activated, ALL must be true:

- Blueprint exists at `/blueprints/<name>/BLUEPRINT.md` (the ONLY valid location)
- Blueprint conforms to BLUEPRINT INSTANCE FORMAT
- Blueprint status is "approved"
- Blueprint has no unresolved questions
- Explicit human intent to activate is present
- `CURRENT_STATE_SNAPSHOT.md` is updated with `ACTIVE_BLUEPRINT: <blueprint_name>`

**Activation Mechanism:**
- Activation occurs ONLY when `ACTIVE_BLUEPRINT` field is set in `CURRENT_STATE_SNAPSHOT.md`
- Directory existence alone does NOT activate a Blueprint
- No other file, directory, or convention can activate a Blueprint

ENGINE does NOT infer readiness.
ENGINE does NOT infer activation from directory presence.

--------------------------------------------------------------------

FORBIDDEN ACTIVATION METHODS

The following are explicitly forbidden:

- Inferring activation from directory presence
- Inferring activation from commit messages
- Inferring activation from CI context
- Activating multiple blueprints
- Activating via conversation context
- Activating by Cursor without human instruction

Any such behavior is a governance violation.

--------------------------------------------------------------------

DEACTIVATION RULES

Deactivation is performed ONLY by:

ACTIVE_BLUEPRINT: none

Rules:
- Deactivation is immediate
- Deactivation freezes all project-specific execution
- Deactivation does NOT delete files
- Deactivation does NOT imply project failure

--------------------------------------------------------------------

CI ENFORCEMENT EXPECTATIONS (DECLARATIVE)

ENGINE CI MUST enforce:

- If ACTIVE_BLUEPRINT is set:
  - The referenced blueprint directory must exist at `/blueprints/<blueprint_name>/BLUEPRINT.md`
  - `/blueprints/` is the ONLY valid location (other locations are invalid)
  - BLUEPRINT.md must be readable

- If ACTIVE_BLUEPRINT is none:
  - No blueprint-specific execution is allowed
  - Directory existence does NOT grant activation
  - No project reasoning may proceed

This document defines EXPECTATIONS only.
Implementation is defined elsewhere.

--------------------------------------------------------------------

CURSOR BEHAVIOR RULES

When ACTIVE_BLUEPRINT is set:

Allowed:
- Read the active blueprint
- Ask questions scoped to the active blueprint
- Prepare plans consistent with the blueprint

Forbidden:
- Reason about inactive blueprints
- Expand scope beyond blueprint
- Assume missing blueprint content

When ACTIVE_BLUEPRINT is none:

Allowed:
- Governance work
- ENGINE infrastructure work
- Blueprint drafting

Forbidden:
- Project-specific implementation
- Project-specific assumptions

--------------------------------------------------------------------

FAILURE MODE

If activation state is ambiguous or invalid:

- STOP
- Report the inconsistency
- Ask for explicit human instruction

Guessing is forbidden.

--------------------------------------------------------------------

END OF BLUEPRINT ACTIVATION SPEC