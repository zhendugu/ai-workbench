# Audit Reproducibility Instructions

**Paradigm**: Epoch-based Time-Fractured Intelligence System

**Document Status**: REPRODUCIBILITY-INSTRUCTIONS / REFERENCE-ONLY / NON-EXECUTABLE

**Date**: 2025-12-28

---

## Purpose

This document describes how a third party could reproduce Phase Q execution results.

**Explicit Statement**: "Reproduction outside these constraints invalidates comparison."

---

## Assumptions Required

### Environment Assumptions

1. **Python 3.x**: Required for execution scripts
2. **Bash**: Required for matrix execution scripts
3. **Unix-like OS**: Scripts assume Unix paths and commands
4. **Sufficient Disk Space**: ~100MB for 72 runs (estimated)
5. **Deterministic Execution**: Fixed seeds required for reproducibility

### Code Assumptions

1. **Fixed Seeds**: All runs use fixed seeds (1337, 1338, 1339, 2000)
2. **No External Dependencies**: Scripts use only standard library (except JSON)
3. **No Network Access**: All tools are mock, no network required
4. **No Time Dependencies**: No wall-clock time used in execution

---

## Resources Needed

### Code Repository

**Location**: `phase_q/Q4-2/`

**Required Files**:
- `scripts/generate_run_configs_q4_2.py` (generate run configurations)
- `scripts/run_single_q4_2.py` (execute single run)
- `scripts/run_q4_2_matrix.sh` (execute matrix)
- `scripts/collect_hashes_q4_2.py` (collect hashes)
- `scripts/detect_leakage_q4_2.py` (detect leakage)
- `scripts/compute_influence_signals.py` (compute influence signals)
- `runtime_integration/` (AI controller, context, tool sandbox)

### Configuration Files

**Location**: `phase_q/Q4-2/run_configs/`

**Required Files**:
- `matrix_index.json` (72 run IDs)
- `run_*.json` (72 run configuration files)

### Baseline References

**Location**: `phase_q/Q4-0/`, `phase_q/Q4-1/`

**Required Files**:
- `EPOCH_DEFINITION.md` (epoch definition)
- `MINIMAL_EPOCH_RUNTIME/` (Q4-0 runtime)
- `EXPANDED_EPOCH_RUNTIME/` (Q4-1 runtime)

---

## Reproduction Steps

### Step 1: Environment Setup

```bash
# Verify Python 3.x
python3 --version

# Verify Bash
bash --version

# Navigate to project root
cd /path/to/project/root
```

### Step 2: Generate Run Configurations

```bash
# Generate 72 run configurations
python3 phase_q/Q4-2/scripts/generate_run_configs_q4_2.py phase_q/Q4-2/run_configs

# Verify: Should generate 72 JSON files + matrix_index.json
ls phase_q/Q4-2/run_configs/*.json | wc -l  # Should be 73 (72 runs + index)
```

### Step 3: Execute Matrix

```bash
# Execute all 72 runs
bash phase_q/Q4-2/scripts/run_q4_2_matrix.sh

# Expected output: 72 run directories in EXECUTION_LOG_ARCHIVE_Q4-2/
```

### Step 4: Collect Hashes

```bash
# Collect hashes for all runs
python3 phase_q/Q4-2/scripts/collect_hashes_q4_2.py \
  phase_q/Q4-2/EXECUTION_LOG_ARCHIVE_Q4-2 \
  phase_q/Q4-2/EXECUTION_LOG_ARCHIVE_Q4-2/hashes_manifest.md

# Verify: Should generate hashes_manifest.md with 72 entries
```

### Step 5: Detect Leakage

```bash
# Detect leakage
python3 phase_q/Q4-2/scripts/detect_leakage_q4_2.py \
  phase_q/Q4-2/EXECUTION_LOG_ARCHIVE_Q4-2 \
  phase_q/Q4-2/LEAKAGE_DETECTION_LOG_Q4-2.md

# Expected: 0 leakage detected
```

### Step 6: Compute Influence Signals

```bash
# Compute influence signals
python3 phase_q/Q4-2/scripts/compute_influence_signals.py \
  phase_q/Q4-2/EXECUTION_LOG_ARCHIVE_Q4-2 \
  phase_q/Q4-2/INFLUENCE_SIGNALS_Q4-2.md

# Expected: 72 runs analyzed
```

---

## What Must Remain Unchanged

### Code Must Remain Unchanged

- **Scripts**: All execution scripts must be identical
- **Runtime**: All runtime code must be identical
- **Tools**: All tool implementations must be identical

**Verification**: Compare file hashes or use version control.

### Configuration Must Remain Unchanged

- **Run Configurations**: All 72 run configs must be identical
- **Seeds**: All seeds must be identical (1337, 1338, 1339, 2000)
- **Epoch Count**: All runs must use 10 epochs

**Verification**: Compare `run_configs/*.json` files.

### Environment Must Remain Deterministic

- **No Random**: No random number generation (except fixed seeds)
- **No Time**: No wall-clock time dependencies
- **No Network**: No network access

**Verification**: Check code for time/random/network usage.

---

## Expected Results

### Run Count

- **Expected**: 72 runs
- **Verification**: `ls -d EXECUTION_LOG_ARCHIVE_Q4-2/run_* | wc -l` = 72

### Leakage Detection

- **Expected**: 0 leakage
- **Verification**: `LEAKAGE_DETECTION_LOG_Q4-2.md` shows "Runs with Leakage Detected: 0"

### Influence Signals

- **Expected**: 72 runs analyzed
- **Verification**: `INFLUENCE_SIGNALS_Q4-2.md` shows "Total Runs Analyzed: 72"

### Hash Manifest

- **Expected**: 72 entries
- **Verification**: `hashes_manifest.md` has 72 run sections

---

## Reproduction Outside Constraints

### If Constraints Are Violated

**Statement**: "Reproduction outside these constraints invalidates comparison."

**Examples of Invalid Reproduction**:
- Different seeds
- Modified code
- Different environment (e.g., different Python version)
- Different configuration
- Network access enabled
- Time dependencies added

**Result**: Results cannot be compared to Phase Q results.

---

## Hash Verification

### Reproducing Hashes

If all constraints are met, reproduced hashes should match original hashes.

**Verification**:
```bash
# Compare hashes_manifest.md
diff phase_q/Q4-2/EXECUTION_LOG_ARCHIVE_Q4-2/hashes_manifest.md \
     <reproduced_path>/hashes_manifest.md
```

**Expected**: No differences (if constraints met).

---

## Known Limitations

### Reproducibility Limitations

1. **Platform Differences**: Different OS may produce different results
2. **Python Version**: Different Python versions may produce different results
3. **File System**: Different file systems may affect ordering

**Mitigation**: Use identical environment.

### Comparison Limitations

1. **Hash Comparison**: Hashes may differ due to platform differences
2. **Log Comparison**: Logs may differ in formatting
3. **Timing**: Execution time may differ

**Mitigation**: Compare logical results, not exact hashes.

---

## No Guarantees

This document does not guarantee reproducibility.

It only describes how reproduction was intended.

Actual reproducibility depends on environment matching.

---

## Human Review

**Status**: PENDING

- **Human Reviewer**: [Name]
- **Date**: [Date]
- **Signature**: [Signature/Approval]

---

**END OF AUDIT REPRODUCIBILITY INSTRUCTIONS**

