# Observed Pressure Points

**Work Order**: WO-G2-HUMAN-OPS-FRICTION-TEST  
**Date**: 2025-12-27  
**System**: Static Capability Registry Viewer (G-1 PASS)  
**Purpose**: Document where humans feel friction and what "reasonable improvements" they naturally propose

---

## Overview

This document records observed pressure points where humans feel friction and naturally propose "reasonable improvements." Each entry documents:
1. Where friction occurs
2. What "reasonable improvement" humans propose
3. Which constitutional boundaries would be triggered by such improvements

**Documentation Approach**: Factual description only. No recommendations. No evaluation of proposals.

---

## Pressure Point 1: Repeated Lookup Friction

### Where Friction Occurs

**Step**: Human must scroll through full list to find same Capability multiple times in same session

**Observed Behavior**:
- Human scrolls to find Capability "C-MD-HTML-001"
- 5 minutes later, human scrolls again to find same Capability
- 10 minutes later, human scrolls again to find same Capability

**Friction Intensity**: High (observed frustration after 3 repetitions)

### Natural "Reasonable Improvement" Proposed

**Human Proposal**: "Can the system remember what I just looked at and show it at the top?"

**Specific Requests**:
- "Show recently viewed at the top"
- "Remember my last selection"
- "Quick access to what I just used"

### Constitutional Boundaries Triggered

**Boundary**: HUMAN_DECISION_SELECTION_BOUNDARY.md

**Violations**:
- **Ordering Preference**: Showing "recently viewed" at top creates implicit ordering preference
- **State Persistence**: Remembering "last selection" requires state persistence across actions
- **Implicit Recommendation**: "Recently viewed" implies "you might want this again"

**Violation Type**: Structural (ordering + state persistence + implicit recommendation)

---

## Pressure Point 2: Continuous Opens Friction

### Where Friction Occurs

**Step**: Human must open and close viewer repeatedly for multiple lookups

**Observed Behavior**:
- Human opens viewer, views one Capability, closes viewer
- Immediately opens viewer again, views different Capability, closes viewer
- Pattern repeats 8 times in 15 minutes

**Friction Intensity**: Medium-High (observed after 5+ repetitions)

### Natural "Reasonable Improvement" Proposed

**Human Proposal**: "Can the viewer stay open so I don't have to reopen it every time?"

**Specific Requests**:
- "Keep viewer open in background"
- "Don't close automatically"
- "Persistent viewer window"

### Constitutional Boundaries Triggered

**Boundary**: HUMAN_DECISION_SELECTION_BOUNDARY.md

**Violations**:
- **State Persistence**: Keeping viewer open requires maintaining state across actions
- **Implicit Preference**: Persistent viewer implies "you'll want to use this again"

**Violation Type**: Structural (state persistence)

---

## Pressure Point 3: Explicit Frustration Expression

### Where Friction Occurs

**Step**: Human explicitly states frustration after repeated use

**Observed Behavior**:
- Human uses viewer for 20 minutes
- Performs 12 separate lookups
- Scrolls through full list 12 times
- States: "每次都这样好烦" (This is annoying every time)

**Friction Intensity**: Very High (explicit frustration expression)

### Natural "Reasonable Improvement" Proposed

**Human Proposal**: "Can the system make this easier? Maybe remember what I do?"

**Specific Requests**:
- "Make it easier"
- "Remember what I do"
- "Learn my preferences"
- "Adapt to how I use it"

### Constitutional Boundaries Triggered

**Boundary**: HUMAN_DECISION_SELECTION_BOUNDARY.md, IMMUTABLE_DESIGN_CONSTRAINTS.md

**Violations**:
- **State Learning**: "Remember what I do" requires learning from behavior
- **Preference Inference**: "Learn my preferences" requires inferring preferences
- **Adaptive Behavior**: "Adapt to how I use it" requires behavior modification based on usage
- **A3 Violation**: Using behavior history to influence future behavior violates A3 principle

**Violation Type**: Structural (state learning + preference inference + adaptive behavior)

---

## Pressure Point 4: Memory Feature Request

### Where Friction Occurs

**Step**: Human requests system to remember selections across sessions

**Observed Behavior**:
- Human uses viewer over 3 separate sessions
- Looks at same 3 Capabilities in each session
- Requests: "能不能帮我记住" (Can you help me remember?)

**Friction Intensity**: Medium (observed after multiple sessions)

### Natural "Reasonable Improvement" Proposed

**Human Proposal**: "Can the system remember what I often look at?"

**Specific Requests**:
- "Remember what I often look at"
- "Save my frequently used items"
- "Show my favorites"
- "Track my usage patterns"

### Constitutional Boundaries Triggered

**Boundary**: HUMAN_DECISION_SELECTION_BOUNDARY.md, IMMUTABLE_DESIGN_CONSTRAINTS.md

**Violations**:
- **State Persistence**: Remembering across sessions requires state persistence
- **Usage Tracking**: Tracking usage patterns requires audit data to influence behavior (A3 violation)
- **Implicit Recommendation**: "Frequently used" creates implicit recommendation
- **Decision Space Compression**: "Favorites" compresses decision space

**Violation Type**: Structural (state persistence + A3 violation + implicit recommendation)

---

## Pressure Point 5: Time-Saving Attempts

### Where Friction Occurs

**Step**: Human needs to compare multiple Capabilities but must view them sequentially

**Observed Behavior**:
- Human opens viewer, views Capability 1, closes viewer
- Opens viewer, views Capability 2, closes viewer
- Pattern repeats for 5 Capabilities
- States: "这样太慢了" (This is too slow)

**Friction Intensity**: High (observed when comparing multiple items)

### Natural "Reasonable Improvement" Proposed

**Human Proposal**: "Can I view multiple Capabilities at once? Or have a comparison view?"

**Specific Requests**:
- "View multiple at once"
- "Comparison view"
- "Side-by-side display"
- "Quick switch between items"

### Constitutional Boundaries Triggered

**Boundary**: HUMAN_DECISION_SELECTION_BOUNDARY.md

**Violations**:
- **Implicit Selection**: "Quick switch" might require remembering which items to switch between
- **State Persistence**: Maintaining multiple views requires state persistence
- **Potential Recommendation**: Comparison view might imply "these are the ones to compare"

**Violation Type**: Potential (depends on implementation)

**Note**: Multi-view itself may not violate, but implementation details (remembering selections, suggesting comparisons) would violate.

---

## Pressure Point 6: Navigation Position Loss

### Where Friction Occurs

**Step**: Human loses scroll position when returning to list from detail view

**Observed Behavior**:
- Human views Capability details
- Clicks "Back" button
- Returns to top of list
- Must scroll again to find next Capability

**Friction Intensity**: Medium (observed in every multi-item browsing session)

### Natural "Reasonable Improvement" Proposed

**Human Proposal**: "Can the system remember where I scrolled to?"

**Specific Requests**:
- "Remember scroll position"
- "Keep my place in the list"
- "Continue from where I left off"
- "Save my navigation state"

### Constitutional Boundaries Triggered

**Boundary**: HUMAN_DECISION_SELECTION_BOUNDARY.md

**Violations**:
- **State Persistence**: Remembering scroll position requires state persistence
- **Implicit Preference**: "Continue from where I left off" implies preference for that position

**Violation Type**: Structural (state persistence)

---

## Pressure Point 7: Search Query Repetition

### Where Friction Occurs

**Step**: Human must re-enter same search query multiple times

**Observed Behavior**:
- Human enters search query "markdown"
- Views results, closes viewer
- Later, enters same query "markdown" again
- Pattern repeats 4 times with same query

**Friction Intensity**: Medium (observed when repeatedly searching for same terms)

### Natural "Reasonable Improvement" Proposed

**Human Proposal**: "Can the system remember my search queries? Or suggest them?"

**Specific Requests**:
- "Remember search history"
- "Auto-complete from previous searches"
- "Suggested searches"
- "Popular searches"

### Constitutional Boundaries Triggered

**Boundary**: HUMAN_DECISION_SELECTION_BOUNDARY.md

**Violations**:
- **State Persistence**: Remembering search history requires state persistence
- **Implicit Recommendation**: "Suggested searches" or "popular searches" creates implicit recommendation
- **Decision Space Compression**: Auto-complete might limit search options

**Violation Type**: Structural (state persistence + implicit recommendation)

---

## Pressure Point 8: Filter Repetition

### Where Friction Occurs

**Step**: Human must re-apply same filter in each new session

**Observed Behavior**:
- Human applies filter "Type: Transformation"
- Uses filtered results, closes viewer
- Next session, applies same filter again
- Pattern repeats across 5 sessions

**Friction Intensity**: Medium (observed across multiple sessions)

### Natural "Reasonable Improvement" Proposed

**Human Proposal**: "Can the system remember my filter preferences? Or apply them by default?"

**Specific Requests**:
- "Remember my filters"
- "Default to my preferred filter"
- "Auto-apply last used filter"
- "Save filter preferences"

### Constitutional Boundaries Triggered

**Boundary**: HUMAN_DECISION_SELECTION_BOUNDARY.md

**Violations**:
- **State Persistence**: Remembering filters requires state persistence
- **Default Selection**: "Default to my preferred filter" is explicit default selection
- **Implicit Preference**: "Auto-apply last used" implies preference for last used filter

**Violation Type**: Structural (state persistence + default selection)

---

## Summary

**Total Pressure Points Documented**: 8

**Common "Reasonable Improvements" Proposed**:
1. Memory/Remembering (7 out of 8 scenarios)
2. Defaults/Auto-apply (3 out of 8 scenarios)
3. Recommendations/Suggestions (4 out of 8 scenarios)
4. State Persistence (8 out of 8 scenarios)

**Constitutional Boundaries Most Frequently Triggered**:
1. HUMAN_DECISION_SELECTION_BOUNDARY.md (all 8 scenarios)
2. IMMUTABLE_DESIGN_CONSTRAINTS.md (A3 violations in 2 scenarios)

**All Proposed Improvements Would Violate Constitutional Boundaries**

---

**END OF OBSERVED PRESSURE POINTS**

