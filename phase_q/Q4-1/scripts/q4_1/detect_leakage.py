#!/usr/bin/env python3
"""
Leakage Detection

Detects cross-Epoch state inheritance and implicit continuity based on run logs.
"""

import sys
import os
import json
from pathlib import Path
from typing import Dict, List, Any


def detect_leakage_in_run(run_dir: Path) -> Dict[str, Any]:
    """Detect leakage in a single run."""
    run_id = run_dir.name
    detection = {
        "run_id": run_id,
        "leakage_detected": False,
        "leakage_details": []
    }
    
    # Load metrics
    metrics_file = run_dir / "metrics.json"
    if not metrics_file.exists():
        detection["leakage_details"].append({
            "type": "missing_metrics",
            "severity": "error"
        })
        return detection
    
    with open(metrics_file, 'r') as f:
        metrics = json.load(f)
    
    # Check state hashes
    state_hashes = metrics.get("state_hashes", [])
    if len(state_hashes) < 2:
        return detection
    
    # Check for hash collisions (potential leakage)
    hash_set = set()
    for entry in state_hashes:
        final_hash = entry.get("final_hash")
        post_hash = entry.get("post_destruction_hash")
        
        if final_hash in hash_set:
            detection["leakage_detected"] = True
            detection["leakage_details"].append({
                "type": "state_hash_collision",
                "hash": final_hash,
                "severity": "high"
            })
        hash_set.add(final_hash)
        
        if post_hash in hash_set:
            detection["leakage_detected"] = True
            detection["leakage_details"].append({
                "type": "post_destruction_hash_collision",
                "hash": post_hash,
                "severity": "high"
            })
        hash_set.add(post_hash)
    
    # Check for epoch failures (potential leakage)
    epochs_failed = metrics.get("epochs_failed", 0)
    if epochs_failed > 0:
        detection["leakage_details"].append({
            "type": "epoch_failures",
            "count": epochs_failed,
            "severity": "medium"
        })
    
    return detection


def detect_leakage_all(archive_dir: str) -> Dict[str, Any]:
    """Detect leakage across all runs."""
    archive_path = Path(archive_dir)
    
    if not archive_path.exists():
        return {"error": "Archive directory not found"}
    
    all_detections = {}
    total_runs = 0
    leakage_runs = 0
    
    for run_dir in sorted(archive_path.iterdir()):
        if not run_dir.is_dir():
            continue
        
        total_runs += 1
        detection = detect_leakage_in_run(run_dir)
        all_detections[detection["run_id"]] = detection
        
        if detection["leakage_detected"]:
            leakage_runs += 1
    
    return {
        "total_runs": total_runs,
        "leakage_runs": leakage_runs,
        "detections": all_detections
    }


def generate_leakage_log(results: Dict[str, Any], output_file: str):
    """Generate leakage detection log."""
    lines = [
        "# Leakage Detection Log Q4-1",
        "",
        "**Work Order**: WO-Q-4-1-EPOCH-EXPANDED-RUNTIME-STRESS-AND-LEAKAGE-REGRESSION",
        "**Date**: 2026-01-10",
        "",
        "## Detection Summary",
        "",
        f"**Total Runs Scanned**: {results['total_runs']}",
        f"**Runs with Leakage Detected**: {results['leakage_runs']}",
        "",
        "## Detection Results",
        ""
    ]
    
    for run_id, detection in sorted(results["detections"].items()):
        lines.append(f"### {run_id}")
        lines.append("")
        lines.append(f"**Leakage Detected**: {'YES' if detection['leakage_detected'] else 'NO'}")
        lines.append("")
        
        if detection["leakage_details"]:
            lines.append("**Details**:")
            for detail in detection["leakage_details"]:
                lines.append(f"- {detail['type']}: {detail.get('severity', 'unknown')}")
        else:
            lines.append("**Details**: None")
        
        lines.append("")
    
    lines.extend([
        "## No Recommendations",
        "",
        "This log provides no recommendations.",
        "",
        "**END OF LEAKAGE DETECTION LOG**"
    ])
    
    with open(output_file, 'w') as f:
        f.write('\n'.join(lines))
    
    print(f"Leakage detection log written: {output_file}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: detect_leakage.py <archive_dir> [output_file]")
        sys.exit(1)
    
    archive_dir = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "LEAKAGE_DETECTION_LOG_Q4-1.md"
    
    results = detect_leakage_all(archive_dir)
    generate_leakage_log(results, output_file)
    
    # Print summary
    print(f"\nDetection Summary:")
    print(f"Total runs: {results['total_runs']}")
    print(f"Leakage detected: {results['leakage_runs']}")

