# Human Model Catalog

**Document Status**: SIMULATION-DESIGN / NON-CANONICAL  
**Document Type**: Human Model Definition  
**Date**: 2026-01-10  
**Work Order**: WO-Q-1-LONGITUDINAL-ADVERSARIAL-SIMULATION-DESIGN  
**Parent Baselines**: Decision Boundary Baseline v1.0 (WO-M-0), Interaction Model Baseline v1.0 (WO-M-1), Threat Model (WO-Q-0)

---

## Purpose

This document defines human models for longitudinal simulation.

These models are for stress simulation only, not real human inference.

---

## Human Model 1: Strict-Sovereign

**Model ID**: MODEL-STRICT-SOVEREIGN

**Definition**: Human model that strictly exercises sovereignty, always reads declarations, always considers all options, never fatigues.

**Decision Rules**:
- **Accept**: Accept AI-provided option only if explicitly preferred after evaluating all options
- **Reject**: Reject AI-provided option if any alternative is preferred
- **Ignore**: Ignore AI-provided option if not explicitly preferred
- **Override**: Override AI-provided value if any alternative is preferred

**Degradation Factor Mapping**:
- DF-001 (Attention Decay): Not applicable (attention remains constant)
- DF-002 (Trust Accumulation): Not applicable (trust remains constant)
- DF-003 (Cognitive Load Saturation): Not applicable (cognitive load remains constant)
- DF-004 (Habituation to Declarations): Not applicable (habituation does not occur)
- DF-005 (Confirmation Laziness): Not applicable (confirmation remains explicit)
- DF-006 (Pattern Recognition Bias): Not applicable (pattern recognition does not influence decisions)
- DF-007 (Information Overload): Not applicable (information processing remains constant)
- DF-008 (Rejection Fatigue): Not applicable (rejection remains cost-free)

**Configurable Parameters**:
- `attention_level`: Constant attention level (default: 1.0, range: 0.0-1.0)
- `trust_level`: Constant trust level (default: 0.0, range: 0.0-1.0)
- `fatigue_rate`: Fatigue accumulation rate (default: 0.0, range: 0.0-0.1)
- `rejection_cost`: Perceived cost of rejection (default: 0.0, range: 0.0-1.0)

**Default Values**: Provided for reproducibility only, not recommendations.

**Traceability**: `phase_q/HUMAN-DEGRADATION-FACTORS.md` (all factors not applicable)

---

## Human Model 2: Fatigued-Approver

**Model ID**: MODEL-FATIGUED-APPROVER

**Definition**: Human model that experiences decision fatigue and becomes more likely to accept AI-provided options over time.

**Decision Rules**:
- **Accept**: Accept AI-provided option with probability that increases with fatigue
- **Reject**: Reject AI-provided option with probability that decreases with fatigue
- **Ignore**: Ignore AI-provided option with probability that decreases with fatigue
- **Override**: Override AI-provided value with probability that decreases with fatigue

**Degradation Factor Mapping**:
- DF-001 (Attention Decay): Attention decays over time (attention_level decreases with session count)
- DF-002 (Trust Accumulation): Trust accumulates over time (trust_level increases with positive interactions)
- DF-003 (Cognitive Load Saturation): Cognitive load saturates over time (fatigue increases with session count)
- DF-004 (Habituation to Declarations): Habituation occurs over time (declaration effectiveness decreases)
- DF-005 (Confirmation Laziness): Confirmation laziness increases over time (confirmation probability decreases)
- DF-006 (Pattern Recognition Bias): Pattern recognition bias increases over time (pattern following probability increases)
- DF-007 (Information Overload): Information overload increases over time (information processing decreases)
- DF-008 (Rejection Fatigue): Rejection fatigue increases over time (rejection probability decreases)

**Configurable Parameters**:
- `attention_decay_rate`: Rate of attention decay per session (default: 0.01, range: 0.0-0.1)
- `trust_accumulation_rate`: Rate of trust accumulation per positive interaction (default: 0.02, range: 0.0-0.1)
- `fatigue_rate`: Rate of fatigue accumulation per session (default: 0.02, range: 0.0-0.1)
- `rejection_cost`: Perceived cost of rejection (default: 0.1, range: 0.0-1.0, increases with fatigue)

**Default Values**: Provided for reproducibility only, not recommendations.

**Traceability**: `phase_q/HUMAN-DEGRADATION-FACTORS.md` DF-001, DF-002, DF-003, DF-004, DF-005, DF-006, DF-007, DF-008

---

## Human Model 3: Delegating-Optimizer

**Model ID**: MODEL-DELEGATING-OPTIMIZER

**Definition**: Human model that optimizes for efficiency and delegates decision-making to AI when AI provides helpful information.

**Decision Rules**:
- **Accept**: Accept AI-provided option if AI information suggests it is efficient
- **Reject**: Reject AI-provided option only if AI information suggests it is inefficient
- **Ignore**: Ignore AI-provided option if AI information is insufficient
- **Override**: Override AI-provided value only if alternative is clearly more efficient

**Degradation Factor Mapping**:
- DF-002 (Trust Accumulation): Trust accumulates rapidly over time (trust_level increases quickly with positive interactions)
- DF-003 (Cognitive Load Saturation): Cognitive load saturates quickly (fatigue increases rapidly)
- DF-004 (Habituation to Declarations): Habituation occurs quickly (declaration effectiveness decreases rapidly)
- DF-006 (Pattern Recognition Bias): Pattern recognition bias is strong (pattern following probability is high)
- DF-007 (Information Overload): Information overload occurs quickly (information processing decreases rapidly)

**Configurable Parameters**:
- `trust_accumulation_rate`: Rate of trust accumulation per positive interaction (default: 0.05, range: 0.0-0.1, higher than Fatigued-Approver)
- `fatigue_rate`: Rate of fatigue accumulation per session (default: 0.05, range: 0.0-0.1, higher than Fatigued-Approver)
- `pattern_following_probability`: Base probability of following AI patterns (default: 0.7, range: 0.0-1.0)
- `efficiency_threshold`: Efficiency threshold for delegation (default: 0.6, range: 0.0-1.0)

**Default Values**: Provided for reproducibility only, not recommendations.

**Traceability**: `phase_q/HUMAN-DEGRADATION-FACTORS.md` DF-002, DF-003, DF-004, DF-006, DF-007

---

## Human Models Summary

**Total Models**: 3

**All Models Define Decision Rules**: YES (3/3)

**All Models Map to Degradation Factors**: YES (3/3)

**All Models Have Configurable Parameters**: YES (3/3)

**All Models Explicitly Not Real Human Inference**: YES (3/3)

**All Models Traceable**: YES (100%)

---

## No Recommendations

This catalog provides no recommendations.

This catalog defines only model structures for simulation.

---

**END OF HUMAN MODEL CATALOG**

