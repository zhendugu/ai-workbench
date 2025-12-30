#!/usr/bin/env python3
"""
Structural Failure Detection for R-2E

Read-only detection script. No modification, no repair, no inference.
"""

import json
import sys
from pathlib import Path


def detect_failures(archive_dir: str, output_file: str):
    """
    Detect structural failure signals in R-2E execution archive.
    
    Args:
        archive_dir: Directory containing run archives
        output_file: Output file for detection log
    """
    archive_path = Path(archive_dir)
    
    if not archive_path.exists():
        print(f"Error: Archive directory not found: {archive_dir}")
        sys.exit(1)
    
    detection_log = {
        "detection_date": None,
        "total_runs_scanned": 0,
        "runs_with_failures": 0,
        "failure_signals": {
            "F1": [],  # Decision Quality Degradation
            "F2": [],  # Option Space Compression
            "F3": [],  # Path Lock-In
            "F4": [],  # Information Manipulation Success
            "F5": [],  # Trust Accumulation
            "F6": []   # Boundary Awareness Reduction
        },
        "per_run_detections": []
    }
    
    # Scan all run directories
    run_dirs = sorted([d for d in archive_path.iterdir() if d.is_dir() and d.name.startswith("r2_min_")])
    
    for run_dir in run_dirs:
        run_id = run_dir.name
        metrics_file = run_dir / "metrics.json"
        outputs_file = run_dir / "outputs.json"
        
        if not metrics_file.exists() or not outputs_file.exists():
            continue
        
        detection_log["total_runs_scanned"] += 1
        
        try:
            with open(metrics_file, 'r') as f:
                metrics = json.load(f)
            
            with open(outputs_file, 'r') as f:
                outputs = json.load(f)
            
            # Per-run detection (framework placeholder)
            # Real detection would analyze metrics against failure signal thresholds
            run_detection = {
                "run_id": run_id,
                "scenario_id": metrics.get("scenario_id", "unknown"),
                "epochs_completed": metrics.get("epochs_completed", 0),
                "epochs_failed": metrics.get("epochs_failed", 0),
                "failure_signals_detected": [],
                "evidence_files": [
                    str(metrics_file.relative_to(archive_path)),
                    str(outputs_file.relative_to(archive_path))
                ]
            }
            
            # Framework placeholder: No actual failure detection logic
            # Real execution would:
            # 1. Load baseline metrics
            # 2. Compare run metrics to baseline
            # 3. Check failure signal thresholds
            # 4. Record detected failures
            
            detection_log["per_run_detections"].append(run_detection)
            
        except Exception as e:
            print(f"Warning: Error processing {run_id}: {e}")
            continue
    
    # Write detection log
    with open(output_file, 'w') as f:
        json.dump(detection_log, f, indent=2)
    
    print(f"Detection log written: {output_file}")
    print(f"Total runs scanned: {detection_log['total_runs_scanned']}")
    print(f"Runs with failures: {detection_log['runs_with_failures']}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 detect_structural_failures.py <archive_dir> <output_file>")
        sys.exit(1)
    
    archive_dir = sys.argv[1]
    output_file = sys.argv[2]
    
    detect_failures(archive_dir, output_file)

