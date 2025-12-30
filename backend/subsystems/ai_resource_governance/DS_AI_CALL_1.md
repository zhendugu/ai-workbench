# DS-AI-CALL-1: AICallRecord Data Structure

**Subsystem**: AI Resource Governance (Subsystem 10)  
**Phase**: Phase-3 Level 1  
**Status**: ✅ IMPLEMENTED

---

## Purpose

DS-AI-CALL-1 represents a single AI call for recording and querying purposes.

**This structure is DESCRIPTIVE ONLY**, not prescriptive.  
It does NOT enforce limits, trigger actions, or influence behavior.

---

## Structure

```python
@dataclass
class AICallRecord:
    call_id: str
    model: str
    provider: str
    input_tokens: int
    output_tokens: int
    total_tokens: int
    estimated_cost: float
    currency: str
    caller: str  # subsystem / component name
    purpose: str  # human-readable
    created_at: str  # ISO8601 timestamp
```

---

## Field Descriptions

### Required Fields

- **call_id**: Unique identifier for the AI call
- **model**: AI model identifier (e.g., "gpt-4", "claude-3")
- **provider**: AI provider identifier (e.g., "openai", "anthropic")
- **input_tokens**: Number of input tokens
- **output_tokens**: Number of output tokens
- **total_tokens**: Total tokens (input + output)
- **estimated_cost**: Estimated cost in the specified currency
- **currency**: Currency code (e.g., "USD", "CNY")
- **caller**: Subsystem / component name that made the call
- **purpose**: Human-readable purpose of the call
- **created_at**: ISO8601 timestamp of the call

---

## Forbidden Fields

**Phase-3 Level 1 explicitly prohibits**:
- ❌ execution_flags
- ❌ retry_info
- ❌ decision_outcomes
- ❌ enforcement_markers
- ❌ Any field that implies behavior or enforcement

---

## Usage

DS-AI-CALL-1 is used by:
- **C-AI-GOV-1**: Record AI Call (input parameter)
- **C-AI-GOV-2**: Query AI Usage (stored records)

---

## Constraints

### Descriptive Only

- ✅ Records AI call information
- ✅ Provides data for querying and reporting
- ❌ Does NOT enforce limits
- ❌ Does NOT trigger actions
- ❌ Does NOT influence behavior

### Phase-3 Level 1 Constraints

- ✅ No enforcement fields
- ✅ No behavior triggers
- ✅ No execution flags
- ✅ Pure data structure

---

**END OF DS-AI-CALL-1 DOCUMENTATION**

