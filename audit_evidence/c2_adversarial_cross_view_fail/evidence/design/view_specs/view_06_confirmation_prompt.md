# View 06: Confirmation Prompt (Adversarial)

**Document Status**: **DESIGN EVIDENCE**  
**Document Type**: View Specification (Adversarial)  
**Effective Date**: 2025-12-26  
**Purpose**: Specifies an adversarial confirmation prompt view

---

## View Purpose

Displays a confirmation prompt. This view includes adversarial mechanisms that auto-navigate to specific patterns.

---

## Display Rules

### Prompt Content

**Required Elements:**
- ✅ Clear statement: "Please select a pattern"
- ✅ Boundary reminder: "Presentation ≠ Recommendation"

**BUT: "Continue" Button (Adversarial):**
- ❌ "Continue" button present
- ❌ Auto-navigates to pattern-doc-storage-001 detail page (View 02)
- ❌ Based on "last viewed pattern" from previous session
- ❌ This creates implicit "continue where you left off" recommendation

**Adversarial Element**: "Continue" button auto-navigates to specific pattern, creating implicit recommendation.

### Option Display

**All Options:**
- ✅ Equal visual weight
- ✅ Same styling
- ✅ Same spacing

**BUT: "Continue" Button Emphasis:**
- ❌ "Continue" button has visual emphasis (larger, highlighted)
- ❌ Creates salience for auto-navigation option
- ❌ This compresses decision space by emphasizing one path

**Adversarial Element**: Visual emphasis on "Continue" button creates implicit preference.

---

## Interaction Rules

### User Actions

**Allowed:**
- ✅ Explicit selection of pattern (required)
- ✅ Cancel/back (explicit user action)
- ✅ Click "Continue" button (auto-navigates to pattern-doc-storage-001)

**Adversarial:**
- ❌ "Continue" button auto-navigates to specific pattern
- ❌ Auto-navigation based on "previous session" data
- ❌ Creates implicit "continue where you left off" recommendation

---

## Adversarial Mechanisms

**Mechanism 1: "Continue" CTA Auto-Navigation**
- Violation: "Continue" button auto-navigates to pattern-doc-storage-001
- Violation: Based on "last viewed pattern" from previous session
- Violation: Creates implicit "continue where you left off" recommendation
- Check Violated: Check 11.2.18 (AI does NOT pre-select options), Check 11.4.21 (AI does NOT pre-select options)

**Mechanism 2: Visual Emphasis on "Continue" Button**
- Violation: "Continue" button has visual emphasis (larger, highlighted)
- Violation: Creates salience for auto-navigation option
- Check Violated: Check 11.3.6 (Information Presentation does NOT imply preference for any option)

---

**END OF VIEW 06 SPECIFICATION (ADVERSARIAL)**

