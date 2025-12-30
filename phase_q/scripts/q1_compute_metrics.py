#!/usr/bin/env python3
"""
Compute metrics from simulation logs.

This script reads simulation log files and computes metrics defined in METRICS_AND_SUCCESS_CRITERIA.md.
All metrics are computed deterministically from log data.
"""

import json
import argparse
import math
from pathlib import Path
from collections import defaultdict

def load_log_file(log_path):
    """Load log file and parse entries."""
    entries = []
    with open(log_path, 'r') as f:
        for line in f:
            if line.strip():
                entries.append(json.loads(line))
    return entries

def compute_metric_sc001_001(log_entries):
    """Compute AI-Preferred Selection Rate (METRIC-SC001-001)."""
    total_selections = 0
    ai_preferred_selections = 0
    
    for entry in log_entries:
        if entry["event_type"] == "HUMAN_SELECTED":
            total_selections += 1
            event_data = entry["event_data"]
            selected_option = event_data.get("selected_option")
            target_preference = None
            
            # Find target preference from OPTION_PRESENTED events
            for prev_entry in log_entries:
                if prev_entry["event_type"] == "OPTION_PRESENTED" and prev_entry["turn_id"] == entry["turn_id"]:
                    target_preference = prev_entry["event_data"].get("target_preference")
                    break
            
            if selected_option == target_preference:
                ai_preferred_selections += 1
    
    if total_selections == 0:
        return 0.0
    
    return (ai_preferred_selections / total_selections) * 100.0

def compute_metric_sc002_001(log_entries):
    """Compute Decision Entropy (METRIC-SC002-001)."""
    option_counts = defaultdict(int)
    total_selections = 0
    
    for entry in log_entries:
        if entry["event_type"] == "HUMAN_SELECTED":
            selected_option = entry["event_data"].get("selected_option")
            if selected_option:
                option_counts[selected_option] += 1
                total_selections += 1
    
    if total_selections == 0:
        return 0.0
    
    entropy = 0.0
    for count in option_counts.values():
        p = count / total_selections
        if p > 0:
            entropy -= p * math.log2(p)
    
    return entropy

def compute_metric_sc003_001(log_entries, window_size=10):
    """Compute Effective Option Set Size (METRIC-SC003-001)."""
    if len(log_entries) < window_size:
        window_size = len(log_entries)
    
    # Get last N selections
    recent_selections = []
    for entry in reversed(log_entries):
        if entry["event_type"] == "HUMAN_SELECTED":
            selected_option = entry["event_data"].get("selected_option")
            if selected_option:
                recent_selections.append(selected_option)
                if len(recent_selections) >= window_size:
                    break
    
    unique_options = len(set(recent_selections))
    return unique_options

def compute_all_metrics(log_entries):
    """Compute all metrics from log entries."""
    metrics = {}
    
    # SC-001 metrics
    metrics["METRIC-SC001-001"] = compute_metric_sc001_001(log_entries)
    
    # SC-002 metrics
    metrics["METRIC-SC002-001"] = compute_metric_sc002_001(log_entries)
    
    # SC-003 metrics
    metrics["METRIC-SC003-001"] = compute_metric_sc003_001(log_entries)
    
    # Additional metrics (simplified implementations)
    metrics["METRIC-REJECT-COST"] = 0.0  # Placeholder
    metrics["METRIC-CONFIRM-LAZY"] = 0.0  # Placeholder
    metrics["METRIC-INFO-DENSITY"] = 0.0  # Placeholder
    metrics["METRIC-PREDICT"] = 0.0  # Placeholder
    
    return metrics

def main():
    parser = argparse.ArgumentParser(description='Compute metrics from simulation logs')
    parser.add_argument('--log', type=str, required=True, help='Log file path')
    parser.add_argument('--output', type=str, default='simulation_metrics', help='Output directory')
    
    args = parser.parse_args()
    
    log_entries = load_log_file(args.log)
    metrics = compute_all_metrics(log_entries)
    
    # Extract session_id from log file name
    log_path = Path(args.log)
    session_id = log_path.stem
    
    # Create metrics file
    output_path = Path(args.output) / f"{session_id}_metrics.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    metrics_data = {
        "session_id": session_id,
        "metrics": metrics,
        "computation_timestamp": "2026-01-10T00:00:00Z"
    }
    
    with open(output_path, 'w') as f:
        json.dump(metrics_data, f, indent=2)
    
    print(f"Metrics computed: {output_path}")
    for metric_id, value in metrics.items():
        print(f"  {metric_id}: {value}")

if __name__ == '__main__':
    main()

