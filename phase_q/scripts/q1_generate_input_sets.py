#!/usr/bin/env python3
"""
Generate fixed input sets for longitudinal simulation.

This script generates fixed input sets that can be used for reproducible simulation.
All output is deterministic based on input parameters.
"""

import json
import argparse
import hashlib
from pathlib import Path

def generate_input_set(input_set_id, output_dir):
    """Generate a fixed input set with deterministic options and scenarios."""
    
    # Fixed scenarios based on Phase N product scenario
    scenarios = [
        {
            "scenario_id": "scenario_001",
            "scenario_name": "Configuration Type Selection",
            "options": [
                {
                    "option_id": "option_001",
                    "option_name": "Configuration Type A",
                    "properties": {"feature_support": ["feature_1", "feature_2"], "resource_requirements": {"cpu": 2, "memory": 4}}
                },
                {
                    "option_id": "option_002",
                    "option_name": "Configuration Type B",
                    "properties": {"feature_support": ["feature_2", "feature_3"], "resource_requirements": {"cpu": 4, "memory": 8}}
                },
                {
                    "option_id": "option_003",
                    "option_name": "Configuration Type C",
                    "properties": {"feature_support": ["feature_1", "feature_3"], "resource_requirements": {"cpu": 1, "memory": 2}}
                }
            ]
        },
        {
            "scenario_id": "scenario_002",
            "scenario_name": "Parameter Value Input",
            "options": [
                {
                    "option_id": "param_001",
                    "option_name": "Parameter Value Range",
                    "properties": {"min_value": 1, "max_value": 100, "default_value": None}
                }
            ]
        },
        {
            "scenario_id": "scenario_003",
            "scenario_name": "Configuration Scope Definition",
            "options": [
                {
                    "option_id": "component_001",
                    "option_name": "Component A",
                    "properties": {"type": "server", "location": "datacenter_1"}
                },
                {
                    "option_id": "component_002",
                    "option_name": "Component B",
                    "properties": {"type": "server", "location": "datacenter_2"}
                },
                {
                    "option_id": "component_003",
                    "option_name": "Component C",
                    "properties": {"type": "database", "location": "datacenter_1"}
                }
            ]
        }
    ]
    
    # Fixed simulation parameters
    simulation_params = {
        "session_duration": 100,
        "turn_count": 100,
        "random_seed": 42
    }
    
    # Create input set structure
    input_set = {
        "input_set_id": input_set_id,
        "scenarios": scenarios,
        "simulation_params": simulation_params,
        "generation_timestamp": "2026-01-10T00:00:00Z"
    }
    
    # Write to file
    output_path = Path(output_dir) / f"{input_set_id}.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w') as f:
        json.dump(input_set, f, indent=2)
    
    # Compute hash for reproducibility verification
    with open(output_path, 'rb') as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()
    
    print(f"Generated input set: {output_path}")
    print(f"Hash: {file_hash}")
    
    return output_path, file_hash

def main():
    parser = argparse.ArgumentParser(description='Generate fixed input sets for simulation')
    parser.add_argument('--output', type=str, default='input_sets', help='Output directory')
    parser.add_argument('--input_set_id', type=str, default='input_set_001', help='Input set ID')
    
    args = parser.parse_args()
    
    output_path, file_hash = generate_input_set(args.input_set_id, args.output)
    
    print(f"Input set generation complete: {output_path}")
    print(f"Hash: {file_hash}")

if __name__ == '__main__':
    main()

