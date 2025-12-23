# Stage 5 – Controlled Implementation (Expanded)

## Purpose
Allow controlled implementation of additional endpoints under strict registry and CI enforcement, while maintaining the same execution constraints as Stage 4. Stage 5 enables incremental expansion of the executable surface area through explicit registry-based authorization.

## Current Stage Declaration
Current Stage: Stage 5

Stage 5 is ACTIVE.

Stage 4 is CLOSED and LOCKED (baseline remains frozen).

## Relationship to Stage 4

Stage 5 builds upon Stage 4's foundation with **one key difference**:

- **Stage 4**: Only endpoints explicitly listed in `docs/registry/stage_4_endpoints.yaml` are authorized
- **Stage 5**: Allows additional endpoints to be authorized through registry updates, but **only after explicit human approval** and CI verification

**All other Stage 4 constraints remain unchanged in Stage 5.**

## Allowed

Stage 5 maintains the same execution constraints as Stage 4:

- Executable endpoints **only if** they conform to the "Authorized Execution Pattern" (same as Stage 4)
- No persistence
- No external API calls
- No background tasks
- No state mutation beyond in-memory constants

**Additional allowance in Stage 5:**

- New endpoints may be added to the registry **only after**:
  - Explicit human approval
  - Registry update in `docs/registry/stage_5_endpoints.yaml` (or appropriate registry file)
  - CI verification passes
  - Endpoint implementation conforms to the Authorized Execution Pattern

## Forbidden

All Stage 4 forbidden items remain forbidden in Stage 5:

- Database integration
- Auth
- Async workflows
- AI calls
- Side effects

**Additional restriction in Stage 5:**

- No endpoint may be implemented or activated without explicit registry entry and human approval
- No endpoint may be added to the registry without going through the approval process

## Authorized Execution Pattern

Stage 5 uses the **same execution pattern as Stage 4**:

### Execution Constraints
An authorized endpoint must satisfy **all** of the following:

- HTTP GET only
- No parameters
- No request body
- No access to runtime state, filesystem, network, environment variables, or database
- No conditional logic based on external or runtime input
- No side effects
- Synchronous execution only
- Deterministic, constant response
- JSON-serializable return value

### Authorization Rule
Any executable backend logic that does not fully conform to this pattern is considered an **implementation violation** and is blocked by CI.

## Endpoint Registry

All executable endpoints authorized in Stage 5 must be defined in:

- `docs/registry/stage_5_endpoints.yaml` (or appropriate stage-specific registry)

Any executable endpoint not present in the registry is considered unauthorized.

## Human Gate

**Every new endpoint addition requires:**

1. **Explicit Human Approval**: No endpoint may be added without explicit approval
2. **Registry Update**: Endpoint must be added to the appropriate registry file
3. **CI Verification**: CI must pass with the new endpoint registered
4. **Implementation Conformance**: Endpoint implementation must conform to the Authorized Execution Pattern

## Differences from Stage 4

The **only difference** between Stage 4 and Stage 5 is:

- **Stage 4**: Fixed set of endpoints (baseline locked)
- **Stage 5**: Allows incremental expansion through registry updates, but maintains all execution constraints and requires explicit approval for each addition

All execution constraints, forbidden items, and CI requirements remain identical to Stage 4.

## Stage 4 to Stage 5 Transition Status

Stage 5 transition is COMPLETE:

1. ✅ `docs/stage_status.md` declares Stage 5 as active
2. ✅ All Stage 4 constraints remain in effect
3. ✅ Stage 5 endpoint registry established (`docs/registry/stage_5_endpoints.yaml`)
4. ✅ CI enforcement for registry compliance active

Stage 4 baseline is LOCKED and FROZEN.

