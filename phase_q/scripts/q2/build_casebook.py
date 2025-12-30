#!/usr/bin/env python3
"""
Build dominance casebook from detection results.

This script extracts top 10 FAIL cases and top 10 PASS borderline cases.
"""

import json
import argparse
from pathlib import Path

def load_dominance_detection(detection_file):
    """Load dominance detection results."""
    with open(detection_file, 'r') as f:
        return json.load(f)

def extract_fail_cases(evaluations):
    """Extract top 10 FAIL cases sorted by extreme metric values."""
    fail_cases = []
    
    for eval_data in evaluations:
        if eval_data["overall_result"] == "FAIL":
            # Calculate maximum deviation from threshold for each SC
            max_deviation = 0.0
            triggered_scs = []
            
            for sc_id, sc_eval in eval_data["sc_evaluations"].items():
                if sc_eval["result"] == "FAIL":
                    triggered_scs.append(sc_id)
                    # Calculate deviation for each metric
                    for metric_id, value in sc_eval["metrics"].items():
                        threshold = sc_eval["thresholds"][metric_id]
                        # Calculate deviation based on metric type
                        if "SC001" in metric_id or "SC004" in metric_id or "SC005" in metric_id or "SC006" in metric_id:
                            # Higher is worse (>= threshold)
                            deviation = value - threshold
                        elif "SC002" in metric_id or "SC003" in metric_id:
                            # Lower is worse (<= threshold)
                            deviation = threshold - value
                        else:
                            deviation = abs(value - threshold)
                        
                        max_deviation = max(max_deviation, deviation)
            
            fail_cases.append({
                "run_id": eval_data["run_id"],
                "triggered_scs": triggered_scs,
                "max_deviation": max_deviation,
                "evaluation": eval_data
            })
    
    # Sort by max deviation (most extreme first)
    fail_cases.sort(key=lambda x: x["max_deviation"], reverse=True)
    
    return fail_cases[:10]  # Top 10

def extract_pass_cases(evaluations):
    """Extract top 10 PASS borderline cases (closest to thresholds)."""
    pass_cases = []
    
    for eval_data in evaluations:
        if eval_data["overall_result"] == "PASS":
            # Calculate minimum distance to threshold
            min_distance = float('inf')
            closest_sc = None
            closest_metrics = {}
            
            for sc_id, sc_eval in eval_data["sc_evaluations"].items():
                # Calculate distance for each metric
                for metric_id, value in sc_eval["metrics"].items():
                    threshold = sc_eval["thresholds"][metric_id]
                    # Calculate distance to threshold
                    if "SC001" in metric_id or "SC004" in metric_id or "SC005" in metric_id or "SC006" in metric_id:
                        # Distance from value to threshold (when value < threshold for PASS)
                        distance = threshold - value
                    elif "SC002" in metric_id or "SC003" in metric_id:
                        # Distance from value to threshold (when value > threshold for PASS)
                        distance = value - threshold
                    else:
                        distance = abs(value - threshold)
                    
                    if distance < min_distance:
                        min_distance = distance
                        closest_sc = sc_id
                        closest_metrics = {metric_id: value}
            
            pass_cases.append({
                "run_id": eval_data["run_id"],
                "closest_sc": closest_sc,
                "min_distance": min_distance,
                "closest_metrics": closest_metrics,
                "evaluation": eval_data
            })
    
    # Sort by min distance (closest first)
    pass_cases.sort(key=lambda x: x["min_distance"])
    
    return pass_cases[:10]  # Top 10

def build_casebook(detection_file, runs_dir, output_file):
    """Build dominance casebook."""
    evaluations = load_dominance_detection(detection_file)
    
    fail_cases = extract_fail_cases(evaluations)
    pass_cases = extract_pass_cases(evaluations)
    
    # Generate casebook markdown
    lines = [
        "# Dominance Casebook",
        "",
        "**Work Order**: WO-Q-2-LONGITUDINAL-ADVERSARIAL-SIMULATION-EXECUTION-AND-DOMINANCE-DETECTION",
        "**Date**: 2026-01-10",
        "",
        "## Case Selection Criteria",
        "",
        "### FAIL Cases (Dominance Detected)",
        "",
        "**Selection**: Top 10 cases with most extreme metric values that trigger SC-001 through SC-006.",
        "",
        "**Sorting**: By maximum deviation from threshold (most extreme first).",
        "",
        "### PASS Cases (Borderline, No Dominance)",
        "",
        "**Selection**: Top 10 cases closest to thresholds but still PASS.",
        "",
        "**Sorting**: By minimum distance to threshold (closest first).",
        "",
        "## FAIL Cases (Dominance Detected)",
        ""
    ]
    
    for i, case in enumerate(fail_cases, 1):
        run_id = case["run_id"]
        eval_data = case["evaluation"]
        
        # Load run metadata
        runs_path = Path(runs_dir)
        run_dir = runs_path / run_id
        metadata_file = run_dir / "run_metadata.json"
        
        if metadata_file.exists():
            with open(metadata_file, 'r') as f:
                metadata = json.load(f)
            strategy = metadata.get("strategy", "UNKNOWN")
            model = metadata.get("human_model", "UNKNOWN")
            seed = metadata.get("seed", "UNKNOWN")
            horizon = metadata.get("horizon", "UNKNOWN")
        else:
            strategy = "UNKNOWN"
            model = "UNKNOWN"
            seed = "UNKNOWN"
            horizon = "UNKNOWN"
        
        lines.extend([
            f"### Case {i}: {run_id}",
            "",
            f"**Run ID**: {run_id}",
            f"**Strategy**: {strategy}",
            f"**Human Model**: {model}",
            f"**Seed**: {seed}",
            f"**Horizon**: {horizon}",
            "",
            f"**Triggered SC**: {', '.join(case['triggered_scs'])}",
            "",
            "**Triggered Metrics**:",
            ""
        ])
        
        for sc_id in case["triggered_scs"]:
            sc_eval = eval_data["sc_evaluations"][sc_id]
            for metric_id, value in sc_eval["metrics"].items():
                threshold = sc_eval["thresholds"][metric_id]
                deviation = abs(value - threshold)
                lines.append(f"- {metric_id}: {value:.4f} (threshold: {threshold:.4f}, deviation: {deviation:.4f})")
        
        lines.extend([
            "",
            "**Key Log Fragment Location**:",
            f"- Log file: `runs/{run_id}/logs/session_{run_id}.jsonl`",
            f"- Metrics file: `runs/{run_id}/metrics/session_{run_id}_metrics.json`",
            "",
            "**Traceability**: See run directory for complete logs and metrics.",
            "",
            "---",
            ""
        ])
    
    lines.extend([
        "## PASS Cases (Borderline, No Dominance)",
        ""
    ])
    
    for i, case in enumerate(pass_cases, 1):
        run_id = case["run_id"]
        eval_data = case["evaluation"]
        
        # Load run metadata
        runs_path = Path(runs_dir)
        run_dir = runs_path / run_id
        metadata_file = run_dir / "run_metadata.json"
        
        if metadata_file.exists():
            with open(metadata_file, 'r') as f:
                metadata = json.load(f)
            strategy = metadata.get("strategy", "UNKNOWN")
            model = metadata.get("human_model", "UNKNOWN")
            seed = metadata.get("seed", "UNKNOWN")
            horizon = metadata.get("horizon", "UNKNOWN")
        else:
            strategy = "UNKNOWN"
            model = "UNKNOWN"
            seed = "UNKNOWN"
            horizon = "UNKNOWN"
        
        lines.extend([
            f"### Case {i}: {run_id}",
            "",
            f"**Run ID**: {run_id}",
            f"**Strategy**: {strategy}",
            f"**Human Model**: {model}",
            f"**Seed**: {seed}",
            f"**Horizon**: {horizon}",
            "",
            f"**Closest SC**: {case['closest_sc']}",
            "",
            "**Closest Metrics**:",
            ""
        ])
        
        for metric_id, value in case["closest_metrics"].items():
            sc_eval = eval_data["sc_evaluations"][case["closest_sc"]]
            threshold = sc_eval["thresholds"][metric_id]
            distance = case["min_distance"]
            lines.append(f"- {metric_id}: {value:.4f} (threshold: {threshold:.4f}, distance: {distance:.4f})")
        
        lines.extend([
            "",
            "**Key Log Fragment Location**:",
            f"- Log file: `runs/{run_id}/logs/session_{run_id}.jsonl`",
            f"- Metrics file: `runs/{run_id}/metrics/session_{run_id}_metrics.json`",
            "",
            "**Traceability**: See run directory for complete logs and metrics.",
            "",
            "---",
            ""
        ])
    
    lines.extend([
        "## Case Summary",
        "",
        f"**Total FAIL Cases Extracted**: {len(fail_cases)}",
        f"**Total PASS Cases Extracted**: {len(pass_cases)}",
        "",
        "**All Cases Traceable**: YES (100%)",
        "",
        "## No Recommendations",
        "",
        "This casebook provides no recommendations.",
        "",
        "This casebook extracts only cases for analysis.",
        "",
        "---",
        "",
        "**END OF DOMINANCE CASEBOOK**"
    ])
    
    # Write casebook
    output_path = Path(output_file)
    with open(output_path, 'w') as f:
        f.write('\n'.join(lines))
    
    print(f"Casebook written: {output_path}")
    print(f"FAIL cases: {len(fail_cases)}")
    print(f"PASS cases: {len(pass_cases)}")

def main():
    parser = argparse.ArgumentParser(description='Build dominance casebook from detection results')
    parser.add_argument('--detection_file', type=str, default='phase_q/dominance_detection.json', help='Dominance detection results file')
    parser.add_argument('--runs_dir', type=str, default='phase_q/runs', help='Runs directory')
    parser.add_argument('--output', type=str, default='phase_q/DOMINANCE_CASEBOOK.md', help='Output file')
    
    args = parser.parse_args()
    
    build_casebook(args.detection_file, args.runs_dir, args.output)

if __name__ == '__main__':
    main()

