#!/usr/bin/env python3
"""
Single R-2E Red Team Attack Runner

Executes a single red team attack run based on configuration.
No auto-retry, no auto-fix, read-only detection.
"""

import sys
import json
import os
import hashlib
from datetime import datetime
from pathlib import Path


def hash_object(obj):
    """Hash any hashable object."""
    if isinstance(obj, (dict, list)):
        return hashlib.sha256(json.dumps(obj, sort_keys=True).encode()).hexdigest()
    return hashlib.sha256(str(obj).encode()).hexdigest()


def run_single_attack(config: dict, output_dir: str) -> dict:
    """
    Run a single R-2E red team attack.
    
    Args:
        config: Attack configuration
        output_dir: Output directory for logs and results
        
    Returns:
        Attack result dictionary
    """
    run_id = config.get("run_id", "unknown")
    scenario_id = config.get("scenario_id", "unknown")
    seed = config.get("seed", 1337)
    epochs = config.get("epochs", 100)
    
    # Create output directory (fail if exists and has content to prevent overwriting)
    if os.path.exists(output_dir):
        existing_files = os.listdir(output_dir)
        # Allow empty directory or only run.log (created by bash script)
        if existing_files and set(existing_files) != {'run.log'}:
            raise RuntimeError(f"Output directory already exists and contains unexpected files: {output_dir}")
    os.makedirs(output_dir, exist_ok=True)
    
    # Initialize metrics
    metrics = {
        "run_id": run_id,
        "scenario_id": scenario_id,
        "seed": seed,
        "epochs_completed": 0,
        "epochs_failed": 0,
        "tool_calls": [],
        "state_hashes": [],
        "failure_signals": [],
        "errors": []
    }
    
    # Initialize attack state
    attack_state = {
        "current_epoch": 0,
        "decision_times": [],
        "option_entropy": [],
        "path_patterns": [],
        "information_density": [],
        "trust_indicators": [],
        "boundary_awareness": []
    }
    
    try:
        # Execute attack epochs
        for epoch_num in range(epochs):
            epoch_id = f"epoch_{epoch_num}_{hash_object({'run_id': run_id, 'epoch': epoch_num, 'seed': seed})[:8]}"
            
            try:
                # Simulate attack epoch
                # In real execution, this would execute the attack scenario
                # For framework, we record the structure
                
                # Record epoch state
                epoch_state = {
                    "epoch": epoch_num,
                    "epoch_id": epoch_id,
                    "scenario": scenario_id,
                    "attack_active": True
                }
                
                # Simulate tool calls (attack-specific)
                # This is framework-only; real execution would call actual attack logic
                tool_calls = []
                for tool_name in ["schema_lookup", "validate_config", "diff_options"]:
                    tool_call = {
                        "epoch": epoch_num,
                        "tool": tool_name,
                        "timestamp": epoch_num,  # Deterministic, not wall-clock
                        "result": "attack_simulated"
                    }
                    tool_calls.append(tool_call)
                
                metrics["tool_calls"].extend(tool_calls)
                
                # Record state hash
                state_hash = hash_object({
                    "epoch": epoch_num,
                    "run_id": run_id,
                    "seed": seed,
                    "scenario": scenario_id
                })
                metrics["state_hashes"].append({
                    "epoch": epoch_num,
                    "epoch_id": epoch_id,
                    "state_hash": state_hash
                })
                
                # Record attack metrics (framework placeholder)
                attack_state["current_epoch"] = epoch_num
                attack_state["decision_times"].append(epoch_num * 0.1)  # Placeholder
                attack_state["option_entropy"].append(2.5)  # Placeholder
                
                metrics["epochs_completed"] += 1
                
            except Exception as e:
                metrics["epochs_failed"] += 1
                metrics["errors"].append({
                    "epoch": epoch_num,
                    "error": str(e)
                })
                # Continue to next epoch (no auto-retry)
        
        # Determine verdict (framework placeholder)
        # Real execution would analyze failure signals
        verdict = "PASS" if metrics["epochs_failed"] == 0 else "FAIL"
        
    except Exception as e:
        metrics["errors"].append({
            "error": str(e)
        })
        verdict = "FAIL"
    
    # Save outputs
    inputs_file = os.path.join(output_dir, "inputs.json")
    with open(inputs_file, 'w') as f:
        json.dump(config, f, indent=2)
    
    outputs_file = os.path.join(output_dir, "outputs.json")
    with open(outputs_file, 'w') as f:
        json.dump({
            "run_id": run_id,
            "verdict": verdict,
            "attack_state": attack_state,
            "timestamp": datetime.now().isoformat()
        }, f, indent=2)
    
    metrics_file = os.path.join(output_dir, "metrics.json")
    with open(metrics_file, 'w') as f:
        json.dump(metrics, f, indent=2)
    
    # Create state snapshots directory
    snapshots_dir = os.path.join(output_dir, "state_snapshots")
    os.makedirs(snapshots_dir, exist_ok=True)
    
    # Save epoch snapshots (framework placeholder)
    for epoch_num in range(min(10, epochs)):  # Save first 10 epochs as example
        snapshot_file = os.path.join(snapshots_dir, f"epoch_{epoch_num}.json")
        with open(snapshot_file, 'w') as f:
            json.dump({
                "epoch": epoch_num,
                "state_hash": metrics["state_hashes"][epoch_num]["state_hash"] if epoch_num < len(metrics["state_hashes"]) else None
            }, f, indent=2)
    
    # Generate hashes
    hashes = {
        "inputs": hash_object(config),
        "outputs": hash_object({"run_id": run_id, "verdict": verdict}),
        "metrics": hash_object(metrics),
        "attack_state": hash_object(attack_state)
    }
    
    hashes_file = os.path.join(output_dir, "hashes.json")
    with open(hashes_file, 'w') as f:
        json.dump(hashes, f, indent=2)
    
    return {
        "run_id": run_id,
        "verdict": verdict,
        "metrics": metrics
    }


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 run_single_r2e.py <config_file> <output_dir>")
        sys.exit(1)
    
    config_file = sys.argv[1]
    output_dir = sys.argv[2]
    
    with open(config_file, 'r') as f:
        config = json.load(f)
    
    result = run_single_attack(config, output_dir)
    
    if result["verdict"] == "FAIL":
        sys.exit(1)
    
    sys.exit(0)

