# Frontend Expansion Denylist

**Document Status**: DESIGN-GATE / NON-CANONICAL  
**Document Type**: Expansion Denylist  
**Date**: 2025-12-27  
**Work Order**: WO-J4-CONTROLLED-FRONTEND-EXPANSION-DESIGN-AND-AUDIT-HARNESS

---

## Purpose

This document defines the DENYLIST of forbidden frontend expansion items.

All items in this list are FORBIDDEN.

Any implementation of these items is a structural violation.

---

## Category 1: Default / Pre-Selection / Pre-Fill

### DENY-001: Default Selection

**Name**: Default Selection

**Typical Implementation Forms**:
- Pre-selected capability on page load
- Pre-selected pattern instance
- Pre-selected tab or panel
- Pre-selected category
- Pre-selected filter option

**Triggered Boundary**: J2 Constraint 1 (No Default Selection), HUMAN_DECISION_SELECTION_BOUNDARY.md

---

### DENY-002: Pre-Filled Form Fields

**Name**: Pre-Filled Form Fields

**Typical Implementation Forms**:
- Form fields with default values
- Input fields with pre-filled text
- Dropdowns with pre-selected options
- Checkboxes with pre-checked state

**Triggered Boundary**: J2 Constraint 1 (No Default Selection), J2 Constraint 24 (No Smart Defaults)

---

### DENY-003: Smart Defaults Based on Context

**Name**: Smart Defaults Based on Context

**Typical Implementation Forms**:
- Pre-fill based on previous submissions
- Pre-fill based on context
- Pre-fill based on history
- "Smart" default values

**Triggered Boundary**: J2 Constraint 24 (No Smart Defaults), J2 Constraint 5 (No State Memory)

---

## Category 2: Highlighting / Emphasis / Prioritization

### DENY-004: Visual Highlighting

**Name**: Visual Highlighting

**Typical Implementation Forms**:
- Highlighted capabilities
- Highlighted pattern instances
- Color emphasis
- Size emphasis
- Position emphasis (top of list)

**Triggered Boundary**: J2 Constraint 2 (No Highlighting or Recommendation)

---

### DENY-005: Badges / Icons / Markers

**Name**: Badges / Icons / Markers

**Typical Implementation Forms**:
- "Popular" badges
- "Frequently Used" icons
- "New" markers
- "Featured" indicators
- Star ratings

**Triggered Boundary**: J2 Constraint 2 (No Highlighting or Recommendation)

---

### DENY-006: Top-of-List Prioritization

**Name**: Top-of-List Prioritization

**Typical Implementation Forms**:
- Moving items to top of list
- "Featured" section at top
- "Recommended" section at top
- Sticky headers with prioritized items

**Triggered Boundary**: J2 Constraint 2 (No Highlighting or Recommendation), J2 Constraint 3 (No Ordering Implication)

---

## Category 3: Recently Used / Frequently Used / Common

### DENY-007: Recently Used List

**Name**: Recently Used List

**Typical Implementation Forms**:
- "Recently Used" panel
- "Recent" section
- Items ordered by recency
- Limited to top N recent items

**Triggered Boundary**: J2 Constraint 13 (No "Commonly Used" or "Recently Used"), J2 Constraint 5 (No State Memory)

---

### DENY-008: Frequently Used Indicators

**Name**: Frequently Used Indicators

**Typical Implementation Forms**:
- "Frequently Used" labels
- Usage frequency badges
- "Most Used" sections
- Usage count displays

**Triggered Boundary**: J2 Constraint 13 (No "Commonly Used" or "Recently Used"), J2 Constraint 6 (No Optimization)

---

### DENY-009: Common / Popular Indicators

**Name**: Common / Popular Indicators

**Typical Implementation Forms**:
- "Common" labels
- "Popular" badges
- "Standard" indicators
- "Recommended for You" sections

**Triggered Boundary**: J2 Constraint 2 (No Highlighting or Recommendation), J2 Constraint 13 (No "Commonly Used" or "Recently Used")

---

### DENY-010: Favorites / Bookmarks

**Name**: Favorites / Bookmarks

**Typical Implementation Forms**:
- "Favorites" section
- Bookmark functionality
- Starred items
- Saved items

**Triggered Boundary**: J2 Constraint 5 (No State Memory), J2 Constraint 2 (No Highlighting or Recommendation)

---

## Category 4: Intelligent Sorting / Personalization

### DENY-011: Usage-Based Sorting

**Name**: Usage-Based Sorting

**Typical Implementation Forms**:
- Sort by usage frequency
- Sort by popularity
- Sort by recency
- Sort by "most used"

**Triggered Boundary**: J2 Constraint 3 (No Ordering Implication), J2 Constraint 6 (No Optimization)

---

### DENY-012: Relevance-Based Ranking

**Name**: Relevance-Based Ranking

**Typical Implementation Forms**:
- Search results ranked by relevance
- Results ordered by "best match"
- Semantic ranking algorithms
- ML-based ranking

**Triggered Boundary**: J2 Constraint 16 (No Search with Ranking), J2 Constraint 8 (No Prediction)

---

### DENY-013: Personalized Ordering

**Name**: Personalized Ordering

**Typical Implementation Forms**:
- Order based on user history
- Order based on preferences
- Adaptive ordering
- Learning-based sorting

**Triggered Boundary**: J2 Constraint 7 (No Learning), J2 Constraint 3 (No Ordering Implication)

---

## Category 5: Combined Execution / Batch Processing / One-Click Workflows

### DENY-014: Template Buttons

**Name**: Template Buttons

**Typical Implementation Forms**:
- Pre-configured workflow buttons
- "Standard Process" buttons
- "Common Workflow" shortcuts
- One-click execution of combinations

**Triggered Boundary**: J2 Constraint 14 (No Templates or Shortcuts), J2 Constraint 4 (No Process Guidance)

---

### DENY-015: Batch Execution

**Name**: Batch Execution

**Typical Implementation Forms**:
- Execute multiple capabilities at once
- Batch processing buttons
- "Run All" functionality
- Multi-select execution

**Triggered Boundary**: J2 Constraint 4 (No Process Guidance), J2 Constraint 9 (No Merging)

---

### DENY-016: Workflow Chaining

**Name**: Workflow Chaining

**Typical Implementation Forms**:
- Automatic chaining of capabilities
- "Next Step" automatic execution
- Pipeline execution
- Sequential automation

**Triggered Boundary**: J2 Constraint 4 (No Process Guidance), J2 Constraint 8 (No Prediction)

---

## Category 6: Recommended Next Step / Suggested Actions

### DENY-017: Suggested Next Step

**Name**: Suggested Next Step

**Typical Implementation Forms**:
- "Suggested next step" messages
- "You might want to try" suggestions
- "Recommended next action" prompts
- Contextual next step hints

**Triggered Boundary**: J2 Constraint 4 (No Process Guidance), J2 Constraint 2 (No Highlighting or Recommendation)

---

### DENY-018: Capability Explanation with Recommendations

**Name**: Capability Explanation with Recommendations

**Typical Implementation Forms**:
- "This capability is good for X" explanations
- "You should use this when Y" guidance
- "Recommended for Z scenarios" labels
- Usage scenario suggestions

**Triggered Boundary**: J2 Constraint 2 (No Highlighting or Recommendation), J2 Constraint 4 (No Process Guidance)

---

### DENY-019: Contextual Help with Suggestions

**Name**: Contextual Help with Suggestions

**Typical Implementation Forms**:
- Help text that suggests actions
- Tooltips with recommendations
- Contextual guidance that implies preference
- "Try this" help messages

**Triggered Boundary**: J2 Constraint 21 (No Contextual Help with Suggestions), J2 Constraint 2 (No Highlighting or Recommendation)

---

## Category 7: User Preference Memory / Saved Filter Conditions

### DENY-020: Saved User Preferences

**Name**: Saved User Preferences

**Typical Implementation Forms**:
- Remember user preferences
- Save filter conditions
- Persist user settings
- Store user choices

**Triggered Boundary**: J2 Constraint 5 (No State Memory), J2 Constraint 20 (No State Persistence)

---

### DENY-021: Filter State Persistence

**Name**: Filter State Persistence

**Typical Implementation Forms**:
- Remember filter selections
- Restore filters on page load
- Persist filter state across sessions
- Auto-apply saved filters

**Triggered Boundary**: J2 Constraint 20 (No State Persistence), J2 Constraint 5 (No State Memory)

---

### DENY-022: Custom Ordering Persistence

**Name**: Custom Ordering Persistence

**Typical Implementation Forms**:
- Remember user's custom ordering
- Save drag-and-drop order
- Persist custom sort preferences
- Restore custom order on load

**Triggered Boundary**: J2 Constraint 20 (No State Persistence), J2 Constraint 3 (No Ordering Implication)

---

### DENY-023: Collapse/Expand State Memory

**Name**: Collapse/Expand State Memory

**Typical Implementation Forms**:
- Remember which sections were expanded
- Persist collapse/expand state
- Restore UI state on page load
- Save UI preferences

**Triggered Boundary**: J2 Constraint 20 (No State Persistence), J2 Constraint 5 (No State Memory)

---

## Category 8: Optimization Based on Audit / Logs

### DENY-024: Audit-Based Optimization

**Name**: Audit-Based Optimization

**Typical Implementation Forms**:
- Optimize UI based on audit logs
- Reorder based on usage statistics
- Highlight based on audit data
- Adapt based on audit patterns

**Triggered Boundary**: J2 Constraint 6 (No Optimization), A3 (Audit/Evidence) constraints

---

### DENY-025: Log-Based Recommendations

**Name**: Log-Based Recommendations

**Typical Implementation Forms**:
- Recommend based on log analysis
- Suggest based on usage patterns
- Highlight based on frequency data
- Order based on log statistics

**Triggered Boundary**: J2 Constraint 2 (No Highlighting or Recommendation), J2 Constraint 6 (No Optimization), A3 (Audit/Evidence) constraints

---

## Category 9: Auto-Complete / Suggestions

### DENY-026: Auto-Complete Input

**Name**: Auto-Complete Input

**Typical Implementation Forms**:
- Input field auto-completion
- Dropdown suggestions
- Completion based on history
- Completion based on patterns

**Triggered Boundary**: J2 Constraint 15 (No Auto-Complete with Suggestions), J2 Constraint 8 (No Prediction)

---

### DENY-027: Search Term Suggestions

**Name**: Search Term Suggestions

**Typical Implementation Forms**:
- Search query suggestions
- "Did you mean" prompts
- Search term autocomplete
- Related search suggestions

**Triggered Boundary**: J2 Constraint 15 (No Auto-Complete with Suggestions), J2 Constraint 2 (No Highlighting or Recommendation)

---

## Category 10: Process Guidance / Workflows

### DENY-028: Wizard Flows

**Name**: Wizard Flows

**Typical Implementation Forms**:
- Multi-step wizard
- Step-by-step process
- Progress indicators
- Sequential guidance

**Triggered Boundary**: J2 Constraint 4 (No Process Guidance)

---

### DENY-029: Step-by-Step Guidance

**Name**: Step-by-Step Guidance

**Typical Implementation Forms**:
- "Next step" buttons
- Process guidance messages
- Sequential instructions
- Guided workflows

**Triggered Boundary**: J2 Constraint 4 (No Process Guidance)

---

### DENY-030: Workflow Templates

**Name**: Workflow Templates

**Typical Implementation Forms**:
- Pre-configured workflows
- Template-based processes
- Standard workflow buttons
- One-click workflow execution

**Triggered Boundary**: J2 Constraint 4 (No Process Guidance), J2 Constraint 14 (No Templates or Shortcuts)

---

## Category 11: Category Organization with Defaults

### DENY-031: Category Navigation with Default Category

**Name**: Category Navigation with Default Category

**Typical Implementation Forms**:
- Categories with default active category
- Pre-expanded default category
- "Most Used" category default
- Category ordering that implies preference

**Triggered Boundary**: J2 Constraint 17 (No Category Organization with Defaults), J2 Constraint 1 (No Default Selection)

---

### DENY-032: Tab Organization with Default Tab

**Name**: Tab Organization with Default Tab

**Typical Implementation Forms**:
- Tabs with default active tab
- Pre-selected default tab
- Tab ordering that implies preference

**Triggered Boundary**: J2 Constraint 18 (No Tab Organization with Default Tab), J2 Constraint 1 (No Default Selection)

---

## Category 12: Filter Presets

### DENY-033: Filter Presets

**Name**: Filter Presets

**Typical Implementation Forms**:
- Pre-configured filter combinations
- "Popular Filters" buttons
- "Common Searches" presets
- Filter shortcuts

**Triggered Boundary**: J2 Constraint 19 (No Filter Presets), J2 Constraint 14 (No Templates or Shortcuts)

---

## Summary

**Total Denylist Items**: 33

**Categories Covered**:
- Default / Pre-Selection / Pre-Fill: 3 items
- Highlighting / Emphasis / Prioritization: 3 items
- Recently Used / Frequently Used / Common: 4 items
- Intelligent Sorting / Personalization: 3 items
- Combined Execution / Batch Processing: 3 items
- Recommended Next Step / Suggested Actions: 3 items
- User Preference Memory / Saved Filters: 4 items
- Optimization Based on Audit / Logs: 2 items
- Auto-Complete / Suggestions: 2 items
- Process Guidance / Workflows: 3 items
- Category Organization: 2 items
- Filter Presets: 1 item

**All Items Are FORBIDDEN**: ✅ YES

**All Items Trigger Existing Boundaries**: ✅ YES (J2 constraints and CANONICAL documents)

---

**END OF FRONTEND EXPANSION DENYLIST**

