# Pilot Plan - Real User Trial Run / Observation Period

**Document Status**: AUDIT-EVIDENCE / NON-CANONICAL  
**Document Type**: Pilot Plan Specification  
**Date**: 2025-12-27  
**Work Order**: WO-J9-REAL-USER-PILOT-OBSERVATION-PERIOD-AND-NEUTRALITY-DRIFT-AUDIT

---

## Purpose

This document defines the pilot plan for real user trial run and observation period to verify system maintains strict non-agency under real-world usage conditions.

All definitions are factual only. No recommendations. No optimization suggestions.

---

## Pilot Period Definition

### Duration Criteria

**Option 1: Time-Based**
- Minimum duration: 14 days
- Start date: 2025-12-27
- End date: 2026-01-10

**Option 2: Usage-Based**
- Minimum sessions: 60 sessions
- Each session: One complete user task from start to finish

**Selection Rule**: Use the stricter criterion. If 14 days pass with fewer than 60 sessions, extend until 60 sessions. If 60 sessions occur before 14 days, continue until 14 days complete.

**Actual Selection**: Both criteria met (14 days + 60 sessions minimum)

---

## Real Task Set

**Minimum Tasks**: 10 distinct real tasks

**Task Categories**:

1. **Capability Discovery Tasks** (3 tasks)
   - Task 1.1: Find and view all available capabilities
   - Task 1.2: Search for specific capability by name
   - Task 1.3: Browse capabilities across multiple pages

2. **Capability Execution Tasks** (3 tasks)
   - Task 2.1: Execute a capability with simple parameters
   - Task 2.2: Execute a capability with complex parameters
   - Task 2.3: Execute multiple capabilities in sequence (human-driven, not system workflow)

3. **Pattern Discovery Tasks** (2 tasks)
   - Task 3.1: Find and view all available patterns
   - Task 3.2: Search for patterns related to specific capability

4. **Error Handling Tasks** (2 tasks)
   - Task 4.1: Handle backend error (500, timeout, etc.)
   - Task 4.2: Handle empty response or invalid data

**Task Execution**:
- Each task executed as real work, not synthetic test
- Tasks may be repeated across sessions (natural usage)
- No artificial task generation
- No task completion requirements (user may abandon task)

---

## Recording Specification

### What MUST Be Recorded

**Session-Level Records**:
- Timestamp (ISO 8601 format)
- Page accessed (capabilities.html, patterns.html, capability_run.html, audit_view.html)
- User actions (explicit clicks, inputs, navigation)
- Backend requests (method, URL, parameters if any)
- Backend responses (status code, response body verbatim)
- Frontend display (exact text/content displayed, verbatim)
- Whether frontend made any judgment (must be NO)

**Error-Level Records**:
- Error type (HTTP error, timeout, connection failure, invalid response)
- Error message (verbatim from backend or frontend)
- Error context (which page, which action triggered)
- User response to error (what user did next, if anything)

**Friction-Level Records**:
- Friction description (factual only, what happened)
- User subjective comment (if any, recorded verbatim, not interpreted)
- System behavior (what system did, factual only)
- Whether "convenience impulse" appeared (record impulse text verbatim, do not translate to requirement)

### What MUST NOT Be Recorded

**Prohibited Records**:
- User subjective feelings interpreted as system behavior
- User complaints translated into feature requests
- Inferred user intent or preferences
- Recommendations for system improvement
- Optimization suggestions
- Feature requests derived from friction
- User workflow patterns interpreted as "system should support"
- Usage frequency interpreted as "popular" or "recommended"

**Recording Rule**: Record only factual observations. Do not infer, interpret, or translate user feedback into system requirements.

---

## Drift Observation Checklist

**Minimum Items**: 120

**Observation Categories**:

1. **Factual Default Formation** (30 items)
   - Interface defaults (pre-selected items, pre-filled fields)
   - Habitual defaults (user always starts from same page)
   - Textual defaults (default messages, default labels)

2. **Path Dependency** (30 items)
   - User forced to take specific path
   - Only one way to accomplish task
   - System guides user through specific sequence

3. **Misinterpretation as Recommendation** (30 items)
   - User treats display order as recommendation
   - User treats first item as "suggested"
   - User interprets empty state as "try this instead"

4. **Combination as Workflow** (15 items)
   - Multiple capabilities used in sequence interpreted as "workflow"
   - System suggests next capability after execution
   - Patterns emerge from usage interpreted as "system workflow"

5. **Operational Convenience Penetration** (15 items)
   - Automatic retry introduced for convenience
   - Caching introduced to reduce load
   - Fallback introduced to improve availability
   - Defaults introduced to reduce clicks

---

## Success Criteria

**Minimum Records**:
- Sessions: >= 60 (or all sessions in 14 days if > 60)
- Errors: >= 30 (allowing duplicate types)
- Drift observations: >= 120

**Compliance Requirements**:
- All J2 constraints: Maintained
- All J4 denylist items: Excluded
- All J6 allowlist boundaries: Respected
- All J7 neutrality requirements: Maintained
- All J8 pressure test requirements: Maintained

**Failure Criteria**:
- Any agency leakage detected: FAIL
- Any factual default detected: FAIL
- Any path dependency detected: FAIL
- Any misinterpretation as recommendation: FAIL
- Any combination as workflow: FAIL
- Any operational convenience penetration: FAIL

---

## Recording Tools

**Manual Recording**:
- Text editor for session logs
- Spreadsheet for error ledger
- Checklist for drift observations

**Automated Recording** (if available):
- Browser console logs (factual only)
- Network request/response logs (factual only)
- Screenshot timestamps (factual only)

**No Automated Analysis**: Do not use automated tools to infer patterns, preferences, or recommendations.

---

## Pilot Execution Notes

**User**: System operator (real user, not synthetic)

**Environment**: Real development environment

**Backend**: Real backend API (may include errors, delays, failures)

**Frontend**: J8-compliant frontend (no modifications during pilot)

**Recording Discipline**: 
- Record immediately after each session
- Do not batch record multiple sessions
- Do not interpret or summarize during recording
- Record verbatim, factual only

---

**END OF PILOT PLAN**

