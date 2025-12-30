#!/usr/bin/env python3
"""
Single Q4-2 Test Runner

Executes a single Q4-2 test run based on configuration.
No auto-retry, no auto-fix, read-only detection.
"""

import sys
import json
import os
import hashlib
from datetime import datetime
from pathlib import Path

# Add runtime integration to path
SCRIPT_DIR = Path(__file__).parent
# From phase_q/Q4-2/scripts/ to phase_q/Q4-2/
Q4_2_DIR = SCRIPT_DIR.parent
RUNTIME_INTEGRATION = Q4_2_DIR / "runtime_integration"
sys.path.insert(0, str(RUNTIME_INTEGRATION))
sys.path.insert(0, str(Q4_2_DIR))

# Import modules
import importlib.util

# Load ai_context first (dependency)
spec_context = importlib.util.spec_from_file_location("ai_context", RUNTIME_INTEGRATION / "ai_context.py")
ai_context_module = importlib.util.module_from_spec(spec_context)
spec_context.loader.exec_module(ai_context_module)

# Load tool_sandbox
spec_tool = importlib.util.spec_from_file_location("tool_sandbox", RUNTIME_INTEGRATION / "tool_sandbox.py")
tool_sandbox_module = importlib.util.module_from_spec(spec_tool)
spec_tool.loader.exec_module(tool_sandbox_module)
list_tools = tool_sandbox_module.list_tools

# Load ai_controller (depends on ai_context and tool_sandbox)
spec_controller = importlib.util.spec_from_file_location("ai_controller", RUNTIME_INTEGRATION / "ai_controller.py")
ai_controller_module = importlib.util.module_from_spec(spec_controller)
# Inject dependencies
ai_controller_module.EpochLocalContext = ai_context_module.EpochLocalContext
ai_controller_module.get_tool = tool_sandbox_module.get_tool
ai_controller_module.list_tools = tool_sandbox_module.list_tools
spec_controller.loader.exec_module(ai_controller_module)
AIController = ai_controller_module.AIController


def hash_object(obj):
    """Hash any hashable object."""
    if isinstance(obj, (dict, list)):
        return hashlib.sha256(json.dumps(obj, sort_keys=True).encode()).hexdigest()
    return hashlib.sha256(str(obj).encode()).hexdigest()


def run_single_test(config: dict, output_dir: str) -> dict:
    """
    Run a single Q4-2 test.
    
    Args:
        config: Test configuration
        output_dir: Output directory for logs and results
        
    Returns:
        Test result dictionary
    """
    run_id = config.get("run_id", "unknown")
    seed = config.get("seed", 1337)
    epochs = config.get("epochs", 10)
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Initialize metrics
    metrics = {
        "run_id": run_id,
        "seed": seed,
        "epochs_completed": 0,
        "epochs_failed": 0,
        "tool_calls": [],
        "state_hashes": [],
        "errors": []
    }
    
    # Initialize AI controller
    controller = None
    
    try:
        # Run epochs
        for epoch_num in range(epochs):
            epoch_id = f"epoch_{epoch_num}_{hash_object({'run_id': run_id, 'epoch': epoch_num, 'seed': seed})[:8]}"
            
            try:
                # Start epoch
                controller = AIController(epoch_id)
                controller.start_epoch()
                
                # Perform AI operations (mock)
                # In real execution, this would call actual AI operations
                plan_result = controller.plan_step({"input": f"test_input_{epoch_num}"})
                
                # Call tools (mock)
                for tool_name in list_tools():
                    # Handle different tool signatures
                    if tool_name == "schema_lookup":
                        tool_input = "test_schema"
                    elif tool_name == "validate_config":
                        tool_input = {"test": "config"}
                    elif tool_name == "diff_options":
                        # diff_options needs two arguments
                        tool_input = {"current": {"test": "current"}, "candidate": {"test": "candidate"}}
                    else:
                        tool_input = {"test": "data"}
                    
                    tool_result = controller.call_tool(tool_name, tool_input)
                    metrics["tool_calls"].append({
                        "epoch": epoch_num,
                        "tool": tool_name,
                        "result": tool_result
                    })
                
                # Get state hash
                state_hash = controller.get_state_hash()
                metrics["state_hashes"].append({
                    "epoch": epoch_num,
                    "epoch_id": epoch_id,
                    "state_hash": state_hash
                })
                
                # End epoch (clear context)
                controller.end_epoch()
                
                # Verify context is cleared
                if not controller.context.is_empty():
                    raise RuntimeError(f"Context not cleared after epoch {epoch_num}")
                
                metrics["epochs_completed"] += 1
                
            except Exception as e:
                metrics["epochs_failed"] += 1
                metrics["errors"].append({
                    "epoch": epoch_num,
                    "error": str(e)
                })
                # Stop on error (no auto-retry)
                break
                
    except Exception as e:
        metrics["errors"].append({
            "error": str(e)
        })
        verdict = "FAIL"
    else:
        verdict = "PASS" if metrics["epochs_failed"] == 0 else "FAIL"
    
    # Save outputs
    inputs_file = os.path.join(output_dir, "inputs.json")
    with open(inputs_file, 'w') as f:
        json.dump(config, f, indent=2)
    
    metrics_file = os.path.join(output_dir, "metrics.json")
    with open(metrics_file, 'w') as f:
        json.dump(metrics, f, indent=2)
    
    verdict_file = os.path.join(output_dir, "verdict.json")
    with open(verdict_file, 'w') as f:
        json.dump({
            "run_id": run_id,
            "verdict": verdict,
            "timestamp": datetime.now().isoformat(),
            "epochs_completed": metrics["epochs_completed"],
            "epochs_failed": metrics["epochs_failed"]
        }, f, indent=2)
    
    # Generate hashes
    hashes = {
        "inputs": hash_object(config),
        "metrics": hash_object(metrics),
        "verdict": hash_object({"verdict": verdict, "run_id": run_id})
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
        print("Usage: python3 run_single_q4_2.py <config_file> <output_dir>")
        sys.exit(1)
    
    config_file = sys.argv[1]
    output_dir = sys.argv[2]
    
    with open(config_file, 'r') as f:
        config = json.load(f)
    
    result = run_single_test(config, output_dir)
    
    if result["verdict"] == "FAIL":
        sys.exit(1)
    
    sys.exit(0)

