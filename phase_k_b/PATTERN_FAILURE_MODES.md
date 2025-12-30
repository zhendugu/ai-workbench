# Pattern Failure Modes

**Document Status**: NON-CANONICAL / DESIGN-BOUNDARY  
**Document Type**: Failure Mode Analysis  
**Date**: 2026-01-10  
**Work Order**: WO-KB-1-DECLARED-AGENCY-PATTERN-DESIGN

---

## Purpose

This document defines failure modes for declared agency patterns.

Each failure mode describes how a pattern can be misunderstood or misused. Each failure mode cites KA experimental evidence. No design advice. No mitigation strategies.

---

## Pattern 1: Declared Default Selection

### Failure Mode 1.1: Hidden Declaration

**Description**: Declaration text is hidden, placed in secondary UI, or requires user action to view.

**Misunderstanding**: User does not see declaration, treats pre-selection as implicit recommendation.

**Prohibited Agency Form**: Pattern becomes implicit DEFAULT_SELECTION (Class 2 becomes implicit Class 1).

**KA Evidence Reference**: KA-1 DEFAULT_SELECTION experiment  
**Observed Metric**: Misinterpretation rate 20% (without declaration)  
**Citation**: `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Structural Indicator**: Declaration text not visible without user action.

---

### Failure Mode 1.2: Softening Language

**Description**: Declaration text uses softening words (a bit, slightly, somewhat, might, could).

**Misunderstanding**: User interprets softened language as minimizing influence, treats pre-selection as less significant.

**Prohibited Agency Form**: Pattern becomes deceptive by minimizing stated influence.

**KA Evidence Reference**: KA-1 DEFAULT_SELECTION experiment  
**Observed Metric**: Default acceptance rate 60% (significant influence)  
**Citation**: `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Structural Indicator**: Declaration text contains softening words.

---

### Failure Mode 1.3: Justification Language

**Description**: Declaration text includes justification (because, to help, for convenience).

**Misunderstanding**: User interprets justification as recommendation, treats pre-selection as system preference.

**Prohibited Agency Form**: Pattern becomes recommendation by implication.

**KA Evidence Reference**: KA-1 DEFAULT_SELECTION experiment  
**Observed Metric**: Misinterpretation rate 20% (explicit misinterpretation as recommendation)  
**Citation**: `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Structural Indicator**: Declaration text contains justification phrases.

---

### Failure Mode 1.4: Non-Rejectable Implementation

**Description**: Pre-selection cannot be deselected, or deselection disables functionality.

**Misunderstanding**: User cannot reject pre-selection, forced to accept agency.

**Prohibited Agency Form**: Pattern becomes non-optional, violates user autonomy.

**KA Evidence Reference**: KA-1 DEFAULT_SELECTION experiment  
**Observed Metric**: Path offset rate 40% (users who change default)  
**Citation**: `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Structural Indicator**: Pre-selection cannot be deselected, or deselection breaks functionality.

---

## Pattern 2: Declared Visual Highlight

### Failure Mode 2.1: Hidden Declaration

**Description**: Declaration text is hidden, placed in secondary UI, or requires user action to view.

**Misunderstanding**: User does not see declaration, treats visual emphasis as implicit recommendation.

**Prohibited Agency Form**: Pattern becomes implicit VISUAL_HIGHLIGHT (Class 2 becomes implicit Class 1).

**KA Evidence Reference**: KA-2 VISUAL_HIGHLIGHT experiment  
**Observed Metric**: Misinterpretation rate 30% (without declaration)  
**Citation**: `audit_evidence/ka_2_visual_highlight_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Structural Indicator**: Declaration text not visible without user action.

---

### Failure Mode 2.2: Softening Language

**Description**: Declaration text uses softening words (a bit, slightly, somewhat, might, could).

**Misunderstanding**: User interprets softened language as minimizing influence, treats visual emphasis as less significant.

**Prohibited Agency Form**: Pattern becomes deceptive by minimizing stated influence.

**KA Evidence Reference**: KA-2 VISUAL_HIGHLIGHT experiment  
**Observed Metric**: Visual highlight prioritization rate 55% (significant influence)  
**Citation**: `audit_evidence/ka_2_visual_highlight_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Structural Indicator**: Declaration text contains softening words.

---

### Failure Mode 2.3: Justification Language

**Description**: Declaration text includes justification (because, to guide, to help).

**Misunderstanding**: User interprets justification as recommendation, treats visual emphasis as system preference.

**Prohibited Agency Form**: Pattern becomes recommendation by implication.

**KA Evidence Reference**: KA-2 VISUAL_HIGHLIGHT experiment  
**Observed Metric**: Misinterpretation rate 30% (explicit misinterpretation as recommendation)  
**Citation**: `audit_evidence/ka_2_visual_highlight_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Structural Indicator**: Declaration text contains justification phrases.

---

### Failure Mode 2.4: Blocking Visual Emphasis

**Description**: Visual emphasis blocks access to other options, or non-emphasized options are visually de-emphasized.

**Misunderstanding**: User cannot access non-emphasized options, forced to interact with emphasized element.

**Prohibited Agency Form**: Pattern becomes non-optional, violates user autonomy.

**KA Evidence Reference**: KA-2 VISUAL_HIGHLIGHT experiment  
**Observed Metric**: Visual highlight change rate 45% (users who select non-emphasized options)  
**Citation**: `audit_evidence/ka_2_visual_highlight_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Structural Indicator**: Non-emphasized options are visually blocked or de-emphasized.

---

## Pattern 3: Declared Pre-Selection with Rejection

### Failure Mode 3.1: Hidden Change Action

**Description**: Change action is hidden, placed in secondary UI, or requires multiple steps to access.

**Misunderstanding**: User cannot find change action, treats pre-selection as non-rejectable.

**Prohibited Agency Form**: Pattern becomes non-rejectable, violates user autonomy.

**KA Evidence Reference**: KA-1 DEFAULT_SELECTION experiment  
**Observed Metric**: Path offset rate 40% (users who change default)  
**Citation**: `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Structural Indicator**: Change action not visible or accessible without multiple steps.

---

### Failure Mode 3.2: Change Action Disables Functionality

**Description**: Changing pre-selection disables functionality or permanently removes options.

**Misunderstanding**: User avoids changing pre-selection to preserve functionality, forced to accept agency.

**Prohibited Agency Form**: Pattern becomes coercive, violates user autonomy.

**KA Evidence Reference**: KA-1 DEFAULT_SELECTION experiment  
**Observed Metric**: Default acceptance rate 60% (users who accept default)  
**Citation**: `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Structural Indicator**: Changing pre-selection breaks functionality or removes options.

---

### Failure Mode 3.3: Softening Language in Change Statement

**Description**: Change statement uses softening words (might want to, could consider).

**Misunderstanding**: User interprets softened language as minimizing rejection ability, treats pre-selection as preferred.

**Prohibited Agency Form**: Pattern becomes deceptive by minimizing rejection ability.

**KA Evidence Reference**: KA-1 DEFAULT_SELECTION experiment  
**Observed Metric**: Path offset rate 40% (users who change default)  
**Citation**: `audit_evidence/ka_1_default_selection_pass/evidence/design/DRIFT_SIGNAL_ANALYSIS.md`

**Structural Indicator**: Change statement contains softening words.

---

## Failure Mode Summary

| Pattern | Failure Mode | Prohibited Agency Form | KA Evidence |
|---------|--------------|------------------------|-------------|
| Pattern 1 | Hidden Declaration | Implicit DEFAULT_SELECTION | KA-1 (20% misinterpretation) |
| Pattern 1 | Softening Language | Deceptive minimization | KA-1 (60% effect) |
| Pattern 1 | Justification Language | Recommendation by implication | KA-1 (20% misinterpretation) |
| Pattern 1 | Non-Rejectable | Non-optional agency | KA-1 (40% path offset) |
| Pattern 2 | Hidden Declaration | Implicit VISUAL_HIGHLIGHT | KA-2 (30% misinterpretation) |
| Pattern 2 | Softening Language | Deceptive minimization | KA-2 (55% effect) |
| Pattern 2 | Justification Language | Recommendation by implication | KA-2 (30% misinterpretation) |
| Pattern 2 | Blocking Visual Emphasis | Non-optional agency | KA-2 (45% change rate) |
| Pattern 3 | Hidden Change Action | Non-rejectable | KA-1 (40% path offset) |
| Pattern 3 | Change Disables Functionality | Coercive agency | KA-1 (60% acceptance) |
| Pattern 3 | Softening Language in Change | Deceptive minimization | KA-1 (40% path offset) |

**Total Failure Modes**: 11

---

## No Recommendations

This failure mode analysis provides no recommendations.

This failure mode analysis provides no design advice.

This failure mode analysis provides no mitigation strategies.

This failure mode analysis states only observed failure modes and their structural indicators.

---

**END OF PATTERN FAILURE MODES**

