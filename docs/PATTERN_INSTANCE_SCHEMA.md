# Pattern Instance Schema

**Document Status**: **CANONICAL**  
**Document Type**: Instance Schema Definition  
**Effective Date**: 2025-12-26  
**Precedence**: Constrained by PATTERN_METHODOLOGY_ONTOLOGY.md, IMMUTABLE_DESIGN_CONSTRAINTS.md, CAPABILITY_ONTOLOGY.md, AUDIT_EVIDENCE_ONTOLOGY.md, and AUTHORIZATION_GOVERNANCE_ONTOLOGY.md

---

## Purpose

This document defines the canonical, instance-level schema for Pattern/Methodology usage.

**This document defines:**
- WHAT a Pattern instance may contain (fields and structure)
- Allowed field types and semantics
- Forbidden field types and semantics
- Instance-level constraints

**This document does NOT define:**
- ❌ How Pattern instances are executed
- ❌ How Pattern instances are evaluated
- ❌ How Pattern instances are interpreted
- ❌ How Pattern instances trigger anything
- ❌ Implementation details
- ❌ Business examples

---

## Schema Scope

**This schema applies to:**
- All Pattern/Methodology instances
- All Pattern/Methodology representations
- All Pattern/Methodology storage formats

**This schema is constrained by:**
- PATTERN_METHODOLOGY_ONTOLOGY.md (ontological structure)
- IMMUTABLE_DESIGN_CONSTRAINTS.md (design constraints)
- CAPABILITY_ONTOLOGY.md (capability reference constraints)
- AUDIT_EVIDENCE_ONTOLOGY.md (audit reference constraints)
- AUTHORIZATION_GOVERNANCE_ONTOLOGY.md (authorization constraints)

---

## Pattern Instance Identity

### What a Pattern Instance IS

**A Pattern Instance is a concrete, external, replaceable, versionable representation of a Pattern/Methodology.**

**A Pattern Instance:**
- Is a concrete instance of a Pattern/Methodology
- Is purely descriptive
- Is human-readable and auditable
- Is externally replaceable and versionable
- Remains outside A2 core
- Contains only allowed fields

### What a Pattern Instance IS NOT

**A Pattern Instance is NOT:**
- ❌ An execution structure
- ❌ A workflow definition
- ❌ A decision-making mechanism
- ❌ An automation trigger
- ❌ Part of A2 core
- ❌ Immutable in core system

---

## Minimal Required Fields

**Every Pattern Instance MUST contain the following fields:**

1. **pattern_id** (required)
2. **pattern_name** (required)
3. **pattern_version** (required)
4. **created_at** (required)
5. **created_by** (required)

**No Pattern Instance may exist without these fields.**

---

## Allowed Fields

**The following fields are allowed in a Pattern Instance:**

### Field 1: pattern_id

**Type**: String (unique identifier)

**Purpose:**
- Provides a unique identifier for the Pattern instance
- Enables reference to the Pattern instance
- Serves as a stable reference point

**Allowed Semantics:**
- ✅ Unique identifier string
- ✅ Human-readable identifier
- ✅ Version-independent identifier

**Explicit Forbidden Semantics:**
- ❌ MUST NOT encode execution order
- ❌ MUST NOT trigger behavior
- ❌ MUST NOT be evaluated for decision-making
- ❌ MUST NOT imply execution requirements

**Required**: Yes

---

### Field 2: pattern_name

**Type**: String (human-readable name)

**Purpose:**
- Provides a human-readable name for the Pattern instance
- Enables human understanding and communication
- Serves as a semantic label

**Allowed Semantics:**
- ✅ Human-readable name string
- ✅ Semantic categorization label
- ✅ Descriptive identifier

**Explicit Forbidden Semantics:**
- ❌ MUST NOT encode execution order
- ❌ MUST NOT trigger behavior
- ❌ MUST NOT be evaluated for decision-making
- ❌ MUST NOT imply execution requirements
- ❌ MUST NOT encode workflow ordering

**Required**: Yes

---

### Field 3: pattern_version

**Type**: String (version identifier)

**Purpose:**
- Provides version identification for the Pattern instance
- Enables versioning and replacement
- Serves as a version marker

**Allowed Semantics:**
- ✅ Version identifier string
- ✅ Semantic version string
- ✅ Version metadata

**Explicit Forbidden Semantics:**
- ❌ MUST NOT encode execution order
- ❌ MUST NOT trigger behavior
- ❌ MUST NOT be evaluated for decision-making
- ❌ MUST NOT imply execution requirements

**Required**: Yes

---

### Field 4: created_at

**Type**: String (ISO8601 timestamp)

**Purpose:**
- Records when the Pattern instance was created
- Enables auditability and traceability
- Serves as a temporal marker

**Allowed Semantics:**
- ✅ ISO8601 timestamp string
- ✅ Creation timestamp
- ✅ Temporal metadata

**Explicit Forbidden Semantics:**
- ❌ MUST NOT encode execution order
- ❌ MUST NOT trigger behavior
- ❌ MUST NOT be evaluated for decision-making
- ❌ MUST NOT imply execution requirements

**Required**: Yes

---

### Field 5: created_by

**Type**: String (human identifier)

**Purpose:**
- Records who created the Pattern instance
- Enables auditability and traceability
- Serves as a source marker

**Allowed Semantics:**
- ✅ Human identifier string
- ✅ Creator identifier
- ✅ Source metadata

**Explicit Forbidden Semantics:**
- ❌ MUST NOT encode execution order
- ❌ MUST NOT trigger behavior
- ❌ MUST NOT be evaluated for decision-making
- ❌ MUST NOT imply execution requirements

**Required**: Yes

---

### Field 6: description

**Type**: String (human-readable description)

**Purpose:**
- Provides a human-readable description of the Pattern instance
- Enables human understanding of the Pattern's purpose
- Serves as documentation

**Allowed Semantics:**
- ✅ Human-readable description string
- ✅ Purpose statement
- ✅ Semantic description

**Explicit Forbidden Semantics:**
- ❌ MUST NOT encode execution instructions
- ❌ MUST NOT imply workflow steps
- ❌ MUST NOT trigger behavior
- ❌ MUST NOT be evaluated for decision-making
- ❌ MUST NOT imply execution requirements
- ❌ MUST NOT encode process flow

**Required**: No

---

### Field 7: capability_references

**Type**: Array of Capability Reference Objects

**Purpose:**
- References capabilities (A2) that may be used in the Pattern
- Provides informational linkage to system capabilities
- Enables human understanding of which capabilities relate to the Pattern

**Allowed Semantics:**
- ✅ Array of capability reference objects
- ✅ Capability identifier references (reference only)
- ✅ Informational linkage only
- ✅ Descriptive association

**Capability Reference Object Structure:**
- **capability_id** (required): String (capability identifier)
- **capability_name** (optional): String (human-readable name)
- **reference_purpose** (optional): String (descriptive purpose)

**Explicit Forbidden Semantics:**
- ❌ MUST NOT execute the referenced capability
- ❌ MUST NOT trigger capability execution
- ❌ MUST NOT evaluate capability conditions
- ❌ MUST NOT infer capability requirements
- ❌ MUST NOT encode capability ordering
- ❌ MUST NOT represent capability workflow
- ❌ MUST NOT imply capability behavior
- ❌ MUST NOT create reverse influence (Capability → Pattern)

**Required**: No

**Relationship Constraint:**
- Pattern → Capability: Reference only (one-way)
- Capability → Pattern: Forbidden (no reverse influence)

---

### Field 8: evidence_references

**Type**: Array of Evidence Reference Objects

**Purpose:**
- References audit evidence (A3) that documents the Pattern
- Provides informational linkage to audit records
- Enables human review of Pattern usage evidence

**Allowed Semantics:**
- ✅ Array of evidence reference objects
- ✅ Audit record identifier references (reference only)
- ✅ Informational linkage only
- ✅ Descriptive association

**Evidence Reference Object Structure:**
- **audit_record_id** (required): String (audit record identifier)
- **evidence_type** (optional): String (descriptive type)
- **reference_purpose** (optional): String (descriptive purpose)

**Explicit Forbidden Semantics:**
- ❌ MUST NOT evaluate audit evidence for decision-making
- ❌ MUST NOT trigger behavior based on audit evidence
- ❌ MUST NOT interpret audit evidence as success/failure
- ❌ MUST NOT use audit evidence for routing or triggering
- ❌ MUST NOT create reverse influence (Audit → Pattern)

**Required**: No

**Relationship Constraint:**
- Pattern → Audit: Evidence reference only (one-way)
- Audit → Pattern: Forbidden (no reverse influence)

---

### Field 9: metadata

**Type**: Object (key-value pairs)

**Purpose:**
- Provides additional descriptive metadata for the Pattern instance
- Enables extensibility for descriptive information
- Serves as a container for descriptive data

**Allowed Semantics:**
- ✅ Key-value pairs (string keys, string values)
- ✅ Descriptive metadata only
- ✅ Human-readable information

**Explicit Forbidden Semantics:**
- ❌ MUST NOT encode execution order
- ❌ MUST NOT encode workflow sequence
- ❌ MUST NOT encode conditional logic
- ❌ MUST NOT encode state transitions
- ❌ MUST NOT trigger behavior
- ❌ MUST NOT be evaluated for decision-making
- ❌ MUST NOT imply execution requirements

**Required**: No

---

## Explicitly Forbidden Fields

**The following fields are explicitly FORBIDDEN in Pattern Instances:**

### Forbidden Field 1: execution_order

**Forbidden because:**
- ❌ Encodes execution order
- ❌ Implies workflow sequence
- ❌ Violates "MUST NOT encode execution order" prohibition

---

### Forbidden Field 2: workflow_steps

**Forbidden because:**
- ❌ Encodes workflow steps
- ❌ Implies process flow
- ❌ Violates "MUST NOT encode workflow logic" prohibition

---

### Forbidden Field 3: conditions

**Forbidden because:**
- ❌ Encodes conditional logic
- ❌ Implies decision-making
- ❌ Violates "MUST NOT evaluate" prohibition

---

### Forbidden Field 4: success_criteria

**Forbidden because:**
- ❌ Encodes success/failure semantics
- ❌ Implies judgment
- ❌ Violates "MUST NOT infer success/failure" prohibition

---

### Forbidden Field 5: failure_criteria

**Forbidden because:**
- ❌ Encodes success/failure semantics
- ❌ Implies judgment
- ❌ Violates "MUST NOT infer success/failure" prohibition

---

### Forbidden Field 6: triggers

**Forbidden because:**
- ❌ Encodes automation triggers
- ❌ Implies automatic execution
- ❌ Violates "MUST NOT execute" prohibition

---

### Forbidden Field 6: automation_rules

**Forbidden because:**
- ❌ Encodes automation rules
- ❌ Implies automatic execution
- ❌ Violates "MUST NOT execute" prohibition

---

### Forbidden Field 7: state_machine

**Forbidden because:**
- ❌ Encodes state transitions
- ❌ Implies execution flow
- ❌ Violates "MUST NOT encode workflow logic" prohibition

---

### Forbidden Field 8: execution_config

**Forbidden because:**
- ❌ Encodes execution configuration
- ❌ Implies execution semantics
- ❌ Violates "MUST NOT execute" prohibition

---

## Schema Validation Rules

**All Pattern Instances MUST comply with the following validation rules:**

1. **Required Fields Present**
   - pattern_id MUST be present
   - pattern_name MUST be present
   - pattern_version MUST be present
   - created_at MUST be present
   - created_by MUST be present

2. **Field Type Compliance**
   - All fields MUST match their defined types
   - capability_references MUST be an array (if present)
   - evidence_references MUST be an array (if present)
   - metadata MUST be an object (if present)

3. **Reference Validity**
   - capability_references MUST contain valid capability identifiers (reference only)
   - evidence_references MUST contain valid audit record identifiers (reference only)

4. **Forbidden Fields Absent**
   - No forbidden fields MAY be present
   - No execution semantics MAY be encoded
   - No workflow semantics MAY be encoded
   - No conditional semantics MAY be encoded

5. **External Replaceability**
   - Pattern Instance MUST be externally replaceable
   - Pattern Instance MUST be versionable
   - Pattern Instance MUST remain outside A2 core

---

## Instance Storage Requirements

**Pattern Instances MUST be stored:**
- Externally to A2 core
- In a replaceable format
- In a versionable format
- In a human-readable format

**Pattern Instances MUST NOT be stored:**
- ❌ Within A2 core
- ❌ In an immutable format
- ❌ In a binary-only format
- ❌ In a non-human-readable format

---

## Compatibility with Ontology Documents

**This schema is fully compatible with:**

1. **PATTERN_METHODOLOGY_ONTOLOGY.md**
   - Schema fields map to ontology element types
   - Schema constraints enforce ontology prohibitions
   - Schema relationships enforce ontology relationships

2. **IMMUTABLE_DESIGN_CONSTRAINTS.md**
   - Pattern Instances remain outside A2 core
   - Pattern Instances do NOT execute capabilities
   - Pattern Instances do NOT trigger automation

3. **CAPABILITY_ONTOLOGY.md**
   - capability_references are reference-only
   - No reverse influence (Capability → Pattern)
   - No execution semantics

4. **AUDIT_EVIDENCE_ONTOLOGY.md**
   - evidence_references are reference-only
   - No reverse influence (Audit → Pattern)
   - No evaluation semantics

5. **AUTHORIZATION_GOVERNANCE_ONTOLOGY.md**
   - Pattern Instances do NOT grant authorization
   - Pattern Instances do NOT infer permission
   - Pattern Instances do NOT trigger execution

---

## Stop Conditions

**If any of the following appear in a Pattern Instance, STOP:**

1. **Execution Semantics**
   - If execution logic appears → STOP
   - If execution triggers appear → STOP
   - If execution coordination appears → STOP

2. **Workflow Semantics**
   - If workflow steps appear → STOP
   - If step ordering appears → STOP
   - If process flow appears → STOP

3. **Conditional Semantics**
   - If condition evaluation appears → STOP
   - If conditional logic appears → STOP
   - If decision-making conditions appear → STOP

4. **Success/Failure Semantics**
   - If success/failure inference appears → STOP
   - If outcome interpretation appears → STOP
   - If judgment logic appears → STOP

5. **Automation Semantics**
   - If automation triggers appear → STOP
   - If automatic execution appears → STOP
   - If automation rules appear → STOP

6. **State Machine Semantics**
   - If state transitions appear → STOP
   - If state machine logic appears → STOP
   - If state-based routing appears → STOP

---

## Example Schema Structure (Informational Only)

**The following is an example structure for informational purposes only. This is NOT an implementation specification.**

```json
{
  "pattern_id": "string (required)",
  "pattern_name": "string (required)",
  "pattern_version": "string (required)",
  "created_at": "ISO8601 timestamp (required)",
  "created_by": "string (required)",
  "description": "string (optional)",
  "capability_references": [
    {
      "capability_id": "string (required)",
      "capability_name": "string (optional)",
      "reference_purpose": "string (optional)"
    }
  ],
  "evidence_references": [
    {
      "audit_record_id": "string (required)",
      "evidence_type": "string (optional)",
      "reference_purpose": "string (optional)"
    }
  ],
  "metadata": {
    "key": "value (string only)"
  }
}
```

**This example is for illustration only. Actual implementation formats may vary.**

---

## Summary

**This document establishes the canonical instance-level schema for Pattern/Methodology usage.**

**Key Definitions:**
1. Pattern Instance is a concrete, external, replaceable, versionable representation
2. Required fields: pattern_id, pattern_name, pattern_version, created_at, created_by
3. Allowed fields: description, capability_references, evidence_references, metadata
4. Forbidden fields: execution_order, workflow_steps, conditions, success_criteria, failure_criteria, triggers, automation_rules, state_machine, execution_config

**Key Constraints:**
- Pattern Instances MUST be purely descriptive
- Pattern Instances MUST reference capabilities (reference only)
- Pattern Instances MAY reference audit evidence (reference only, optional)
- Pattern Instances MUST NOT encode execution order, workflow, conditions, success/failure, automation
- Pattern Instances MUST be human-readable and auditable
- Pattern Instances MUST be externally replaceable and versionable
- Pattern Instances MUST remain outside A2 core

**Compatibility:**
- Fully compatible with PATTERN_METHODOLOGY_ONTOLOGY.md
- Fully compatible with IMMUTABLE_DESIGN_CONSTRAINTS.md
- Fully compatible with CAPABILITY_ONTOLOGY.md
- Fully compatible with AUDIT_EVIDENCE_ONTOLOGY.md
- Fully compatible with AUTHORIZATION_GOVERNANCE_ONTOLOGY.md

**Enforcement:**
- All Pattern Instances MUST comply with this schema
- All violations MUST be rejected
- Stop conditions must be checked before any Pattern Instance is accepted

---

**END OF PATTERN INSTANCE SCHEMA**

**This document is CANONICAL and IMMUTABLE.**
**No Pattern Instance may violate this schema.**

