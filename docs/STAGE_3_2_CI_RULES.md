# STAGE 3.2 — CI ENFORCEMENT RULES

Status: Authoritative  
Scope: Cursor Pro execution constraint  
Applies To: All automated execution agents  

---

## 1. Purpose

Stage 3.2 establishes **CI-enforced execution constraints** to prevent:
- Unauthorized stage advancement
- Technology stack contamination
- Silent requirement mutation
- Premature implementation logic
- AI-driven overreach

All rules below are **mandatory** and **machine-enforceable**.

---

## 2. Stage Guard Rule

### Rule

CI MUST read `/docs/stage_status.md`.

If current stage is:
- `Stage 3`
- `Stage 3.1`
- `Stage 3.2`

Then CI MUST enforce:

- ❌ No new business logic
- ❌ No inferred workflows
- ❌ No semantic interpretation
- ❌ No feature expansion

### Violation Result

CI MUST FAIL with message:

Stage violation: unauthorized implementation detected

---

## 3. Technology Stack Lock

### Backend (`/backend`)

#### Allowed
- `.py`
- `requirements.txt`
- `pyproject.toml`
- `.env.example`

#### Forbidden
- `.ts`
- `.js`
- `package.json`
- `node_modules/`

### Frontend (`/frontend`)

#### Allowed
- `.ts`
- `.tsx`
- `package.json`
- `vite.config.*`
- `webpack.config.*`

#### Forbidden
- `.py`
- `requirements.txt`
- Any FastAPI / Flask imports

### Violation Result

CI MUST FAIL with message:

Stack violation: unauthorized technology detected

---

## 4. SSOT (Single Source of Truth) Lock

The following documents are **immutable**:

- `AI_Virtual_Company_Organizational_GCD_v2`
- `/docs/GCD.md`
- `/docs/S1_frontend_definition.md`
- `/docs/S2_backend_definition.md`

### Rule

- ❌ CI MUST NOT allow modification
- ❌ CI MUST NOT auto-fix
- ❌ Cursor MUST NOT regenerate

### Violation Result

CI MUST FAIL with message:

SSOT violation: frozen document modified — human approval required

---

## 5. Implementation Ban (Pre-Stage-4)

### Backend Prohibited Patterns

- Database operations
- Persistent storage logic
- AI API calls
- Meaningful control flow (`if`, `for`, `while` with non-empty bodies)

### Backend Allowed

- `pass`
- `raise NotImplementedError`
- Empty return values

### Frontend Prohibited Patterns

- API calls with real endpoints
- State transition logic
- Validation logic
- Side-effect-driven `useEffect`

### Frontend Allowed

- Placeholder JSX
- Empty handlers
- Mock props

### Violation Result

CI MUST FAIL with message:

Implementation violation: executable logic detected before authorization

---

## 6. Human Escalation Rule

If CI encounters:

- Rule conflict
- Ambiguous file ownership
- Undefined mapping to S1 / S2 / GCD
- New concept without documentation source

Then:

- ❌ CI MUST NOT auto-resolve
- ❌ CI MUST NOT guess
- ❌ Cursor MUST STOP

### Required CI Output

Escalation required.
Reason: 
Reference: HUMAN_ESCALATION.md

---

## 7. CI Behavior Contract

CI is a **gatekeeper**, not an implementer.

CI MUST:
- Fail loudly
- Provide deterministic error messages
- Prevent forward progress on violation

CI MUST NOT:
- Auto-correct requirements
- Introduce assumptions
- Silence violations

---

## 8. Authority

This document overrides:
- Prompt-level instructions
- Agent heuristics
- Execution optimism

Compliance is mandatory.