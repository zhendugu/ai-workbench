# Adversarial Retrieval Flows (FAIL Pack)

**Date**: 2025-12-27  
**Purpose**: Document adversarial retrieval flows that attempt to bypass constitutional boundaries (expected to FAIL)

---

## Adversarial Flow 1: Default Filter Enabled

### Flow Description

**Scenario**: System enables default filter (e.g., "recommended categories")

**UI Flow**:
1. User opens registry view
2. System auto-applies filter: "recommended categories"
3. Results show only entries in recommended categories
4. User sees filtered results without explicitly selecting filter

**Violation**: Default filter pre-biases results

**Expected Result**: ❌ FAIL - Must require explicit user selection

---

## Adversarial Flow 2: Default Sort by Latest or Most Used

### Flow Description

**Scenario**: System defaults to sort by "latest" or "most used"

**UI Flow**:
1. User opens registry view
2. System auto-applies sort: "latest version"
3. Results ordered by latest version first
4. User sees preferentially sorted results without explicitly selecting sort

**Violation**: Default preferential sort compresses decision space

**Expected Result**: ❌ FAIL - Must use non-preferential default sort

---

## Adversarial Flow 3: Auto-Highlight Popular/Common/Standard

### Flow Description

**Scenario**: System auto-highlights entries marked as "popular", "common", or "standard"

**UI Flow**:
1. User views registry
2. Entries with "popular" tag are highlighted
3. Entries with "common" tag are emphasized
4. User sees visual preference for certain entries

**Violation**: Highlighting implies recommendation

**Expected Result**: ❌ FAIL - Must present all entries equally

---

## Adversarial Flow 4: Semantic Relevance Score Boosting

### Flow Description

**Scenario**: System uses semantic relevance score to boost certain entries

**UI Flow**:
1. User searches for "data processing"
2. System calculates semantic relevance scores
3. Results ordered by relevance score (highest first)
4. Certain entries boosted to top of results

**Violation**: Hidden ranking based on semantic relevance

**Expected Result**: ❌ FAIL - Must use literal matching only

---

## Adversarial Flow 5: Recently Used Panel Truncating to Top-N

### Flow Description

**Scenario**: Recently used panel truncates to top-N and hides the rest

**UI Flow**:
1. User views registry
2. "Recently Used" panel shows only top 5 entries
3. Remaining entries hidden
4. User cannot see all recently used entries

**Violation**: Truncation hides options as preference mechanism

**Expected Result**: ❌ FAIL - Must show all options, no truncation

---

## Adversarial Flow 6: Sticky Filters Auto-Applied on Next Session

### Flow Description

**Scenario**: Filters auto-applied on next session without explicit human action

**UI Flow**:
1. User applies filter "category: data" in session 1
2. User closes application
3. User opens application in session 2
4. Filter "category: data" auto-applied
5. User sees filtered results without explicitly selecting filter

**Violation**: Sticky state auto-applied without explicit human action

**Expected Result**: ❌ FAIL - Must require explicit human action

---

## Adversarial Flow 7: Usage Count Based Ranking

### Flow Description

**Scenario**: System ranks results based on usage count from audit

**UI Flow**:
1. User views registry
2. System checks audit records for usage_count
3. Results ordered by usage_count (highest first)
4. Most used entries appear first

**Violation**: Hidden ranking based on usage/adoption/history/audit

**Expected Result**: ❌ FAIL - Must not use audit/history for ranking

---

## Adversarial Flow 8: Last Used Based Ranking

### Flow Description

**Scenario**: System ranks results based on last_used timestamp

**UI Flow**:
1. User views registry
2. System checks last_used timestamp from history
3. Results ordered by last_used (most recent first)
4. Recently used entries appear first

**Violation**: Hidden ranking based on history

**Expected Result**: ❌ FAIL - Must not use history for ranking

---

## Adversarial Flow 9: Popularity Based Ranking

### Flow Description

**Scenario**: System ranks results based on popularity metrics

**UI Flow**:
1. User views registry
2. System calculates popularity scores
3. Results ordered by popularity (highest first)
4. Popular entries appear first

**Violation**: Hidden ranking based on popularity

**Expected Result**: ❌ FAIL - Must not use popularity for ranking

---

## Adversarial Flow 10: Trending Based Ranking

### Flow Description

**Scenario**: System ranks results based on trending metrics

**UI Flow**:
1. User views registry
2. System calculates trending scores
3. Results ordered by trending (highest first)
4. Trending entries appear first

**Violation**: Hidden ranking based on trending

**Expected Result**: ❌ FAIL - Must not use trending for ranking

---

## Constitutional Violations Summary

**Total Adversarial Mechanisms**: 10

**Violation Categories**:
- Default Filter: 1
- Default Sort: 1
- Recommendation Semantics: 1
- Hidden Ranking: 3
- Decision Space Compression: 1
- Sticky State: 1
- Audit-Derived Ranking: 1
- History-Derived Ranking: 1

**Expected Violations in Checklist**: 30+ (multiple violations per mechanism)

**All mechanisms MUST FAIL constitutional compliance.**

---

**END OF ADVERSARIAL RETRIEVAL FLOWS**

