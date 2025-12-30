# Pattern / Methodology Ontology

**Document Status**: **CANONICAL**  
**Document Type**: Constitutional-Level Ontology Definition  
**Effective Date**: 2025-12-26  
**Precedence**: Compatible with IMMUTABLE_DESIGN_CONSTRAINTS.md

---

## Purpose

This document defines the immutable ontological structure for Pattern and Methodology representation in the system.

**This document exists to:**
- Establish immutable boundaries for Pattern/Methodology representation
- Define allowed element types within Patterns
- Prevent execution, judgment, or automation semantics from entering Pattern/Methodology structures
- Ensure Patterns remain descriptive structures only
- Provide highest-level constraints for all Pattern/Methodology representations

**This document does NOT:**
- Provide implementation solutions
- Give specific business examples
- Authorize new capabilities or features
- Define execution semantics
- Define workflow semantics

---

## Pattern / Methodology Identity Statement

### What a Pattern / Methodology IS

**A Pattern / Methodology is a descriptive structure that represents a reusable approach or method.**

**A Pattern / Methodology:**
- Is a declarative description of a reusable approach
- Contains only descriptive elements
- References capabilities (A2) for informational purposes only
- May be associated with audit evidence (A3) for informational purposes only
- Is external to the core system (A2)

**A Pattern / Methodology provides:**
- Descriptive representation of a reusable approach
- Reference to capabilities that may be used in the approach
- Evidence links to audit records that document the approach
- Structural organization of descriptive elements

### What a Pattern / Methodology IS NOT

**A Pattern / Methodology is NOT:**
- ❌ An execution structure
- ❌ A workflow definition
- ❌ A decision-making mechanism
- ❌ An automation trigger
- ❌ A condition evaluator
- ❌ A success/failure judge
- ❌ A behavioral specification

**A Pattern / Methodology does NOT:**
- ❌ Execute capabilities
- ❌ Trigger actions
- ❌ Evaluate conditions
- ❌ Infer success or failure
- ❌ Encode workflow logic
- ❌ Hardcode methodology into core system
- ❌ Drive runtime behavior

---

## Minimal Set of Allowed Element Types

**The following element types are the minimal set allowed within a Pattern / Methodology:**

1. **Element Type 1: Descriptive Label**
2. **Element Type 2: Capability Reference**
3. **Element Type 3: Evidence Reference**
4. **Element Type 4: Structural Container**

**No other element types are allowed.**

**These are element TYPES, not instances, not steps.**

---

## Element Type Definitions

### Element Type 1: Descriptive Label

**Purpose:**
- Provides a human-readable identifier for the Pattern/Methodology
- Serves as a semantic label for categorization and identification
- Enables human understanding and communication

**Allowed Semantics:**
- ✅ Text string identifier
- ✅ Human-readable name
- ✅ Semantic categorization label
- ✅ Descriptive metadata

**Explicit Forbidden Semantics:**
- ❌ MUST NOT be evaluated for decision-making
- ❌ MUST NOT trigger behavior
- ❌ MUST NOT be interpreted as a condition
- ❌ MUST NOT imply execution requirements
- ❌ MUST NOT encode workflow ordering
- ❌ MUST NOT represent state transitions

---

### Element Type 2: Capability Reference

**Purpose:**
- References a capability (A2) that may be used in the Pattern/Methodology
- Provides informational linkage to system capabilities
- Enables human understanding of which capabilities relate to the Pattern/Methodology

**Allowed Semantics:**
- ✅ Reference identifier to a capability (A2)
- ✅ Informational linkage only
- ✅ Human-readable capability name reference
- ✅ Descriptive association

**Explicit Forbidden Semantics:**
- ❌ MUST NOT execute the referenced capability
- ❌ MUST NOT trigger capability execution
- ❌ MUST NOT evaluate capability conditions
- ❌ MUST NOT infer capability requirements
- ❌ MUST NOT encode capability ordering
- ❌ MUST NOT represent capability workflow
- ❌ MUST NOT imply capability behavior
- ❌ MUST NOT create reverse influence (Capability → Pattern)

**Relationship Constraint:**
- Pattern → Capability: Reference only (one-way)
- Capability → Pattern: Forbidden (no reverse influence)

---

### Element Type 3: Evidence Reference

**Purpose:**
- References audit evidence (A3) that documents the Pattern/Methodology
- Provides informational linkage to audit records
- Enables human review of Pattern/Methodology usage evidence

**Allowed Semantics:**
- ✅ Reference identifier to an audit record (A3)
- ✅ Informational linkage only
- ✅ Human-readable evidence reference
- ✅ Descriptive association

**Explicit Forbidden Semantics:**
- ❌ MUST NOT evaluate audit evidence for decision-making
- ❌ MUST NOT trigger behavior based on audit evidence
- ❌ MUST NOT interpret audit evidence as success/failure
- ❌ MUST NOT use audit evidence for routing or triggering
- ❌ MUST NOT create reverse influence (Audit → Pattern)

**Relationship Constraint:**
- Pattern → Audit: Evidence reference only (one-way)
- Audit → Pattern: Forbidden (no reverse influence)

---

### Element Type 4: Structural Container

**Purpose:**
- Organizes other elements within the Pattern/Methodology
- Provides hierarchical or categorical organization
- Enables structural representation of Pattern/Methodology components

**Allowed Semantics:**
- ✅ Container for other element types
- ✅ Hierarchical organization structure
- ✅ Categorical grouping structure
- ✅ Descriptive organization only

**Explicit Forbidden Semantics:**
- ❌ MUST NOT encode execution order
- ❌ MUST NOT represent workflow sequence
- ❌ MUST NOT imply step ordering
- ❌ MUST NOT encode conditional logic
- ❌ MUST NOT represent state transitions
- ❌ MUST NOT trigger behavior based on structure
- ❌ MUST NOT evaluate structure for decision-making

---

## Explicit One-Way Relationships

### Relationship 1: Pattern → Capability (Reference Only)

**Direction:** Pattern → Capability (one-way only)

**Allowed Semantics:**
- ✅ Pattern may reference a capability (A2) by identifier
- ✅ Reference is informational only
- ✅ Reference enables human understanding of capability association

**Explicit Forbidden Semantics:**
- ❌ MUST NOT execute the referenced capability
- ❌ MUST NOT trigger capability execution
- ❌ MUST NOT evaluate capability conditions
- ❌ MUST NOT create reverse influence (Capability → Pattern)

**Enforcement:**
- Pattern may contain capability references
- Capability MUST NOT contain pattern references
- No bidirectional relationship allowed

---

### Relationship 2: Pattern → Audit (Evidence Only)

**Direction:** Pattern → Audit (one-way only)

**Allowed Semantics:**
- ✅ Pattern may reference an audit record (A3) by identifier
- ✅ Reference is evidence linkage only
- ✅ Reference enables human review of Pattern/Methodology usage

**Explicit Forbidden Semantics:**
- ❌ MUST NOT evaluate audit evidence for decision-making
- ❌ MUST NOT trigger behavior based on audit evidence
- ❌ MUST NOT interpret audit evidence as success/failure
- ❌ MUST NOT create reverse influence (Audit → Pattern)

**Enforcement:**
- Pattern may contain audit references
- Audit MUST NOT contain pattern references
- No bidirectional relationship allowed

---

## Immutable Prohibitions

**The following prohibitions are immutable and apply to all Pattern/Methodology representations:**

### Prohibition 1: MUST NOT Evaluate

**Pattern/Methodology MUST NOT evaluate anything.**

**This means:**
- ❌ MUST NOT evaluate conditions
- ❌ MUST NOT evaluate state
- ❌ MUST NOT evaluate audit data
- ❌ MUST NOT evaluate capability results
- ❌ MUST NOT evaluate success or failure

**Enforcement:**
- No evaluation logic may exist in Pattern/Methodology structures
- No conditional evaluation may be encoded
- No decision-making evaluation may be performed

---

### Prohibition 2: MUST NOT Execute

**Pattern/Methodology MUST NOT execute anything.**

**This means:**
- ❌ MUST NOT execute capabilities
- ❌ MUST NOT trigger actions
- ❌ MUST NOT initiate processes
- ❌ MUST NOT coordinate execution
- ❌ MUST NOT schedule execution

**Enforcement:**
- No execution logic may exist in Pattern/Methodology structures
- No execution triggers may be encoded
- No execution coordination may be performed

---

### Prohibition 3: MUST NOT Infer Success/Failure

**Pattern/Methodology MUST NOT infer success or failure.**

**This means:**
- ❌ MUST NOT interpret state as success or failure
- ❌ MUST NOT interpret audit data as success or failure
- ❌ MUST NOT infer outcomes
- ❌ MUST NOT provide judgment

**Enforcement:**
- No success/failure inference may exist in Pattern/Methodology structures
- No outcome interpretation may be encoded
- No judgment logic may be performed

---

### Prohibition 4: MUST NOT Encode Workflow Logic

**Pattern/Methodology MUST NOT encode workflow logic.**

**This means:**
- ❌ MUST NOT encode step ordering
- ❌ MUST NOT encode sequence logic
- ❌ MUST NOT encode conditional branching
- ❌ MUST NOT encode state transitions
- ❌ MUST NOT encode process flow

**Enforcement:**
- No workflow logic may exist in Pattern/Methodology structures
- No ordering semantics may be encoded
- No process flow may be represented

---

### Prohibition 5: MUST NOT Hardcode Methodology

**Pattern/Methodology MUST NOT hardcode methodology into core system.**

**This means:**
- ❌ MUST NOT be part of core system (A2)
- ❌ MUST NOT be enforced by core system
- ❌ MUST NOT be required by core system
- ❌ MUST NOT be immutable in core system

**Enforcement:**
- Pattern/Methodology MUST remain external to core system
- No methodology may be hardcoded into A2
- No methodology enforcement may exist in core system

---

## Compatibility with IMMUTABLE_DESIGN_CONSTRAINTS.md

**This document is fully compatible with IMMUTABLE_DESIGN_CONSTRAINTS.md.**

**Compatibility Points:**

1. **A2 (Capability Substrate) is the Only Core**
   - Pattern/Methodology references capabilities (A2) but is NOT part of A2
   - Pattern/Methodology remains external to core system
   - Pattern/Methodology does NOT execute capabilities

2. **A1 (Execution/Automation) is NOT a System Goal**
   - Pattern/Methodology does NOT execute anything
   - Pattern/Methodology does NOT trigger automation
   - Pattern/Methodology does NOT coordinate execution

3. **A3 (Audit/Evidence) Never Drives Behavior**
   - Pattern/Methodology references audit (A3) for evidence only
   - Pattern/Methodology does NOT evaluate audit data
   - Pattern/Methodology does NOT trigger behavior based on audit

4. **Auditable ≠ Auto-Judgment**
   - Pattern/Methodology may reference audit evidence
   - Pattern/Methodology does NOT interpret audit evidence
   - Pattern/Methodology does NOT provide automatic judgment

5. **State Existence ≠ State Interpretation**
   - Pattern/Methodology does NOT interpret state
   - Pattern/Methodology does NOT infer success/failure from state
   - Pattern/Methodology does NOT use state for decision-making

6. **MUST NOT Freeze Methodology into Core System**
   - Pattern/Methodology MUST remain external to core system
   - No methodology may be hardcoded into A2
   - No methodology enforcement may exist in core system

---

## Relationship to Existing Phases and Gates

**This document constrains all existing and future Pattern/Methodology representations:**

- **Phase-1**: Pattern/Methodology representations must comply with this ontology
- **Phase-2**: Pattern/Methodology representations must comply with this ontology
- **Phase-3**: Pattern/Methodology representations must comply with this ontology
- **Phase-4**: Pattern/Methodology representations must comply with this ontology
- **Future Phases**: Pattern/Methodology representations must comply with this ontology

- **Gate A**: Pattern/Methodology representations must comply with this ontology
- **Future Gates**: Pattern/Methodology representations must comply with this ontology

**This document does NOT:**
- ❌ Override phase-specific constraints
- ❌ Override gate-specific constraints
- ❌ Override capability-specific constraints
- ❌ Provide implementation guidance

**This document DOES:**
- ✅ Provide highest-level constraints for all Pattern/Methodology representations
- ✅ Ensure Patterns remain descriptive structures only
- ✅ Prevent execution, judgment, or automation semantics

---

## Stop Conditions

**If any of the following appear in Pattern/Methodology representations, STOP:**

1. **Execution Semantics**
   - If execution logic appears → STOP
   - If execution triggers appear → STOP
   - If execution coordination appears → STOP

2. **Condition Semantics**
   - If condition evaluation appears → STOP
   - If conditional logic appears → STOP
   - If decision-making conditions appear → STOP

3. **Judgment Semantics**
   - If success/failure inference appears → STOP
   - If outcome interpretation appears → STOP
   - If judgment logic appears → STOP

4. **Workflow Ordering**
   - If step ordering appears → STOP
   - If sequence logic appears → STOP
   - If process flow appears → STOP

5. **Capability Behavior Implication**
   - If capability execution is implied → STOP
   - If capability triggering is implied → STOP
   - If capability coordination is implied → STOP

---

## Summary

**This document establishes immutable ontological structure for Pattern/Methodology representation.**

**Key Definitions:**
1. Pattern/Methodology is a descriptive structure only
2. Four allowed element types: Descriptive Label, Capability Reference, Evidence Reference, Structural Container
3. One-way relationships: Pattern → Capability (reference only), Pattern → Audit (evidence only)

**Key Prohibitions:**
- MUST NOT evaluate
- MUST NOT execute
- MUST NOT infer success/failure
- MUST NOT encode workflow logic
- MUST NOT hardcode methodology

**Compatibility:**
- Fully compatible with IMMUTABLE_DESIGN_CONSTRAINTS.md
- Constrains all phases and gates
- Ensures Patterns remain external to core system

**Enforcement:**
- All Pattern/Methodology representations MUST comply
- All violations MUST be rejected
- Stop conditions must be checked before any Pattern/Methodology representation is accepted

---

**END OF PATTERN / METHODOLOGY ONTOLOGY**

**This document is CANONICAL and IMMUTABLE.**
**No Pattern/Methodology representation may violate this ontology.**

