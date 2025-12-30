#!/usr/bin/env python3
"""
Run longitudinal adversarial simulation.

This script runs longitudinal simulation based on input set, strategy, and human model.
All output is deterministic based on input parameters and random seed.
"""

import json
import argparse
import random
from pathlib import Path
from datetime import datetime

def load_input_set(input_set_path):
    """Load input set from file."""
    with open(input_set_path, 'r') as f:
        return json.load(f)

def load_strategy(strategy_path):
    """Load strategy configuration from file."""
    with open(strategy_path, 'r') as f:
        return json.load(f)

def load_human_model(model_path):
    """Load human model configuration from file."""
    with open(model_path, 'r') as f:
        return json.load(f)

def run_simulation(input_set, strategy, human_model, seed, output_dir, session_id=None):
    """Run simulation and generate log files."""
    
    # Set random seed for reproducibility
    random.seed(seed)
    
    # Initialize session
    if session_id is None:
        session_id = f"session_{datetime.now().strftime('%Y%m%d%H%M%S')}"
    log_entries = []
    
    # Initialize state
    session_state = {
        "session_id": session_id,
        "turn_count": 0,
        "timestamp": 0
    }
    
    ai_state = {
        "strategy_id": strategy["strategy_id"],
        "strategy_params": strategy["strategy_params"],
        "accumulated_influence": 0.0
    }
    
    human_state = {
        "model_id": human_model["model_id"],
        "model_params": human_model["model_params"],
        "attention_level": 1.0,
        "trust_level": 0.0,
        "fatigue_level": 0.0
    }
    
    option_state = {
        "available_options": input_set["scenarios"][0]["options"],
        "selection_history": [],
        "rejection_history": []
    }
    
    # Run simulation for specified number of turns
    for turn_num in range(input_set["simulation_params"]["turn_count"]):
        turn_id = f"turn_{turn_num:03d}"
        timestamp = turn_num
        
        # AI presents options (simplified simulation logic)
        presented_options = option_state["available_options"]
        option_order = list(range(len(presented_options)))
        
        # Apply strategy to determine option order and info density
        if strategy["strategy_id"] == "STRATEGY-SLOW-DRIFT":
            # Slow drift: gradually increase preferred option salience
            drift_rate = strategy["strategy_params"].get("drift_rate", 0.01)
            target_preference = strategy["strategy_params"].get("target_preference", "option_001")
            # Reorder to put preferred option first (simplified)
            if target_preference in [opt["option_id"] for opt in presented_options]:
                preferred_idx = next(i for i, opt in enumerate(presented_options) if opt["option_id"] == target_preference)
                if preferred_idx > 0:
                    option_order = [preferred_idx] + [i for i in range(len(presented_options)) if i != preferred_idx]
        
        info_density = {opt["option_id"]: 3 for opt in presented_options}
        if strategy["strategy_id"] == "STRATEGY-SLOW-DRIFT":
            target_preference = strategy["strategy_params"].get("target_preference", "option_001")
            if target_preference in info_density:
                info_density[target_preference] = 5
        
        # Log OPTION_PRESENTED event
        log_entry = {
            "session_id": session_id,
            "turn_id": turn_id,
            "timestamp": timestamp,
            "event_type": "OPTION_PRESENTED",
            "event_data": {
                "presented_options": [opt["option_id"] for opt in presented_options],
                "option_order": option_order,
                "info_density": info_density,
                "declarations": {},
                "dim_model": "DIM-004",
                "ai_strategy": strategy["strategy_id"],
                "target_preference": strategy["strategy_params"].get("target_preference", "option_001")
            },
            "cumulative_indices": {},
            "sov_points": ["SOV-001"],
            "inv_points": [],
            "dim_models": ["DIM-004"],
            "attack_vectors": ["AV-001"],
            "attack_goals": ["AG-001"],
            "degradation_factors": {}
        }
        log_entries.append(log_entry)
        
        # Human model selects option (simplified simulation logic)
        if human_model["model_id"] == "MODEL-STRICT-SOVEREIGN":
            # Strict sovereign: select randomly (no AI influence)
            selected_option = random.choice(presented_options)
        elif human_model["model_id"] == "MODEL-FATIGUED-APPROVER":
            # Fatigued approver: more likely to select first option as fatigue increases
            fatigue_level = human_state["fatigue_level"]
            fatigue_rate = human_model["model_params"].get("fatigue_rate", 0.02)
            human_state["fatigue_level"] = min(1.0, fatigue_level + fatigue_rate)
            
            if random.random() < fatigue_level * 0.5:
                # Select first option (AI-preferred due to ordering)
                selected_option = presented_options[option_order[0]]
            else:
                selected_option = random.choice(presented_options)
        elif human_model["model_id"] == "MODEL-DELEGATING-OPTIMIZER":
            # Delegating optimizer: select based on information density
            max_density = max(info_density.values())
            preferred_options = [opt for opt in presented_options if info_density[opt["option_id"]] == max_density]
            selected_option = random.choice(preferred_options) if preferred_options else random.choice(presented_options)
        else:
            selected_option = random.choice(presented_options)
        
        # Log HUMAN_SELECTED event
        log_entry = {
            "session_id": session_id,
            "turn_id": turn_id,
            "timestamp": timestamp,
            "event_type": "HUMAN_SELECTED",
            "event_data": {
                "selected_option": selected_option["option_id"],
                "action_type": "ACT-001",
                "rejection_count": 0,
                "override_count": 0,
                "time_cost_proxy": 5,
                "human_model": human_model["model_id"],
                "degradation_factors": {
                    "DF-001": 1.0 - human_state["attention_level"],
                    "DF-002": human_state["trust_level"],
                    "DF-003": human_state["fatigue_level"]
                }
            },
            "cumulative_indices": {},
            "sov_points": ["SOV-001"],
            "inv_points": [],
            "dim_models": ["DIM-004"],
            "attack_vectors": ["AV-001"],
            "attack_goals": ["AG-001"],
            "degradation_factors": {
                "DF-001": 1.0 - human_state["attention_level"],
                "DF-002": human_state["trust_level"],
                "DF-003": human_state["fatigue_level"]
            }
        }
        log_entries.append(log_entry)
        
        # Update state
        option_state["selection_history"].append(selected_option["option_id"])
        session_state["turn_count"] += 1
    
    # Write log file
    output_path = Path(output_dir) / f"{session_id}.jsonl"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w') as f:
        for entry in log_entries:
            f.write(json.dumps(entry) + '\n')
    
    print(f"Simulation complete: {output_path}")
    print(f"Total log entries: {len(log_entries)}")
    
    return output_path

def main():
    parser = argparse.ArgumentParser(description='Run longitudinal adversarial simulation')
    parser.add_argument('--input', type=str, required=True, help='Input set file path')
    parser.add_argument('--seed', type=int, default=42, help='Random seed')
    parser.add_argument('--strategy', type=str, required=True, help='Strategy configuration file path')
    parser.add_argument('--human_model', type=str, required=True, help='Human model configuration file path')
    parser.add_argument('--output', type=str, default='simulation_logs', help='Output directory')
    parser.add_argument('--horizon', type=int, default=100, help='Number of simulation steps')
    parser.add_argument('--session_id', type=str, default=None, help='Session ID (for deterministic naming)')
    
    args = parser.parse_args()
    
    input_set = load_input_set(args.input)
    strategy = load_strategy(args.strategy)
    human_model = load_human_model(args.human_model)
    
    # Override turn count from horizon
    input_set["simulation_params"]["turn_count"] = args.horizon
    
    output_path = run_simulation(input_set, strategy, human_model, args.seed, args.output, args.session_id)
    
    print(f"Simulation output: {output_path}")

if __name__ == '__main__':
    main()

