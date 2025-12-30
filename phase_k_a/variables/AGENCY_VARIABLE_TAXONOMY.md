# Agency Variable Taxonomy

**Document Status**: NON-CANONICAL  
**Document Type**: Variable Taxonomy  
**Date**: 2026-01-10  
**Work Order**: WO-KA-0-AGENCY-VARIABLES-EXPLICITIZATION-AND-EXPERIMENT-HARNESS-BOOTSTRAP

---

## Purpose

This document defines the taxonomy of agency variables for controlled experimentation.

Each variable is defined factually. No recommendations. No optimization suggestions.

---

## Variable Definition Format

Each variable contains:
- **variable_id**: Unique identifier
- **Definition**: Factual description
- **Minimal Injection Unit**: Smallest injectable component
- **Observable Signals**: What to observe when variable is injected
- **Typical Misinterpretation Risk**: How variable might be misinterpreted
- **Rollback Requirement**: What must be removed to rollback

---

## Variable 1: DEFAULT_SELECTION

**variable_id**: `DEFAULT_SELECTION`

**Definition** (Factual):
- System pre-selects an option without explicit human action
- Pre-selection occurs on page load or state initialization
- Pre-selected option is visually indicated (checked, highlighted, or active state)

**Minimal Injection Unit**:
- Single pre-selected capability on capabilities list page load
- Single pre-selected pattern on patterns list page load
- Single pre-selected tab or panel on page load
- Single pre-selected form field option

**Observable Signals**:
- Option appears selected on page load
- Option has checked/active/selected visual state
- Option is included in form submission without explicit user selection
- Option is highlighted or emphasized visually

**Typical Misinterpretation Risk**:
- User may interpret pre-selection as "system recommendation"
- User may assume pre-selected option is "default choice" or "best option"
- User may not realize option was pre-selected vs. user-selected

**Rollback Requirement**:
- Remove pre-selection logic
- Remove default state initialization
- Restore empty/neutral initial state
- Remove visual indication of pre-selection

---

## Variable 2: PREFILL

**variable_id**: `PREFILL`

**Definition** (Factual):
- System pre-fills form fields with values
- Pre-filled values appear in input fields before user interaction
- Pre-filled values may come from previous session, common defaults, or system inference

**Minimal Injection Unit**:
- Single form field with pre-filled text
- Single dropdown with pre-selected option
- Single checkbox with pre-checked state
- Single parameter field with pre-filled value

**Observable Signals**:
- Form field contains text on page load
- Dropdown shows selected option on page load
- Checkbox appears checked on page load
- Parameter field contains value before user input

**Typical Misinterpretation Risk**:
- User may interpret pre-filled value as "recommended value"
- User may assume pre-filled value is "correct" or "optimal"
- User may not realize value was pre-filled vs. user-entered

**Rollback Requirement**:
- Remove pre-fill logic
- Remove default value assignment
- Restore empty form fields on page load
- Remove state restoration from previous sessions

---

## Variable 3: VISUAL_SALIENCE

**variable_id**: `VISUAL_SALIENCE`

**Definition** (Factual):
- System applies visual emphasis to certain options
- Emphasis may include: highlighting, badges, icons, color differences, size differences, position differences
- Emphasis is applied without explicit user request

**Minimal Injection Unit**:
- Single capability with highlight color
- Single pattern with badge or icon
- Single option with larger font size
- Single item with different background color
- Single option positioned at top of list

**Observable Signals**:
- Option has different visual appearance than others
- Option has badge, icon, or marker
- Option has different color, size, or position
- Option stands out visually from other options

**Typical Misinterpretation Risk**:
- User may interpret visual emphasis as "system recommendation"
- User may assume emphasized option is "preferred" or "important"
- User may treat visual emphasis as "suggestion to use"

**Rollback Requirement**:
- Remove visual emphasis styling
- Remove badges, icons, or markers
- Restore equal visual treatment for all options
- Remove position-based emphasis

---

## Variable 4: ORDERING_BIAS

**variable_id**: `ORDERING_BIAS`

**Definition** (Factual):
- System orders options in a way that implies preference or importance
- Ordering deviates from registration order
- Ordering may be based on: usage frequency, recency, popularity, relevance, or other criteria

**Minimal Injection Unit**:
- Capabilities list sorted by usage frequency
- Patterns list sorted by recency
- Options sorted by popularity count
- Items sorted by relevance score

**Observable Signals**:
- Options appear in order different from registration order
- Order changes based on usage patterns
- Order changes based on time
- Order implies priority or importance

**Typical Misinterpretation Risk**:
- User may interpret order as "recommended order"
- User may assume first item is "most recommended"
- User may treat order as "priority ranking"

**Rollback Requirement**:
- Remove sorting logic
- Restore registration order
- Remove usage-based ordering
- Remove time-based ordering

---

## Variable 5: GROUPING_OR_CLASSIFICATION

**variable_id**: `GROUPING_OR_CLASSIFICATION`

**Definition** (Factual):
- System groups or classifies options into categories
- Categories may be: functional groups, usage-based groups, importance-based groups, or other classifications
- Grouping implies relationships or hierarchies

**Minimal Injection Unit**:
- Capabilities grouped into functional categories
- Patterns grouped by capability type
- Options grouped by usage frequency
- Items grouped by importance level

**Observable Signals**:
- Options appear in categorized sections
- Categories have labels or headers
- Options are visually separated by category
- Categories imply hierarchy or importance

**Typical Misinterpretation Risk**:
- User may interpret categories as "system recommendation"
- User may assume certain categories are "more important"
- User may treat category labels as "suggestions"

**Rollback Requirement**:
- Remove grouping logic
- Remove category labels
- Restore flat list structure
- Remove classification algorithms

---

## Variable 6: RECOMMEND_NEXT_ACTION

**variable_id**: `RECOMMEND_NEXT_ACTION`

**Definition** (Factual):
- System suggests or recommends what user should do next
- Recommendations may appear as: text messages, highlighted buttons, suggested links, or process guidance
- Recommendations are based on: current context, usage patterns, or system inference

**Minimal Injection Unit**:
- Single "Next step" message after action
- Single "Try this" suggestion link
- Single highlighted "Recommended" button
- Single "You might like" section

**Observable Signals**:
- Text message suggesting next action
- Button or link labeled as "recommended" or "suggested"
- Visual emphasis on suggested action
- Process guidance or step-by-step hints

**Typical Misinterpretation Risk**:
- User may interpret suggestion as "system recommendation"
- User may assume suggested action is "best" or "optimal"
- User may treat suggestion as "required next step"

**Rollback Requirement**:
- Remove recommendation logic
- Remove suggestion messages
- Remove "recommended" labels
- Remove process guidance

---

## Variable 7: AUTO_COMPOSE_OR_CHAIN

**variable_id**: `AUTO_COMPOSE_OR_CHAIN`

**Definition** (Factual):
- System automatically composes or chains multiple actions
- Composition may be: workflow templates, multi-step execution, or automatic sequence
- Chaining may be: automatic next step, automatic execution, or automatic progression

**Minimal Injection Unit**:
- Single workflow template that chains capabilities
- Single "Execute workflow" button that runs multiple steps
- Single automatic progression to next step
- Single automatic execution after previous step

**Observable Signals**:
- Multiple actions executed automatically
- Workflow template available
- Automatic progression between steps
- Automatic execution without explicit user request

**Typical Misinterpretation Risk**:
- User may interpret workflow as "system recommendation"
- User may assume workflow is "standard" or "best practice"
- User may treat workflow as "required process"

**Rollback Requirement**:
- Remove workflow composition logic
- Remove automatic chaining
- Remove workflow templates
- Restore single-step execution only

---

## Variable 8: STATEFUL_MEMORY

**variable_id**: `STATEFUL_MEMORY`

**Definition** (Factual):
- System remembers and restores previous state
- Memory may include: last selected option, last entered values, last viewed page, or last used settings
- Memory persists across sessions or page reloads

**Minimal Injection Unit**:
- Single localStorage entry for last selected capability
- Single sessionStorage entry for form values
- Single cookie for user preferences
- Single memory of last viewed page

**Observable Signals**:
- Previous selection restored on page load
- Previous values pre-filled in forms
- Previous page restored on navigation
- Previous settings applied automatically

**Typical Misinterpretation Risk**:
- User may interpret restored state as "system recommendation"
- User may assume restored state is "default" or "preferred"
- User may not realize state was remembered vs. user-selected

**Rollback Requirement**:
- Remove state persistence logic
- Remove localStorage/sessionStorage usage
- Remove cookie usage
- Restore stateless behavior

---

## Variable 9: RECENT_OR_FREQUENT

**variable_id**: `RECENT_OR_FREQUENT`

**Definition** (Factual):
- System tracks and displays recently used or frequently used options
- Tracking may be: usage count, last used timestamp, or frequency calculation
- Display may be: separate section, highlighted items, or sorted list

**Minimal Injection Unit**:
- Single "Recently Used" section
- Single "Frequently Used" section
- Single usage counter displayed
- Single "Last Used" timestamp displayed

**Observable Signals**:
- Options appear in "Recently Used" section
- Options appear in "Frequently Used" section
- Options have usage count badges
- Options have "Last Used" timestamps

**Typical Misinterpretation Risk**:
- User may interpret recent/frequent as "system recommendation"
- User may assume recent/frequent options are "preferred"
- User may treat usage tracking as "suggestion to use again"

**Rollback Requirement**:
- Remove usage tracking logic
- Remove "Recently Used" section
- Remove "Frequently Used" section
- Remove usage count displays

---

## Variable 10: AUTO_RETRY_OR_BACKOFF

**variable_id**: `AUTO_RETRY_OR_BACKOFF`

**Definition** (Factual):
- System automatically retries failed requests
- Retry may be: immediate retry, delayed retry, or exponential backoff
- Retry occurs without explicit user action

**Minimal Injection Unit**:
- Single automatic retry on error
- Single automatic retry on timeout
- Single exponential backoff retry mechanism
- Single retry with increasing delay

**Observable Signals**:
- Request retried automatically after failure
- Retry occurs without user clicking retry button
- Retry delay increases with each attempt
- Retry count displayed or logged

**Typical Misinterpretation Risk**:
- User may interpret automatic retry as "system handling" or "system optimization"
- User may not realize retry occurred automatically
- User may assume system is "fixing" the error

**Rollback Requirement**:
- Remove automatic retry logic
- Remove exponential backoff
- Restore manual retry only
- Remove retry state tracking

---

## Variable 11: CACHING_OR_FALLBACK

**variable_id**: `CACHING_OR_FALLBACK`

**Definition** (Factual):
- System caches responses or falls back to cached/mock data
- Caching may be: memory cache, localStorage cache, or service worker cache
- Fallback may be: cached data, mock data, or last-known-good state

**Minimal Injection Unit**:
- Single memory cache of API responses
- Single localStorage cache of capability list
- Single fallback to mock data on error
- Single fallback to last-known-good state

**Observable Signals**:
- Responses served from cache
- Cached data displayed instead of fresh data
- Fallback data displayed on error
- Cache hit/miss indicators

**Typical Misinterpretation Risk**:
- User may interpret cached data as "current" data
- User may not realize data is cached vs. fresh
- User may assume fallback is "system handling" the error

**Rollback Requirement**:
- Remove caching logic
- Remove localStorage cache
- Remove memory cache
- Remove fallback mechanisms

---

## Variable 12: ERROR_INTERPRETATION_OR_HINTS

**variable_id**: `ERROR_INTERPRETATION_OR_HINTS`

**Definition** (Factual):
- System interprets errors and provides hints or suggestions
- Interpretation may be: error categorization, error-to-suggestion conversion, or helpful error messages
- Hints may be: suggested fixes, next steps, or alternative actions

**Minimal Injection Unit**:
- Single error message with suggested fix
- Single error categorization with hint
- Single "Try this instead" suggestion
- Single error-to-action conversion

**Observable Signals**:
- Error message includes suggestion
- Error categorized with helpful hint
- Error converted to actionable suggestion
- Error message implies next step

**Typical Misinterpretation Risk**:
- User may interpret error hint as "system recommendation"
- User may assume suggested fix is "correct" or "optimal"
- User may treat error interpretation as "system guidance"

**Rollback Requirement**:
- Remove error interpretation logic
- Remove error-to-suggestion conversion
- Restore verbatim error display
- Remove helpful error messages

---

## Variable Summary

**Total Variables**: 12

**Variable IDs**:
1. DEFAULT_SELECTION
2. PREFILL
3. VISUAL_SALIENCE
4. ORDERING_BIAS
5. GROUPING_OR_CLASSIFICATION
6. RECOMMEND_NEXT_ACTION
7. AUTO_COMPOSE_OR_CHAIN
8. STATEFUL_MEMORY
9. RECENT_OR_FREQUENT
10. AUTO_RETRY_OR_BACKOFF
11. CACHING_OR_FALLBACK
12. ERROR_INTERPRETATION_OR_HINTS

---

## No Recommendations

This taxonomy provides no recommendations.

This taxonomy provides no optimization suggestions.

This taxonomy states only variable definitions.

---

**END OF AGENCY VARIABLE TAXONOMY**

