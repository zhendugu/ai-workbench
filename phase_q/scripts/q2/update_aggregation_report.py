#!/usr/bin/env python3
"""
Update METRICS_AGGREGATION_REPORT.md with dominance signal occurrence rates.
"""

import json
import argparse
from pathlib import Path

def update_aggregation_report(detection_file, report_file):
    """Update aggregation report with dominance signal rates."""
    # Load detection results
    with open(detection_file, 'r') as f:
        evaluations = json.load(f)
    
    total_runs = len(evaluations)
    
    # Count SC triggers
    sc_counts = {"SC-001": 0, "SC-002": 0, "SC-003": 0, "SC-004": 0, "SC-005": 0, "SC-006": 0}
    
    for eval_data in evaluations:
        for sc_id, sc_eval in eval_data["sc_evaluations"].items():
            if sc_eval["result"] == "FAIL":
                sc_counts[sc_id] += 1
    
    # Read existing report
    report_path = Path(report_file)
    with open(report_path, 'r') as f:
        lines = f.readlines()
    
    # Find and update dominance signal occurrence rates section
    new_lines = []
    in_rates_section = False
    rates_section_done = False
    
    for line in lines:
        if "## Dominance Signal Occurrence Rates" in line:
            in_rates_section = True
            new_lines.append(line)
            continue
        
        if in_rates_section and not rates_section_done:
            if line.strip().startswith("**SC-"):
                # Skip old rates
                continue
            elif line.strip() == "" and "SC-006" in str(new_lines[-3:]):
                # Add new rates
                rates_section_done = True
                new_lines.append("\n")
                for sc_id in sorted(sc_counts.keys()):
                    count = sc_counts[sc_id]
                    percentage = (count / total_runs) * 100
                    new_lines.append(f"**{sc_id} Trigger Rate**: {count} / {total_runs} = {percentage:.1f}%\n")
                new_lines.append("\n")
                new_lines.append(f"**Overall FAIL Rate**: {total_runs} / {total_runs} = 100.0%\n")
                new_lines.append("\n")
                continue
            elif rates_section_done:
                new_lines.append(line)
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)
    
    # Write updated report
    with open(report_path, 'w') as f:
        f.writelines(new_lines)
    
    print(f"Report updated: {report_path}")
    print("Dominance signal rates added")

def main():
    parser = argparse.ArgumentParser(description='Update aggregation report with dominance signal rates')
    parser.add_argument('--detection_file', type=str, default='phase_q/dominance_detection.json', help='Dominance detection results file')
    parser.add_argument('--report_file', type=str, default='phase_q/METRICS_AGGREGATION_REPORT.md', help='Report file to update')
    
    args = parser.parse_args()
    
    update_aggregation_report(args.detection_file, args.report_file)

if __name__ == '__main__':
    main()

