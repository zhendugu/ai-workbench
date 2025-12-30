# Run Matrix Definition Q4-2

**Work Order**: WO-Q-4-2-0-AI-INTEGRATION-MINIMAL-EPOCH-COMPATIBILITY-AND-STRUCTURAL-CONTROL-VALIDATION

**Document Status**: IMPLEMENTATION-SPEC / NON-CANONICAL

**Date**: 2026-01-10

---

## Purpose

This document defines the minimum run matrix for Q4-2 validation.

---

## Matrix Dimensions

### Human Models
- **H1**: 谨慎 (Cautious) - Strict verification, high rejection rate
- **H2**: 疲劳 (Fatigued) - Reduced verification, increased acceptance
- **H3**: 随意 (Casual) - Minimal verification, high acceptance

### Adversary Strategies
- **A0**: 非对抗 (Non-Adversarial) - Baseline, no adversarial behavior
- **A1**: 软性措辞漂移 (Soft Wording Drift) - Subtle language shifts
- **A2**: 信息密度操控 (Information Density Manipulation) - Information density variations

### Tool Behaviors
- **T0**: 无缓存 (No Cache) - No tool result caching
- **T1**: 显式缓存 (Explicit Cache) - Explicit cache with guard constraints

### Concurrency Levels
- **C0**: 单线程 (Single Thread) - Sequential execution
- **C1**: 最小并发 (Minimal Concurrency) - Minimal concurrent operations

### Seeds
- Fixed seeds: 1337, 1338, 1339, 2000 (deterministic)

---

## Run Matrix

### Minimum Runs: 24

Matrix: 3 human models × 3 adversary strategies × 2 tool behaviors × 2 concurrency levels × 2 seeds = 72 potential runs

**Minimum Selection**: 24 runs covering all combinations with at least 2 seeds per combination.

### Run Naming Convention

`run_{human_model}_{adversary}_{tool}_{concurrency}_s{seed}`

Example: `run_H1_A0_T0_C0_s1337`

---

## Run Configuration Structure

Each run configuration includes:
- **run_id**: Unique run identifier
- **human_model**: H1, H2, or H3
- **adversary_strategy**: A0, A1, or A2
- **tool_behavior**: T0 or T1
- **concurrency**: C0 or C1
- **seed**: Fixed seed value
- **epochs**: Number of epochs (default: 10)
- **inputs**: Test input data

---

## Expected Output Types

- **Information Presentation**: AI presents information only
- **Validation Feedback**: AI provides validation results
- **Candidate Comparison**: AI compares options
- **Confirmation Request**: AI requests human confirmation (human-triggered)

---

## Stop Conditions

- **Epoch Completion**: All epochs complete successfully
- **Error Stop**: Any error stops the run (no auto-retry)
- **Leakage Detection**: Any leakage detected stops the run
- **Timeout**: Maximum execution time exceeded

---

## Execution Order

1. **Smoke Run**: 1 run (H1/A0/T0/C0) for framework validation
2. **Full Matrix**: ≥24 runs covering all combinations
3. **Optional Long Run**: 2k epochs × 2 runs (if needed)

---

## No Recommendations

This matrix definition provides no recommendations.

This matrix defines only run configurations and execution requirements.

---

**END OF RUN MATRIX DEFINITION**

