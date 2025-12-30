# Frontend Boundaries Fact Audit (Negative Capability List)

**Work Order**: WO-FE-FACT-0

**Document Status**: FACT-AUDIT / READ-ONLY

**Purpose**: List capabilities that frontend MUST NOT provide, based on GCD_v2 and Phase Q/R constraints.

**Authority**: AI_Virtual_Company_Organizational_GCD_v2.md, Phase Q/R frozen documents, S1_BOUNDARY_ASSERTIONS.md, EXECUTION_CONTRACT.md

---

## Frontend Prohibited Capabilities

### 1. Execution Capabilities

**Prohibition**: Frontend MUST NOT execute work orders, trigger scripts, or invoke Python scripts.

**Authority**:
- `S1_BOUNDARY_ASSERTIONS.md`: "No buttons that: say 'Run', say 'Execute', say 'Approve', say 'Fix', say 'Optimize'"
- `S1_UI_ARCHITECTURE.md`: "The UI MUST NOT: run shell commands, invoke Python scripts, call any AI API"
- `S1_OPERATOR_README.md`: "This UI is a CONTROL SURFACE, not a control system. It must NOT: execute work orders, trigger scripts"

**Evidence**:
- `s1_ui/s1_server.py`: All endpoints are GET-only (read-only)
- `s1_ui/s1_data_indexer.py`: Only file read operations (no write, no execution)
- `s1_ui/static/js/*.js`: Only fetch() calls to API (no subprocess, no shell invocation)

**Fact**: Frontend is read-only. No execution capabilities exist in current implementation.

---

### 2. File Modification Capabilities

**Prohibition**: Frontend MUST NOT modify files, write to disk, or update markdown documents.

**Authority**:
- `S1_BOUNDARY_ASSERTIONS.md`: "No write() calls anywhere"
- `S1_UI_ARCHITECTURE.md`: "The UI MUST NOT: write to disk, modify markdown"
- `S1_OPERATOR_README.md`: "It must NOT: modify files"

**Evidence**:
- `s1_ui/s1_server.py`: No file write operations (only read operations)
- `s1_ui/s1_data_indexer.py`: Only `read_text()` operations (no `write_text()`)
- `s1_ui/static/js/*.js`: No `localStorage.setItem()` or file write operations

**Fact**: Frontend is read-only. No file modification capabilities exist in current implementation.

---

### 3. AI API Invocation Capabilities

**Prohibition**: Frontend MUST NOT call any AI API, invoke AI models, or trigger AI operations.

**Authority**:
- `S1_BOUNDARY_ASSERTIONS.md`: "No network calls" (except to local Flask server)
- `S1_UI_ARCHITECTURE.md`: "The UI MUST NOT: call any AI API"
- GCD_v2 Section 15.3: "AI 调用必须满足以下原则: 必须通过统一的 AI Gateway / Service 层"

**Evidence**:
- `s1_ui/s1_server.py`: No AI API calls (only file system reads)
- `s1_ui/static/js/*.js`: Only fetch() calls to local Flask API (no external API calls)
- No AI Gateway integration in frontend

**Fact**: Frontend does not call AI APIs. All AI operations must go through backend AI Gateway (not frontend).

---

### 4. Recommendation Capabilities

**Prohibition**: Frontend MUST NOT suggest actions, recommend decisions, or infer "next steps".

**Authority**:
- `S1_BOUNDARY_ASSERTIONS.md`: "UI does not infer or suggest actions"
- `S1_UI_ARCHITECTURE.md`: "The UI MUST NOT: infer 'next steps', suggest decisions, auto-detect improvements, summarize risks, perform audits, display 'recommendations'"
- GCD_v2 Section 6: "明确禁止的反模式: 为'管理便利'牺牲执行闭环"

**Evidence**:
- `s1_ui/static/js/*.js`: Only data display (no recommendation logic)
- No "suggest" or "recommend" functions in frontend code
- No AI-based recommendation system in frontend

**Fact**: Frontend does not provide recommendations. All recommendations must come from human judgment (not frontend).

---

### 5. Decision-Making Capabilities

**Prohibition**: Frontend MUST NOT make decisions, approve actions, or replace human judgment.

**Authority**:
- `S1_BOUNDARY_ASSERTIONS.md`: "No buttons that: say 'Approve'"
- `S1_UI_ARCHITECTURE.md`: "The UI MUST NOT: assist decision-making"
- GCD_v2 Section 2.1: "不以'人 / AI 实例'为中心" (human sovereignty)
- `docs/HUMAN_ESCALATION.md`: "Humans intervene only when machine execution cannot proceed without judgment"

**Evidence**:
- `s1_ui/static/js/*.js`: No decision-making logic (only data display)
- No "approve" or "reject" buttons in frontend
- No automated decision-making in frontend

**Fact**: Frontend does not make decisions. All decisions must be made by humans (not frontend).

---

### 6. Work Order Creation/Modification Capabilities

**Prohibition**: Frontend MUST NOT create or modify work orders.

**Authority**:
- `S1_BOUNDARY_ASSERTIONS.md`: "No write() calls anywhere"
- `S1_UI_ARCHITECTURE.md`: "The UI MUST NOT: write to disk, modify markdown"
- `docs/WORKFLOW_RULES.md` Section 3: "Tasks are not manually written by humans" (but also not by frontend)

**Evidence**:
- `s1_ui/s1_server.py`: No work order creation endpoints (only read endpoints)
- `s1_ui/s1_data_indexer.py`: Only reads work order files (does not create or modify)
- No work order creation UI in frontend

**Fact**: Frontend cannot create or modify work orders. Work orders are created via human action (not frontend).

---

### 7. Phase Advancement Capabilities

**Prohibition**: Frontend MUST NOT advance phases or modify phase status.

**Authority**:
- `docs/WORKFLOW_RULES.md` Section 4: "Cursor Pro may NOT advance stages. Only a human decision may authorize: Entry into Stage 3, Any modification of GCD, S1, or S2"
- `S1_BOUNDARY_ASSERTIONS.md`: "No buttons that: say 'Run', say 'Execute'"

**Evidence**:
- `s1_ui/s1_server.py`: No phase advancement endpoints (only read endpoints)
- `s1_ui/s1_data_indexer.py`: Only reads phase status files (does not modify)
- No phase advancement UI in frontend

**Fact**: Frontend cannot advance phases. Phase advancement requires human authorization (not frontend).

---

### 8. Evidence Pack Creation Capabilities

**Prohibition**: Frontend MUST NOT create or modify evidence packs.

**Authority**:
- `S1_BOUNDARY_ASSERTIONS.md`: "No write() calls anywhere"
- `S1_UI_ARCHITECTURE.md`: "The UI MUST NOT: write to disk, modify markdown, generate evidence"

**Evidence**:
- `s1_ui/s1_server.py`: No evidence pack creation endpoints (only read endpoints)
- `s1_ui/s1_data_indexer.py`: Only reads evidence pack directories (does not create or modify)
- No evidence pack creation UI in frontend

**Fact**: Frontend cannot create or modify evidence packs. Evidence packs are created via scripts or manual action (not frontend).

---

### 9. Decision Document Creation/Modification Capabilities

**Prohibition**: Frontend MUST NOT create or modify decision documents.

**Authority**:
- `S1_BOUNDARY_ASSERTIONS.md`: "No write() calls anywhere"
- `S1_UI_ARCHITECTURE.md`: "The UI MUST NOT: write to disk, modify markdown"
- Decision documents are FROZEN / REFERENCE-ONLY (per PARADIGM_FREEZE_DECLARATION.md)

**Evidence**:
- `s1_ui/s1_server.py`: No decision document creation endpoints (only read endpoints)
- `s1_ui/s1_data_indexer.py`: Only reads decision documents (does not create or modify)
- Decision documents are marked as FROZEN in document status

**Fact**: Frontend cannot create or modify decision documents. Decision documents are created via human sign-off (not frontend).

---

### 10. State Mutation Capabilities

**Prohibition**: Frontend MUST NOT mutate system state, persist state, or store state beyond UI rendering.

**Authority**:
- `S1_BOUNDARY_ASSERTIONS.md`: "No state mutation beyond UI rendering"
- `S1_UI_ARCHITECTURE.md`: "Frontend modules do not store persistent state"
- GCD_v2 Section 2.3: "稳定性来自边界，而非层级" (state stability from boundaries)

**Evidence**:
- `s1_ui/static/js/*.js`: No `localStorage.setItem()` or persistent state storage
- `s1_ui/s1_server.py`: No state mutation (only read operations)
- `s1_ui/s1_data_indexer.py`: Index rebuilt on startup (no persistent state)

**Fact**: Frontend does not mutate system state. All state is read-only (no persistence, no mutation).

---

### 11. Implicit Agency Capabilities

**Prohibition**: Frontend MUST NOT provide implicit agency (defaults, visual highlights, ordering, grouping, proximity that influence user behavior).

**Authority**:
- Phase K (Agency Governance): WO-KA-1 through WO-KA-5 tested agency variables (DEFAULT_SELECTION, VISUAL_HIGHLIGHT, ORDERING, GROUPING, PROXIMITY)
- `docs/FRONTEND_EXPANSION_DENYLIST.md`: Denylist for frontend expansion (implicit agency patterns)
- GCD_v2 Section 6: "明确禁止的反模式: 为'管理便利'牺牲执行闭环"

**Evidence**:
- Phase K evidence packs: `audit_evidence/ka_*_pass/`, `audit_evidence/ka_*_fail/` (agency variable testing)
- `docs/FRONTEND_EXPANSION_DENYLIST.md`: Explicit denylist of agency patterns
- Frontend non-agency constraints from Phase J

**Fact**: Frontend must not provide implicit agency. All agency must be explicit and declared (per Phase K governance).

---

### 12. Workflow Automation Capabilities

**Prohibition**: Frontend MUST NOT automate workflows, trigger sequential actions, or execute multi-step processes.

**Authority**:
- `S1_BOUNDARY_ASSERTIONS.md`: "No buttons that: say 'Run', say 'Execute'"
- `S1_UI_ARCHITECTURE.md`: "The UI MUST NOT: trigger scripts"
- GCD_v2 Section 2.2: "执行必须闭环" (execution must be closed-loop, not automated by frontend)

**Evidence**:
- `s1_ui/static/js/*.js`: No workflow automation logic (only data display)
- No sequential action triggers in frontend
- No multi-step process execution in frontend

**Fact**: Frontend does not automate workflows. All workflow execution must be triggered by humans (not frontend).

---

### 13. Implied Capability Suggestions

**Prohibition**: Frontend MUST NOT imply that capabilities exist when they do not.

**Authority**:
- `S1_BOUNDARY_ASSERTIONS.md`: "UI does not infer or suggest actions"
- GCD_v2 Section 6: "明确禁止的反模式" (explicitly forbidden anti-patterns)

**Evidence**:
- `s1_ui/static/js/*.js`: No capability suggestions (only data display)
- No "would you like to..." prompts in frontend
- No implied action buttons in frontend

**Fact**: Frontend does not imply capabilities. All capabilities must be explicitly declared (not implied).

---

## Summary Table

| Prohibited Capability | Authority | Evidence | Current Status |
|----------------------|-----------|----------|----------------|
| Execution | S1_BOUNDARY_ASSERTIONS.md | s1_ui read-only | ✅ Enforced |
| File Modification | S1_BOUNDARY_ASSERTIONS.md | s1_ui read-only | ✅ Enforced |
| AI API Invocation | S1_UI_ARCHITECTURE.md, GCD_v2 15.3 | No AI calls in frontend | ✅ Enforced |
| Recommendations | S1_UI_ARCHITECTURE.md | No recommendation logic | ✅ Enforced |
| Decision-Making | S1_BOUNDARY_ASSERTIONS.md, HUMAN_ESCALATION.md | No decision logic | ✅ Enforced |
| Work Order Creation/Modification | S1_BOUNDARY_ASSERTIONS.md | No write endpoints | ✅ Enforced |
| Phase Advancement | WORKFLOW_RULES.md | No phase endpoints | ✅ Enforced |
| Evidence Pack Creation | S1_BOUNDARY_ASSERTIONS.md | No write endpoints | ✅ Enforced |
| Decision Document Creation | S1_BOUNDARY_ASSERTIONS.md | No write endpoints | ✅ Enforced |
| State Mutation | S1_BOUNDARY_ASSERTIONS.md | No persistent state | ✅ Enforced |
| Implicit Agency | Phase K, FRONTEND_EXPANSION_DENYLIST.md | Agency governance | ✅ Enforced |
| Workflow Automation | S1_BOUNDARY_ASSERTIONS.md | No automation logic | ✅ Enforced |
| Implied Capabilities | S1_BOUNDARY_ASSERTIONS.md | No capability suggestions | ✅ Enforced |

---

## Frontend Boundary Fact Conclusion

**All prohibited capabilities are currently enforced** in the `s1_ui/` implementation:
- Read-only operations only
- No execution capabilities
- No file modification
- No AI API calls
- No recommendations
- No decision-making
- No state mutation
- No implicit agency

**Frontend can only**:
- Read existing artifacts
- Display data
- Navigate structure
- Reduce cognitive load (via visualization)

**Frontend cannot**:
- Execute anything
- Modify anything
- Suggest anything
- Decide anything
- Automate anything

---

**END OF FRONTEND BOUNDARIES FACT AUDIT**

