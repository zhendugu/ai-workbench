# Time & Memory Policy - Adversarial

**Document Status**: **DESIGN EVIDENCE**  
**Document Type**: Time & Memory Policy (Adversarial)  
**Effective Date**: 2025-12-26  
**Purpose**: Describes adversarial time and memory mechanisms that introduce implicit recommendation via history/session/audit

---

## Purpose

This document describes adversarial time and memory mechanisms that introduce implicit recommendation signals through history, session, and audit data. These mechanisms are designed to FAIL the constitutional compliance audit.

---

## Adversarial Mechanisms

### Mechanism 1: Preselect Last Used Pattern Version as Default

**Description**: When a user views a Pattern Instance, the system preselects the last used version as the default selection.

**Adversarial Element**: Default selection based on "last used" timestamp creates implicit "continue with last choice" recommendation.

**Violation**: Check 11.2.11 (Default selection is FORBIDDEN), Check 11.3.28 (Default Selection is FORBIDDEN)

---

### Mechanism 2: Auto-Highlight "Recently Used"

**Description**: The system auto-highlights patterns that were "recently used" (within last 7 days) in the registry list view.

**Adversarial Element**: Visual emphasis on "recently used" patterns creates implicit ranking and preference signals.

**Violation**: Check 11.3.6 (Information Presentation does NOT imply preference for any option), Check 11.4.24 (AI does NOT highlight to recommend)

---

### Mechanism 3: "Continue" Button Bypassing Selection View

**Description**: A "Continue" button appears that auto-navigates to the last viewed pattern detail page, bypassing the selection view.

**Adversarial Element**: "Continue" button creates implicit "continue where you left off" recommendation and compresses decision space.

**Violation**: Check 11.2.18 (AI does NOT pre-select options), Check 11.2.21 (AI does NOT influence human selection), Check 11.4.21 (AI does NOT pre-select options)

---

### Mechanism 4: Auto-Apply Last Filters/Tags Across Sessions

**Description**: The system auto-applies the last used filters/tags from the previous session when the user opens the search/filter view.

**Adversarial Element**: Auto-applied filters create implicit preference and compress decision space.

**Violation**: Check 11.2.11 (Default selection is FORBIDDEN), Check 11.3.28 (Default Selection is FORBIDDEN), Check 11.4.9 (AI does NOT judge any option as "default")

---

### Mechanism 5: "Frequently Used" Ordering

**Description**: The registry list is ordered by "frequently used" count (patterns with higher usage count appear first).

**Adversarial Element**: Usage-based ordering creates implicit ranking and preference signals.

**Violation**: Check 11.3.15 (Ordering does NOT order based on "better" or "optimal"), Check 11.3.18 (Ordering does NOT imply "best" option by ordering), Check 11.4.23 (AI does NOT order to recommend)

---

### Mechanism 6: "Recent Activity" Panel Limited to Top N

**Description**: A "Recent Activity" panel shows only the top 5 most recently viewed patterns, truncating the list.

**Adversarial Element**: Truncated "recent activity" list hides options and creates implicit ranking.

**Violation**: Check 11.2.17 (AI does NOT hide options), Check 11.3.5 (Information Presentation does NOT hide any option), Check 11.4.20 (AI does NOT hide options)

---

### Mechanism 7: "Suggested Next" Based on History

**Description**: A "Suggested Next" section appears that shows patterns based on "users who viewed this pattern also viewed" history data.

**Adversarial Element**: History-based suggestions create implicit recommendation without explicit recommendation words.

**Violation**: Check 11.4.1 (AI does NOT recommend "use this Pattern"), Check 11.4.4 (AI does NOT suggest "best Pattern for this"), Check 12.5.1 (No recommendation logic appears in Pattern structures)

---

### Mechanism 8: Session Persistence of Shortlist with Sticky Ranking

**Description**: The shortlist persists across sessions, and items are ranked by "last added" timestamp (most recently added items appear first).

**Adversarial Element**: Sticky shortlist with timestamp-based ranking creates implicit "continue with previous shortlist" recommendation and ranking.

**Violation**: Check 11.1.7 (Human Selection is NOT automatic selection), Check 11.2.18 (AI does NOT pre-select options), Check 11.3.18 (Ordering does NOT imply "best" option by ordering)

---

### Mechanism 9: Using Audit Reference Count as Proxy Signal in Ordering

**Description**: Patterns are ordered by audit reference count (patterns with more audit references appear first), using audit data as a proxy for "popularity" or "quality".

**Adversarial Element**: Audit-derived ordering creates implicit ranking and violates audit read-only principle.

**Violation**: Check 4.1.14 (Audit / Evidence does NOT influence behavior), Check 10.1.6 (Audit evidence is NOT evaluated for decision-making), Check 11.3.17 (Ordering does NOT order based on audit data evaluation), Check 11.4.13 (AI does NOT use audit data to influence selection)

---

### Mechanism 10: "Resume Where You Left Off" Skipping Neutral Presentation

**Description**: A "Resume" button appears that auto-navigates to the last viewed pattern detail page, skipping the neutral registry list presentation.

**Adversarial Element**: "Resume" functionality creates implicit "continue where you left off" recommendation and compresses decision space.

**Violation**: Check 11.2.18 (AI does NOT pre-select options), Check 11.2.21 (AI does NOT influence human selection), Check 11.4.21 (AI does NOT pre-select options), Check 7.1.11 (Pattern Registry is NOT a decision-making mechanism)

---

## Decision Space Compression Analysis

**Compression Mechanisms:**
1. Default-to-last-choice → Preselects last used version
2. Auto-highlight "recently used" → Creates salience for certain patterns
3. "Continue" button → Bypasses selection, auto-navigates
4. Auto-apply last filters → Pre-selects certain patterns
5. "Frequently used" ordering → Creates implicit ranking
6. "Recent activity" truncated → Hides options, creates ranking
7. "Suggested next" based on history → Creates implicit recommendation
8. Sticky shortlist with ranking → Pre-selects and ranks items
9. Audit reference count ordering → Uses audit data to influence selection
10. "Resume" functionality → Skips neutral presentation, auto-navigates

**Result**: Decision space is compressed through multiple time/memory-based mechanisms, creating emergent recommendation signals without explicit recommendation words.

---

**END OF TIME & MEMORY POLICY (ADVERSARIAL)**

**This document is DESIGN EVIDENCE for adversarial boundary testing only.**
**This design is INTENDED TO FAIL the constitutional compliance audit.**

