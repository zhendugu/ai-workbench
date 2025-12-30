# Human Testing Guide 001

**Document ID**: HUMAN-TESTING-GUIDE-001

**Status**: TESTING GUIDE

**Date**: 2025-12-29

**Authority**: docs/frontend/DT_FE_DECISION_RECORD_001.md (HIGHEST AUTHORITY)

**Purpose**: Guide for human testers to verify system behavior matches declared boundaries and intent.

---

## Testing Context

**System Status**: COMPLETE, SEMANTICALLY CLOSED

**System Type**: Declarative, inert structural registry

**Testing Scope**: Verify that system behavior matches frozen boundaries and declared intent.

**Testing Approach**: Read-only verification, boundary compliance checking, semantic validation.

---

## Startup Commands and Access URLs

### Frontend Applications

#### 1. Run-Time Frontend (Read-Only Viewing Interface)

**Location**: `run_time_frontend/`

**Startup Command**:
```bash
cd run_time_frontend
npm install  # First time only
npm run dev
```

**Access URL**: 
- Development: `http://localhost:5173`
- Default Vite port: `5173`

**Purpose**: Read-only interface for viewing **frozen** AI Virtual Company structures.

**Key Characteristics**:
- **Mode**: RUN-TIME (FROZEN) ONLY - Read-only viewing
- **Data State**: Displays frozen, immutable Company structures
- **Interface Feel**: Like reading a legal entity registry, inspecting a frozen architecture blueprint, auditing a declared structure
- **NOT**: Dashboard, control panel, monitoring tool, workflow engine
- **Strictly Forbidden**: Any editable field, state mutation, live data indicator, refresh/polling, progress indicators, recommendations, workflows
- **Required Language**: Use "read, inspect, examine, audit" - NOT "run, execute, start, stop, monitor, update"
- **Timestamps**: MUST be labeled as "Frozen at"

**Use Case**: View and inspect already-frozen Company structures that cannot be modified.

**Note**: This frontend operates independently. No backend connection required.

---

#### 2. Design-Time Frontend (Design Interface)

**Location**: `design_time_frontend/`

**Startup Command**:
```bash
cd design_time_frontend
npm install  # First time only
npm run dev
```

**Access URL**: 
- Development: `http://localhost:5173` (or next available port if 5173 is in use)
- Default Vite port: `5173`

**Purpose**: Design interface for **creating and managing Draft** Company structures before freezing.

**Key Characteristics**:
- **Mode**: DESIGN-TIME - Draft creation and editing
- **Data State**: Works with mutable Draft Company structures
- **States**: Only Draft and Frozen (no intermediate stages)
- **Components**: 
  - Company Context (L1)
  - Cell Management (L2)
  - Topology Canvas (L3)
  - Methodology Selector (L4)
  - Template Library (L5) - Copy source only, no recommendations
  - Freeze Confirmation (L6)
- **Template Semantics**: Templates are structural copy sources ONLY - no recommendations, scoring, or matching
- **Draft ID**: Technical identifier only - no progress/maturity encoding
- **No Design Stage**: No early/mid/late design stages, no step-by-step wizards
- **Freeze Action**: Single commitment point to convert Draft to Frozen

**Use Case**: Create, edit, and manage Draft Company structures, then freeze them when ready.

**Note**: This frontend operates independently. No backend connection required.

---

### Key Differences Between Run-Time and Design-Time Frontends

| Aspect | Run-Time Frontend | Design-Time Frontend |
|--------|------------------|---------------------|
| **Purpose** | View frozen structures | Create/edit draft structures |
| **Data State** | Frozen (immutable) | Draft (mutable) |
| **Editability** | Read-only | Editable |
| **Interface Type** | Inspection/audit interface | Design/creation interface |
| **Metaphor** | Legal registry, frozen blueprint | Design workspace |
| **Actions Allowed** | View, inspect, examine, audit | Create, edit, manage, freeze |
| **Timestamps** | "Frozen at" | Draft creation/modification times |
| **State Management** | No state mutation | Draft state management |
| **Workflow** | View switching only | Design workflow (but no stages) |
| **Template Usage** | N/A (already frozen) | Template library for copying |
| **Freeze Action** | N/A (already frozen) | Freeze confirmation available |

---

#### 3. AI Company Interface (Next.js Application)

**Location**: `ai-company-interface/`

**Startup Command**:
```bash
cd ai-company-interface
npm install  # First time only
npm run dev
```

**Access URL**: 
- Development: `http://localhost:3000`
- Default Next.js port: `3000`

**Purpose**: Alternative interface implementation (Next.js stack).

**Note**: This frontend operates independently. No backend connection required.

---

### Backend Status

**Important**: According to frozen system boundaries:

- **Backend is EXCLUDED** from system reality (see `BACKEND_LEGACY_INVALIDATION_NOTE_001.md`)
- **Backend has no system authority** (see `SYSTEM_BOUNDARY_INDEX_001.md`)
- **Backend semantics are nullified** (see `SYSTEM_COMPLETION_AND_INTENT_DECLARATION_001.md`)

**Testing Implication**: 
- Frontend applications are designed to operate **without backend connection**
- All data is loaded from Authority Layer files (frozen facts)
- No backend server is required for testing

**If Backend Code Exists**:
- Backend code may exist in `backend/` directory as legacy artifact
- Backend code has no active semantic effect
- Backend is not part of the valid system boundary
- **Do NOT start backend for testing** (it is excluded from system reality)

---

### Quick Start for Testing

**Recommended Testing Sequence**:

1. **Start Run-Time Frontend** (for read-only verification):
   ```bash
   cd run_time_frontend
   npm install  # First time only
   npm run dev
   ```
   Access: `http://localhost:5173`

2. **Start Design-Time Frontend** (for design interface testing):
   ```bash
   cd design_time_frontend
   npm install  # First time only
   npm run dev
   ```
   Access: `http://localhost:5174` (or next available port)

**Note**: Both frontends can run simultaneously on different ports.

---

### Port Configuration

**Default Ports**:
- Vite (Run-Time Frontend): `5173`
- Vite (Design-Time Frontend): `5174` (if 5173 is in use, Vite will auto-increment)
- Next.js (AI Company Interface): `3000`

**Port Conflicts**: 
- If a port is in use, Vite will automatically use the next available port
- Check terminal output for actual port number after startup

---

## What to Test

### 1. Authority Layer Fact Verification

**Objective**: Verify that Authority Layer facts are correctly defined and frozen.

**Test Points**:

#### 1.1 Schema Compliance

**Verify**: All entity types match frozen schemas exactly.

**Test Steps**:
1. Check Company schema: Should have exactly 5 fields (company_identifier, company_name, company_description, frozen_at, frozen_by)
2. Check Cell schema: Should have exactly 5 fields (cell_identifier, cell_name, responsibility_what, responsibility_what_not, role_constraints)
3. Check Role schema: Should have exactly 5 fields (role_identifier, role_name, constraint_type, constraint_description, attached_to_cell_identifier)
4. Check Topology schema: Should have exactly 5 fields per relationship
5. Check Methodology schema: Should have exactly 3 fields
6. Check FreezeRecord schema: Should have exactly 6 fields

**Expected Result**: All schemas match frozen definitions exactly. No additional fields.

**Failure Criteria**: Any schema contains fields not in frozen definitions.

#### 1.2 No Status/Stage/Progress Fields

**Verify**: Authority Layer schemas contain no status, stage, or progress fields.

**Test Steps**:
1. Inspect Company schema: No `status`, `stage`, `progress`, `lifecycle_state` fields
2. Inspect Cell schema: No status or progress fields
3. Inspect Role schema: No status or progress fields
4. Inspect Topology schema: No status or progress fields
5. Inspect Methodology schema: No status or progress fields
6. Inspect FreezeRecord schema: No status or progress fields

**Expected Result**: No status, stage, or progress fields in any Authority schema.

**Failure Criteria**: Any Authority schema contains status, stage, or progress fields.

#### 1.3 Immutability Verification

**Verify**: Frozen facts cannot be modified.

**Test Steps**:
1. Attempt to modify a frozen Company fact
2. Attempt to modify a frozen Cell fact
3. Attempt to modify a frozen Role fact
4. Attempt to modify a frozen Topology relationship
5. Attempt to modify a frozen FreezeRecord

**Expected Result**: All modification attempts fail or are rejected. Frozen facts remain immutable.

**Failure Criteria**: Any frozen fact can be modified.

---

### 2. Frontend Read-Only Verification

**Objective**: Verify that Frontend Layer is read-only and non-operational.

**Test Points**:

#### 2.1 Read-Only Presentation

**Verify**: Frontend displays frozen facts only. No modification capabilities.

**Test Steps**:
1. Open Run-Time Frontend
2. Navigate to Company view
3. Navigate to Cell view
4. Navigate to Topology view
5. Attempt to edit any displayed fact
6. Attempt to create new facts
7. Attempt to delete existing facts

**Expected Result**: 
- All facts are displayed in read-only mode
- No edit buttons or controls are present
- No create buttons or controls are present
- No delete buttons or controls are present
- All displayed data matches Authority Layer facts

**Failure Criteria**: Any modification, creation, or deletion capability exists in Frontend.

#### 2.2 No Control Mechanisms

**Verify**: Frontend contains no control mechanisms.

**Test Steps**:
1. Inspect all UI components for control buttons
2. Check for "Execute", "Run", "Deploy", "Activate" buttons
3. Check for "Start", "Stop", "Trigger" buttons
4. Check for workflow controls
5. Check for monitoring controls
6. Check for decision-making controls

**Expected Result**: No control mechanisms present. Only display and navigation.

**Failure Criteria**: Any control mechanism exists in Frontend.

#### 2.3 No Side Effects

**Verify**: Frontend actions produce no side effects.

**Test Steps**:
1. Navigate through all Frontend views
2. Click all available navigation elements
3. Interact with all UI components
4. Monitor system state for changes
5. Check for any external API calls (except read-only data loading)
6. Check for any state mutations

**Expected Result**: 
- No side effects observed
- No state mutations
- No external API calls (except read-only data loading)
- Only data reading occurs

**Failure Criteria**: Any side effects or state mutations occur.

#### 2.4 No Live State Representation

**Verify**: Frontend does not represent live or real-time state.

**Test Steps**:
1. Check UI for "current", "live", "real-time", "ongoing" indicators
2. Check for status indicators (active, running, executing)
3. Check for progress indicators
4. Check for monitoring displays
5. Verify all displayed data is labeled as "frozen at" or "as of"

**Expected Result**: 
- No live state indicators
- No real-time updates
- All data labeled with freeze timestamps
- All data represents frozen snapshots

**Failure Criteria**: Any live state or real-time representation exists.

---

### 3. Execution Boundary Verification

**Objective**: Verify that no execution semantics exist in the system.

**Test Points**:

#### 3.1 No Execution Functions

**Verify**: No execution functions are accessible or functional.

**Test Steps**:
1. Search codebase for `execute_*` function names
2. Search codebase for `run_*` function names
3. Search codebase for `trigger_*` function names
4. Search codebase for `deploy_*` function names
5. Search codebase for `activate_*` function names
6. Attempt to invoke any execution-related functions via Frontend

**Expected Result**: 
- No execution functions accessible via Frontend
- No execution functions callable by users
- All execution-related code is in excluded Backend (legacy artifact)

**Failure Criteria**: Any execution function is accessible or functional.

#### 3.2 No Workflow Engines

**Verify**: No workflow engines exist or are accessible.

**Test Steps**:
1. Search for workflow engine references
2. Search for process orchestration references
3. Search for task scheduling references
4. Check Frontend for workflow controls
5. Check for workflow visualization

**Expected Result**: No workflow engines exist or are accessible.

**Failure Criteria**: Any workflow engine exists or is accessible.

#### 3.3 No Monitoring Systems

**Verify**: No monitoring systems exist or are accessible.

**Test Steps**:
1. Search for monitoring references
2. Search for logging systems
3. Search for tracing systems
4. Search for metrics systems
5. Check Frontend for monitoring displays

**Expected Result**: No monitoring systems exist or are accessible.

**Failure Criteria**: Any monitoring system exists or is accessible.

---

### 4. Governance Boundary Verification

**Objective**: Verify that Governance Layer boundaries are respected.

**Test Points**:

#### 4.1 No Decision-Making

**Verify**: System does not make decisions.

**Test Steps**:
1. Attempt to trigger automated decisions
2. Check for decision-making interfaces
3. Check for recommendation systems
4. Check for advice systems
5. Verify all decisions require human input

**Expected Result**: No decision-making capability exists. All decisions require human input.

**Failure Criteria**: Any automated decision-making exists.

#### 4.2 No Recommendation Systems

**Verify**: System does not provide recommendations.

**Test Steps**:
1. Check for recommendation interfaces
2. Check for suggestion systems
3. Check for guidance systems
4. Check for best practices systems
5. Verify system only presents facts

**Expected Result**: No recommendation capability exists. System only presents facts.

**Failure Criteria**: Any recommendation system exists.

#### 4.3 No Automation

**Verify**: System does not automate processes.

**Test Steps**:
1. Check for automation interfaces
2. Check for automated workflows
3. Check for automated triggers
4. Check for scheduled tasks
5. Verify all actions require human initiation

**Expected Result**: No automation capability exists. All actions require human initiation.

**Failure Criteria**: Any automation capability exists.

---

### 5. Backend Exclusion Verification

**Objective**: Verify that Backend is excluded from system reality.

**Test Points**:

#### 5.1 Backend Not Accessible

**Verify**: Backend subsystems are not accessible via Frontend.

**Test Steps**:
1. Attempt to access Backend APIs via Frontend
2. Check Frontend code for Backend imports
3. Check for Backend function calls
4. Verify Frontend does not depend on Backend

**Expected Result**: 
- Backend is not accessible via Frontend
- Frontend does not import Backend code
- Frontend does not call Backend functions
- Frontend operates independently of Backend

**Failure Criteria**: Any Backend access exists via Frontend.

#### 5.2 Backend Semantics Nullified

**Verify**: Backend execution/monitoring/mutation semantics have no system effect.

**Test Steps**:
1. Verify Backend execution functions exist but are not called
2. Verify Backend monitoring functions exist but are not called
3. Verify Backend mutation functions exist but are not called
4. Verify system behavior is unaffected by Backend code

**Expected Result**: 
- Backend code exists but has no system effect
- Backend semantics are nullified
- System operates without Backend authority

**Failure Criteria**: Backend semantics affect system behavior.

---

### 6. Semantic Consistency Verification

**Objective**: Verify that system semantics match declared intent.

**Test Points**:

#### 6.1 Declarative Language Verification

**Verify**: All system outputs use declarative language only.

**Test Steps**:
1. Review all UI text for operational verbs
2. Check for "execute", "run", "trigger", "deploy" in positive statements
3. Check for "should", "must", "may", "could" in prescriptive statements
4. Verify all language is declarative (describes what is, not what to do)

**Expected Result**: All system outputs use declarative language only.

**Failure Criteria**: Any operational or prescriptive language exists in positive statements.

#### 6.2 Frozen State Verification

**Verify**: All displayed data represents frozen states.

**Test Steps**:
1. Verify all facts display "frozen at" timestamps
2. Verify no "current" or "live" state indicators
3. Verify all data is labeled as frozen snapshots
4. Verify no real-time updates occur

**Expected Result**: All data represents frozen states with timestamps.

**Failure Criteria**: Any live or current state representation exists.

#### 6.3 Boundary Compliance

**Verify**: System complies with all frozen boundaries.

**Test Steps**:
1. Verify Execution Layer boundaries are respected
2. Verify Authority Layer boundaries are respected
3. Verify Governance Layer boundaries are respected
4. Verify Backend exclusion is respected
5. Verify GCD semantic resolution is respected

**Expected Result**: All frozen boundaries are respected.

**Failure Criteria**: Any boundary violation exists.

---

## What NOT to Test

### Do NOT Test Execution Capabilities

**Do NOT attempt to**:
- Execute actions
- Run processes
- Trigger workflows
- Deploy systems
- Activate services

**Reason**: System has no execution capability. Testing execution would be testing non-existent functionality.

### Do NOT Test Monitoring Capabilities

**Do NOT attempt to**:
- Monitor operations
- Track activities
- Observe processes
- Report status
- Collect metrics

**Reason**: System has no monitoring capability. Testing monitoring would be testing non-existent functionality.

### Do NOT Test Automation Capabilities

**Do NOT attempt to**:
- Automate processes
- Schedule tasks
- Trigger automated actions
- Enable automated workflows

**Reason**: System has no automation capability. Testing automation would be testing non-existent functionality.

### Do NOT Test Decision-Making Capabilities

**Do NOT attempt to**:
- Trigger automated decisions
- Test recommendation systems
- Test advice systems
- Test decision engines

**Reason**: System has no decision-making capability. Testing decision-making would be testing non-existent functionality.

---

## Testing Methodology

### Phase 1: Static Verification

**Objective**: Verify code and documentation match frozen boundaries.

**Methods**:
1. Code review for forbidden vocabulary
2. Schema inspection for compliance
3. Documentation review for boundary alignment
4. Static analysis for execution/monitoring semantics

**Tools**:
- `scripts/verify-no-execution-semantics.sh`
- Manual code inspection
- Schema comparison tools

### Phase 2: Runtime Verification

**Objective**: Verify system behavior matches declared boundaries.

**Methods**:
1. Frontend interaction testing
2. Read-only verification
3. Boundary compliance testing
4. Semantic consistency checking

**Tools**:
- Browser developer tools
- Network monitoring
- State inspection tools

### Phase 3: Semantic Verification

**Objective**: Verify system semantics match declared intent.

**Methods**:
1. Language analysis
2. Boundary compliance verification
3. Exclusion verification
4. Precedence rule verification

**Tools**:
- Manual review
- Documentation comparison
- Semantic analysis

---

## Test Checklist

### Authority Layer Tests

- [ ] All schemas match frozen definitions exactly
- [ ] No status/stage/progress fields in Authority schemas
- [ ] Frozen facts are immutable
- [ ] Authority Layer is source of truth

### Frontend Layer Tests

- [ ] Frontend is read-only
- [ ] No control mechanisms exist
- [ ] No side effects occur
- [ ] No live state representation
- [ ] All data displays frozen timestamps

### Execution Boundary Tests

- [ ] No execution functions accessible
- [ ] No workflow engines exist
- [ ] No monitoring systems exist
- [ ] No automation exists

### Governance Boundary Tests

- [ ] No decision-making capability
- [ ] No recommendation systems
- [ ] No automation capability
- [ ] All boundaries respected

### Backend Exclusion Tests

- [ ] Backend not accessible via Frontend
- [ ] Backend semantics nullified
- [ ] System operates without Backend

### Semantic Consistency Tests

- [ ] Declarative language only
- [ ] Frozen state representation
- [ ] Boundary compliance
- [ ] Precedence rules respected

---

## Expected Test Results

### All Tests Should Pass

**Expected Outcome**: All boundary compliance tests pass.

**System Behavior**:
- System is read-only
- System is declarative
- System is inert
- System has no execution capability
- System has no monitoring capability
- System has no automation capability
- System has no decision-making capability
- Backend is excluded

### No False Positives

**Expected Outcome**: No false positive test failures.

**If Tests Fail**:
- Document exact failure
- Identify boundary violation
- Reference frozen documents
- Do not propose solutions (testing only)

---

## Test Reporting

### Test Report Format

**For each test**:
1. Test ID and description
2. Test steps executed
3. Expected result
4. Actual result
5. Pass/Fail status
6. Evidence (screenshots, logs, code references)

### Violation Reporting

**If boundary violation is found**:
1. Document exact violation
2. Reference frozen boundary document
3. Provide evidence
4. State that violation exists
5. Do not propose solutions

---

## Testing Constraints

### Testing Limitations

**Testing is limited to**:
- Read-only verification
- Boundary compliance checking
- Semantic validation
- Documentation review

**Testing does NOT include**:
- Code modification
- Feature implementation
- Bug fixes
- Solution proposals

### Testing Authority

**Testers have authority to**:
- Verify system behavior
- Document violations
- Report findings
- Request clarification

**Testers do NOT have authority to**:
- Modify code
- Change boundaries
- Propose solutions
- Implement fixes

---

## Authority References

This testing guide is subordinate to:

1. **docs/frontend/DT_FE_DECISION_RECORD_001.md** (HIGHEST AUTHORITY)
2. **docs/governance/SYSTEM_COMPLETION_AND_INTENT_DECLARATION_001.md** (FROZEN)
3. **docs/governance/SYSTEM_BOUNDARY_INDEX_001.md** (FROZEN)
4. **docs/execution/EXECUTION_BOUNDARY_001.md** (FROZEN)

---

## Testing Summary

**System to Test**: Declarative, inert structural registry

**Testing Focus**: Verify system matches frozen boundaries and declared intent

**Testing Approach**: Read-only verification, boundary compliance, semantic validation

**Expected Outcome**: All tests pass. System behaves as declared.

**Testing Status**: Ready for human testing

---

**END OF HUMAN TESTING GUIDE**

**Note**: This guide provides testing methodology for verifying system compliance with frozen boundaries. It does not propose solutions or modifications. Testing is verification only.

