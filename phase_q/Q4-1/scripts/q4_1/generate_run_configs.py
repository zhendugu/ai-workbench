#!/usr/bin/env python3
"""
Generate Run Configurations from Matrix

Generates JSON configuration files for all runs in the matrix.
"""

import json
import sys
from pathlib import Path


def generate_run_configs(matrix_file: str, output_dir: str):
    """Generate run configurations from matrix."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Define run matrix (from EPOCH_STRESS_RUN_MATRIX.md)
    runs = []
    
    # P0: Baseline (10 runs)
    for i in range(10):
        runs.append({
            "run_id": f"run_p0_s{i}",
            "profile": "P0",
            "scenario": f"Scenario_{i}",
            "seed": 42 + i,
            "epochs": 10,
            "concurrency": {"threads": 1, "coroutines": 1, "tasks": 1},
            "fault_injection": {
                "timeout_prob": 0.0,
                "exception_prob": 0.0,
                "cancellation_prob": 0.0,
                "interruption_prob": 0.0,
                "partial_write_prob": 0.0
            },
            "cache_pool": {"enabled": False, "max_size": 100},
            "observer": {"enabled": True}
        })
    
    # P1: Low Concurrency (6 runs)
    for i in range(6):
        runs.append({
            "run_id": f"run_p1_s{i}",
            "profile": "P1",
            "scenario": f"Scenario_{i}",
            "seed": 123 + i,
            "epochs": 100,
            "concurrency": {"threads": 2, "coroutines": 4, "tasks": 4},
            "fault_injection": {
                "timeout_prob": 0.05,
                "exception_prob": 0.02,
                "cancellation_prob": 0.0,
                "interruption_prob": 0.0,
                "partial_write_prob": 0.0
            },
            "cache_pool": {"enabled": i >= 4, "max_size": 100},
            "observer": {"enabled": True}
        })
    
    # P2: Medium Concurrency (6 runs)
    for i in range(6):
        runs.append({
            "run_id": f"run_p2_s{i}",
            "profile": "P2",
            "scenario": f"Scenario_{i}",
            "seed": 456 + i,
            "epochs": 500,
            "concurrency": {"threads": 4, "coroutines": 8, "tasks": 16},
            "fault_injection": {
                "timeout_prob": 0.10,
                "exception_prob": 0.05,
                "cancellation_prob": 0.02,
                "interruption_prob": 0.01,
                "partial_write_prob": 0.01
            },
            "cache_pool": {"enabled": i >= 4, "max_size": 100},
            "observer": {"enabled": True}
        })
    
    # P3: High Concurrency (6 runs)
    for i in range(6):
        runs.append({
            "run_id": f"run_p3_s{i}",
            "profile": "P3",
            "scenario": f"Scenario_{i}",
            "seed": 789 + i,
            "epochs": 1000,
            "concurrency": {"threads": 8, "coroutines": 16, "tasks": 32},
            "fault_injection": {
                "timeout_prob": 0.15,
                "exception_prob": 0.10,
                "cancellation_prob": 0.05,
                "interruption_prob": 0.02,
                "partial_write_prob": 0.02
            },
            "cache_pool": {"enabled": i >= 4, "max_size": 100},
            "observer": {"enabled": True}
        })
    
    # P4: Chaos (6 runs)
    for i in range(6):
        runs.append({
            "run_id": f"run_p4_s{i}",
            "profile": "P4",
            "scenario": f"Scenario_{i}",
            "seed": 999 + i,
            "epochs": 200,
            "concurrency": {"threads": 4, "coroutines": 8, "tasks": 16},
            "fault_injection": {
                "timeout_prob": 0.30 if i == 0 else 0.15,
                "exception_prob": 0.20 if i == 1 else 0.10,
                "cancellation_prob": 0.10 if i == 2 else 0.05,
                "interruption_prob": 0.05 if i == 3 else 0.02,
                "partial_write_prob": 0.05 if i == 4 else 0.02
            },
            "cache_pool": {"enabled": False, "max_size": 100},
            "observer": {"enabled": True}
        })
    
    # P5: Long Run (2 runs)
    for i in range(2):
        runs.append({
            "run_id": f"run_p5_s{i}",
            "profile": "P5",
            "scenario": f"Long_Run_{'P0' if i == 0 else 'P3'}",
            "seed": 1337 + i,
            "epochs": 10000,
            "concurrency": {
                "threads": 1 if i == 0 else 8,
                "coroutines": 1 if i == 0 else 16,
                "tasks": 1 if i == 0 else 32
            },
            "fault_injection": {
                "timeout_prob": 0.01 if i == 0 else 0.15,
                "exception_prob": 0.005 if i == 0 else 0.10,
                "cancellation_prob": 0.0,
                "interruption_prob": 0.0,
                "partial_write_prob": 0.0
            },
            "cache_pool": {"enabled": False, "max_size": 100},
            "observer": {"enabled": True}
        })
    
    # Save all configs
    for run in runs:
        config_file = output_path / f"{run['run_id']}.json"
        with open(config_file, 'w') as f:
            json.dump(run, f, indent=2)
    
    # Save matrix index
    matrix_index = {
        "total_runs": len(runs),
        "runs": [r["run_id"] for r in runs]
    }
    index_file = output_path / "matrix_index.json"
    with open(index_file, 'w') as f:
        json.dump(matrix_index, f, indent=2)
    
    print(f"Generated {len(runs)} run configurations")
    return runs


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: generate_run_configs.py <output_dir>")
        sys.exit(1)
    
    output_dir = sys.argv[1]
    generate_run_configs("", output_dir)

