# Minimal Epoch Runtime

**Purpose**: Minimal, unoptimized Epoch mechanism implementation for leakage validation.

**Status**: IMPLEMENTATION / NON-CANONICAL

---

## Components

### epoch_controller.py
- Manual Epoch lifecycle control
- Explicit start/end triggers
- No automatic behavior

### epoch_context.py
- Epoch-local state container
- No global access
- Explicit destruction

### epoch_guard.py
- Runtime leakage detection
- State hash tracking
- Object reference monitoring

---

## How to Run

### Basic Usage

```python
from epoch_controller import EpochController

# Create controller
controller = EpochController()

# Start Epoch
epoch_id = controller.start_epoch()

# Get context
context = controller.get_current_context()

# Use context
context.set("key", "value")
value = context.get("key")

# End Epoch
report = controller.end_epoch()
```

### Multiple Epochs

```python
controller = EpochController()

# Epoch 1
epoch_id_1 = controller.start_epoch()
context_1 = controller.get_current_context()
context_1.set("data", "value1")
report_1 = controller.end_epoch()

# Epoch 2
epoch_id_2 = controller.start_epoch()
context_2 = controller.get_current_context()
context_2.set("data", "value2")
report_2 = controller.end_epoch()
```

---

## How to Reproduce

### Single Epoch Test

```bash
cd phase_q/Q4-0/MINIMAL_EPOCH_RUNTIME
python3 -c "
from epoch_controller import EpochController
controller = EpochController()
epoch_id = controller.start_epoch()
context = controller.get_current_context()
context.set('test', 'value')
report = controller.end_epoch()
print(report)
"
```

### Multiple Epoch Test

```bash
cd phase_q/Q4-0/MINIMAL_EPOCH_RUNTIME
python3 test_epoch_transitions.py
```

---

## Constraints

- **No caching**: All state is ephemeral
- **No optimization**: Explicit operations only
- **No automatic behavior**: Manual triggers only
- **No global state**: All state in EpochContext
- **No persistence**: All state destroyed at Epoch end

---

## Verification

After each Epoch:
1. State hash is computed
2. State is explicitly destroyed
3. Post-destruction hash is computed
4. Guard verifies no leakage

---

## No Recommendations

This runtime provides no recommendations.

This runtime implements only structural requirements.

---

**END OF README**

