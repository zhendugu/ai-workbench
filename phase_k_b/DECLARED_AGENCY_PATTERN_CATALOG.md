# Declared Agency Pattern Catalog

**Document Status**: NON-CANONICAL / DESIGN-BOUNDARY  
**Document Type**: Pattern Specification  
**Date**: 2026-01-10  
**Work Order**: WO-KB-1-DECLARED-AGENCY-PATTERN-DESIGN

---

## Purpose

This document defines declared-agency patterns that explicitly acknowledge agency instead of hiding it.

All patterns map to Class 2: Declared Agency mechanisms from KB-0. All patterns cite KA experimental evidence. No implicit influence. No neutrality claims. No optimization.

---

## Pattern 1: Declared Default Selection

**Pattern ID**: PATTERN-DECLARED-DEFAULT-SELECTION

**Base Mechanism**: DEFAULT_SELECTION (Class 2: Declared Agency)

**KA Evidence Reference**: KA-1 DEFAULT_SELECTION experiment  
**Evidence File**: `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`  
**Observed Metric**: Default acceptance rate 60%, misinterpretation rate 20%

---

### Declared Agency Statement

**Exact Text**: "This option is pre-selected. This pre-selection influences attention and choice."

**Language Characteristics**:
- Factual statement of pre-selection state
- Explicit statement of influence on attention
- Explicit statement of influence on choice
- No justification
- No recommendation tone
- No persuasion

---

### UI Mechanism

**Structural Components**:
1. Pre-selected option visually indicated (border, background, or equivalent)
2. Disclosure text displayed adjacent to pre-selected option
3. Disclosure text uses exact canonical language from AGENCY_DISCLOSURE_LANGUAGE.md
4. Disclosure text is visible without user action (not hidden in tooltip or secondary UI)

**Visual Requirements**:
- Pre-selected state must be visually distinct
- Disclosure text must be legible and visible
- No additional visual emphasis beyond pre-selection indication

---

### User Rejection Mechanism

**Rejection Method**: User can deselect pre-selected option

**Rejection Invariant**: After deselection, system continues to function. All options remain available. No option is permanently disabled. No functionality is lost.

**Rejection Visibility**: Rejection action is explicit and visible. User action (click, tap, or equivalent) changes pre-selected state to unselected state.

---

### KA Evidence Reference

**Experiment**: KA-1 DEFAULT_SELECTION  
**Effect Strength**: 60% (default acceptance rate)  
**Misinterpretation Rate**: 20% (explicit misinterpretation as recommendation)

**Pattern Design Justification**: Declaration reduces misinterpretation risk by explicitly stating pre-selection state and influence. Misinterpretation rate without declaration: 20%. Pattern requires explicit declaration to reduce misinterpretation risk.

**Citation**: `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

---

## Pattern 2: Declared Visual Highlight

**Pattern ID**: PATTERN-DECLARED-VISUAL-HIGHLIGHT

**Base Mechanism**: VISUAL_HIGHLIGHT (Class 2: Declared Agency)

**KA Evidence Reference**: KA-2 VISUAL_HIGHLIGHT experiment  
**Evidence File**: `audit_evidence/ka_2_visual_highlight_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`  
**Observed Metric**: Visual highlight prioritization rate 55%, misinterpretation rate 30%

---

### Declared Agency Statement

**Exact Text**: "This element is visually emphasized. This emphasis influences attention and choice."

**Language Characteristics**:
- Factual statement of visual emphasis
- Explicit statement of influence on attention
- Explicit statement of influence on choice
- No justification
- No recommendation tone
- No persuasion

---

### UI Mechanism

**Structural Components**:
1. Visually emphasized element (border, background, font weight, or equivalent)
2. Disclosure text displayed adjacent to emphasized element
3. Disclosure text uses exact canonical language from AGENCY_DISCLOSURE_LANGUAGE.md
4. Disclosure text is visible without user action (not hidden in tooltip or secondary UI)

**Visual Requirements**:
- Visual emphasis must be visually distinct
- Disclosure text must be legible and visible
- Visual emphasis is explicitly declared, not implied

---

### User Rejection Mechanism

**Rejection Method**: User can dismiss visual emphasis or ignore emphasized element

**Rejection Invariant**: After rejection, system continues to function. All options remain available. No option is permanently disabled. Visual emphasis does not block access to other options. No functionality is lost.

**Rejection Visibility**: Rejection is implicit through user choice to ignore emphasized element. User can select non-emphasized options without additional steps.

---

### KA Evidence Reference

**Experiment**: KA-2 VISUAL_HIGHLIGHT  
**Effect Strength**: 55% (visual highlight prioritization rate)  
**Misinterpretation Rate**: 30% (explicit misinterpretation as recommendation)

**Pattern Design Justification**: Declaration reduces misinterpretation risk by explicitly stating visual emphasis and influence. Misinterpretation rate without declaration: 30%. Pattern requires explicit declaration to reduce misinterpretation risk.

**Citation**: `audit_evidence/ka_2_visual_highlight_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

---

## Pattern 3: Declared Pre-Selection with Rejection

**Pattern ID**: PATTERN-DECLARED-PRE-SELECTION-REJECTION

**Base Mechanism**: DEFAULT_SELECTION (Class 2: Declared Agency) with explicit rejection path

**KA Evidence Reference**: KA-1 DEFAULT_SELECTION experiment  
**Evidence File**: `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`  
**Observed Metric**: Default acceptance rate 60%, path offset rate 40%

---

### Declared Agency Statement

**Exact Text**: "This option is pre-selected. You can change it. This pre-selection influences attention and choice."

**Language Characteristics**:
- Factual statement of pre-selection state
- Explicit statement of user ability to change
- Explicit statement of influence on attention
- Explicit statement of influence on choice
- No justification
- No recommendation tone
- No persuasion

---

### UI Mechanism

**Structural Components**:
1. Pre-selected option visually indicated
2. Disclosure text displayed adjacent to pre-selected option
3. Disclosure text includes explicit "You can change it" statement
4. Change action is visible and accessible (button, link, or equivalent)
5. Disclosure text uses exact canonical language from AGENCY_DISCLOSURE_LANGUAGE.md

**Visual Requirements**:
- Pre-selected state must be visually distinct
- Disclosure text must be legible and visible
- Change action must be visible and accessible
- No additional visual emphasis beyond pre-selection indication

---

### User Rejection Mechanism

**Rejection Method**: User can explicitly change pre-selected option via visible change action

**Rejection Invariant**: After change, system continues to function. All options remain available. New selection is treated identically to original pre-selection. No option is permanently disabled. No functionality is lost.

**Rejection Visibility**: Rejection action is explicit and visible. User action (click, tap, or equivalent) changes pre-selected state to user-selected state.

---

### KA Evidence Reference

**Experiment**: KA-1 DEFAULT_SELECTION  
**Effect Strength**: 60% (default acceptance rate)  
**Path Offset Rate**: 40% (users who changed default)

**Pattern Design Justification**: Declaration with explicit rejection path acknowledges that 40% of users change defaults. Pattern provides explicit rejection mechanism to support user autonomy.

**Citation**: `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

---

## Pattern Summary

| Pattern ID | Base Mechanism | Declaration Type | Rejection Type |
|------------|----------------|------------------|----------------|
| PATTERN-DECLARED-DEFAULT-SELECTION | DEFAULT_SELECTION | Pre-selection state + influence | Implicit (deselect) |
| PATTERN-DECLARED-VISUAL-HIGHLIGHT | VISUAL_HIGHLIGHT | Visual emphasis + influence | Implicit (ignore) |
| PATTERN-DECLARED-PRE-SELECTION-REJECTION | DEFAULT_SELECTION | Pre-selection state + change ability + influence | Explicit (change action) |

**Total Patterns**: 3

---

## No Recommendations

This catalog provides no recommendations.

This catalog provides no design advice.

This catalog provides no optimization strategies.

This catalog states only pattern specifications.

---

**END OF DECLARED AGENCY PATTERN CATALOG**

