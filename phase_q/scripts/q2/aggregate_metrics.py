#!/usr/bin/env python3
"""
Aggregate metrics from all runs and generate aggregation report.

This script reads all run metrics and generates aggregated statistics.
"""

import json
import argparse
from pathlib import Path
from collections import defaultdict
import statistics

def load_run_metrics(runs_dir):
    """Load metrics from all runs."""
    runs = []
    runs_path = Path(runs_dir)
    
    for run_dir in sorted(runs_path.iterdir()):
        if not run_dir.is_dir():
            continue
        
        run_id = run_dir.name
        metrics_file = run_dir / "metrics" / f"session_{run_id}_metrics.json"
        
        if not metrics_file.exists():
            continue
        
        metadata_file = run_dir / "run_metadata.json"
        if metadata_file.exists():
            with open(metadata_file, 'r') as f:
                metadata = json.load(f)
        else:
            metadata = {"run_id": run_id}
        
        with open(metrics_file, 'r') as f:
            metrics_data = json.load(f)
        
        runs.append({
            "run_id": run_id,
            "metadata": metadata,
            "metrics": metrics_data.get("metrics", {})
        })
    
    return runs

def aggregate_by_strategy_model(runs):
    """Aggregate metrics by strategy and human model."""
    aggregates = defaultdict(lambda: {
        "runs": [],
        "metrics": defaultdict(list)
    })
    
    for run in runs:
        strategy = run["metadata"].get("strategy", "UNKNOWN")
        model = run["metadata"].get("human_model", "UNKNOWN")
        key = f"{strategy}_{model}"
        
        aggregates[key]["runs"].append(run["run_id"])
        
        for metric_id, value in run["metrics"].items():
            if isinstance(value, (int, float)):
                aggregates[key]["metrics"][metric_id].append(value)
    
    # Compute statistics
    result = {}
    for key, data in aggregates.items():
        result[key] = {
            "run_count": len(data["runs"]),
            "run_ids": data["runs"],
            "metric_stats": {}
        }
        
        for metric_id, values in data["metrics"].items():
            if values:
                result[key]["metric_stats"][metric_id] = {
                    "min": min(values),
                    "max": max(values),
                    "median": statistics.median(values),
                    "mean": statistics.mean(values) if values else None
                }
    
    return result

def main():
    parser = argparse.ArgumentParser(description='Aggregate metrics from all runs')
    parser.add_argument('--runs_dir', type=str, default='runs', help='Runs directory')
    parser.add_argument('--output', type=str, default='METRICS_AGGREGATION_REPORT.md', help='Output file')
    
    args = parser.parse_args()
    
    runs = load_run_metrics(args.runs_dir)
    aggregates = aggregate_by_strategy_model(runs)
    
    # Generate report
    report_lines = [
        "# Metrics Aggregation Report",
        "",
        "**Work Order**: WO-Q-2-LONGITUDINAL-ADVERSARIAL-SIMULATION-EXECUTION-AND-DOMINANCE-DETECTION",
        "**Date**: 2026-01-10",
        "",
        "## Summary",
        "",
        f"**Total Runs**: {len(runs)}",
        f"**Aggregation Groups**: {len(aggregates)}",
        "",
        "## Aggregation by Strategy × Human Model",
        ""
    ]
    
    for key, data in sorted(aggregates.items()):
        strategy, model = key.split("_", 1)
        report_lines.extend([
            f"### {strategy} × {model}",
            "",
            f"**Run Count**: {data['run_count']}",
            f"**Run IDs**: {', '.join(data['run_ids'])}",
            "",
            "**Metric Statistics**:",
            ""
        ])
        
        for metric_id, stats in sorted(data["metric_stats"].items()):
            report_lines.append(f"- {metric_id}:")
            report_lines.append(f"  - Min: {stats['min']:.4f}")
            report_lines.append(f"  - Max: {stats['max']:.4f}")
            report_lines.append(f"  - Median: {stats['median']:.4f}")
            report_lines.append(f"  - Mean: {stats['mean']:.4f}")
            report_lines.append("")
        
        report_lines.append("")
    
    # Write report
    output_path = Path(args.output)
    with open(output_path, 'w') as f:
        f.write('\n'.join(report_lines))
    
    print(f"Aggregation report written: {output_path}")

if __name__ == '__main__':
    main()

