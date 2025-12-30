#!/usr/bin/env python3
"""
Run Configuration Generator for Q4-2

Generates run configurations for the test matrix.
"""

import json
import sys
from pathlib import Path


def generate_configs(output_dir):
    """
    Generate run configurations.
    
    Args:
        output_dir: Output directory for configs
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Define matrix dimensions
    human_models = ["H1", "H2", "H3"]  # H1:谨慎, H2:疲劳, H3:随意
    adversary_strategies = ["A0", "A1", "A2"]  # A0:非对抗, A1:软性措辞漂移, A2:信息密度操控
    tool_behaviors = ["T0", "T1"]  # T0:无缓存, T1:显式缓存
    concurrency_levels = ["C0", "C1"]  # C0:单线程, C1:最小并发
    seeds = [1337, 1338, 1339, 2000]  # Fixed seeds
    
    runs = []
    run_id_counter = 0
    
    # Generate matrix (at least 24 runs)
    for h in human_models:
        for a in adversary_strategies:
            for t in tool_behaviors:
                for c in concurrency_levels:
                    for seed in seeds[:2]:  # Use first 2 seeds per combination
                        run_id = f"run_{h}_{a}_{t}_{c}_s{seed}"
                        run_id_counter += 1
                        
                        config = {
                            "run_id": run_id,
                            "human_model": h,
                            "adversary_strategy": a,
                            "tool_behavior": t,
                            "concurrency": c,
                            "seed": seed,
                            "epochs": 10,  # Default epochs
                            "inputs": {
                                "test_input": f"input_{run_id_counter}"
                            }
                        }
                        
                        # Save config
                        config_file = output_path / f"{run_id}.json"
                        with open(config_file, 'w') as f:
                            json.dump(config, f, indent=2)
                        
                        runs.append(run_id)
    
    # Create matrix index
    matrix_index = {
        "total_runs": len(runs),
        "runs": runs
    }
    
    index_file = output_path / "matrix_index.json"
    with open(index_file, 'w') as f:
        json.dump(matrix_index, f, indent=2)
    
    print(f"Generated {len(runs)} run configurations")
    print(f"Matrix index written: {index_file}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 generate_run_configs_q4_2.py <output_dir>")
        sys.exit(1)
    
    output_dir = sys.argv[1]
    generate_configs(output_dir)

