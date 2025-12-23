# ENGINE VERSION DECLARATION SPEC

## Purpose

This document defines how ENGINE versions are declared, identified, enforced, and upgraded.

ENGINE versioning governs governance rules, CI enforcement, and AI/Cursor behavior.
ENGINE versioning does NOT govern project/business logic.

ENGINE versions are explicit, immutable once activated, and cannot be inferred.

---

## Core Principle

ENGINE version is a FACT, not a guess.

- ENGINE version MUST be explicitly declared
- ENGINE version MUST be machine-readable
- ENGINE version MUST be enforced by CI
- ENGINE version MUST be respected by all AI agents

Absence of explicit version declaration is a hard failure.

---

## Authoritative Version Declaration

### Single Source of Truth

The ONLY authoritative source of ENGINE version is:

CURRENT_STATE_SNAPSHOT.md (repository root)

No other file, directory, branch, tag, or conversation context may declare ENGINE version.

---

### Required Field

CURRENT_STATE_SNAPSHOT.md MUST contain the following field:

ENGINE_VERSION: v{N}

Where:
- {N} is a positive integer (v1, v2, v3, ...)

Example:

ENGINE_VERSION: v1

---

### Mandatory Rules

- ENGINE_VERSION field MUST exist
- ENGINE_VERSION value MUST be parseable
- ENGINE_VERSION value MUST match a known ENGINE version
- ENGINE_VERSION value MUST NOT be inferred or defaulted

Violation of any rule above MUST cause CI failure.

---

## Version Activation Semantics

### Single Active Version

At any point in time:
- Exactly ONE ENGINE version is active
- The active version is the value declared in CURRENT_STATE_SNAPSHOT.md

Multiple ENGINE versions may coexist in documentation,
but ONLY the declared version is active.

---

### Version Immutability After Activation

Once ENGINE_VERSION is set to a value:

- Governance rules of that version apply immediately
- CI enforcement MUST switch to that version
- AI/Cursor behavior MUST be constrained by that version

Changing ENGINE_VERSION constitutes a governance-critical action.

---

## Governance Authority by Version

Each ENGINE version defines its own governance boundary.

### ENGINE v1

- Defined by ENGINE_V1_FREEZE.md
- Frozen permanently
- Rules cannot be weakened, removed, or reinterpreted
- Only additive extensions allowed via higher versions

### ENGINE v2 and Beyond

- Must be explicitly declared via versioned governance documents
- May extend or modify governance rules
- MUST NOT retroactively affect earlier versions

---

## CI Enforcement Requirements

CI MUST:

1. Read ENGINE_VERSION from CURRENT_STATE_SNAPSHOT.md
2. Validate that the version is known and supported
3. Load version-specific governance rules
4. Enforce ONLY the active version's rules
5. Fail immediately if version declaration is missing or invalid

CI MUST NOT:
- Guess version based on files present
- Default to latest version
- Allow mixed-version enforcement

---

## AI / Cursor Behavior Requirements

All AI agents (including Cursor Pro) MUST:

1. Read CURRENT_STATE_SNAPSHOT.md at startup
2. Identify ENGINE_VERSION explicitly
3. Load behavior constraints for that version only
4. Refuse to act if version is missing or ambiguous

AI agents MUST NOT:
- Infer version from repository structure
- Assume newest version
- Apply rules from a different ENGINE version
- Blend rules across versions

When uncertain, AI MUST STOP and ask the human.

---

## Version Upgrade Rules

### Explicit Human Action Required

Changing ENGINE_VERSION requires:

- Explicit human intent
- Direct modification of CURRENT_STATE_SNAPSHOT.md
- CI approval under anti-tamper and governance rules

AI agents are NOT permitted to upgrade ENGINE version autonomously.

---

### No Silent Upgrade

ENGINE version upgrade MUST NOT occur via:

- CI changes alone
- Documentation addition alone
- Registry changes
- Code structure changes

Only CURRENT_STATE_SNAPSHOT.md may activate a new version.

---

## Failure Modes

CI MUST fail with clear error messages if:

- ENGINE_VERSION field is missing
- ENGINE_VERSION value is unrecognized
- Multiple conflicting version declarations are detected
- Version-specific governance documents are missing

AI agents MUST refuse execution in the same cases.

---

## Non-Goals

This document does NOT:

- Define ENGINE v2 governance rules
- Define how business logic is written
- Define project upgrade procedures
- Define migration tooling

This document defines ONLY version declaration and activation rules.

---

## Finality

This specification is binding for all ENGINE versions.

ENGINE versioning rules defined here apply to:
- ENGINE v1
- ENGINE v2
- All future ENGINE versions

No ENGINE version may bypass this declaration mechanism.

---

END OF ENGINE VERSION DECLARATION SPEC

