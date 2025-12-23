# Stage 4 – Controlled Implementation

## Purpose
Allow minimal real implementation under strict CI and human approval.

## Current Stage Declaration
Current Stage: Stage 4

## Allowed
- Executable endpoints **only if** they conform to the
  "Authorized Execution Pattern (Stage 4)" defined below
- No persistence
- No external API calls
- No background tasks
- No state mutation beyond in-memory constants

## Explicitly Authorized Endpoints
The following endpoints are the **only concrete instantiations**
of the Authorized Execution Pattern in Stage 4:

- `/health` - Returns fixed `{"status": "ok"}` response

## Forbidden
- Database integration
- Auth
- Async workflows
- AI calls
- Side effects

## CI Requirement
- All CI checks must pass
- Any violation blocks merge

## Human Gate
- Any scope expansion requires explicit human approval

## Authorized Execution Pattern (Stage 4)

Stage 4 permits a strictly limited form of executable backend code
only under the following execution pattern.

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
Any executable backend logic that does not fully conform to this pattern
is considered an **implementation violation** and is blocked by CI.

### Scope Limitation
This execution pattern is valid **only for Stage 4**.
Any expansion or modification of this pattern requires:
- Explicit documentation update
- Human approval
- CI rule update

## Authorized Endpoint Registry

All executable endpoints authorized in Stage 4
are defined exclusively in:

- `docs/registry/stage_4_endpoints.yaml`

Any executable endpoint not present in this registry
is considered unauthorized.

## Stage 4 Baseline Lock

The Stage 4 baseline has been locked. This means:

- **Baseline Status**: Stage 4 baseline is locked
- **Endpoint Registry Enforcement**: Registry-based endpoint enforcement is active
- **CI Enforcement**: CI blocks any unregistered endpoint
- **Non-Authorized Endpoints**: All non-authorized endpoints have been frozen or converted to stubs

Any expansion of executable surface area requires:

- **Registry Update**: Endpoint must be added to `docs/registry/stage_4_endpoints.yaml`
- **CI Verification**: CI must pass with the new endpoint registered
- **Human Approval**: Explicit human approval is required for any scope expansion

This baseline lock ensures that Stage 4 remains in a controlled, auditable state
until explicit approval is granted for progression beyond Stage 4.