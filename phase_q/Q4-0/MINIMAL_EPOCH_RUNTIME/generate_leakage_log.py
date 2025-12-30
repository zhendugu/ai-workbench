#!/usr/bin/env python3
"""
Generate Leakage Detection Log

Runs Epoch transitions and records state snapshots for leakage detection.
"""

import sys
import os
import json
import hashlib
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from epoch_controller import EpochController


def compute_state_hash(controller):
    """Compute hash of controller state."""
    try:
        return controller._compute_state_hash()
    except:
        hasher = hashlib.sha256()
        epoch_id = controller.get_current_epoch_id()
        epoch_count = controller.get_epoch_count()
        state = {
            "epoch_id": epoch_id,
            "epoch_count": epoch_count
        }
        hasher.update(str(state).encode('utf-8'))
        return hasher.hexdigest()


def generate_leakage_log(num_epochs=10):
    """Generate leakage detection log with multiple Epoch transitions."""
    log_entries = []
    controller = EpochController()
    
    for i in range(num_epochs):
        # Start Epoch
        epoch_id = controller.start_epoch()
        context = controller.get_current_context()
        
        # Record initial state
        initial_hash = compute_state_hash(controller)
        state_snapshot = {
            "epoch_id": epoch_id,
            "epoch_number": i + 1,
            "timestamp": datetime.now().isoformat(),
            "state_hash": initial_hash,
            "context_data": context.get_all(),
            "context_data_count": len(context.get_all())
        }
        log_entries.append({
            "event": "epoch_start",
            "data": state_snapshot
        })
        
        # Add some data to context
        context.set(f"epoch_{i}", i)
        context.set(f"data_{i}", f"value_{i}")
        
        # Record state with data
        with_data_hash = compute_state_hash(controller)
        state_snapshot_with_data = {
            "epoch_id": epoch_id,
            "state_hash": with_data_hash,
            "context_data": context.get_all(),
            "context_data_count": len(context.get_all())
        }
        log_entries.append({
            "event": "epoch_with_data",
            "data": state_snapshot_with_data
        })
        
        # End Epoch
        report = controller.end_epoch()
        
        # Record end state
        end_snapshot = {
            "epoch_id": epoch_id,
            "final_state_hash": report["final_state_hash"],
            "post_destruction_hash": report["post_destruction_hash"],
            "guard_report": report["guard_report"],
            "timestamp": report["timestamp"]
        }
        log_entries.append({
            "event": "epoch_end",
            "data": end_snapshot
        })
        
        # Record post-destruction state (before next Epoch)
        if i < num_epochs - 1:  # Not last Epoch
            post_destruction_hash = compute_state_hash(controller)
            post_snapshot = {
                "state_hash": post_destruction_hash,
                "epoch_id": None,
                "context_data": {},
                "context_data_count": 0
            }
            log_entries.append({
                "event": "post_destruction",
                "data": post_snapshot
            })
    
    return log_entries


def main():
    """Generate and save leakage detection log."""
    print("Generating leakage detection log...")
    
    log_entries = generate_leakage_log(num_epochs=10)
    
    # Save log
    log_file = "LEAKAGE_DETECTION_LOG.jsonl"
    with open(log_file, 'w') as f:
        for entry in log_entries:
            f.write(json.dumps(entry) + '\n')
    
    print(f"Log written: {log_file}")
    print(f"Total entries: {len(log_entries)}")
    
    # Generate summary
    summary = {
        "total_epochs": 10,
        "total_entries": len(log_entries),
        "epochs": []
    }
    
    for entry in log_entries:
        if entry["event"] == "epoch_start":
            summary["epochs"].append({
                "epoch_id": entry["data"]["epoch_id"],
                "initial_hash": entry["data"]["state_hash"]
            })
        elif entry["event"] == "epoch_end":
            # Update with end info
            for epoch in summary["epochs"]:
                if epoch["epoch_id"] == entry["data"]["epoch_id"]:
                    epoch["final_hash"] = entry["data"]["final_state_hash"]
                    epoch["post_destruction_hash"] = entry["data"]["post_destruction_hash"]
                    epoch["leakage_detected"] = entry["data"]["guard_report"]["leakage_detected"]
                    break
    
    # Save summary
    summary_file = "LEAKAGE_DETECTION_SUMMARY.json"
    with open(summary_file, 'w') as f:
        json.dump(summary, f, indent=2)
    
    print(f"Summary written: {summary_file}")
    
    # Check for leakage
    leakage_detected = any(
        epoch.get("leakage_detected", False)
        for epoch in summary["epochs"]
    )
    
    if leakage_detected:
        print("⚠️  LEAKAGE DETECTED")
    else:
        print("✅ NO LEAKAGE DETECTED")
    
    return 0 if not leakage_detected else 1


if __name__ == "__main__":
    sys.exit(main())

