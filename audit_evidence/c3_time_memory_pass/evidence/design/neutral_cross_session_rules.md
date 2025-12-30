# Neutral Cross-Session Rules

**Document Status**: **DESIGN EVIDENCE**  
**Document Type**: Cross-Session Rules (Neutral)  
**Effective Date**: 2025-12-26  
**Purpose**: Defines neutral cross-session behavior that maintains strict neutrality

---

## Purpose

This document defines the neutral cross-session rules for the system. Cross-session persistence is explicitly forbidden to prevent implicit recommendation signals and decision space compression.

---

## Core Principle: No Cross-Session Persistence of Selections

**Cross-session persistence of selections MUST NOT exist.**

**This means:**
- ✅ No sticky shortlist across sessions
- ✅ No auto-apply last filters/tags across sessions
- ✅ No prefill search/filter based on history
- ✅ No "continue" button that restores previous state
- ✅ No "resume where you left off" that preselects
- ✅ No "recently viewed" persistence
- ✅ No "last used" persistence
- ✅ No "most used" persistence

**This does NOT mean:**
- ❌ Audit records cannot persist (audit is read-only, passive)
- ❌ Pattern Registry cannot persist (registry is descriptive, not behavioral)

---

## Forbidden Cross-Session Behaviors

### Forbidden: Sticky Shortlist Across Sessions

**MUST NOT:**
- ❌ Pre-populate shortlist with items from previous session
- ❌ Auto-add items to shortlist based on previous session
- ❌ Persist shortlist state across sessions
- ❌ Create "continue with previous shortlist" functionality

**Reason**: Sticky shortlist creates implicit "continue" recommendation and compresses decision space.

---

### Forbidden: Auto-Apply Last Filters/Tags Across Sessions

**MUST NOT:**
- ❌ Auto-apply last filters from previous session
- ❌ Auto-apply last tags from previous session
- ❌ Prefill search query from previous session
- ❌ Persist filter state across sessions

**Reason**: Auto-applied filters create implicit preference and compress decision space.

---

### Forbidden: "Continue" / "Resume" Shortcuts

**MUST NOT:**
- ❌ "Continue" button that bypasses selection
- ❌ "Resume where you left off" that preselects
- ❌ "Continue" button that auto-navigates to specific pattern
- ❌ Any shortcut that restores previous session state

**Reason**: "Continue" shortcuts create implicit recommendation and compress decision space.

---

### Forbidden: "Recently Viewed" Persistence

**MUST NOT:**
- ❌ Persist "recently viewed" across sessions
- ❌ Create "recently viewed" section based on previous sessions
- ❌ Track view history across sessions
- ❌ Display "recently viewed" from previous sessions

**Reason**: "Recently viewed" persistence creates implicit ranking and compresses decision space.

---

### Forbidden: "Last Used" / "Most Used" Persistence

**MUST NOT:**
- ❌ Persist "last used" across sessions
- ❌ Persist "most used" across sessions
- ❌ Track usage statistics across sessions
- ❌ Display usage-based ordering from previous sessions

**Reason**: Usage-based persistence creates implicit ranking and compresses decision space.

---

## Allowed Cross-Session Behaviors

### Allowed: Audit Record Persistence (Read-Only)

**Audit records may persist across sessions:**
- ✅ Event records (read-only, passive)
- ✅ State snapshots (read-only, passive)
- ✅ Temporal markers (read-only, passive)
- ✅ Source references (read-only, passive)

**Constraints:**
- Read-only access only
- No behavior influence
- No selection influence
- No evaluation or judgment

---

### Allowed: Pattern Registry Persistence (Descriptive)

**Pattern Registry may persist across sessions:**
- ✅ Registry entries (descriptive, not behavioral)
- ✅ Version lineage (factual relationships only)
- ✅ Traceability information (factual references only)

**Constraints:**
- Descriptive only
- No selection authority
- No judgment authority
- No evolution authority

---

## Neutrality Guarantees

**This Policy Guarantees:**
- ✅ No cross-session persistence of selections
- ✅ No sticky shortlist across sessions
- ✅ No auto-apply last filters/tags across sessions
- ✅ No "continue" / "resume" shortcuts
- ✅ No "recently viewed" persistence
- ✅ No "last used" / "most used" persistence
- ✅ All cross-session data is read-only (audit) or descriptive (registry)
- ✅ All cross-session data does not influence behavior

---

**END OF NEUTRAL CROSS-SESSION RULES**

**This document is DESIGN EVIDENCE for boundary testing only.**

