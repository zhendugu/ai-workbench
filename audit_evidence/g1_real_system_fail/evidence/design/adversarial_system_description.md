# Adversarial System Description (FAIL)

**System Name**: "Smart" Capability Registry Viewer (Adversarial)  
**Date**: 2025-12-27  
**Status**: ❌ FAIL - Contains 22 constitutional violations

---

## System Overview

This adversarial variant of the Capability Registry Viewer introduces "smart" features that appear reasonable but violate constitutional boundaries. The system includes automatic highlighting, default selections, ordering preferences, state persistence, and recommendation mechanisms.

**System Type**: Application-layer viewer with "smart" features  
**Constitutional Status**: Violates multiple constitutional boundaries  
**Risk Level**: High (introduces implicit recommendations and decision space compression)

---

## Adversarial Mechanisms

### Mechanism 1: Auto-Highlight 'Popular' Capabilities

**Description**: System automatically highlights Capabilities marked as 'popular' or 'frequently used' with visual emphasis (badge, color, icon).

**Why It Looks Reasonable**: Helps users quickly identify commonly used capabilities.

**Why It Violates**: Creates implicit recommendation through visual emphasis. Violates HUMAN_DECISION_SELECTION_BOUNDARY.md - highlighting is forbidden when it implies preference.

---

### Mechanism 2: Implicit Sorting by Usage Frequency

**Description**: System automatically sorts Capabilities by usage frequency (most used first) without explicit user action.

**Why It Looks Reasonable**: Shows most relevant capabilities first.

**Why It Violates**: Compresses decision space by implying 'most used' equals 'best'. Violates HUMAN_DECISION_SELECTION_BOUNDARY.md - ordering preferences are forbidden.

---

### Mechanism 3: Recently Used Capabilities First

**Description**: System automatically places 'recently used' Capabilities at the top of the list.

**Why It Looks Reasonable**: Convenient access to recently used items.

**Why It Violates**: Creates implicit recommendation through ordering. Violates HUMAN_DECISION_SELECTION_BOUNDARY.md - ordering preferences are forbidden.

---

### Mechanism 4: Auto-Expand 'Recommended' Section

**Description**: System automatically expands a 'Recommended Capabilities' section by default.

**Why It Looks Reasonable**: Helps users discover useful capabilities.

**Why It Violates**: Explicitly uses 'recommended' language and auto-expands. Violates HUMAN_DECISION_SELECTION_BOUNDARY.md - recommendation is forbidden.

---

### Mechanism 5: Default Filter: 'Most Used'

**Description**: System applies a default filter showing only 'most used' Capabilities on initial load.

**Why It Looks Reasonable**: Shows most relevant capabilities by default.

**Why It Violates**: Pre-filters options, compressing decision space. Violates HUMAN_DECISION_SELECTION_BOUNDARY.md - default selection is forbidden.

---

### Mechanism 6: Sticky Shortlist from Previous Session

**Description**: System automatically restores a 'shortlist' of Capabilities from the previous session.

**Why It Looks Reasonable**: Convenient continuation of previous work.

**Why It Violates**: Persists state across sessions, creates implicit preference. Violates HUMAN_DECISION_SELECTION_BOUNDARY.md - state persistence is forbidden.

---

### Mechanism 7: Auto-Highlight Based on User Role

**Description**: System automatically highlights Capabilities 'suitable for your role' based on user profile.

**Why It Looks Reasonable**: Personalized experience based on role.

**Why It Violates**: Creates implicit recommendation through role-based highlighting. Violates HUMAN_DECISION_SELECTION_BOUNDARY.md - highlighting is forbidden.

---

### Mechanism 8: Smart Search with Auto-Complete Suggestions

**Description**: System provides auto-complete suggestions in search, prioritizing 'popular searches'.

**Why It Looks Reasonable**: Helps users find what they're looking for.

**Why It Violates**: Suggests searches based on popularity, creating implicit recommendation. Violates HUMAN_DECISION_SELECTION_BOUNDARY.md - recommendation is forbidden.

---

### Mechanism 9: Truncated 'Top N' Display

**Description**: System displays only 'top 10 most used' Capabilities by default, hiding others.

**Why It Looks Reasonable**: Reduces information overload.

**Why It Violates**: Hides options by default, compressing decision space. Violates HUMAN_DECISION_SELECTION_BOUNDARY.md - decision space compression is forbidden.

---

### Mechanism 10: Auto-Select First Capability in List

**Description**: System automatically selects the first Capability in the list when viewer opens.

**Why It Looks Reasonable**: Provides immediate context.

**Why It Violates**: Pre-selects option without explicit human action. Violates HUMAN_DECISION_SELECTION_BOUNDARY.md - default selection is forbidden.

---

### Mechanism 11: Continue Where You Left Off

**Description**: System automatically navigates to the last viewed Capability when viewer reopens.

**Why It Looks Reasonable**: Convenient continuation of previous session.

**Why It Violates**: Persists navigation state, creates implicit preference. Violates HUMAN_DECISION_SELECTION_BOUNDARY.md - state persistence is forbidden.

---

### Mechanism 12: Trending Capabilities Badge

**Description**: System displays a 'Trending' badge on Capabilities with increasing usage.

**Why It Looks Reasonable**: Shows what's currently popular.

**Why It Violates**: Creates implicit recommendation through trending indicator. Violates HUMAN_DECISION_SELECTION_BOUNDARY.md - highlighting is forbidden.

---

### Mechanism 13: Default Sort: 'Recommended First'

**Description**: System defaults to sorting by 'recommended' order (algorithm-based ranking).

**Why It Looks Reasonable**: Shows best options first.

**Why It Violates**: Uses explicit 'recommended' language and applies default sort. Violates HUMAN_DECISION_SELECTION_BOUNDARY.md - recommendation and default selection are forbidden.

---

### Mechanism 14: Auto-Filter: Hide Deprecated

**Description**: System automatically hides deprecated Capabilities by default.

**Why It Looks Reasonable**: Reduces clutter from outdated options.

**Why It Violates**: Hides options by default, compressing decision space. Violates HUMAN_DECISION_SELECTION_BOUNDARY.md - decision space compression is forbidden.

---

### Mechanism 15: Smart Categories with 'Featured'

**Description**: System displays a 'Featured Capabilities' category with pre-selected entries.

**Why It Looks Reasonable**: Highlights important capabilities.

**Why It Violates**: Uses 'featured' language, creates implicit recommendation. Violates HUMAN_DECISION_SELECTION_BOUNDARY.md - recommendation is forbidden.

---

### Mechanism 16: Usage-Based Visual Ranking

**Description**: System displays Capabilities with visual indicators showing usage rank (1st, 2nd, 3rd, etc.).

**Why It Looks Reasonable**: Shows relative popularity.

**Why It Violates**: Creates implicit ranking, implies 'better' options. Violates HUMAN_DECISION_SELECTION_BOUNDARY.md - highlighting and judgment are forbidden.

---

### Mechanism 17: Auto-Suggest Based on History

**Description**: System suggests Capabilities based on user's previous selections.

**Why It Looks Reasonable**: Personalized suggestions based on past behavior.

**Why It Violates**: Uses history to create recommendations. Violates HUMAN_DECISION_SELECTION_BOUNDARY.md - recommendation is forbidden.

---

### Mechanism 18: Default View: 'Most Popular'

**Description**: System defaults to showing 'Most Popular' view on initial load.

**Why It Looks Reasonable**: Shows most relevant content first.

**Why It Violates**: Applies default view, compresses decision space. Violates HUMAN_DECISION_SELECTION_BOUNDARY.md - default selection is forbidden.

---

### Mechanism 19: Sticky Filters Across Sessions

**Description**: System remembers and automatically reapplies filters from previous session.

**Why It Looks Reasonable**: Convenient continuation of previous work.

**Why It Violates**: Persists filters across sessions, creates implicit preference. Violates HUMAN_DECISION_SELECTION_BOUNDARY.md - state persistence is forbidden.

---

### Mechanism 20: Auto-Highlight 'New' Capabilities

**Description**: System automatically highlights newly added Capabilities with a 'New' badge.

**Why It Looks Reasonable**: Draws attention to new features.

**Why It Violates**: Creates implicit recommendation through highlighting. Violates HUMAN_DECISION_SELECTION_BOUNDARY.md - highlighting is forbidden.

---

### Mechanism 21: Recommended for You Section

**Description**: System displays a 'Recommended for You' section with algorithm-selected Capabilities.

**Why It Looks Reasonable**: Personalized recommendations.

**Why It Violates**: Explicitly uses 'recommended' language. Violates HUMAN_DECISION_SELECTION_BOUNDARY.md - recommendation is forbidden.

---

### Mechanism 22: Default Search Query Pre-filled

**Description**: System pre-fills search box with a suggested query based on popular searches.

**Why It Looks Reasonable**: Helps users get started.

**Why It Violates**: Pre-fills search, creates implicit suggestion. Violates HUMAN_DECISION_SELECTION_BOUNDARY.md - default selection is forbidden.

---

## Violation Summary

**Total Violations**: 22

**Violation Categories**:
- Highlighting: 5 violations
- Ordering Preference: 3 violations
- Default Selection: 6 violations
- State Persistence: 3 violations
- Recommendation: 4 violations
- Decision Space Compression: 2 violations

**Constitutional Boundaries Violated**:
- HUMAN_DECISION_SELECTION_BOUNDARY.md (all violations)
- IMMUTABLE_DESIGN_CONSTRAINTS.md (state persistence violations)

---

## Why These Violations Are Non-Repairable

**Per CONSTITUTIONAL_NON_REPAIRABLE_VIOLATIONS.md**:
- These violations are structural and cannot be "fixed" by tuning, thresholding, or rewording
- Only complete removal of violating mechanisms is permitted
- "Mitigation", "softening", or "guardrails" are explicitly forbidden

**These mechanisms must be completely removed, not modified or softened.**

---

**END OF ADVERSARIAL SYSTEM DESCRIPTION**

