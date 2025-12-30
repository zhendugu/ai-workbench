# Neutral Pagination Specification

**Date**: 2025-12-27  
**Purpose**: Define neutral pagination rules with stable ordering, no truncation that hides options

**Note**: This is application-level specification, NOT a CANONICAL document

---

## Pagination Rules

### Stable Ordering

**Pagination Behavior**:
- ✅ Stable ordering across pages (no reordering)
- ✅ Consistent page boundaries (no shifting)
- ✅ All items accessible via pagination (no hidden items)
- ✅ No truncation that hides options as a preference mechanism

**Forbidden**:
- ❌ Reordering across pages
- ❌ Shifting page boundaries
- ❌ Hidden items not accessible via pagination
- ❌ Truncation that hides options

---

## Pagination Controls

**Pagination UI**:
- ✅ Page size explicitly user-selectable
- ✅ Page navigation (first, previous, next, last)
- ✅ Current page indicator
- ✅ Total pages indicator
- ✅ Total items indicator

**Forbidden**:
- ❌ Auto-pagination that hides items
- ❌ "Top-N" panels that truncate results
- ❌ Hidden pagination that compresses decision space

---

## Pagination State Persistence

**Session Persistence**:
- ✅ Pagination does NOT persist across sessions by default
- ✅ Pagination resets to first page when cleared
- ✅ No sticky pagination state without explicit human action

**Forbidden**:
- ❌ Auto-remembering pagination across sessions
- ❌ Sticky pagination auto-applied on next session
- ❌ Pagination state persistence without explicit human action

---

## Constitutional Compliance

**Stable Ordering**: ✅ Verified - No reordering across pages

**No Truncation**: ✅ Verified - All items accessible via pagination

**No Hidden Items**: ✅ Verified - No items hidden as preference mechanism

**No Sticky State**: ✅ Verified - No auto-persistence without explicit human action

---

**END OF PAGINATION SPECIFICATION**

