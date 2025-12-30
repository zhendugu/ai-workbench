# Adversarial Audit Summary (FAIL Pack)

**Audit Date**: 2025-12-27  
**Audit Type**: Search/Filter/Sort/Pagination Neutrality Boundary Test - FAIL Pack (Adversarial)  
**Overall Status**: ❌ NON-COMPLIANT (Expected)

**Total Check Items**: 145  
**Items Passed**: 115  
**Items Failed**: 30  
**Violations**: 30

**Key Finding**: 10 adversarial mechanisms tested. All mechanisms correctly detected and rejected. 30 violations identified across default filter, default sort, recommendation semantics, hidden ranking, decision space compression, sticky state, and audit/history-derived logic categories.

**Violations Detected**:
- ❌ Default filter enabled (2 violations)
- ❌ Default sort by latest or most used (3 violations)
- ❌ Auto-highlight popular/common/standard (1 violation)
- ❌ Semantic relevance score boosting (1 violation)
- ❌ Recently used panel truncating to top-N (2 violations)
- ❌ Sticky filters auto-applied on next session (3 violations)
- ❌ Usage count based ranking (1 violation)
- ❌ Last used based ranking (1 violation)
- ❌ Popularity based ranking (1 violation)
- ❌ Trending based ranking (1 violation)
- ❌ Hidden ranking mechanisms (5 violations)
- ❌ Audit-derived logic (2 violations)

**All violations correctly detected. Adversarial mechanisms fail as expected.**

---

**END OF ADVERSARIAL AUDIT SUMMARY**

