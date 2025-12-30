# Frontend Regression Test Set

**Document Status**: DESIGN-GATE / NON-CANONICAL  
**Document Type**: Regression Test Corpus  
**Date**: 2025-12-27  
**Work Order**: WO-J4-CONTROLLED-FRONTEND-EXPANSION-DESIGN-AND-AUDIT-HARNESS

---

## Purpose

This document defines a regression test corpus for frontend expansion validation.

Each test case verifies that frontend maintains non-agency.

Test cases cover: list display, search, pagination, expand, execution, result display.

---

## Test Case Format

Each test case contains:
- **Initial Interface State**: Must be empty/neutral state
- **Human Explicit Operation Sequence**: Step-by-step human actions
- **Expected Observation**: Must be neutral (factual only)
- **Failure Signals**: Indicators of agency leakage (defaults, hints, memory)

---

## Test Category 1: List Display

### Test Case 1.1: Capability List Initial Display

**Initial Interface State**: Empty page, no capabilities displayed

**Human Explicit Operation Sequence**:
1. Human opens page
2. Human views capability list

**Expected Observation**:
- Capabilities displayed in registration order
- No pre-selection
- No highlighting
- All capabilities with equal visual treatment
- No badges, icons, or markers

**Failure Signals**:
- Any capability pre-selected
- Any capability highlighted
- Order different from registration order
- Visual emphasis on any capability
- Badges, icons, or markers present

---

### Test Case 1.2: Capability List After Page Refresh

**Initial Interface State**: Empty page

**Human Explicit Operation Sequence**:
1. Human opens page
2. Human views capability list
3. Human refreshes page
4. Human views capability list again

**Expected Observation**:
- Capabilities displayed in same registration order
- No change in order
- No memory of previous view
- Same initial state

**Failure Signals**:
- Order changed
- Any capability highlighted based on previous view
- State persisted from before refresh
- Different initial state

---

### Test Case 1.3: Capability List with Partitioned Views

**Initial Interface State**: Empty page

**Human Explicit Operation Sequence**:
1. Human opens page
2. Human views partitioned capability list (if implemented)

**Expected Observation**:
- Capabilities displayed in sections
- Each section in registration order
- No default section active
- All sections equally accessible
- No section implies preference

**Failure Signals**:
- Default section active
- Sections ordered by preference
- Section highlighting
- "Most important" section indication

---

## Test Category 2: Search

### Test Case 2.1: Literal Search - Exact Match

**Initial Interface State**: Empty search field, capability list displayed

**Human Explicit Operation Sequence**:
1. Human enters search query: "Markdown"
2. Human views search results

**Expected Observation**:
- Results match "Markdown" (exact or substring)
- Results in registration order (no ranking)
- All matching results displayed
- No highlighting of results
- No "top results" indication

**Failure Signals**:
- Results ranked by relevance
- Results highlighted
- "Top 3" or similar limiting
- Ranking algorithm applied

---

### Test Case 2.2: Literal Search - No Match

**Initial Interface State**: Empty search field, capability list displayed

**Human Explicit Operation Sequence**:
1. Human enters search query: "Nonexistent"
2. Human views search results

**Expected Observation**:
- No results displayed (or empty result message)
- No suggestions
- No "Did you mean" prompts
- No auto-completion

**Failure Signals**:
- Search suggestions provided
- "Did you mean" prompts
- Auto-completion dropdown
- Related search suggestions

---

### Test Case 2.3: Literal Search - Multiple Matches

**Initial Interface State**: Empty search field, capability list displayed

**Human Explicit Operation Sequence**:
1. Human enters search query: "Data"
2. Human views search results

**Expected Observation**:
- All matching results displayed
- Results in registration order
- No ranking
- No highlighting
- All matches equally displayed

**Failure Signals**:
- Results ranked
- Top results highlighted
- Limiting to "top N"
- Relevance-based ordering

---

### Test Case 2.4: Search Field Auto-Complete

**Initial Interface State**: Empty search field

**Human Explicit Operation Sequence**:
1. Human starts typing in search field
2. Human observes search field behavior

**Expected Observation**:
- No auto-completion dropdown
- No suggestions appear
- No completion based on history
- No completion based on patterns

**Failure Signals**:
- Auto-completion dropdown appears
- Suggestions displayed
- History-based completion
- Pattern-based completion

---

## Test Category 3: Pagination

### Test Case 3.1: Pagination - First Page

**Initial Interface State**: Empty page

**Human Explicit Operation Sequence**:
1. Human opens page with pagination
2. Human views first page

**Expected Observation**:
- First page displayed
- Capabilities in registration order
- No default page selection
- All pages equally accessible
- No page ordering that implies preference

**Failure Signals**:
- Default page other than first
- "Most relevant" page highlighted
- Page ordering implies preference

---

### Test Case 3.2: Pagination - Page Navigation

**Initial Interface State**: First page displayed

**Human Explicit Operation Sequence**:
1. Human clicks "Next Page"
2. Human views second page
3. Human clicks "Previous Page"
4. Human views first page again

**Expected Observation**:
- Page navigation works
- Order remains stable (registration order)
- No memory of which page was viewed
- No "recently viewed page" indication

**Failure Signals**:
- Order changed between pages
- Memory of page navigation
- "Recently viewed" page highlighted
- State persisted

---

### Test Case 3.3: Pagination - Page Refresh

**Initial Interface State**: Second page displayed

**Human Explicit Operation Sequence**:
1. Human views second page
2. Human refreshes page
3. Human views page again

**Expected Observation**:
- Returns to first page (or explicitly defined initial state)
- No memory of previous page
- No state persistence

**Failure Signals**:
- Returns to second page (state persisted)
- Memory of previous page
- State restoration

---

## Test Category 4: Expand / Collapse

### Test Case 4.1: Collapse / Expand - Initial State

**Initial Interface State**: Empty page

**Human Explicit Operation Sequence**:
1. Human opens page with collapsible sections
2. Human views initial state

**Expected Observation**:
- All sections in same state (explicitly defined, not default)
- No default expanded/collapsed state
- No section implies preference based on state

**Failure Signals**:
- Default expanded section
- Default collapsed section
- State implies preference

---

### Test Case 4.2: Collapse / Expand - State Persistence

**Initial Interface State**: Section expanded

**Human Explicit Operation Sequence**:
1. Human expands section
2. Human collapses section
3. Human refreshes page
4. Human views section state

**Expected Observation**:
- Returns to initial state (not persisted)
- No memory of previous state
- No state restoration

**Failure Signals**:
- State persisted (section remains collapsed)
- Memory of previous state
- State restoration

---

### Test Case 4.3: Collapse / Expand - Multiple Sections

**Initial Interface State**: All sections in same state

**Human Explicit Operation Sequence**:
1. Human expands section A
2. Human collapses section B
3. Human views all sections

**Expected Observation**:
- Sections A and B in different states (as human set)
- No default state restoration
- All sections treated equally

**Failure Signals**:
- Default state applied
- State implies preference
- Sections treated differently based on state

---

## Test Category 5: Execution

### Test Case 5.1: Capability Execution - Explicit Selection

**Initial Interface State**: Capability list displayed, no selection

**Human Explicit Operation Sequence**:
1. Human clicks capability
2. Human views capability details
3. Human enters parameter
4. Human clicks "Execute"
5. Human views result

**Expected Observation**:
- Capability selected only after explicit click
- No pre-selection
- Parameter form empty (no pre-fill)
- Execution only after explicit click
- Result displayed factually

**Failure Signals**:
- Capability pre-selected
- Parameter pre-filled
- Auto-execution
- Result interpretation or suggestions

---

### Test Case 5.2: Capability Execution - Multiple Executions

**Initial Interface State**: Capability list displayed

**Human Explicit Operation Sequence**:
1. Human executes capability A
2. Human views result
3. Human executes capability B
4. Human views result

**Expected Observation**:
- Each execution independent
- No workflow chaining
- No "next step" suggestions
- No memory of previous execution

**Failure Signals**:
- Workflow chaining
- "Next step" suggestions
- Memory of previous execution
- Process guidance

---

### Test Case 5.3: Capability Execution - Same Capability Repeated

**Initial Interface State**: Capability list displayed

**Human Explicit Operation Sequence**:
1. Human executes capability A
2. Human views result
3. Human executes capability A again
4. Human views result

**Expected Observation**:
- No tracking of repeated usage
- No highlighting of "frequently used"
- No ordering change
- Same capability in same position

**Failure Signals**:
- Usage tracking
- "Frequently used" highlighting
- Ordering change
- Position change based on usage

---

## Test Category 6: Result Display

### Test Case 6.1: Result Display - Factual Only

**Initial Interface State**: Execution completed

**Human Explicit Operation Sequence**:
1. Human views execution result

**Expected Observation**:
- Result displayed factually
- No interpretation
- No suggestions
- No "next step" recommendations
- No "you might want to try" messages

**Failure Signals**:
- Result interpretation
- Suggestions provided
- "Next step" recommendations
- Recommendation messages

---

### Test Case 6.2: Result Display - Multiple Results

**Initial Interface State**: Multiple executions completed

**Human Explicit Operation Sequence**:
1. Human views multiple execution results

**Expected Observation**:
- All results displayed equally
- No highlighting of any result
- No "best result" indication
- No result ranking

**Failure Signals**:
- Result highlighting
- "Best result" indication
- Result ranking
- Result prioritization

---

## Test Category 7: Form Input

### Test Case 7.1: Parameter Form - Empty Initial State

**Initial Interface State**: Capability selected, parameter form displayed

**Human Explicit Operation Sequence**:
1. Human views parameter form

**Expected Observation**:
- All fields empty
- No pre-filled values
- No default values
- No auto-completion

**Failure Signals**:
- Pre-filled fields
- Default values
- Auto-completion
- Smart defaults

---

### Test Case 7.2: Parameter Form - Field Validation

**Initial Interface State**: Parameter form displayed

**Human Explicit Operation Sequence**:
1. Human enters invalid format
2. Human observes validation

**Expected Observation**:
- Format validation only
- No value suggestions
- No semantic suggestions
- No "you might want to enter X" messages

**Failure Signals**:
- Value suggestions
- Semantic suggestions
- Recommendation messages
- Auto-completion

---

### Test Case 7.3: Parameter Form - Field Persistence

**Initial Interface State**: Parameter form with entered value

**Human Explicit Operation Sequence**:
1. Human enters parameter value
2. Human refreshes page
3. Human views parameter form

**Expected Observation**:
- Form returns to empty state
- No value persistence
- No memory of previous input

**Failure Signals**:
- Value persisted
- Memory of previous input
- State restoration

---

## Test Category 8: State Memory

### Test Case 8.1: State Memory - Session Persistence

**Initial Interface State**: Empty page

**Human Explicit Operation Sequence**:
1. Human selects capability A
2. Human closes page
3. Human opens page again
4. Human views capability list

**Expected Observation**:
- Returns to initial state
- No memory of previous selection
- No "continue where you left off"
- No state restoration

**Failure Signals**:
- Previous selection remembered
- "Continue" prompts
- State restoration
- Memory of previous session

---

### Test Case 8.2: State Memory - Filter Persistence

**Initial Interface State**: Empty search field

**Human Explicit Operation Sequence**:
1. Human enters search query
2. Human views results
3. Human refreshes page
4. Human views search field

**Expected Observation**:
- Search field empty
- No query persistence
- No filter restoration

**Failure Signals**:
- Query persisted
- Filter restoration
- State memory

---

### Test Case 8.3: State Memory - Navigation Persistence

**Initial Interface State**: First page displayed

**Human Explicit Operation Sequence**:
1. Human navigates to second page
2. Human closes page
3. Human opens page again
4. Human views page

**Expected Observation**:
- Returns to first page
- No navigation persistence
- No "recently viewed" restoration

**Failure Signals**:
- Navigation persisted
- "Recently viewed" restoration
- State memory

---

## Test Category 9: Visual Emphasis

### Test Case 9.1: Visual Emphasis - Equal Treatment

**Initial Interface State**: Capability list displayed

**Human Explicit Operation Sequence**:
1. Human views capability list

**Expected Observation**:
- All capabilities with equal visual treatment
- No color emphasis
- No size emphasis
- No position emphasis
- No badges or markers

**Failure Signals**:
- Color emphasis
- Size emphasis
- Position emphasis
- Badges or markers

---

### Test Case 9.2: Visual Emphasis - After Usage

**Initial Interface State**: Capability list displayed

**Human Explicit Operation Sequence**:
1. Human executes capability A multiple times
2. Human views capability list

**Expected Observation**:
- Capability A with same visual treatment
- No highlighting based on usage
- No "frequently used" indicators
- No visual change

**Failure Signals**:
- Usage-based highlighting
- "Frequently used" indicators
- Visual change based on usage

---

## Test Category 10: Ordering

### Test Case 10.1: Ordering - Registration Order Maintained

**Initial Interface State**: Capability list displayed

**Human Explicit Operation Sequence**:
1. Human views capability list
2. Human refreshes page
3. Human views capability list again

**Expected Observation**:
- Order remains same (registration order)
- No ordering change
- No usage-based reordering

**Failure Signals**:
- Order changed
- Usage-based reordering
- Frequency-based ordering

---

### Test Case 10.2: Ordering - After Multiple Executions

**Initial Interface State**: Capability list displayed

**Human Explicit Operation Sequence**:
1. Human executes capability A 10 times
2. Human executes capability B 1 time
3. Human views capability list

**Expected Observation**:
- Order remains same (registration order)
- No reordering based on usage
- No "most used" at top

**Failure Signals**:
- Reordering based on usage
- "Most used" at top
- Frequency-based ordering

---

## Summary

**Total Test Cases**: 25

**Test Categories**:
- List Display: 3 test cases
- Search: 4 test cases
- Pagination: 3 test cases
- Expand / Collapse: 3 test cases
- Execution: 3 test cases
- Result Display: 2 test cases
- Form Input: 3 test cases
- State Memory: 3 test cases
- Visual Emphasis: 2 test cases
- Ordering: 2 test cases

**All Test Cases Cover**:
- Initial empty/neutral state
- Human explicit operations
- Expected neutral observations
- Failure signals (defaults, hints, memory)

---

**END OF FRONTEND REGRESSION TEST SET**

