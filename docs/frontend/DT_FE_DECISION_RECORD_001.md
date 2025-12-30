# Design-Time Frontend Decision Record（冻结裁决）

**Document ID**: DT-FE-DECISION-RECORD-001

**Status**: FROZEN

**Scope**: Design-Time Frontend Only

**Authority**: Human Owner

**Date**: 2025-12-28

**Priority**: HIGHEST - This document OVERRIDES any ambiguity in other documents.

---

This document records irreversible human decisions regarding the Design-Time frontend.
All items in this document are FINAL.
No interpretation, extension, optimization, or substitution is allowed without creating a new Decision Record.

==================================================
DR-01: Template Semantic Boundary
==================================================

**Decision**:
Template is defined as a STRUCTURAL COPY SOURCE ONLY.

**Rules**:
- A Template provides an initial structural snapshot (Company + Cells + Relations).
- A Template does NOT carry:
  - Best practices
  - Recommendations
  - Methodology authority
  - Quality implication
  - Maturity implication
- Using a Template creates a NEW Draft that is fully independent.
- After copy, the Draft MUST NOT retain any runtime or semantic linkage to the Template.

**Explicitly Forbidden**:
- Template suitability scoring
- Template recommendation
- Template matching
- "This template fits you" semantics
- Auto-application or silent application of templates

**Rationale**:
Templates exist only to reduce mechanical setup cost, not to guide decisions.

==================================================
DR-02: Draft ID Semantic Boundary
==================================================

**Decision**:
Draft ID is a TECHNICAL IDENTIFIER ONLY.

**Rules**:
- Draft ID exists solely for:
  - Persistence
  - Reference
  - Version distinction
- Draft ID MUST NOT encode or imply:
  - Design stage
  - Progress
  - Completeness
  - Readiness
  - Maturity
  - Priority

**Explicitly Forbidden**:
- Stage-like naming (e.g. draft-1, draft-final, v2-ready)
- Progress indicators derived from Draft ID
- UI language implying advancement through Draft IDs

**Rationale**:
Draft represents mutability, not progression.

==================================================
DR-03: Design Stage Concept
==================================================

**Decision**:
The concept of "Design Stage" is EXPLICITLY NOT INTRODUCED in this version.

**Rules**:
- The only valid Company states are:
  - Draft
  - Frozen
- No intermediate or sub-states are allowed.
- No phase, step, stage, or readiness abstraction may be added.

**Explicitly Forbidden**:
- Early / Mid / Late design
- Stage 1 / Stage 2 / Stage 3
- Preparation / Review / Ready
- Any UI or logic implying partial completion

**Rationale**:
Design-Time is not a process pipeline.
It is an open-ended human design space with a single commitment point (Freeze).

==================================================
GLOBAL ENFORCEMENT RULE
==================================================

- This document OVERRIDES any ambiguity in other documents.
- If any future specification conflicts with this record:
  - This record takes precedence.
- Any change requires:
  - A new Decision Record
  - Explicit human approval
  - No retroactive interpretation

==================================================
IMPLEMENTATION DIRECTIVE (For Cursor)
==================================================

- Treat this document as immutable.
- Do NOT attempt to "improve usability" by adding inferred semantics.
- If implementation encounters ambiguity:
  - STOP
  - ASK
  - DO NOT ASSUME

==================================================
END OF RECORD
==================================================

