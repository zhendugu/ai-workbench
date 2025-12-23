# WORKFLOW RULES — Execution Governance

## 0. Purpose

This document defines how work progresses.
It does NOT define what to build.

---

## 1. Allowed Stages

Only the following stages exist:

- Stage 2: Implementation Preparation
- Stage 3: Implementation (explicitly authorized later)

Current authorized stage: Stage 2.

---

## 2. Stage 2 — Implementation Preparation

Allowed outputs:

- Code skeletons
- Folder structures
- Empty or placeholder files
- Type definitions without logic
- Interface stubs
- Configuration scaffolding

Disallowed outputs:

- Business logic
- Control flow
- Data validation
- State transitions
- Execution semantics

---

## 3. Task Generation Rule

Tasks are not manually written by humans.

Cursor Pro may generate an internal task list ONLY if:

- Tasks are mechanical
- Tasks do not require interpretation
- Tasks map 1:1 to S1 / S2 definitions

If a task requires judgment, STOP.

---

## 4. Advancement Rule

Cursor Pro may NOT advance stages.

Only a human decision may authorize:
- Entry into Stage 3
- Any modification of GCD, S1, or S2

---

## 5. Completion Rule

When no further Stage-legal actions remain:

- Cursor Pro must STOP
- Cursor Pro must report “No further authorized actions”
- Cursor Pro must not invent follow-up work

---

## 6. Anti-Drift Rule

Cursor Pro must not:

- “Prepare for future stages”
- Add hooks for later logic
- Create speculative extensibility

Work ends exactly at current authorization boundary.

---

## 7. Immutability

This workflow is frozen.
Cursor Pro cannot reinterpret or extend it.