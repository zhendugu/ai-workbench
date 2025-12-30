# Capability Ontology (A2)

**Document Status**: **CANONICAL**  
**Document Type**: Constitutional-Level Ontology Definition  
**Effective Date**: 2025-12-26  
**Precedence**: Compatible with IMMUTABLE_DESIGN_CONSTRAINTS.md, PATTERN_METHODOLOGY_ONTOLOGY.md, and AUDIT_EVIDENCE_ONTOLOGY.md

---

## Purpose

This document defines the immutable ontological structure for Capability (A2) representation in the system.

**This document exists to:**
- Establish immutable boundaries for Capability (A2) representation
- Define allowed element types within Capability
- Prevent workflow, judgment, or execution coordination semantics from entering Capability structures
- Ensure Capabilities remain descriptive, atomic, and referable
- Provide highest-level constraints for all Capability representations

**This document does NOT:**
- Provide implementation solutions
- Give specific business examples
- Authorize new capabilities or features
- Define workflow semantics
- Define execution semantics
- Define conditional semantics
- Define judgment semantics

---

## Capability Identity Statement

### What a Capability IS

**A Capability (A2) is a descriptive, atomic, referable unit that defines what the system CAN do.**

**A Capability (A2):**
- Is a declarative description of a system function
- Is atomic (cannot be decomposed into sub-capabilities for execution purposes)
- Is referable (can be referenced by other structures)
- Defines what the system CAN do, not what it DOES do
- Is descriptive, not prescriptive
- Is the system's sole core

**A Capability (A2) provides:**
- Declarative definition of a system function
- Atomic unit of system functionality
- Reference point for Patterns and other structures
- Foundation for all system operations

### What a Capability IS NOT

**A Capability (A2) is NOT:**
- ❌ A workflow definition
- ❌ A process specification
- ❌ A judgment mechanism
- ❌ An execution coordinator
- ❌ A decision-making system
- ❌ A behavior trigger
- ❌ A condition evaluator
- ❌ A success/failure interpreter

**A Capability (A2) does NOT:**
- ❌ Form workflows with other capabilities
- ❌ Automatically trigger execution
- ❌ Interpret success or failure
- ❌ Coordinate multi-step processes
- ❌ Evaluate conditions for execution
- ❌ Make decisions
- ❌ Trigger behavior based on conditions

---

## Minimal Set of Allowed Element Types

**The following element types are the minimal set allowed within a Capability (A2):**

1. **Element Type 1: Capability Identifier**
2. **Element Type 2: Input Specification**
3. **Element Type 3: Output Specification**
4. **Element Type 4: Semantic Description**

**No other element types are allowed.**

**These are element TYPES, not instances, not workflows.**

---

## Element Type Definitions

### Element Type 1: Capability Identifier

**Purpose:**
- Provides a unique identifier for the Capability
- Enables reference to the Capability by other structures
- Serves as a stable reference point

**Allowed Semantics:**
- ✅ Unique identifier string
- ✅ Human-readable name
- ✅ Semantic categorization label
- ✅ Descriptive metadata

**Explicit Forbidden Semantics:**
- ❌ MUST NOT encode execution order
- ❌ MUST NOT imply workflow sequence
- ❌ MUST NOT trigger behavior
- ❌ MUST NOT evaluate conditions
- ❌ MUST NOT encode conditional logic
- ❌ MUST NOT represent state transitions

---

### Element Type 2: Input Specification

**Purpose:**
- Describes the input requirements for the Capability
- Provides declarative specification of expected inputs
- Enables human understanding of Capability requirements

**Allowed Semantics:**
- ✅ Input type specification (descriptive only)
- ✅ Input structure description
- ✅ Input validation rules (descriptive only)
- ✅ Input metadata

**Explicit Forbidden Semantics:**
- ❌ MUST NOT evaluate input conditions
- ❌ MUST NOT trigger behavior based on input
- ❌ MUST NOT route based on input
- ❌ MUST NOT encode conditional logic based on input
- ❌ MUST NOT infer execution requirements from input
- ❌ MUST NOT represent workflow ordering

---

### Element Type 3: Output Specification

**Purpose:**
- Describes the output structure for the Capability
- Provides declarative specification of expected outputs
- Enables human understanding of Capability results

**Allowed Semantics:**
- ✅ Output type specification (descriptive only)
- ✅ Output structure description
- ✅ Output metadata

**Explicit Forbidden Semantics:**
- ❌ MUST NOT evaluate output for success/failure
- ❌ MUST NOT interpret output as success or failure
- ❌ MUST NOT trigger behavior based on output
- ❌ MUST NOT route based on output
- ❌ MUST NOT encode conditional logic based on output
- ❌ MUST NOT infer conclusions from output
- ❌ MUST NOT represent workflow continuation

---

### Element Type 4: Semantic Description

**Purpose:**
- Provides human-readable description of the Capability's purpose
- Enables human understanding of what the Capability does
- Serves as documentation and reference

**Allowed Semantics:**
- ✅ Human-readable description
- ✅ Purpose statement
- ✅ Semantic categorization
- ✅ Descriptive metadata

**Explicit Forbidden Semantics:**
- ❌ MUST NOT encode execution instructions
- ❌ MUST NOT imply workflow steps
- ❌ MUST NOT trigger behavior
- ❌ MUST NOT evaluate conditions
- ❌ MUST NOT encode conditional logic
- ❌ MUST NOT represent process flow

---

## Explicit One-Way Relationships

### Relationship 1: Capability → Audit (Record Only)

**Direction:** Capability → Audit (one-way only)

**Allowed Semantics:**
- ✅ Capability may create an audit record (A3)
- ✅ Record is passive and read-only
- ✅ Record provides evidence of capability execution
- ✅ Record enables human review of capability usage

**Explicit Forbidden Semantics:**
- ❌ MUST NOT evaluate audit record for decision-making
- ❌ MUST NOT trigger behavior based on audit record
- ❌ MUST NOT interpret audit record as success/failure
- ❌ MUST NOT create reverse influence (Audit → Capability)

**Enforcement:**
- Capability may create audit records
- Audit MUST NOT influence capability behavior
- No bidirectional relationship allowed

---

### Relationship 2: Pattern → Capability (Reference Only)

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

### Relationship 3: Capability → (No Other Capabilities)

**Direction:** Capability → (no relationships to other Capabilities)

**Allowed Semantics:**
- ✅ Capability is atomic (no decomposition for execution)
- ✅ Capability is independent (no execution dependencies on other capabilities)
- ✅ Capability is referable (can be referenced, not composed)

**Explicit Forbidden Semantics:**
- ❌ MUST NOT form workflows with other capabilities
- ❌ MUST NOT chain with other capabilities
- ❌ MUST NOT coordinate with other capabilities
- ❌ MUST NOT depend on other capabilities for execution
- ❌ MUST NOT trigger other capabilities
- ❌ MUST NOT represent capability sequences

**Enforcement:**
- Capabilities MUST NOT form execution workflows
- Capabilities MUST NOT chain or sequence
- Capabilities MUST remain atomic and independent

---

## Immutable Prohibitions

**The following prohibitions are immutable and apply to all Capability (A2) representations:**

### Prohibition 1: MUST NOT Form Workflows

**Capabilities MUST NOT form workflows with other capabilities.**

**This means:**
- ❌ MUST NOT chain capabilities for execution
- ❌ MUST NOT sequence capabilities
- ❌ MUST NOT coordinate multi-capability processes
- ❌ MUST NOT represent capability dependencies
- ❌ MUST NOT encode execution order between capabilities

**Enforcement:**
- No workflow logic may exist between capabilities
- No capability chaining may be encoded
- No capability sequencing may be represented

---

### Prohibition 2: MUST NOT Automatically Trigger

**Capabilities MUST NOT automatically trigger execution.**

**This means:**
- ❌ MUST NOT trigger based on conditions
- ❌ MUST NOT trigger based on state
- ❌ MUST NOT trigger based on events
- ❌ MUST NOT trigger based on audit data
- ❌ MUST NOT trigger based on other capabilities

**Enforcement:**
- No automatic triggering mechanisms may exist in capabilities
- No condition-based triggering may be encoded
- No event-based triggering may be performed

---

### Prohibition 3: MUST NOT Interpret Success/Failure

**Capabilities MUST NOT interpret success or failure.**

**This means:**
- ❌ MUST NOT interpret output as success or failure
- ❌ MUST NOT interpret state as success or failure
- ❌ MUST NOT infer outcomes
- ❌ MUST NOT provide automatic judgment

**Enforcement:**
- No success/failure interpretation may exist in capabilities
- No outcome interpretation may be encoded
- No automatic judgment logic may be performed

---

### Prohibition 4: MUST NOT Coordinate Execution

**Capabilities MUST NOT coordinate execution.**

**This means:**
- ❌ MUST NOT coordinate multi-step processes
- ❌ MUST NOT orchestrate other capabilities
- ❌ MUST NOT schedule execution
- ❌ MUST NOT manage execution flow

**Enforcement:**
- No execution coordination logic may exist in capabilities
- No orchestration mechanisms may be encoded
- No execution flow management may be performed

---

## Capability Characteristics

### Characteristic 1: Descriptive

**Capabilities are descriptive.**

**This means:**
- ✅ Capabilities describe what the system CAN do
- ✅ Capabilities are declarative, not imperative
- ✅ Capabilities define functionality, not execution
- ✅ Capabilities are specifications, not implementations

**This does NOT mean:**
- ❌ Capabilities execute functionality
- ❌ Capabilities trigger behavior
- ❌ Capabilities coordinate execution
- ❌ Capabilities manage processes

---

### Characteristic 2: Atomic

**Capabilities are atomic.**

**This means:**
- ✅ Capabilities cannot be decomposed for execution purposes
- ✅ Capabilities are independent units
- ✅ Capabilities do not form execution workflows
- ✅ Capabilities are indivisible for execution coordination

**This does NOT mean:**
- ❌ Capabilities can be chained for execution
- ❌ Capabilities can be sequenced
- ❌ Capabilities can coordinate with each other
- ❌ Capabilities can form workflows

---

### Characteristic 3: Referable

**Capabilities are referable.**

**This means:**
- ✅ Capabilities can be referenced by other structures
- ✅ Capabilities can be identified by unique identifiers
- ✅ Capabilities can be linked from Patterns
- ✅ Capabilities provide stable reference points

**This does NOT mean:**
- ❌ Capabilities can reference other capabilities for execution
- ❌ Capabilities can trigger other capabilities
- ❌ Capabilities can form execution dependencies
- ❌ Capabilities can coordinate with other capabilities

---

## Compatibility with IMMUTABLE_DESIGN_CONSTRAINTS.md

**This document is fully compatible with IMMUTABLE_DESIGN_CONSTRAINTS.md.**

**Compatibility Points:**

1. **A2 (Capability Substrate) is the Only Core**
   - Capability (A2) is the system's sole core
   - All system capabilities are defined within A2
   - A2 defines what the system CAN do, not what it DOES do
   - A2 is descriptive, not prescriptive

2. **A1 (Execution/Automation) is NOT a System Goal**
   - Capability (A2) does NOT automatically execute
   - Capability (A2) does NOT trigger automation
   - Capability (A2) does NOT coordinate execution

3. **A3 (Audit/Evidence) Never Drives Behavior**
   - Capability (A2) may create audit records
   - Capability (A2) does NOT evaluate audit data
   - Capability (A2) does NOT trigger behavior based on audit

4. **Auditable ≠ Auto-Judgment**
   - Capability (A2) may create audit records
   - Capability (A2) does NOT automatically judge success or failure
   - Capability (A2) does NOT automatically interpret audit data

5. **State Existence ≠ State Interpretation**
   - Capability (A2) may use state descriptively
   - Capability (A2) does NOT interpret state as success/failure
   - Capability (A2) does NOT use state for decision-making

---

## Compatibility with PATTERN_METHODOLOGY_ONTOLOGY.md

**This document is fully compatible with PATTERN_METHODOLOGY_ONTOLOGY.md.**

**Compatibility Points:**

1. **Pattern → Capability (Reference Only)**
   - Pattern may reference Capability (A2) for informational purposes
   - Capability (A2) MUST NOT contain pattern references
   - No bidirectional relationship allowed

2. **Capability Independence**
   - Capabilities are atomic and independent
   - Capabilities do NOT form workflows
   - Capabilities do NOT coordinate with each other

3. **No Evaluation, No Judgment, No Behavior**
   - Both documents prohibit evaluation and judgment
   - Both documents prohibit behavioral influence
   - Both documents ensure descriptive structures

---

## Compatibility with AUDIT_EVIDENCE_ONTOLOGY.md

**This document is fully compatible with AUDIT_EVIDENCE_ONTOLOGY.md.**

**Compatibility Points:**

1. **Capability → Audit (Record Only)**
   - Capability (A2) may create audit records (A3)
   - Audit (A3) MUST NOT influence capability behavior
   - No bidirectional relationship allowed

2. **Audit Passivity**
   - Audit records are passive and read-only
   - Audit records do NOT affect capability behavior
   - Capabilities do NOT evaluate audit data

3. **No Evaluation, No Judgment**
   - Both documents prohibit evaluation and judgment
   - Both documents ensure passive, descriptive structures

---

## Relationship to Existing Phases and Gates

**This document constrains all existing and future Capability (A2) representations:**

- **Phase-1**: Capability (A2) representations must comply with this ontology
- **Phase-2**: Capability (A2) representations must comply with this ontology
- **Phase-3**: Capability (A2) representations must comply with this ontology
- **Phase-4**: Capability (A2) representations must comply with this ontology
- **Future Phases**: Capability (A2) representations must comply with this ontology

- **Gate A**: Capability (A2) representations must comply with this ontology
- **Future Gates**: Capability (A2) representations must comply with this ontology

**This document does NOT:**
- ❌ Override phase-specific constraints
- ❌ Override gate-specific constraints
- ❌ Override capability-specific constraints
- ❌ Provide implementation guidance

**This document DOES:**
- ✅ Provide highest-level constraints for all Capability (A2) representations
- ✅ Ensure Capabilities remain descriptive, atomic, and referable
- ✅ Prevent workflow, judgment, or execution coordination semantics

---

## Stop Conditions

**If any of the following appear in Capability (A2) representations, STOP:**

1. **Workflow Semantics**
   - If capability chaining appears → STOP
   - If capability sequencing appears → STOP
   - If multi-capability coordination appears → STOP

2. **Automatic Triggering Semantics**
   - If condition-based triggering appears → STOP
   - If event-based triggering appears → STOP
   - If automatic execution appears → STOP

3. **Success/Failure Interpretation Semantics**
   - If success/failure interpretation appears → STOP
   - If outcome judgment appears → STOP
   - If automatic judgment appears → STOP

4. **Execution Coordination Semantics**
   - If execution coordination appears → STOP
   - If orchestration mechanisms appear → STOP
   - If execution flow management appears → STOP

5. **Conditional Semantics**
   - If conditional logic for execution appears → STOP
   - If decision-making conditions appear → STOP
   - If state-based routing appears → STOP

6. **Process Semantics**
   - If process flow appears → STOP
   - If step ordering appears → STOP
   - If workflow sequence appears → STOP

---

## Summary

**This document establishes immutable ontological structure for Capability (A2) representation.**

**Key Definitions:**
1. Capability (A2) is a descriptive, atomic, referable unit that defines what the system CAN do
2. Four allowed element types: Capability Identifier, Input Specification, Output Specification, Semantic Description
3. One-way relationships: Capability → Audit (record only), Pattern → Capability (reference only), Capability → (no other capabilities)

**Key Prohibitions:**
- MUST NOT form workflows with other capabilities
- MUST NOT automatically trigger execution
- MUST NOT interpret success or failure
- MUST NOT coordinate execution

**Key Characteristics:**
- Descriptive (defines what CAN do, not DOES do)
- Atomic (cannot be decomposed for execution purposes)
- Referable (can be referenced by other structures)

**Compatibility:**
- Fully compatible with IMMUTABLE_DESIGN_CONSTRAINTS.md
- Fully compatible with PATTERN_METHODOLOGY_ONTOLOGY.md
- Fully compatible with AUDIT_EVIDENCE_ONTOLOGY.md
- Constrains all phases and gates
- Ensures Capabilities remain descriptive, atomic, and referable

**Enforcement:**
- All Capability (A2) representations MUST comply
- All violations MUST be rejected
- Stop conditions must be checked before any Capability representation is accepted

---

**END OF CAPABILITY ONTOLOGY**

**This document is CANONICAL and IMMUTABLE.**
**No Capability (A2) representation may violate this ontology.**

