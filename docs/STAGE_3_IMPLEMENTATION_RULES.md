# Stage 3 — Implementation Rules (Frozen)

## Stage Purpose
Stage 3 exists to convert Stage 2 skeletons into
**minimal, runnable implementations**.

This stage is NOT for:
- Feature expansion
- Product design
- Workflow invention
- Business logic enrichment

## Allowed Operations
Cursor Pro MAY:
- Implement minimal executable code based strictly on existing skeletons
- Wire components together in the simplest possible way
- Use placeholders, stubs, or no-op implementations where behavior is undefined
- Add minimal configuration required for execution (build/run)

## Forbidden Operations
Cursor Pro MUST NOT:
- Add new features or capabilities
- Invent workflows, state transitions, or rules
- Interpret or extend S1 / S2 semantics
- Add validation, optimization, or “best practices”
- Refactor structure without explicit authorization
- Modify frozen documents

## Definition of "Minimal"
"Minimal" means:
- Code runs
- UI renders
- APIs respond (even with empty or mock responses)
- No additional meaning is inferred

## Escalation Rule
If implementation requires:
- A decision not explicitly defined in S1 / S2
- Interpretation of business meaning
- Selection between multiple plausible behaviors

Cursor Pro MUST stop and escalate via HUMAN_ESCALATION.md.

## Termination Condition
Stage 3 ends when:
- The system builds and runs
- All skeletons are executable
- No undefined references remain

Further enhancement requires a new Stage authorization.