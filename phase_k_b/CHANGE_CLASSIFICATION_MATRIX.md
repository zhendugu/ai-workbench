# Change Classification Matrix

**Document Status**: NON-CANONICAL / DESIGN-BOUNDARY  
**Document Type**: Classification System  
**Date**: 2026-01-10  
**Work Order**: WO-KB-2-AGENCY-GOVERNANCE-ENFORCEMENT-RULES

---

## Purpose

This document classifies code changes into non-agency, declared agency, and prohibited agency categories.

All classification criteria are structural. No intention-based classification. No examples based on intention.

---

## Classification Categories

### Category 1: Non-Agency

**Definition**: Changes that do not introduce any agency mechanism.

**Structural Criteria**:
- No default selection (no selected, checked, defaultChecked attributes)
- No visual highlighting (no border > 1px, background color, font-weight > normal, color difference)
- No sequential ordering change (no array reordering, no position manipulation)
- No spatial proximity change (no margin/padding differences)
- No container grouping (no new container divs/sections that partition options)
- No state memory (no localStorage, sessionStorage, cookies, URL parameters)
- No automatic execution (no auto-run, no execution without explicit user action)
- No recommendation language (no recommended, suggested, best, preferred, optimal)

**Gate Requirement**: Automatic pass (no declaration required)

**Examples of Structural Indicators**:
- Bug fixes that do not change UI structure
- Code refactoring that does not change UI behavior
- Documentation changes
- Backend-only changes
- Styling changes that maintain uniform appearance

---

### Category 2: Declared Agency

**Definition**: Changes that introduce agency mechanisms with explicit declaration.

**Structural Criteria**:
- Contains default selection (selected, checked, defaultChecked) AND contains canonical declaration text
- Contains visual highlighting (border > 1px, background color, font-weight > normal) AND contains canonical declaration text
- Declaration text is visible in primary UI (not in tooltip, hover, secondary UI)
- Declaration text uses exact canonical language from AGENCY_DISCLOSURE_LANGUAGE.md
- Agency mechanism is rejectable (user can deselect, ignore, or change)

**Gate Requirement**: Review gate (declaration verification required)

**Required Declaration Patterns**:
- Default selection: "This option is pre-selected. This pre-selection influences attention and choice."
- Visual highlighting: "This element is visually emphasized. This emphasis influences attention and choice."
- Default selection with rejection: "This option is pre-selected. You can change it. This pre-selection influences attention and choice."

**Examples of Structural Indicators**:
- Code contains selected attribute AND contains declaration text in primary UI
- Code contains CSS class with visual emphasis AND contains declaration text in primary UI
- Declaration text matches canonical templates exactly

---

### Category 3: Prohibited Agency

**Definition**: Changes that introduce prohibited agency mechanisms.

**Structural Criteria**:
- Contains default selection WITHOUT declaration text
- Contains visual highlighting WITHOUT declaration text
- Contains recommendation language (recommended, suggested, best, preferred, optimal)
- Contains state memory for agency (localStorage, sessionStorage, cookies that influence UI)
- Contains automatic execution (auto-run, execution without explicit user action)
- Declaration text is hidden (in tooltip, hover, secondary UI)
- Declaration text uses softening language (a bit, slightly, somewhat, might, could)
- Declaration text uses justification language (because, to help, for convenience)
- Agency mechanism is non-rejectable (cannot be deselected, ignored, or changed)
- Contains sequential ordering change WITHOUT acknowledgment
- Contains spatial proximity change WITHOUT acknowledgment
- Contains container grouping WITHOUT acknowledgment

**Gate Requirement**: Block merge (immediate rejection)

**Examples of Structural Indicators**:
- Code contains selected attribute but no declaration text
- Code contains CSS class with visual emphasis but no declaration text
- Code contains recommendation words in UI text
- Code contains localStorage.setItem for user preferences
- Code contains automatic capability execution
- Declaration text in tooltip or hover state
- Declaration text contains "a bit" or "slightly"
- Declaration text contains "because" or "to help"

---

## Classification Decision Tree

**Step 1**: Does change introduce default selection (selected, checked, defaultChecked)?
- **YES** → Go to Step 2
- **NO** → Go to Step 3

**Step 2**: Does change contain canonical declaration text visible in primary UI?
- **YES** → Go to Step 4 (check rejection mechanism)
- **NO** → Category 3 (Prohibited Agency)

**Step 3**: Does change introduce visual highlighting (border > 1px, background color, font-weight > normal)?
- **YES** → Go to Step 2 (check declaration)
- **NO** → Go to Step 5

**Step 4**: Is agency mechanism rejectable (user can deselect, ignore, or change)?
- **YES** → Category 2 (Declared Agency)
- **NO** → Category 3 (Prohibited Agency)

**Step 5**: Does change contain recommendation language, state memory for agency, or automatic execution?
- **YES** → Category 3 (Prohibited Agency)
- **NO** → Go to Step 6

**Step 6**: Does change introduce sequential ordering change, spatial proximity change, or container grouping?
- **YES** → Category 3 (Prohibited Agency) - acknowledgment required but missing
- **NO** → Category 1 (Non-Agency)

---

## Classification Summary

| Category | Structural Criteria | Gate Requirement | Rule References |
|----------|---------------------|------------------|-----------------|
| Non-Agency | No agency mechanisms | Automatic pass | N/A |
| Declared Agency | Agency with canonical declaration | Review gate | G-RULE-001, G-RULE-002, G-RULE-003, G-RULE-004, G-RULE-005, G-RULE-007 |
| Prohibited Agency | Agency without declaration or prohibited mechanisms | Block merge | All G-RULE-* rules |

---

## No Recommendations

This classification matrix provides no recommendations.

This classification matrix provides no design advice.

This classification matrix states only structural classification criteria.

---

**END OF CHANGE CLASSASSIFICATION MATRIX**

