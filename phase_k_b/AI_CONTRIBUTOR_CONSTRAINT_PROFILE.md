# AI Contributor Constraint Profile

**Document Status**: NON-CANONICAL / DESIGN-BOUNDARY  
**Document Type**: Constraint Profile  
**Date**: 2026-01-10  
**Work Order**: WO-KB-2-AGENCY-GOVERNANCE-ENFORCEMENT-RULES

---

## Purpose

This document defines constraints for AI tools (Cursor, LLMs, code generators) contributing to the codebase.

All constraints are structural. No intent-based constraints. No discretionary allowances.

---

## Constraint Category 1: Prohibited Output Forms

**Constraint ID**: AI-CONSTRAINT-001

**Statement**: AI tools MUST NOT output UX optimization suggestions.

**Forbidden Output Forms**:
- "Consider adding a default selection to improve UX"
- "You might want to highlight the recommended option"
- "To make this more user-friendly, you could..."
- "Best practice would be to..."
- "For better usability..."

**Required Behavior**: AI tools MUST NOT suggest UX improvements, optimizations, or usability enhancements.

**KB Evidence Reference**: KB-0 Constraint 4, Constraint 5 (prohibition of undeclared agency)

---

## Constraint Category 2: Prohibited Refactoring Suggestions

**Constraint ID**: AI-CONSTRAINT-002

**Statement**: AI tools MUST NOT suggest "best practice" refactors that introduce agency.

**Forbidden Output Forms**:
- "Best practice is to add a default value"
- "You should highlight the most common option"
- "Consider sorting by frequency"
- "It's recommended to group similar items"
- "You could improve this by adding a recommendation"

**Required Behavior**: AI tools MUST NOT suggest refactoring that introduces agency mechanisms without declaration.

**KB Evidence Reference**: KB-0 all constraints, KB-1 declared agency patterns

---

## Constraint Category 3: Prohibition of Implicit Defaults

**Constraint ID**: AI-CONSTRAINT-003

**Statement**: AI tools MUST NOT introduce implicit defaults (pre-selected options, pre-filled fields) without declaration.

**Forbidden Output Forms**:
- Code that sets `selected` or `checked` attributes without declaration text
- Code that sets default values in form fields without declaration text
- Code that pre-selects options without declaration text

**Required Behavior**: If AI tool introduces default selection, MUST also include canonical declaration text in primary UI.

**KB Evidence Reference**: G-RULE-001 (prohibition of undeclared default selection), KB-1 PATTERN-DECLARED-DEFAULT-SELECTION

---

## Constraint Category 4: Prohibition of Implicit Highlighting

**Constraint ID**: AI-CONSTRAINT-004

**Statement**: AI tools MUST NOT introduce implicit visual highlighting without declaration.

**Forbidden Output Forms**:
- CSS classes that create visual emphasis without declaration text
- Inline styles that create visual emphasis without declaration text
- Visual differences (border, background, color) without declaration text

**Required Behavior**: If AI tool introduces visual highlighting, MUST also include canonical declaration text in primary UI.

**KB Evidence Reference**: G-RULE-002 (prohibition of undeclared visual highlighting), KB-1 PATTERN-DECLARED-VISUAL-HIGHLIGHT

---

## Constraint Category 5: Required Declaration Language

**Constraint ID**: AI-CONSTRAINT-005

**Statement**: AI tools MUST use exact canonical language from AGENCY_DISCLOSURE_LANGUAGE.md for declarations.

**Required Output Forms**:
- Default selection: "This option is pre-selected. This pre-selection influences attention and choice."
- Visual highlighting: "This element is visually emphasized. This emphasis influences attention and choice."
- Default selection with rejection: "This option is pre-selected. You can change it. This pre-selection influences attention and choice."

**Required Behavior**: AI tools MUST use exact canonical language. No variations, no softening, no justification.

**KB Evidence Reference**: KB-1 AGENCY_DISCLOSURE_LANGUAGE.md

---

## Constraint Category 6: Prohibition of Recommendation Language

**Constraint ID**: AI-CONSTRAINT-006

**Statement**: AI tools MUST NOT output recommendation language (recommended, suggested, best, preferred, optimal).

**Forbidden Output Forms**:
- UI text containing "recommended", "suggested", "best", "preferred", "optimal"
- Code comments containing recommendation language
- Documentation containing recommendation language

**Required Behavior**: AI tools MUST NOT use recommendation words in any output.

**KB Evidence Reference**: G-RULE-006 (prohibition of recommendation language), KB-0 Class 3 (Prohibited Agency)

---

## Constraint Category 7: Allowed Output Forms

**Constraint ID**: AI-CONSTRAINT-007

**Statement**: AI tools MAY output code that follows declared agency patterns from KB-1.

**Allowed Output Forms**:
- Code that implements PATTERN-DECLARED-DEFAULT-SELECTION (with canonical declaration)
- Code that implements PATTERN-DECLARED-VISUAL-HIGHLIGHT (with canonical declaration)
- Code that implements PATTERN-DECLARED-PRE-SELECTION-REJECTION (with canonical declaration)
- Code that is non-agency (no agency mechanisms)

**Required Behavior**: AI tools MUST follow declared agency patterns if introducing agency, or output non-agency code.

**KB Evidence Reference**: KB-1 DECLARED_AGENCY_PATTERN_CATALOG.md

---

## Constraint Summary

| Constraint ID | Category | Statement | KB Evidence |
|---------------|----------|-----------|-------------|
| AI-CONSTRAINT-001 | Prohibited Output | No UX optimization suggestions | KB-0 C4, C5 |
| AI-CONSTRAINT-002 | Prohibited Refactoring | No "best practice" refactors | KB-0 all |
| AI-CONSTRAINT-003 | Prohibited Implicit Defaults | No implicit defaults without declaration | G-RULE-001 |
| AI-CONSTRAINT-004 | Prohibited Implicit Highlighting | No implicit highlighting without declaration | G-RULE-002 |
| AI-CONSTRAINT-005 | Required Declaration Language | Must use canonical language | KB-1 Disclosure Language |
| AI-CONSTRAINT-006 | Prohibited Recommendation Language | No recommendation words | G-RULE-006 |
| AI-CONSTRAINT-007 | Allowed Output Forms | Must follow declared patterns or be non-agency | KB-1 Patterns |

**Total Constraints**: 7

---

## No Recommendations

This constraint profile provides no recommendations.

This constraint profile provides no design advice.

This constraint profile states only structural constraints for AI tools.

---

**END OF AI CONTRIBUTOR CONSTRAINT PROFILE**

