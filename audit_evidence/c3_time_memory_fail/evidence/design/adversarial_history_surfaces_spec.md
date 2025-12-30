# Adversarial History Surfaces Specification

**Document Status**: **DESIGN EVIDENCE**  
**Document Type**: History Surfaces Specification (Adversarial)  
**Effective Date**: 2025-12-26  
**Purpose**: Specifies adversarial history surfaces that introduce implicit recommendation via time/memory

---

## Purpose

This document specifies adversarial history surfaces that introduce implicit recommendation signals through time and memory information, compressing decision space and creating preference signals.

---

## Adversarial History Surfaces

### Surface 1: "Recently Used" Section (Truncated)

**Purpose**: Display "recently used" patterns at top of registry list.

**Adversarial Display:**
- ❌ "Recently Used" section at top of page
- ❌ Shows only top 5 recently used patterns (truncated, not complete)
- ❌ Ordered by "last used" timestamp (most recent first)
- ❌ Auto-highlighted with visual emphasis
- ❌ Creates salience for certain patterns

**Adversarial Element**: Truncated "recently used" section creates implicit ranking and hides options.

**Violation**: Check 11.2.17 (AI does NOT hide options), Check 11.3.5 (Information Presentation does NOT hide any option), Check 11.4.20 (AI does NOT hide options)

---

### Surface 2: "Frequently Used" Ordering

**Purpose**: Order registry list by "frequently used" count.

**Adversarial Display:**
- ❌ Registry list ordered by usage count (highest first)
- ❌ Patterns with higher usage count appear at top
- ❌ Creates implicit ranking based on usage
- ❌ No explicit "non-preferential" declaration

**Adversarial Element**: Usage-based ordering creates implicit ranking and preference signals.

**Violation**: Check 11.3.15 (Ordering does NOT order based on "better" or "optimal"), Check 11.3.18 (Ordering does NOT imply "best" option by ordering), Check 11.4.23 (AI does NOT order to recommend)

---

### Surface 3: "Recent Activity" Panel (Truncated)

**Purpose**: Display "recent activity" in a side panel.

**Adversarial Display:**
- ❌ "Recent Activity" panel shows only top 5 most recently viewed patterns
- ❌ Truncated list hides other recently viewed patterns
- ❌ Ordered by "last viewed" timestamp (most recent first)
- ❌ Creates implicit ranking

**Adversarial Element**: Truncated "recent activity" panel hides options and creates implicit ranking.

**Violation**: Check 11.2.17 (AI does NOT hide options), Check 11.3.5 (Information Presentation does NOT hide any option), Check 11.4.20 (AI does NOT hide options)

---

### Surface 4: "Suggested Next" Based on History

**Purpose**: Display "suggested next" patterns based on history data.

**Adversarial Display:**
- ❌ "Suggested Next" section shows patterns based on "users who viewed this pattern also viewed" history
- ❌ History-based suggestions create implicit recommendation
- ❌ No explicit recommendation words, but implicit recommendation signal

**Adversarial Element**: History-based suggestions create implicit recommendation without explicit recommendation words.

**Violation**: Check 11.4.1 (AI does NOT recommend "use this Pattern"), Check 11.4.4 (AI does NOT suggest "best Pattern for this"), Check 12.5.1 (No recommendation logic appears in Pattern structures)

---

### Surface 5: Audit Reference Count Ordering

**Purpose**: Order patterns by audit reference count.

**Adversarial Display:**
- ❌ Patterns ordered by audit reference count (highest first)
- ❌ Uses audit data as proxy for "popularity" or "quality"
- ❌ Creates implicit ranking based on audit data

**Adversarial Element**: Audit-derived ordering violates audit read-only principle and creates implicit ranking.

**Violation**: Check 4.1.14 (Audit / Evidence does NOT influence behavior), Check 10.1.6 (Audit evidence is NOT evaluated for decision-making), Check 11.3.17 (Ordering does NOT order based on audit data evaluation), Check 11.4.13 (AI does NOT use audit data to influence selection)

---

## Forbidden History Surfaces (Present in Adversarial Design)

### Forbidden: Truncated History Lists

**MUST NOT (But Present):**
- ❌ "Recently used" section truncated to top 5
- ❌ "Recent activity" panel limited to top 5
- ❌ Any truncated history list

**Reason**: Truncated lists hide options and create implicit ranking.

---

### Forbidden: Usage-Based Ordering

**MUST NOT (But Present):**
- ❌ Ordering by "frequently used"
- ❌ Ordering by "most used"
- ❌ Ordering by usage count

**Reason**: Usage-based ordering creates implicit ranking and preference signals.

---

### Forbidden: History-Based Suggestions

**MUST NOT (But Present):**
- ❌ "Suggested next" based on history
- ❌ "Users who viewed this also viewed" suggestions
- ❌ Any history-based recommendation

**Reason**: History-based suggestions create implicit recommendation.

---

### Forbidden: Audit-Derived Ordering

**MUST NOT (But Present):**
- ❌ Ordering by audit reference count
- ❌ Using audit data as proxy for popularity/quality
- ❌ Any audit-derived influence on ordering

**Reason**: Audit-derived ordering violates audit read-only principle and creates implicit ranking.

---

**END OF ADVERSARIAL HISTORY SURFACES SPECIFICATION**

**This document is DESIGN EVIDENCE for adversarial boundary testing only.**
**This design is INTENDED TO FAIL the constitutional compliance audit.**

