# View 05: Shortlist (Adversarial)

**Document Status**: **DESIGN EVIDENCE**  
**Document Type**: View Specification (Adversarial)  
**Effective Date**: 2025-12-26  
**Purpose**: Specifies an adversarial shortlist view

---

## View Purpose

Displays user's shortlist of Pattern Instances. This view includes adversarial mechanisms that pre-populate the shortlist.

---

## Display Rules

### Shortlist Contents (Adversarial)

**Initial State (Adversarial):**
- ❌ Pre-populated with 2 items from "previous session"
- ❌ Items: pattern-doc-storage-001, pattern-doc-retrieval-001
- ❌ Auto-added items marked with "from previous session" label
- ❌ User can remove items, but initial state is pre-populated
- ❌ This creates implicit recommendation to continue with these patterns

**Adversarial Element**: Pre-populated shortlist creates implicit "continue where you left off" recommendation.

### Item Display

**Per Item:**
- pattern_id
- pattern_name
- pattern_version
- Added timestamp (when user added it OR "from previous session")
- "from previous session" label (for auto-added items)

**Ordering (Adversarial):**
- ❌ Ordered by "last viewed" timestamp (not lexical)
- ❌ Most recently viewed items appear first
- ❌ No explicit "non-preferential" declaration
- ❌ This creates implicit ranking

**Adversarial Element**: Ordering by timestamp creates implicit ranking.

---

## Interaction Rules

### User Actions

**Allowed:**
- ✅ Add item to shortlist (explicit user action)
- ✅ Remove item from shortlist (explicit user action)
- ✅ Clear shortlist (explicit user action)

**Adversarial:**
- ❌ Shortlist pre-populated with items from "previous session"
- ❌ Auto-added items create implicit recommendation
- ❌ Ordering by timestamp creates implicit ranking

---

## State Persistence (Adversarial)

**Cross-Session Persistence (Adversarial):**
- ❌ Shortlist persists across sessions
- ❌ Auto-restored from previous session
- ❌ Creates "continue where you left off" functionality

**Adversarial Element**: Cross-session persistence creates implicit recommendation.

---

## Adversarial Mechanisms

**Mechanism 1: Sticky Shortlist Seeded by Previous Session**
- Violation: Pre-populated with items from "previous session"
- Violation: Auto-added items create implicit recommendation
- Check Violated: Check 11.1.7 (Human Selection is NOT automatic selection), Check 11.2.18 (AI does NOT pre-select options)

**Mechanism 2: Ordering by Timestamp**
- Violation: Ordered by "last viewed" timestamp (not lexical)
- Violation: No explicit "non-preferential" declaration
- Check Violated: Check 11.3.18 (Ordering does NOT imply "best" option by ordering)

**Mechanism 3: Cross-Session Persistence**
- Violation: Shortlist persists across sessions
- Violation: Creates "continue where you left off" functionality
- Check Violated: Check 11.2.18 (AI does NOT pre-select options), Check 11.4.21 (AI does NOT pre-select options)

---

**END OF VIEW 05 SPECIFICATION (ADVERSARIAL)**

