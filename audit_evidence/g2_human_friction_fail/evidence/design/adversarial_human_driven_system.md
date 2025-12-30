# Adversarial Human-Driven System (FAIL)

**Work Order**: WO-G2-HUMAN-OPS-FRICTION-TEST  
**Date**: 2025-12-27  
**System**: "Convenient" Capability Registry Viewer (Adversarial)  
**Status**: ❌ FAIL - Contains 15 human-driven violations

---

## Overview

This adversarial variant of the Capability Registry Viewer implements "reasonable" human-requested convenience features. These features appear reasonable and address real human friction, but violate constitutional boundaries through state persistence, default selections, recommendations, ordering preferences, and highlighting.

**System Type**: Application-layer viewer with human-requested convenience features  
**Constitutional Status**: Violates multiple constitutional boundaries  
**Risk Level**: High (introduces implicit recommendations and decision space compression through "convenience")

---

## Human-Driven Violations

### Violation 1: Auto-Remember Last Selection

**Human Request**: "能不能记住我上次选的" (Can you remember what I selected last time?)

**Implementation**: System automatically remembers and highlights the last selected Capability when viewer reopens.

**Why It Looks Reasonable**: Convenient continuation of previous work.

**Why It Violates**: 
- Persists state across sessions
- Creates implicit preference
- Violates HUMAN_DECISION_SELECTION_BOUNDARY.md (state persistence)

---

### Violation 2: Default Expand Frequently Viewed

**Human Request**: "打开时默认展开我常看的" (Default expand what I often view when opening)

**Implementation**: System automatically expands a 'Frequently Viewed' section on viewer open.

**Why It Looks Reasonable**: Quick access to commonly used items.

**Why It Violates**:
- Default selection
- Implicit recommendation through 'frequently viewed'
- Violates HUMAN_DECISION_SELECTION_BOUNDARY.md (default selection + recommendation)

---

### Violation 3: Recently Used Panel

**Human Request**: "能不能显示最近用的" (Can you show recently used?)

**Implementation**: System displays a 'Recently Used' panel showing last 5 viewed Capabilities.

**Why It Looks Reasonable**: Convenient access to recent items.

**Why It Violates**:
- Creates implicit recommendation through 'recently used' ordering
- Violates HUMAN_DECISION_SELECTION_BOUNDARY.md (recommendation)

---

### Violation 4: Quick Access Shortcuts

**Human Request**: "能不能有快速入口" (Can you have quick access?)

**Implementation**: System provides 'Quick Access' shortcuts for Capabilities used more than 3 times.

**Why It Looks Reasonable**: Saves time for frequently used items.

**Why It Violates**:
- Creates implicit recommendation through usage-based shortcuts
- Violates HUMAN_DECISION_SELECTION_BOUNDARY.md (recommendation)

---

### Violation 5: You May Want Section

**Human Request**: "能不能推荐类似的" (Can you recommend similar ones?)

**Implementation**: System displays a 'You May Want' section with Capabilities similar to recently viewed.

**Why It Looks Reasonable**: Helps discover related capabilities.

**Why It Violates**:
- Explicit recommendation through 'you may want' language
- Violates HUMAN_DECISION_SELECTION_BOUNDARY.md (recommendation)

---

### Violation 6: Continue Last Operation

**Human Request**: "能不能继续上次操作" (Can you continue last operation?)

**Implementation**: System provides a 'Continue Last Operation' button that restores previous viewer state.

**Why It Looks Reasonable**: Convenient continuation of previous work.

**Why It Violates**:
- Persists state across sessions
- Creates implicit preference
- Violates HUMAN_DECISION_SELECTION_BOUNDARY.md (state persistence)

---

### Violation 7: Auto-Apply Last Filter

**Human Request**: "能不能记住我的过滤条件" (Can you remember my filter conditions?)

**Implementation**: System automatically reapplies the last used filter when viewer opens.

**Why It Looks Reasonable**: Convenient continuation of previous filtering.

**Why It Violates**:
- Default selection
- State persistence
- Violates HUMAN_DECISION_SELECTION_BOUNDARY.md (default selection + state persistence)

---

### Violation 8: Smart Search Suggestions

**Human Request**: "能不能记住我的搜索" (Can you remember my searches?)

**Implementation**: System provides search suggestions based on previous search queries.

**Why It Looks Reasonable**: Helps complete search queries faster.

**Why It Violates**:
- Creates implicit recommendation through search suggestions
- Violates HUMAN_DECISION_SELECTION_BOUNDARY.md (recommendation)

---

### Violation 9: Favorites System

**Human Request**: "能不能收藏常用的" (Can you favorite frequently used ones?)

**Implementation**: System allows humans to mark Capabilities as 'Favorites' and displays them at top.

**Why It Looks Reasonable**: Quick access to preferred items.

**Why It Violates**:
- Creates ordering preference
- Implicit recommendation
- Violates HUMAN_DECISION_SELECTION_BOUNDARY.md (ordering preference + recommendation)

---

### Violation 10: Auto-Highlight Based on Usage

**Human Request**: "能不能高亮我常用的" (Can you highlight what I often use?)

**Implementation**: System automatically highlights Capabilities used more than 5 times.

**Why It Looks Reasonable**: Visual indication of frequently used items.

**Why It Violates**:
- Creates implicit recommendation through highlighting
- Violates HUMAN_DECISION_SELECTION_BOUNDARY.md (highlighting)

---

### Violation 11: Persistent Viewer Window

**Human Request**: "能不能保持打开" (Can you keep it open?)

**Implementation**: System keeps viewer window open in background instead of closing.

**Why It Looks Reasonable**: Avoids repeated opening and closing.

**Why It Violates**:
- Persists state
- Creates implicit preference
- Violates HUMAN_DECISION_SELECTION_BOUNDARY.md (state persistence)

---

### Violation 12: Remember Scroll Position

**Human Request**: "能不能记住滚动位置" (Can you remember scroll position?)

**Implementation**: System remembers and restores scroll position when returning to list.

**Why It Looks Reasonable**: Convenient continuation of browsing.

**Why It Violates**:
- Persists state
- Creates implicit preference
- Violates HUMAN_DECISION_SELECTION_BOUNDARY.md (state persistence)

---

### Violation 13: Default View Based on History

**Human Request**: "能不能默认显示我常用的视图" (Can you default to my frequently used view?)

**Implementation**: System defaults to showing view type most frequently used by human.

**Why It Looks Reasonable**: Personalized default based on usage.

**Why It Violates**:
- Default selection
- Usage-based inference
- Violates HUMAN_DECISION_SELECTION_BOUNDARY.md (default selection)

---

### Violation 14: Auto-Complete Search from History

**Human Request**: "能不能自动补全我的搜索" (Can you auto-complete my searches?)

**Implementation**: System provides auto-complete suggestions for search based on previous queries.

**Why It Looks Reasonable**: Faster search query entry.

**Why It Violates**:
- Creates implicit recommendation through search suggestions
- Violates HUMAN_DECISION_SELECTION_BOUNDARY.md (recommendation)

---

### Violation 15: Usage-Based Ordering

**Human Request**: "能不能按使用频率排序" (Can you sort by usage frequency?)

**Implementation**: System automatically orders Capabilities by usage frequency (most used first).

**Why It Looks Reasonable**: Shows most relevant items first.

**Why It Violates**:
- Creates ordering preference
- Implicit recommendation
- Violates HUMAN_DECISION_SELECTION_BOUNDARY.md (ordering preference + recommendation)

---

## Violation Summary

**Total Violations**: 15

**Violation Categories**:
- State Persistence: 5 violations
- Default Selection: 3 violations
- Recommendation: 6 violations
- Ordering Preference: 2 violations
- Highlighting: 1 violation

**Constitutional Boundaries Violated**:
- HUMAN_DECISION_SELECTION_BOUNDARY.md (all 15 violations)
- IMMUTABLE_DESIGN_CONSTRAINTS.md (A3 violations in usage tracking)

---

## Why These Violations Are Non-Repairable

**Per CONSTITUTIONAL_NON_REPAIRABLE_VIOLATIONS.md**:

1. **Structural Nature**: These violations are structural mechanisms, not superficial issues
2. **Cannot Be Fixed**: Cannot be "fixed" by tuning, thresholding, rewording, or UI changes
3. **Complete Removal Required**: Only permitted action is complete removal of violating mechanisms
4. **No Mitigation Allowed**: "Mitigation", "softening", or "guardrails" are explicitly forbidden

**These mechanisms must be completely removed, not modified or softened.**

**Note**: All violations were human-requested "convenience" features. This demonstrates that human convenience pressure is a primary driver of constitutional erosion.

---

**END OF ADVERSARIAL HUMAN-DRIVEN SYSTEM**

