# Neutral Sort Specification

**Date**: 2025-12-27  
**Purpose**: Define neutral sorting rules that require explicit user selection, no default preferential sorting

**Note**: This is application-level specification, NOT a CANONICAL document

---

## Sort Rules

### Explicit User-Selected Only

**Sort Behavior**:
- ✅ Sort must be explicitly user-selected
- ✅ Registry default sort is non-preferential (pattern_id lexical)
- ✅ All sort options presented equally
- ✅ User-chosen sort clearly labeled as user-chosen

**Forbidden**:
- ❌ Default sort by "latest" or "most used"
- ❌ "Smart ordering" that compresses decision space
- ❌ Usage-based default sorting
- ❌ History-based default sorting
- ❌ Audit-based default sorting

---

## Sort Options

**Available Sort Options**:
- ✅ Sort by pattern_id (lexicographic) - default
- ✅ Sort by pattern_name (lexicographic)
- ✅ Sort by pattern_version (lexicographic)
- ✅ Sort by created_at (chronological, factual only)

**Forbidden Sort Options**:
- ❌ Sort by "latest" (implies preference)
- ❌ Sort by "most used" (usage-based)
- ❌ Sort by "popular" (popularity-based)
- ❌ Sort by "recent" (history-based)
- ❌ Sort by "trending" (usage-based)
- ❌ Sort by "common" (usage-based)

---

## Sort State Persistence

**Session Persistence**:
- ✅ Sort does NOT persist across sessions by default
- ✅ Sort resets to default (pattern_id lexical) when cleared
- ✅ No sticky sort state without explicit human action

**Forbidden**:
- ❌ Auto-remembering sort across sessions
- ❌ Sticky sort auto-applied on next session
- ❌ Sort state persistence without explicit human action

---

## Constitutional Compliance

**No Default Preferential Sort**: ✅ Verified - Default sort is non-preferential (pattern_id lexical)

**Explicit User Selection**: ✅ Verified - All sorts require explicit user selection

**No Usage-Based Sorting**: ✅ Verified - No "most used", "popular", or "trending" sorts

**No Sticky State**: ✅ Verified - No auto-persistence without explicit human action

---

**END OF SORT SPECIFICATION**

