# Adversarial Import Flows (FAIL Pack)

**Date**: 2025-12-27  
**Purpose**: Document adversarial import flows that attempt to bypass constitutional boundaries (expected to FAIL)

---

## Adversarial Flow 1: Auto-Select Target Workspace

### Flow Description

**Scenario**: System auto-selects target workspace based on recent usage

**UI Flow**:
1. Human selects import file
2. System checks recent usage: "WORKSPACE-A used most recently"
3. System auto-selects WORKSPACE-A
4. Human sees WORKSPACE-A already selected
5. Human proceeds without explicit selection

**Violation**: Default workspace selection

**Expected Result**: ❌ FAIL - Must require explicit workspace selection

---

## Adversarial Flow 2: Auto-Merge Conflict Resolution with Implied Best

### Flow Description

**Scenario**: System auto-merges conflicts with implied 'best' option

**UI Flow**:
1. Import detects conflict: P-MD-CONV-001 v2.0.0 already exists
2. System auto-selects: "Keep latest version (recommended)"
3. System shows: "This option is recommended because it keeps the latest version"
4. Human proceeds with recommended option

**Violation**: Implied 'best' option in conflict resolution

**Expected Result**: ❌ FAIL - Must present options neutrally without recommendation

---

## Adversarial Flow 3: Upgrade to Latest Toggle Enabled by Default

### Flow Description

**Scenario**: Upgrade to latest version toggle is enabled by default

**UI Flow**:
1. Import dialog shows: "Upgrade to latest version" checkbox
2. Checkbox is pre-checked by default
3. Human proceeds without unchecking
4. System auto-upgrades all patterns to latest versions

**Violation**: Default selection of upgrade option

**Expected Result**: ❌ FAIL - Must require explicit selection

---

## Adversarial Flow 4: Auto-Deprecate Older Versions After Import

### Flow Description

**Scenario**: System automatically deprecates older versions after importing newer versions

**UI Flow**:
1. Import P-MD-CONV-001 v2.0.0
2. System detects existing v1.0.0
3. System automatically deprecates v1.0.0
4. System shows: "Older version v1.0.0 has been automatically deprecated"

**Violation**: Automatic deprecation without explicit human declaration

**Expected Result**: ❌ FAIL - Deprecation must be human-explicit

---

## Adversarial Flow 5: Recommended Mapping of Capabilities

### Flow Description

**Scenario**: System recommends capability mappings during import

**UI Flow**:
1. Import detects capability reference: C-MD-HTML-001
2. System shows: "Recommended mapping: C-MD-HTML-001 -> C-MD-HTML-002 (latest version)"
3. System pre-selects recommended mapping
4. Human proceeds with recommended mapping

**Violation**: Recommended mapping implies preference

**Expected Result**: ❌ FAIL - Must present mappings neutrally

---

## Adversarial Flow 6: Clean Up Duplicates Removes Options by Default

### Flow Description

**Scenario**: Clean up duplicates feature removes options by default

**UI Flow**:
1. Import detects duplicate patterns
2. System shows: "Clean up duplicates" option (enabled by default)
3. System auto-removes duplicate patterns
4. Human sees reduced pattern list without explicit confirmation

**Violation**: Default removal of options compresses decision space

**Expected Result**: ❌ FAIL - Must require explicit selection, no default removal

---

## Adversarial Flow 7: Latest Version Highlighted in Preview

### Flow Description

**Scenario**: Latest version of each pattern is highlighted in import preview

**UI Flow**:
1. Import preview shows patterns
2. P-MD-CONV-001 v2.0.0 is highlighted with "Latest Version" badge
3. P-MD-CONV-001 v1.0.0 is shown in gray (less prominent)
4. Human sees visual preference for latest version

**Violation**: Highlighting implies preference for latest version

**Expected Result**: ❌ FAIL - Must present all versions equally

---

## Adversarial Flow 8: Auto-Select Best Version Based on Usage Stats

### Flow Description

**Scenario**: System auto-selects 'best' version based on usage statistics

**UI Flow**:
1. Import detects multiple versions: P-MD-CONV-001 v1.0.0, v2.0.0
2. System checks audit records: "v2.0.0 has highest usage count"
3. System auto-selects v2.0.0 as "best version"
4. System shows: "v2.0.0 selected (most used version)"

**Violation**: Audit-derived selection, usage-based ranking

**Expected Result**: ❌ FAIL - Must not use audit/history for selection

---

## Constitutional Violations Summary

**Total Adversarial Mechanisms**: 8

**Violation Categories**:
- Default Selection: 2
- Recommendation Semantics: 3
- Auto-Deprecation: 1
- Decision Space Compression: 1
- Audit-Derived Selection: 1

**Expected Violations in Checklist**: 30+ (multiple violations per mechanism)

**All mechanisms MUST FAIL constitutional compliance.**

---

**END OF ADVERSARIAL IMPORT FLOWS**

