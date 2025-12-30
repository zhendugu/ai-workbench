# Governance Attack Surface Map

**Document Status**: NON-CANONICAL / ADVERSARIAL-TEST  
**Document Type**: Attack Surface Enumeration  
**Date**: 2026-01-10  
**Work Order**: WO-KC-A-0-ADVERSARIAL-GOVERNANCE-AUDIT-BOOTSTRAP

---

## Purpose

This document enumerates all structurally triggerable rule points in KB-2 governance system.

No evaluation of strength or weakness. Only lists accessible interfaces. Each item maps to specific G-RULE-ID.

---

## Attack Surface 1: Default Selection Introduction

**Rule ID**: G-RULE-001

**Trigger Condition**: Code change introduces selected attribute, checked attribute, defaultChecked property, or equivalent pre-selection state

**Accessible Interface**: 
- HTML attributes: `selected`, `checked`, `defaultChecked`
- JavaScript properties: `element.selected`, `element.checked`, `element.defaultChecked`
- React props: `defaultValue`, `defaultChecked`
- CSS pseudo-classes: `:checked` (if combined with default state)

**Rule Point**: Introduction of default selection mechanism

**Compliance Requirement**: If default selection exists, MUST include canonical disclosure text

---

## Attack Surface 2: Visual Highlighting Introduction

**Rule ID**: G-RULE-002

**Trigger Condition**: Code change introduces CSS class or inline style that creates visual emphasis difference (border > 1px, background color, font-weight > normal, color difference) relative to non-emphasized elements

**Accessible Interface**:
- CSS classes: `.highlight`, `.emphasized`, `.selected`, `.active`, custom classes
- Inline styles: `style="border: 2px solid #000"`, `style="background-color: #yellow"`, `style="font-weight: bold"`
- CSS properties: `border-width`, `background-color`, `font-weight`, `color`, `background`, `box-shadow`
- CSS pseudo-classes: `:focus`, `:hover` (if combined with emphasis)

**Rule Point**: Introduction of visual highlighting mechanism

**Compliance Requirement**: If visual highlighting exists, MUST include canonical disclosure text

---

## Attack Surface 3: Declaration Text Placement

**Rule ID**: G-RULE-003

**Trigger Condition**: Code change places declaration text in tooltip, hover state, secondary UI, collapsed section, or requires user action to view

**Accessible Interface**:
- Tooltip attributes: `title`, `data-tooltip`, tooltip libraries
- Hover states: CSS `:hover` with visibility, JavaScript hover handlers
- Secondary UI: modals, drawers, sidebars, expandable sections
- Collapsed sections: accordions, collapsible divs, hidden-by-default content
- Conditional visibility: `display: none`, `visibility: hidden`, `opacity: 0`, JavaScript show/hide

**Rule Point**: Declaration text visibility location

**Compliance Requirement**: Declaration text MUST be visible without user action in primary UI

---

## Attack Surface 4: Declaration Language Softening

**Rule ID**: G-RULE-004

**Trigger Condition**: Code change contains declaration text with softening words: a bit, slightly, somewhat, might, could, tends to, usually

**Accessible Interface**:
- Declaration text content: any string containing softening words
- Text nodes: HTML text content, JavaScript string literals, template strings
- Dynamic text: JavaScript string concatenation, template rendering

**Rule Point**: Declaration text language content

**Compliance Requirement**: Declaration text MUST use exact canonical language from AGENCY_DISCLOSURE_LANGUAGE.md

---

## Attack Surface 5: Declaration Language Justification

**Rule ID**: G-RULE-005

**Trigger Condition**: Code change contains declaration text with justification words: because, since, to help, for convenience, to guide, to make it easier

**Accessible Interface**:
- Declaration text content: any string containing justification words
- Text nodes: HTML text content, JavaScript string literals, template strings
- Dynamic text: JavaScript string concatenation, template rendering

**Rule Point**: Declaration text language content

**Compliance Requirement**: Declaration text MUST use exact canonical language from AGENCY_DISCLOSURE_LANGUAGE.md

---

## Attack Surface 6: Recommendation Language Introduction

**Rule ID**: G-RULE-006

**Trigger Condition**: Code change contains UI text with recommendation words: recommended, suggested, best, preferred, optimal, ideal, should

**Accessible Interface**:
- UI text content: any string containing recommendation words
- Text nodes: HTML text content, JavaScript string literals, template strings
- Labels: button labels, link text, form labels, headings
- Alt text: image alt attributes, aria-label attributes
- Dynamic text: JavaScript string concatenation, template rendering

**Rule Point**: UI text language content

**Compliance Requirement**: Recommendation language is prohibited, not declared

---

## Attack Surface 7: Rejection Mechanism Disabling

**Rule ID**: G-RULE-007

**Trigger Condition**: Code change introduces pre-selection that cannot be deselected, visual emphasis that cannot be ignored, or agency mechanism that disables functionality upon rejection

**Accessible Interface**:
- Event handlers: `onclick`, `onchange`, `addEventListener` that prevent deselection
- Disabled states: `disabled` attribute, `readonly` attribute
- Conditional logic: JavaScript conditionals that disable functionality on rejection
- CSS pointer-events: `pointer-events: none` that prevents interaction
- Hidden elements: `display: none`, `visibility: hidden` that hide rejection controls

**Rule Point**: Agency mechanism rejection capability

**Compliance Requirement**: Agency mechanism MUST be rejectable per AGENCY_REJECTION_INVARIANTS.md

---

## Attack Surface 8: Sequential Ordering Without Acknowledgment

**Rule ID**: G-RULE-008

**Trigger Condition**: Code change introduces ordered list, menu, or sequential display of options

**Accessible Interface**:
- HTML lists: `<ul>`, `<ol>`, `<li>` elements
- Array rendering: JavaScript `Array.map()`, `Array.forEach()` rendering
- Menu structures: navigation menus, dropdown menus, select options
- Grid layouts: CSS Grid, Flexbox that creates sequential display
- Component rendering: React/Vue/Angular components that render lists

**Rule Point**: Sequential list introduction

**Compliance Requirement**: Sequential lists MUST include acknowledgment: "This list creates position-based attention bias. Items appear in this order."

---

## Attack Surface 9: Spatial Proximity Without Acknowledgment

**Rule ID**: G-RULE-009

**Trigger Condition**: Code change introduces spacing differences (margin, padding) between options, or spatial grouping without explicit acknowledgment

**Accessible Interface**:
- CSS margin: `margin`, `margin-top`, `margin-bottom`, `margin-left`, `margin-right`
- CSS padding: `padding`, `padding-top`, `padding-bottom`, `padding-left`, `padding-right`
- CSS gap: `gap`, `row-gap`, `column-gap` (Flexbox/Grid)
- Layout spacing: Flexbox spacing, Grid spacing, custom spacing classes
- Inline styles: `style="margin: 10px"`, `style="padding: 5px"`

**Rule Point**: Spatial layout with proximity differences

**Compliance Requirement**: Spatial layouts with proximity differences MUST include acknowledgment: "This layout creates proximity-based attention bias. Spacing differences influence attention."

---

## Attack Surface 10: Container Grouping Without Acknowledgment

**Rule ID**: G-RULE-010

**Trigger Condition**: Code change introduces container divs, sections, or groups that partition options without explicit acknowledgment

**Accessible Interface**:
- HTML containers: `<div>`, `<section>`, `<article>`, `<aside>`, custom container elements
- CSS classes: container classes, section classes, group classes
- Component wrappers: React/Vue/Angular wrapper components that create containers
- Semantic HTML: semantic elements that create grouping structure
- Grid/Flexbox containers: CSS Grid containers, Flexbox containers that partition options

**Rule Point**: Container grouping introduction

**Compliance Requirement**: Container groupings MUST include acknowledgment: "This grouping creates classification-based attention bias. Container structure influences perception."

---

## Attack Surface 11: State Memory for Agency

**Rule ID**: G-RULE-011

**Trigger Condition**: Code change introduces localStorage, sessionStorage, cookie, or URL parameter that stores user selection, preference, or history to influence current UI

**Accessible Interface**:
- localStorage API: `localStorage.setItem()`, `localStorage.getItem()`
- sessionStorage API: `sessionStorage.setItem()`, `sessionStorage.getItem()`
- Cookies: `document.cookie`, cookie libraries
- URL parameters: `URLSearchParams`, `window.location.search`, query string parsing
- State management: Redux, Vuex, Zustand that persist user preferences
- Browser storage: IndexedDB, Web SQL (if used for user preferences)

**Rule Point**: State memory introduction for agency

**Compliance Requirement**: State memory for agency is prohibited, not declared

---

## Attack Surface 12: Automatic Execution

**Rule ID**: G-RULE-012

**Trigger Condition**: Code change introduces automatic capability execution, auto-run, or execution triggered without explicit user click/action

**Accessible Interface**:
- Event handlers: `onload`, `onDOMContentLoaded`, `useEffect` with empty dependency array
- Timer functions: `setTimeout()`, `setInterval()` that trigger execution
- Promise chains: automatic promise resolution that triggers execution
- Lifecycle hooks: React `componentDidMount()`, Vue `mounted()`, Angular `ngOnInit()` that trigger execution
- Auto-submit: form auto-submit, automatic API calls without user action

**Rule Point**: Automatic execution introduction

**Compliance Requirement**: Automatic execution is prohibited, not declared

---

## Attack Surface Summary

| Attack Surface ID | Rule ID | Trigger Condition | Accessible Interface |
|-------------------|---------|-------------------|----------------------|
| AS-001 | G-RULE-001 | Default selection introduction | HTML attributes, JavaScript properties, React props |
| AS-002 | G-RULE-002 | Visual highlighting introduction | CSS classes, inline styles, CSS properties |
| AS-003 | G-RULE-003 | Declaration text placement | Tooltip, hover, secondary UI, collapsed sections |
| AS-004 | G-RULE-004 | Declaration language softening | Declaration text content |
| AS-005 | G-RULE-005 | Declaration language justification | Declaration text content |
| AS-006 | G-RULE-006 | Recommendation language introduction | UI text content |
| AS-007 | G-RULE-007 | Rejection mechanism disabling | Event handlers, disabled states, conditional logic |
| AS-008 | G-RULE-008 | Sequential ordering without acknowledgment | HTML lists, array rendering, menu structures |
| AS-009 | G-RULE-009 | Spatial proximity without acknowledgment | CSS margin/padding/gap, layout spacing |
| AS-010 | G-RULE-010 | Container grouping without acknowledgment | HTML containers, component wrappers |
| AS-011 | G-RULE-011 | State memory for agency | localStorage, sessionStorage, cookies, URL parameters |
| AS-012 | G-RULE-012 | Automatic execution | Event handlers, timers, lifecycle hooks |

**Total Attack Surfaces**: 12

---

## No Recommendations

This attack surface map provides no recommendations.

This attack surface map provides no evaluation.

This attack surface map states only accessible interfaces.

---

**END OF GOVERNANCE ATTACK SURFACE MAP**

