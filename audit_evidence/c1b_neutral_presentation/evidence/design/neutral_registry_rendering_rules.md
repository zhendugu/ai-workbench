# Neutral Registry Rendering Rules

**Document Status**: **DESIGN EVIDENCE**  
**Document Type**: Registry Presentation Rules (Facts Only)  
**Effective Date**: 2025-12-26  
**Purpose**: Describes how registry entries are presented without recommendation signals

---

## Purpose

This document describes the rules for presenting Pattern Registry entries in a strictly neutral manner, ensuring no recommendation signals, decision space compression, or implicit preferences are introduced.

**This document:**
- Describes factual presentation rules only
- Does NOT introduce new constraints
- Does NOT modify existing constraints
- Provides neutral presentation guidelines

**This document does NOT:**
- Provide implementation solutions
- Give business examples
- Define UX or UI patterns
- Authorize new capabilities

---

## Presentation Principles

### Principle 1: Factual Information Only

**Registry entries are presented with factual information only:**
- Pattern identity (pattern_id, pattern_name, pattern_version)
- Registration metadata (registered_at, registered_by)
- Version lineage (parent_version, child_versions) - factual relationships only
- Traceability (source, audit_references) - reference links only
- Descriptive tags (categorization labels only, non-evaluative)

**No evaluative information is presented:**
- No usage statistics
- No adoption counts
- No usage frequency
- No last used timestamps
- No success/failure indicators
- No quality judgments

---

### Principle 2: Neutral Ordering

**If ordering is present, it must be:**
- Explicitly declared as non-preferential
- Mechanically neutral (e.g., lexical by pattern_id)
- Stable and deterministic
- Not based on any evaluative criteria

**Example:**
- Ordering method: "lexical_by_pattern_id"
- Description: "Entries are ordered alphabetically by pattern_id for stable, non-preferential presentation. This ordering is mechanical and does not imply any preference, ranking, or recommendation."
- Non-preferential flag: true

**Forbidden ordering:**
- By adoption count
- By usage frequency
- By last used timestamp
- By version number (implies latest is preferred)
- By any evaluative metric

---

### Principle 3: No Highlighting or Emphasis

**Registry entries are presented without:**
- Highlighting certain entries
- Emphasizing certain entries
- Creating "featured" candidates
- Visual distinctions that imply preference
- Status indicators that suggest preference

**All entries are presented with equal visual weight:**
- No special styling
- No badges or markers that imply preference
- No "recommended" or "featured" labels
- No status indicators (active/inactive) that suggest preference

---

### Principle 4: Neutral Tags Only

**Descriptive tags must be:**
- Non-evaluative
- Categorization labels only
- Symmetrical (no tags that imply preference)
- Factual descriptors only

**Allowed tags:**
- Category labels: "storage", "retrieval", "access-control", "versioning"
- Domain labels: "knowledge-management"
- Functional labels: "document-management"

**Forbidden tags:**
- Evaluative: "commonly-used", "standard-practice", "widely-accepted"
- Comparative: "improved", "enhanced", "better"
- Status with preference: "production-ready", "latest-version"
- Adoption signals: "frequently-adopted", "popular"

---

### Principle 5: No Usage or Adoption Metrics

**Registry entries do NOT display:**
- Usage statistics
- Adoption counts
- Usage frequency
- Last used timestamps
- Success rates
- Failure rates
- Any metric that could influence selection

**Rationale:**
- Usage data is audit/evidence (A3) and must not influence selection
- Adoption metrics create social proof bias
- Usage frequency suggests preference
- Last used timestamps suggest relevance

---

### Principle 6: Version Lineage (Factual Only)

**Version lineage information is presented:**
- As factual relationships only
- Parent-child relationships (factual)
- Sibling relationships (factual)
- No evaluative judgments about versions
- No "latest" or "recommended" version indicators

**Forbidden:**
- "is_latest" flags (implies preference)
- "recommended_version" indicators
- Version quality judgments
- Version comparison semantics

---

### Principle 7: Traceability (Reference Only)

**Traceability information is presented:**
- As reference links only
- Audit references (identifier only, no evaluation)
- Source information (factual only)
- No evaluation of audit evidence
- No interpretation of traceability data

**Forbidden:**
- Evaluation of audit evidence
- Interpretation of traceability data
- Using audit references to suggest preference
- Using traceability to rank or judge patterns

---

## Rendering Rules Summary

**Registry entries are rendered with:**
1. ✅ Factual identity information
2. ✅ Neutral, non-preferential ordering (if any)
3. ✅ Equal visual presentation (no highlighting)
4. ✅ Neutral, non-evaluative tags only
5. ✅ No usage or adoption metrics
6. ✅ Factual version lineage only
7. ✅ Reference-only traceability

**Registry entries are NOT rendered with:**
1. ❌ Usage statistics or adoption metrics
2. ❌ Evaluative tags or labels
3. ❌ Highlighting or emphasis
4. ❌ Ordering that implies ranking
5. ❌ Comparative language
6. ❌ Status indicators that suggest preference
7. ❌ Any mechanism that compresses decision space

---

## Compliance

**This document complies with:**
- HUMAN_DECISION_SELECTION_BOUNDARY.md
- PATTERN_REGISTRY_ONTOLOGY.md
- PATTERN_REGISTRY_LIFECYCLE_RULES.md
- IMMUTABLE_DESIGN_CONSTRAINTS.md

**This document does NOT:**
- Introduce new constraints
- Modify existing constraints
- Provide implementation solutions
- Authorize new capabilities

---

**END OF NEUTRAL REGISTRY RENDERING RULES**

**This document is DESIGN EVIDENCE for audit purposes only.**

