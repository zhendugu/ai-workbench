# Migration Conflict Examples

**Date**: 2025-12-27  
**Purpose**: Provide minimal migration conflict examples as design evidence files

---

## Conflict Example 1: Pattern ID and Version Conflict

### Scenario

**Source Workspace**: WORKSPACE-A  
**Target Workspace**: WORKSPACE-B

**Conflict**:
- WORKSPACE-A has: P-MD-CONV-001 v2.0.0
- WORKSPACE-B has: P-MD-CONV-001 v2.0.0 (different content)

**System Response** (Neutral):
```
Conflict Detected:
- Pattern: P-MD-CONV-001
- Version: 2.0.0
- Conflict Type: Same ID and version, different content

Options:
- Option 1: Skip import of conflicting pattern
- Option 2: Import with new version identifier (2.0.1)
- Option 3: Import with new pattern identifier (P-MD-CONV-002)
- Option 4: Cancel import
```

**Key Characteristics**:
- ✅ All options presented neutrally
- ✅ No suggested resolution
- ✅ No default option selected
- ✅ No "recommended" option
- ✅ Human must explicitly choose

---

## Conflict Example 2: Capability Reference Conflict

### Scenario

**Source Workspace**: WORKSPACE-A  
**Target Workspace**: WORKSPACE-B

**Conflict**:
- WORKSPACE-A pattern references: C-MD-HTML-001
- WORKSPACE-B does not have: C-MD-HTML-001
- WORKSPACE-B has: C-MD-HTML-002 (similar capability)

**System Response** (Neutral):
```
Conflict Detected:
- Pattern: P-MD-CONV-001
- Capability Reference: C-MD-HTML-001
- Conflict Type: Referenced capability does not exist in target workspace

Options:
- Option 1: Skip import of pattern with missing capability reference
- Option 2: Import pattern without capability reference
- Option 3: Import pattern and create capability reference placeholder
- Option 4: Cancel import
```

**Key Characteristics**:
- ✅ All options presented neutrally
- ✅ No capability mapping suggestion
- ✅ No "recommended mapping" shown
- ✅ No default option selected
- ✅ Human must explicitly choose

---

## Conflict Example 3: Version Lineage Conflict

### Scenario

**Source Workspace**: WORKSPACE-A  
**Target Workspace**: WORKSPACE-B

**Conflict**:
- WORKSPACE-A has: P-MD-CONV-001 v1.0.0 -> v2.0.0 lineage
- WORKSPACE-B has: P-MD-CONV-001 v1.0.0 -> v1.5.0 lineage (different branch)

**System Response** (Neutral):
```
Conflict Detected:
- Pattern: P-MD-CONV-001
- Conflict Type: Conflicting version lineage relationships

Existing Lineage (WORKSPACE-B):
- v1.0.0 -> v1.5.0

Import Lineage (WORKSPACE-A):
- v1.0.0 -> v2.0.0

Options:
- Option 1: Skip import of conflicting lineage
- Option 2: Import as parallel lineage (both relationships preserved)
- Option 3: Replace existing lineage with imported lineage
- Option 4: Cancel import
```

**Key Characteristics**:
- ✅ All options presented neutrally
- ✅ No suggested resolution
- ✅ No default option selected
- ✅ No "recommended" option
- ✅ Human must explicitly choose

---

## Constitutional Compliance Verification

**No Suggested Resolution**: ✅ Verified - All conflicts presented neutrally

**No Default Option**: ✅ Verified - No default option selected

**No Recommendation**: ✅ Verified - No recommended option shown

**No Decision Space Compression**: ✅ Verified - All options remain available

**Human Explicit Choice Required**: ✅ Verified - Human must explicitly choose resolution

---

**END OF MIGRATION CONFLICT EXAMPLES**

