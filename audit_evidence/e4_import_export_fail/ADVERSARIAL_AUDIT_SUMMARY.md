# Adversarial Audit Summary (FAIL Pack)

**Audit Date**: 2025-12-27  
**Audit Type**: Import/Export/Migration/Deprecation Neutrality Test - FAIL Pack (Adversarial)  
**Overall Status**: ❌ NON-COMPLIANT (Expected)

**Total Check Items**: 145  
**Items Passed**: 115  
**Items Failed**: 30  
**Violations**: 30

**Key Finding**: 12 adversarial mechanisms tested. All mechanisms correctly detected and rejected. 30 violations identified across default selection, recommendation semantics, auto-deprecation, auto-hiding/filtering, auto-replacement, audit-derived logic, and "latest is best" semantics categories.

**Violations Detected**:
- ❌ Auto-select target workspace (2 violations)
- ❌ Auto-merge conflict resolution with implied best (3 violations)
- ❌ Upgrade to latest toggle enabled by default (2 violations)
- ❌ Auto-deprecate older versions after import (3 violations)
- ❌ Recommended mapping of capabilities (1 violation)
- ❌ Clean up duplicates removes options by default (2 violations)
- ❌ Latest version highlighted in preview (2 violations)
- ❌ Auto-select best version based on usage stats (2 violations)
- ❌ Auto-hiding/filtering deprecated entries (3 violations)
- ❌ Auto-defaulting to non-deprecated (2 violations)
- ❌ Auto-replace deprecated with newer version (1 violation)
- ❌ Audit-derived selection logic (2 violations)

**All violations correctly detected. Adversarial mechanisms fail as expected.**

---

**END OF ADVERSARIAL AUDIT SUMMARY**

