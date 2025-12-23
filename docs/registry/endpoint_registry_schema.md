# Endpoint Registry Schema

This document defines the schema for endpoint registry entries across all stages.

## Schema Definition

Each endpoint entry in a registry YAML file must conform to the following structure:

### Required Fields

#### `name` (string, required)
- Unique identifier for the endpoint
- Used for documentation and reference purposes
- Example: `health_check`, `version`, `get_agents`

#### `stage_introduced` (integer, required)
- The stage number when this endpoint was first introduced
- Used for tracking endpoint lifecycle
- Example: `4`, `5`

#### `path` (string, required)
- The HTTP path for the endpoint
- Must start with `/`
- Example: `/health`, `/version`, `/api/core/agents`

#### `method` (string, required)
- HTTP method (uppercase)
- Must be one of: `GET`, `POST`, `PUT`, `DELETE`, `PATCH`, `HEAD`, `OPTIONS`
- Example: `GET`

#### `response` (object, required)
- Response specification for the endpoint

##### `response.type` (string, required)
- Type of response
- Example: `constant_json`, `dynamic_json`, `error`

##### `response.value` (any, required)
- The response value structure
- For `constant_json`, this is the fixed JSON structure
- Example:
  ```yaml
  value:
    status: ok
  ```

### Optional Fields

#### `notes` (string, optional)
- Additional documentation or notes about the endpoint
- Can include implementation details, constraints, or future plans
- Example: `"Returns fixed health status. No side effects."`

## Example Registry Entry

```yaml
endpoints:
  - name: health_check
    stage_introduced: 4
    path: /health
    method: GET
    response:
      type: constant_json
      value:
        status: ok
    notes: "Minimal health check endpoint. Returns fixed response."
```

## Registry File Structure

Each stage-specific registry file should have the following top-level structure:

```yaml
stage: <stage_number>
registry_type: authorized_endpoints
description: >
  Explicit registry of all executable backend endpoints
  authorized under Stage <stage_number> Controlled Implementation.

execution_pattern: <pattern_name>

endpoints:
  - name: <endpoint_name>
    stage_introduced: <stage_number>
    path: <path>
    method: <method>
    response:
      type: <type>
      value: <value>
    notes: <optional_notes>
```

## Validation Rules

1. All required fields must be present
2. `path` must start with `/`
3. `method` must be a valid HTTP method (uppercase)
4. `stage_introduced` must match the registry file's stage number or be lower
5. `response.type` must be a recognized type
6. `response.value` must be valid for the specified type

