# Neutral Search Specification

**Date**: 2025-12-27  
**Purpose**: Define neutral search query matching rules that do not introduce recommendation signals or hidden ranking

**Note**: This is application-level specification, NOT a CANONICAL document

---

## Search Query Matching Rules

### Literal/Keyword Matching Only

**Search Behavior**:
- ✅ Query matching is literal/keyword only
- ✅ Exact string matching within pattern fields (name, description, tags)
- ✅ Case-insensitive matching (factual, not preferential)
- ✅ No "semantic best match" ranking
- ✅ No relevance scoring
- ✅ No "fuzzy" matching that implies preference

**Forbidden**:
- ❌ Semantic relevance scoring
- ❌ "Best match" ranking
- ❌ Learned ranking
- ❌ Personalization
- ❌ "You may like" suggestions
- ❌ Usage-based ranking
- ❌ History-based ranking
- ❌ Audit-based ranking

---

## Search Result Presentation

**Result Ordering**:
- ✅ Results ordered by pattern_id (lexicographic) when no explicit sort selected
- ✅ No implicit ranking by relevance, popularity, or usage
- ✅ All matching results shown (no hidden items)
- ✅ No "top-N" truncation that hides options

**Forbidden**:
- ❌ Relevance score ordering
- ❌ Popularity-based ordering
- ❌ Usage-based ordering
- ❌ "Most relevant" highlighting
- ❌ Truncation that hides matching results

---

## Constitutional Compliance

**No Recommendation Signals**: ✅ Verified - No recommendation language in search

**No Hidden Ranking**: ✅ Verified - No usage/adoption/history/audit-based ranking

**No Decision Space Compression**: ✅ Verified - All matching results shown

**Literal Matching Only**: ✅ Verified - No semantic or learned ranking

---

**END OF SEARCH SPECIFICATION**

