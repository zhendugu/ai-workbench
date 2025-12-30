# Adversarial UI Flows (FAIL Pack)

**Date**: 2025-12-27  
**Purpose**: Document adversarial UI flows that attempt to bypass constitutional boundaries (expected to FAIL)

---

## Adversarial Flow 1: Infer Authorization from History

### Flow Description

**Scenario**: Operator attempts to execute capability, system infers authorization from audit history

**UI Flow**:
1. Operator selects C-MD-HTML-001
2. Operator attempts execution
3. System checks audit records: "Operator used this capability last time"
4. System infers authorization: "Based on your previous usage, authorization granted"
5. Execution proceeds

**Violation**: Authorization inferred from history instead of explicit record

**Expected Result**: ❌ FAIL - Must require explicit authorization

---

## Adversarial Flow 2: Auto-Grant Based on Role Heuristics

### Flow Description

**Scenario**: System auto-grants permissions based on role patterns

**UI Flow**:
1. ROLE_OPERATOR logs into WORKSPACE-A
2. System checks role: "ROLE_OPERATOR in WORKSPACE-A"
3. System applies heuristic: "All operators in this workspace get access to all capabilities"
4. System auto-grants permissions for all capabilities
5. Operator can execute without explicit authorization

**Violation**: Permissions auto-granted without explicit authorization

**Expected Result**: ❌ FAIL - Must require explicit authorization

---

## Adversarial Flow 3: Continue Previous Session Bypassing Gate

### Flow Description

**Scenario**: Continue button bypasses explicit authorization gate

**UI Flow**:
1. Operator had previous session with C-MD-HTML-001
2. Operator clicks "Continue Previous Session"
3. System auto-selects workspace, capability, and pre-fills parameters
4. System bypasses authorization check: "Continuing previous session, authorization assumed"
5. Execution proceeds without explicit authorization check

**Violation**: UI convenience bypasses explicit authorization requirement

**Expected Result**: ❌ FAIL - Must require explicit authorization even with continue

---

## Adversarial Flow 4: Preselect Workspace for Convenience

### Flow Description

**Scenario**: System preselects workspace based on recent usage

**UI Flow**:
1. Operator logs in
2. System checks recent usage: "WORKSPACE-A used most recently"
3. System preselects WORKSPACE-A
4. Operator sees WORKSPACE-A already selected
5. Operator proceeds without explicit selection

**Violation**: Default selection of workspace

**Expected Result**: ❌ FAIL - Must require explicit selection

---

## Adversarial Flow 5: Preselect Pattern for Convenience

### Flow Description

**Scenario**: System preselects pattern based on frequency

**UI Flow**:
1. Operator selects workspace
2. System checks usage frequency: "P-MD-CONV-001 used most frequently"
3. System preselects P-MD-CONV-001
4. Operator sees pattern already selected
5. Operator proceeds without explicit selection

**Violation**: Default selection of pattern

**Expected Result**: ❌ FAIL - Must require explicit selection

---

## Adversarial Flow 6: Preselect Capability for Convenience

### Flow Description

**Scenario**: System preselects capability based on recent usage

**UI Flow**:
1. Operator selects workspace
2. System checks recent usage: "C-MD-HTML-001 used most recently"
3. System preselects C-MD-HTML-001
4. Operator sees capability already selected
5. Operator proceeds without explicit selection

**Violation**: Default selection of capability

**Expected Result**: ❌ FAIL - Must require explicit selection

---

## Adversarial Flow 7: Audit-Derived Access Control

### Flow Description

**Scenario**: System uses audit records to derive access control

**UI Flow**:
1. Operator attempts execution
2. System checks audit records: "Operator has executed this capability 5 times before"
3. System derives access: "Based on audit history, access granted"
4. Execution proceeds without checking explicit authorization

**Violation**: Access control derived from audit instead of explicit authorization

**Expected Result**: ❌ FAIL - Must use explicit authorization only

---

## Adversarial Flow 8: Cross-Workspace Recent Panels

### Flow Description

**Scenario**: Recent panel shows items from other workspaces

**UI Flow**:
1. Operator in WORKSPACE-A
2. System shows "Recent Items" panel
3. Panel includes items from WORKSPACE-B
4. Operator can see and access items from other workspace

**Violation**: Cross-workspace influence

**Expected Result**: ❌ FAIL - Workspaces must be isolated

---

## Adversarial Flow 9: Cross-Workspace Filter Carryover

### Flow Description

**Scenario**: Filters carry over between workspaces

**UI Flow**:
1. Operator in WORKSPACE-A applies filter "category: transformation"
2. Operator switches to WORKSPACE-B
3. Filter "category: transformation" is still active
4. WORKSPACE-B shows filtered results based on WORKSPACE-A filter

**Violation**: Cross-workspace state carryover

**Expected Result**: ❌ FAIL - Workspaces must be isolated

---

## Adversarial Flow 10: Shared Defaults Across Workspaces

### Flow Description

**Scenario**: Default selections shared across workspaces

**UI Flow**:
1. Operator in WORKSPACE-A selects C-MD-HTML-001 as default
2. Operator switches to WORKSPACE-B
3. C-MD-HTML-001 is pre-selected as default
4. WORKSPACE-B inherits default from WORKSPACE-A

**Violation**: Shared defaults across workspaces

**Expected Result**: ❌ FAIL - Workspaces must be isolated, no shared defaults

---

## Constitutional Violations Summary

**Total Adversarial Mechanisms**: 10

**Violation Categories**:
- Privilege Inference: 1
- Auto-Grant: 1
- Gate Bypass: 1
- Default Selection: 3
- Audit-Derived Logic: 1
- Workspace Isolation Violation: 3

**Expected Violations in Checklist**: 25+ (multiple violations per mechanism)

**All mechanisms MUST FAIL constitutional compliance.**

---

**END OF ADVERSARIAL UI FLOWS**

