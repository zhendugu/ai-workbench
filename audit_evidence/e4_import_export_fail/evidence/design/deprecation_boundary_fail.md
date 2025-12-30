# Deprecation Boundary Test (FAIL Pack)

**Date**: 2025-12-27  
**Purpose**: Document adversarial deprecation behaviors that violate constitutional boundaries (expected to FAIL)

---

## Adversarial Deprecation Mechanism 1: Auto-Hiding Deprecated Entries

### Mechanism Description

**Scenario**: System automatically hides deprecated entries from registry view

**System Behavior**:
- Deprecated patterns are automatically filtered out
- Registry view shows only non-deprecated patterns
- Deprecated patterns are hidden by default

**Violation**: Auto-hiding of deprecated entries

**Expected Result**: ❌ FAIL - Deprecated entries must remain visible

---

## Adversarial Deprecation Mechanism 2: Auto-Filtering Deprecated Entries

### Mechanism Description

**Scenario**: System automatically filters deprecated entries from selection lists

**System Behavior**:
- Selection lists exclude deprecated patterns by default
- "Show deprecated" toggle is off by default
- Deprecated patterns are filtered out automatically

**Violation**: Auto-filtering of deprecated entries

**Expected Result**: ❌ FAIL - Deprecated entries must remain accessible

---

## Adversarial Deprecation Mechanism 3: Auto-Defaulting to Non-Deprecated

### Mechanism Description

**Scenario**: System automatically defaults to non-deprecated version after deprecation

**System Behavior**:
- After deprecating P-MD-CONV-001 v1.0.0
- System automatically selects P-MD-CONV-001 v2.0.0 as default
- Selection changes without explicit human action

**Violation**: Auto-defaulting to non-deprecated version

**Expected Result**: ❌ FAIL - No auto-selection changes after deprecation

---

## Adversarial Deprecation Mechanism 4: Auto-Replace Deprecated with Newer Version

### Mechanism Description

**Scenario**: System automatically replaces deprecated pattern with newer version

**System Behavior**:
- After deprecating P-MD-CONV-001 v1.0.0
- System automatically replaces references with v2.0.0
- "Deprecated -> automatically replace with v2.0.0" behavior

**Violation**: "deprecated -> automatically replace with X"

**Expected Result**: ❌ FAIL - No auto-replacement allowed

---

## Constitutional Violations Summary

**Total Adversarial Deprecation Mechanisms**: 4

**Violation Categories**:
- Auto-Hiding: 1 violation
- Auto-Filtering: 1 violation
- Auto-Defaulting: 1 violation
- Auto-Replacement: 1 violation

**All mechanisms MUST FAIL constitutional compliance.**

---

**END OF DEPRECATION BOUNDARY TEST (FAIL)**

