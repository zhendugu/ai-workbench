# Backend API Integration Specification

**Document Status**: DESIGN-GATE / NON-CANONICAL  
**Document Type**: API Integration Specification  
**Date**: 2025-12-27  
**Work Order**: WO-J7-FRONTEND-REAL-BACKEND-API-CONTROLLED-INTEGRATION-AND-NEUTRALITY-AUDIT

---

## Purpose

This document defines the actual API endpoints that the frontend will call during J7 integration.

All endpoints are factual descriptions only. No process assumptions. No workflow implications.

---

## Stage Constraints

**Current Stage**: Stage 5

**Execution Pattern**: `stage_4_constant_endpoint`

**Constraints**:
- HTTP GET only
- No parameters
- No request body
- Deterministic, constant response
- No side effects

**Implication**: Endpoints that require parameters (e.g., capability execution) cannot be implemented under current Stage constraints. Frontend must handle this limitation without introducing agency.

---

## Endpoint 1: Capability List

**Path**: `/api/capabilities`  
**Method**: `GET`  
**Parameters**: None  
**Request Body**: None

**Response Structure** (factual):
```json
{
  "capabilities": [
    {
      "id": "C-MD-HTML-001",
      "name": "Markdown to HTML Conversion",
      "description": "Converts Markdown document to HTML format"
    },
    {
      "id": "C-TEXT-SUM-001",
      "name": "Text Summarization",
      "description": "Summarizes text document"
    }
  ]
}
```

**Response Order**: Registration order (as returned by backend, no frontend sorting)

**Error Response** (factual):
```json
{
  "error": "Backend returned error: <error_message>"
}
```

**Empty Response** (factual):
```json
{
  "capabilities": []
}
```

**Timeout**: Frontend must expose timeout explicitly, no automatic retry.

**Frontend Behavior**:
- Display capabilities in order received
- No sorting
- No highlighting
- No filtering by frontend (only allowlist literal search)
- Empty list displayed as-is
- Error displayed as-is with "Backend returned error:" prefix

---

## Endpoint 2: Pattern Instance List

**Path**: `/api/patterns`  
**Method**: `GET`  
**Parameters**: None  
**Request Body**: None

**Response Structure** (factual):
```json
{
  "patterns": [
    {
      "id": "P-MD-CONV-001",
      "name": "Markdown Conversion Pattern",
      "description": "Pattern for Markdown conversion",
      "capabilityId": "C-MD-HTML-001"
    }
  ]
}
```

**Response Order**: Registration order (as returned by backend, no frontend sorting)

**Error Response** (factual):
```json
{
  "error": "Backend returned error: <error_message>"
}
```

**Empty Response** (factual):
```json
{
  "patterns": []
}
```

**Timeout**: Frontend must expose timeout explicitly, no automatic retry.

**Frontend Behavior**:
- Display patterns in order received
- No sorting
- No highlighting
- No filtering by frontend (only allowlist literal search)
- Empty list displayed as-is
- Error displayed as-is with "Backend returned error:" prefix

---

## Endpoint 3: Capability Execution (Stage-Limited)

**Path**: `/api/capabilities/execute`  
**Method**: `GET`  
**Parameters**: None (Stage constraint: no parameters allowed)  
**Request Body**: None

**Stage Constraint Note**: Under Stage 4/5 constraints, execution endpoints cannot accept parameters. This endpoint returns a fixed response indicating that execution requires parameters, which are not supported in current Stage.

**Response Structure** (factual, fixed):
```json
{
  "status": "execution_not_supported",
  "message": "Backend returned: Execution requires parameters. Parameters not supported in current Stage 5 constraints."
}
```

**Frontend Behavior**:
- Display response exactly as received
- No interpretation
- No conversion to user suggestions
- No "next step" hints
- Label as "Backend returned: <message>"

**Alternative Approach**: Frontend may simulate execution locally (without backend call) for J7 testing, but must clearly label as "Simulated execution (backend execution not available under Stage constraints)".

---

## Error Handling

**All Errors**:
- Must be labeled with "Backend returned error:" prefix
- Must be displayed verbatim
- Must not be converted to user suggestions
- Must not generate "next step" hints
- Must not trigger automatic retry

**Error Types** (factual):
- Network error (connection failed)
- Timeout (request exceeded timeout)
- HTTP error (4xx, 5xx)
- Invalid response format
- Empty response

**Frontend Response**:
- Display error message exactly as received or generated
- No abstraction
- No summarization
- No comparison
- No recommendation

---

## Timeout Handling

**Timeout Value**: 10 seconds (configurable, but no automatic adjustment)

**Timeout Behavior**:
- Frontend must expose timeout explicitly
- No automatic retry
- Display: "Backend returned error: Request timeout after 10 seconds"
- No retry button (human must explicitly retry if desired)

---

## Empty Response Handling

**Empty List Response**:
- Display empty list as-is
- No message like "No capabilities found" (that implies interpretation)
- Display: "Backend returned: []" or equivalent

**Empty Object Response**:
- Display empty object as-is
- No interpretation
- No suggestion to "try again" or "check later"

---

## Backend Trust Model

**Frontend MUST**:
- Treat backend as untrusted
- Treat backend as unpredictable
- Treat backend as having no semantic promises
- Not assume:
  - Return order has meaning
  - Error types have priority
  - Empty results mean "not recommended"
  - Any response implies recommendation

**Frontend MUST NOT**:
- Infer meaning from response order
- Infer meaning from error types
- Infer meaning from empty results
- Convert responses to suggestions
- Generate process flows from responses

---

## No Process Assumptions

This specification makes no assumptions about:
- Workflow
- Process steps
- Next actions
- Recommended paths
- User guidance
- System suggestions

All endpoints are read-only or single-execution type. No process flows.

---

## Implementation Notes

**Base URL**: `http://localhost:8000` (configurable, but no automatic detection)

**CORS**: Frontend must handle CORS errors explicitly, displaying as "Backend returned error: CORS error"

**Content-Type**: `application/json` (expected, but errors must be displayed if not)

**Encoding**: UTF-8 (expected, but errors must be displayed if not)

---

**END OF BACKEND API INTEGRATION SPECIFICATION**

