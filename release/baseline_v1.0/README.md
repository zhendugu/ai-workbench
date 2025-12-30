# Baseline v1.0 - Minimal Publication Package

**Version**: Baseline v1.0  
**Status**: FROZEN  
**Date**: 2026-01-10  
**Purpose**: Verification and Reference Only

---

## Purpose

This package contains a minimal runnable instance of the baseline system.

**This package is for verification and reference only. Not for commercial use.**

---

## Contents

**Frontend Files**:
- `frontend/capabilities.html` - Capabilities list display
- `frontend/capability_run.html` - Capability execution interface
- `frontend/patterns.html` - Patterns list display
- `frontend/audit_view.html` - Audit records view

**Documentation**:
- `docs/BASELINE_RELEASE_DECLARATION.md` - Release declaration
- `docs/SYSTEM_FREEZE_MANIFEST.md` - Freeze manifest
- `docs/ANTI-MISINTERPRETATION_NOTICE.md` - Anti-misinterpretation notice
- `docs/RELEASE_EVIDENCE_INDEX.md` - Evidence index

**Reference**:
- Frontend source: `../../frontend_app/`
- Backend API specification: `../../docs/BACKEND_API_INTEGRATION_SPEC.md`

---

## Backend API Requirements

**Required Endpoints**:
- `GET /api/capabilities` - Returns capability list
- `GET /api/patterns` - Returns pattern list
- `GET /api/capabilities/execute` - Returns execution response

**API Specification**: See `../../docs/BACKEND_API_INTEGRATION_SPEC.md`

---

## Usage

**Frontend Access**:
- Open `frontend/capabilities.html` in web browser
- Frontend expects backend API at `http://localhost:8000/api/`

**Backend Requirements**:
- Backend must implement endpoints as specified in `BACKEND_API_INTEGRATION_SPEC.md`
- Backend must return responses in registration order
- Backend must return errors in format: `{"error": "Backend returned error: <message>"}`

---

## System Behavior

**Display**:
- Capabilities displayed in registration order
- Patterns displayed in registration order
- Results displayed verbatim
- Errors displayed verbatim

**Interaction**:
- Human explicit selection required
- Human explicit parameter input required
- Human explicit execution request required
- No automatic actions

**Prohibited**:
- No automatic retry
- No caching
- No fallback
- No suggestions
- No recommendations
- No defaults
- No shortcuts
- No workflows

---

## Verification

**Verification Status**: All J0-J9 work orders completed and verified.

**Evidence**: See `docs/RELEASE_EVIDENCE_INDEX.md`

---

## No Guidance

This package provides no usage guidance.

This package provides no onboarding.

This package provides no recommendations.

This package provides no suggestions.

This package states only the system structure.

---

## Version Status

**Version**: Baseline v1.0

**Status**: FROZEN

**Evolution**: NOT PERMITTED

**Reference**: This version serves as immutable reference point.

---

**END OF README**

