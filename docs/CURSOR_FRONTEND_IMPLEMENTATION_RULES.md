# Cursor Frontend Implementation Rules

**Document Status**: DESIGN-GATE / NON-CANONICAL  
**Document Type**: Implementation Rules  
**Date**: 2025-12-27  
**Work Order**: WO-J2-FRONTEND-CONSTRAINT-TRANSLATION-AND-GENERATION-GATE

---

## Purpose

This document defines explicit rules for Cursor when implementing frontend code.

All rules must be verifiable through code audit.

No "best practices". Prohibition list only.

---

## What Cursor MAY Write

### Presentation Code

Cursor MAY write:
- Code that displays capabilities
- Code that displays pattern instances
- Code that displays registry entries
- Code that displays audit records
- Code that displays factual information
- Code that renders UI components
- Code that handles user input
- Code that maps user actions to system operations

### Operation Mapping Code

Cursor MAY write:
- Code that maps human clicks to capability selection
- Code that maps human form input to system operations
- Code that maps human navigation to view changes
- Code that translates between UI and system interfaces

### Explicit Human Action Handling

Cursor MAY write:
- Code that handles button clicks
- Code that handles form submissions
- Code that handles navigation clicks
- Code that handles explicit user selections

---

## What Cursor MUST NOT Write

### Selection Code

Cursor MUST NOT write:
- Code that pre-selects options
- Code that auto-selects based on any criteria
- Code that selects default values
- Code that selects based on usage
- Code that selects based on frequency
- Code that selects based on recency
- Code that selects based on popularity

**Verification**: Search codebase for: `selected`, `defaultSelected`, `preSelect`, `autoSelect`, `selectedByDefault`

### Recommendation Code

Cursor MUST NOT write:
- Code that highlights options
- Code that uses badges or markers
- Code that labels items as "popular", "frequently used", "common", "recommended"
- Code that emphasizes specific options
- Code that suggests options
- Code that recommends actions

**Verification**: Search codebase for: `highlight`, `recommend`, `suggest`, `popular`, `frequent`, `common`, `featured`, `best`

### Default Code

Cursor MUST NOT write:
- Code that provides default selections
- Code that provides default values
- Code that pre-fills form fields
- Code that remembers defaults
- Code that restores defaults

**Verification**: Search codebase for: `default`, `defaultValue`, `preFill`, `remember`, `restore`, `smartDefault`

### Ordering Code

Cursor MUST NOT write:
- Code that orders by usage frequency
- Code that orders by popularity
- Code that orders by recency
- Code that orders by any criteria that implies preference
- Code that sorts results by relevance
- Code that moves items to top based on usage

**Verification**: Search codebase for: `sortBy`, `orderBy`, `frequency`, `popularity`, `recent`, `relevance`, `moveToTop`

### Process Guidance Code

Cursor MUST NOT write:
- Code that creates wizard flows
- Code that creates step-by-step guidance
- Code that creates progress indicators
- Code that suggests next steps
- Code that creates workflow templates
- Code that guides users through processes

**Verification**: Search codebase for: `wizard`, `step`, `progress`, `nextStep`, `workflow`, `template`, `guide`

### State Memory Code

Cursor MUST NOT write:
- Code that remembers previous selections
- Code that tracks usage
- Code that persists state across sessions
- Code that accumulates state over time
- Code that stores user preferences
- Code that stores user behavior
- Code that stores interaction history

**Verification**: Search codebase for: `remember`, `track`, `persist`, `accumulate`, `store`, `localStorage`, `sessionStorage`, `memory`, `history`

### Optimization Code

Cursor MUST NOT write:
- Code that optimizes based on usage
- Code that optimizes based on frequency
- Code that optimizes based on popularity
- Code that optimizes based on history
- Code that adapts based on behavior

**Verification**: Search codebase for: `optimize`, `adapt`, `basedOnUsage`, `basedOnFrequency`, `basedOnPopularity`

### Learning Code

Cursor MUST NOT write:
- Code that learns from user behavior
- Code that learns from usage patterns
- Code that learns from interaction history
- Code that adapts based on learning

**Verification**: Search codebase for: `learn`, `learning`, `adapt`, `basedOnBehavior`, `basedOnPatterns`

### Prediction Code

Cursor MUST NOT write:
- Code that predicts user intent
- Code that predicts next actions
- Code that predicts preferences
- Code that auto-completes based on prediction
- Code that suggests based on prediction

**Verification**: Search codebase for: `predict`, `prediction`, `autoComplete`, `suggest`, `intent`, `nextAction`

### Merging Code

Cursor MUST NOT write:
- Code that merges capabilities
- Code that merges pattern instances
- Code that combines options
- Code that consolidates choices

**Verification**: Search codebase for: `merge`, `combine`, `consolidate`

### Abstraction Code

Cursor MUST NOT write:
- Code that hides options
- Code that simplifies decision space
- Code that creates shortcuts
- Code that uses progressive disclosure
- Code that requires "show more" to reveal options

**Verification**: Search codebase for: `hide`, `simplify`, `shortcut`, `progressiveDisclosure`, `showMore`, `collapse`

### Behavior Inference Code

Cursor MUST NOT write:
- Code that infers user intent
- Code that infers preferences
- Code that infers workflows
- Code that infers relationships

**Verification**: Search codebase for: `infer`, `inference`, `intent`, `preference`, `workflow`

### Decision Space Compression Code

Cursor MUST NOT write:
- Code that reduces available options
- Code that hides options
- Code that limits visible options
- Code that truncates option lists
- Code that filters options by default

**Verification**: Search codebase for: `reduce`, `hide`, `limit`, `truncate`, `filter`, `byDefault`

### Usage-Based Display Code

Cursor MUST NOT write:
- Code that displays "commonly used" lists
- Code that displays "recently used" lists
- Code that tracks usage frequency
- Code that tracks recency
- Code that tracks popularity

**Verification**: Search codebase for: `commonlyUsed`, `recentlyUsed`, `frequentlyUsed`, `usageFrequency`, `recency`, `popularity`

### Template/Shortcut Code

Cursor MUST NOT write:
- Code that creates template buttons
- Code that creates shortcut buttons
- Code that creates "quick access" panels
- Code that creates pre-configured combinations

**Verification**: Search codebase for: `template`, `shortcut`, `quickAccess`, `preConfigured`

### Auto-Complete Code

Cursor MUST NOT write:
- Code that auto-completes input fields
- Code that suggests completions
- Code that ranks suggestions
- Code that pre-highlights suggestions

**Verification**: Search codebase for: `autoComplete`, `suggest`, `completion`, `rank`, `preHighlight`

### Search Ranking Code

Cursor MUST NOT write:
- Code that ranks search results
- Code that orders results by relevance
- Code that orders results by popularity
- Code that highlights top results

**Verification**: Search codebase for: `rank`, `orderBy`, `relevance`, `popularity`, `topResults`

### Category Organization Code

Cursor MUST NOT write:
- Code that organizes by categories with default category
- Code that pre-selects default category
- Code that expands default category

**Verification**: Search codebase for: `category`, `defaultCategory`, `preSelectCategory`, `expandCategory`

### Tab Organization Code

Cursor MUST NOT write:
- Code that organizes content into tabs with default active tab
- Code that pre-selects default tab

**Verification**: Search codebase for: `tab`, `defaultTab`, `activeTab`, `preSelectTab`

### Filter Preset Code

Cursor MUST NOT write:
- Code that creates filter presets
- Code that pre-configures filter combinations
- Code that applies filters by default

**Verification**: Search codebase for: `preset`, `preConfigure`, `filterByDefault`

### State Persistence Code

Cursor MUST NOT write:
- Code that persists expanded/collapsed state
- Code that persists custom ordering
- Code that persists filter selections
- Code that persists navigation state
- Code that persists form field values

**Verification**: Search codebase for: `persist`, `saveState`, `restoreState`, `localStorage`, `sessionStorage`

### Contextual Help Code

Cursor MUST NOT write:
- Code that provides contextual help with action suggestions
- Code that provides contextual help that highlights capabilities
- Code that provides contextual help that recommends options

**Verification**: Search codebase for: `contextualHelp`, `suggestAction`, `highlightCapability`, `recommendOption`

### Progressive Disclosure Code

Cursor MUST NOT write:
- Code that hides options initially
- Code that reveals options progressively
- Code that expands automatically based on behavior

**Verification**: Search codebase for: `hideInitially`, `progressiveDisclosure`, `expandAutomatically`

### Smart Defaults Code

Cursor MUST NOT write:
- Code that pre-fills form fields with "smart" values
- Code that pre-fills based on context
- Code that pre-fills based on history

**Verification**: Search codebase for: `smartDefault`, `preFill`, `basedOnContext`, `basedOnHistory`

### Multi-Step Form Code

Cursor MUST NOT write:
- Code that creates multi-step forms with pre-filled values
- Code that creates multi-step forms with default selections

**Verification**: Search codebase for: `multiStep`, `preFilled`, `defaultSelection`

---

## Code Audit Verification

All rules above can be verified through code search.

**Audit Method**:
1. Search codebase for prohibited keywords
2. Review matches for violations
3. Flag violations for removal

**Violation Detection**:
- Any code matching prohibited patterns is a violation
- Violations are structural and non-repairable
- Only complete removal is permitted

---

## Summary

**What Cursor MAY Write**: Presentation code, operation mapping code, explicit human action handling code

**What Cursor MUST NOT Write**: All mechanisms listed in prohibitions above

**Verification**: All rules are verifiable through code search

**No Best Practices**: This document provides prohibition list only

---

**END OF CURSOR FRONTEND IMPLEMENTATION RULES**

