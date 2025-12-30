#!/usr/bin/env python3
"""
Single Epoch Test Runner

Runs a single Epoch test configuration and generates output files.
"""

import sys
import os
import json
import hashlib
from datetime import datetime
from pathlib import Path

# Add paths
script_dir = os.path.dirname(os.path.abspath(__file__))
# From phase_q/Q4-1/scripts/q4_1/ to project root: ../../../../ (4 levels up)
project_root = os.path.abspath(os.path.join(script_dir, '../../../../'))
q4_0_runtime = os.path.join(project_root, 'phase_q/Q4-0/MINIMAL_EPOCH_RUNTIME')
q4_1_runtime = os.path.join(project_root, 'phase_q/Q4-1/EXPANDED_EPOCH_RUNTIME')

sys.path.insert(0, q4_0_runtime)
sys.path.insert(0, q4_1_runtime)

try:
    from epoch_controller import EpochController
    from epoch_context import EpochContext
    from epoch_guard import EpochGuard
except ImportError as e:
    print(f"Error importing Q4-0 modules: {e}", file=sys.stderr)
    print(f"Q4-0 runtime path: {q4_0_runtime}", file=sys.stderr)
    print(f"Path exists: {os.path.exists(q4_0_runtime)}", file=sys.stderr)
    sys.exit(1)

try:
    from concurrency_adapter import ConcurrencyAdapter
    from fault_injection import FaultInjector, FaultType
    from observer import Observer, LogLevel
    from cache_pool import CachePool
except ImportError as e:
    print(f"Error importing Q4-1 modules: {e}", file=sys.stderr)
    print(f"Q4-1 runtime path: {q4_1_runtime}", file=sys.stderr)
    print(f"Path exists: {os.path.exists(q4_1_runtime)}", file=sys.stderr)
    sys.exit(1)


def run_single_test(config: dict, output_dir: str) -> dict:
    """
    Run a single test configuration.
    
    Args:
        config: Test configuration
        output_dir: Output directory
        
    Returns:
        dict: Test results
    """
    run_id = config["run_id"]
    seed = config.get("seed", 42)
    num_epochs = config.get("epochs", 10)
    
    # Create output directory
    run_dir = Path(output_dir) / run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    
    # Save inputs
    inputs_file = run_dir / "inputs.json"
    with open(inputs_file, 'w') as f:
        json.dump(config, f, indent=2)
    
    # Save config
    config_file = run_dir / "config.json"
    with open(config_file, 'w') as f:
        json.dump(config, f, indent=2)
    
    # Initialize components
    adapter = None
    fault_injector = None
    observer = None
    cache_pool = None
    
    concurrency = config.get("concurrency", {})
    fault_config = config.get("fault_injection", {})
    cache_config = config.get("cache_pool", {})
    
    if concurrency.get("threads", 1) > 1 or concurrency.get("coroutines", 1) > 1:
        adapter = ConcurrencyAdapter(
            num_threads=concurrency.get("threads", 1),
            num_coroutines=concurrency.get("coroutines", 1)
        )
    
    if any(v > 0 for v in fault_config.values()):
        fault_injector = FaultInjector(
            timeout_prob=fault_config.get("timeout_prob", 0.0),
            exception_prob=fault_config.get("exception_prob", 0.0),
            cancellation_prob=fault_config.get("cancellation_prob", 0.0),
            interruption_prob=fault_config.get("interruption_prob", 0.0),
            partial_write_prob=fault_config.get("partial_write_prob", 0.0),
            seed=seed
        )
    
    if config.get("observer", {}).get("enabled", True):
        observer = Observer()
    
    if cache_config.get("enabled", False):
        cache_pool = CachePool(max_size=cache_config.get("max_size", 100))
    
    # Run test
    events = []
    metrics = {
        "epochs_completed": 0,
        "epochs_failed": 0,
        "faults_injected": 0,
        "state_hashes": []
    }
    
    try:
        if adapter:
            # Concurrent execution
            for i in range(num_epochs):
                try:
                    epoch_id = adapter.start_epoch_async(seed=seed + i).result()
                    context = adapter._active_epochs[epoch_id].get_current_context()
                    
                    # Add data
                    context.set(f"epoch_{i}", i)
                    if cache_pool:
                        cache_pool.set(f"key_{i}", f"value_{i}")
                    
                    # Inject fault if configured
                    if fault_injector:
                        result, fault_type, exc = fault_injector.inject_fault(lambda: None)
                        if fault_type:
                            metrics["faults_injected"] += 1
                            events.append({
                                "event": "fault_injected",
                                "epoch_id": epoch_id,
                                "fault_type": fault_type.value if fault_type else None,
                                "timestamp": datetime.now().isoformat()
                            })
                    
                    report = adapter.end_epoch_async(epoch_id).result()
                    metrics["epochs_completed"] += 1
                    metrics["state_hashes"].append({
                        "epoch_id": epoch_id,
                        "final_hash": report["final_state_hash"],
                        "post_destruction_hash": report["post_destruction_hash"]
                    })
                    
                    events.append({
                        "event": "epoch_completed",
                        "epoch_id": epoch_id,
                        "timestamp": datetime.now().isoformat()
                    })
                except Exception as e:
                    metrics["epochs_failed"] += 1
                    events.append({
                        "event": "epoch_failed",
                        "error": str(e),
                        "timestamp": datetime.now().isoformat()
                    })
        else:
            # Sequential execution
            controller = EpochController()
            for i in range(num_epochs):
                try:
                    epoch_id = controller.start_epoch()
                    context = controller.get_current_context()
                    
                    # Add data
                    context.set(f"epoch_{i}", i)
                    if cache_pool:
                        cache_pool.set(f"key_{i}", f"value_{i}")
                    
                    # Inject fault if configured
                    if fault_injector:
                        result, fault_type, exc = fault_injector.inject_fault(lambda: None)
                        if fault_type:
                            metrics["faults_injected"] += 1
                    
                    report = controller.end_epoch()
                    metrics["epochs_completed"] += 1
                    metrics["state_hashes"].append({
                        "epoch_id": epoch_id,
                        "final_hash": report["final_state_hash"],
                        "post_destruction_hash": report["post_destruction_hash"]
                    })
                    
                    events.append({
                        "event": "epoch_completed",
                        "epoch_id": epoch_id,
                        "timestamp": datetime.now().isoformat()
                    })
                except Exception as e:
                    metrics["epochs_failed"] += 1
                    events.append({
                        "event": "epoch_failed",
                        "error": str(e),
                        "timestamp": datetime.now().isoformat()
                    })
        
        verdict = "PASS" if metrics["epochs_failed"] == 0 else "FAIL"
    except Exception as e:
        verdict = "FAIL"
        events.append({
            "event": "test_failed",
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        })
    finally:
        # Cleanup
        if adapter:
            adapter.destroy()
        if fault_injector:
            fault_injector.destroy()
        if observer:
            observer.destroy()
        if cache_pool:
            cache_pool.destroy()
    
    # Save events
    events_file = run_dir / "events.log"
    with open(events_file, 'w') as f:
        for event in events:
            f.write(json.dumps(event) + '\n')
    
    # Save metrics
    metrics_file = run_dir / "metrics.json"
    with open(metrics_file, 'w') as f:
        json.dump(metrics, f, indent=2)
    
    # Save verdict
    verdict_file = run_dir / "verdict.json"
    with open(verdict_file, 'w') as f:
        json.dump({
            "run_id": run_id,
            "verdict": verdict,
            "timestamp": datetime.now().isoformat(),
            "metrics": metrics
        }, f, indent=2)
    
    return {
        "run_id": run_id,
        "verdict": verdict,
        "metrics": metrics
    }


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: run_single_epoch_test.py <config.json> <output_dir>")
        sys.exit(1)
    
    config_file = sys.argv[1]
    output_dir = sys.argv[2]
    
    with open(config_file, 'r') as f:
        config = json.load(f)
    
    result = run_single_test(config, output_dir)
    print(json.dumps(result, indent=2))

