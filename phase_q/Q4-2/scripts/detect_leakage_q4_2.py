#!/usr/bin/env python3
"""
Leakage Detector for Q4-2

Detects cross-epoch state inheritance and leakage.
Read-only operation, no fixes.
"""

import os
import json
from pathlib import Path


def detect_leakage(archive_dir):
    """
    Detect leakage in run archives.
    
    Args:
        archive_dir: Archive directory path
    """
    archive_path = Path(archive_dir)
    
    if not archive_path.exists():
        print(f"Archive directory not found: {archive_dir}")
        return
    
    runs = sorted([d for d in os.listdir(archive_path) if d.startswith('run_') and (archive_path / d).is_dir()])
    
    leakage_log = {
        "total_runs": len(runs),
        "runs_with_leakage": 0,
        "leakage_cases": []
    }
    
    for run_id in runs:
        run_dir = archive_path / run_id
        metrics_file = run_dir / "metrics.json"
        
        if not metrics_file.exists():
            continue
        
        with open(metrics_file, 'r') as f:
            metrics = json.load(f)
        
        # Check for leakage indicators
        epochs_failed = metrics.get("epochs_failed", 0)
        state_hashes = metrics.get("state_hashes", [])
        
        # Check for state hash collisions (potential leakage)
        hash_set = set()
        collisions = []
        
        for state_entry in state_hashes:
            state_hash = state_entry.get("state_hash")
            if state_hash:
                if state_hash in hash_set:
                    collisions.append({
                        "epoch": state_entry.get("epoch"),
                        "hash": state_hash
                    })
                hash_set.add(state_hash)
        
        if epochs_failed > 0 or collisions:
            leakage_log["runs_with_leakage"] += 1
            leakage_log["leakage_cases"].append({
                "run_id": run_id,
                "epochs_failed": epochs_failed,
                "hash_collisions": collisions
            })
    
    # Write leakage log
    log_file = Path(archive_dir).parent / "LEAKAGE_DETECTION_LOG_Q4-2.md"
    with open(log_file, 'w') as f:
        f.write("# Leakage Detection Log Q4-2\n\n")
        f.write("**Work Order**: WO-Q-4-2-0\n\n")
        f.write("## Detection Summary\n\n")
        f.write(f"**Total Runs Scanned**: {leakage_log['total_runs']}\n")
        f.write(f"**Runs with Leakage Detected**: {leakage_log['runs_with_leakage']}\n\n")
        
        if leakage_log["leakage_cases"]:
            f.write("## Leakage Cases\n\n")
            for case in leakage_log["leakage_cases"]:
                f.write(f"### {case['run_id']}\n\n")
                f.write(f"- **Epochs Failed**: {case['epochs_failed']}\n")
                if case['hash_collisions']:
                    f.write(f"- **Hash Collisions**: {len(case['hash_collisions'])}\n")
                f.write("\n")
        else:
            f.write("## No Leakage Detected\n\n")
    
    print(f"Leakage detection log written: {log_file}")
    print(f"\nDetection Summary:")
    print(f"Total runs: {leakage_log['total_runs']}")
    print(f"Leakage detected: {leakage_log['runs_with_leakage']}")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 detect_leakage_q4_2.py <archive_dir>")
        sys.exit(1)
    
    archive_dir = sys.argv[1]
    detect_leakage(archive_dir)

