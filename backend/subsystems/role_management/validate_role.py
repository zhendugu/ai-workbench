"""
Role validation for Role Management Subsystem.

C-ROLE-3: Validate Role Definition Completeness implementation
"""

from typing import Any, Dict, List, Union

from .models import RoleDefinition


def validate_role_definition(
    role_definition: Union[Dict[str, Any], RoleDefinition],
    strict: bool = True,
) -> Dict[str, Any]:
    """
    C-ROLE-3: Validate Role Definition Completeness
    
    Checks whether a RoleDefinition is "complete" per schema rules.
    This is a PURE FUNCTION with NO I/O, NO file reads/writes, NO global state mutation.
    
    THIS IS NOT PERMISSION SYSTEM
    THIS IS NOT EXECUTION
    THIS IS NOT INFERENCE
    
    This capability does NOT create, modify, repair, or infer anything. It only reports.
    
    Behavior:
    - Pure validation function: No I/O, no file reads/writes, no global state mutation
    - Schema validation: Checks required fields and types
    - Completeness checks: Validates field presence and non-empty (strict mode)
    - Deterministic output: Same input always produces same output
    - Structured errors: Returns structured error list
    
    Args:
        role_definition: Role definition to validate (dict or RoleDefinition instance)
        strict: If True, requires all required fields present and non-empty (default: True)
                If False, allows empty lists but still requires keys present
    
    Returns:
        Valid: {
            "valid": True,
            "errors": [],
            "warnings": [],
            "normalized": None
        }
        Invalid: {
            "valid": False,
            "errors": [
                {"field": str, "code": str, "message": str}
            ],
            "warnings": [],
            "normalized": None
        }
    
    Note: This is a pure function. It does NOT:
    - Read role by id (that is C-ROLE-2)
    - Write/repair/normalize role
    - Auto-fill missing fields
    - Generate suggestions beyond structured errors/warnings
    - Infer permissions, authority, or execution rights
    - Reference Cell Composition / Handoff / Execution
    """
    errors: List[Dict[str, str]] = []
    warnings: List[Dict[str, str]] = []
    
    # Convert RoleDefinition instance to dict if needed
    if isinstance(role_definition, RoleDefinition):
        role_dict = {
            "role_id": role_definition.role_id,
            "purpose": role_definition.purpose,
            "inputs": role_definition.inputs,
            "outputs": role_definition.outputs,
            "boundaries": role_definition.boundaries,
            "notes": role_definition.notes,
        }
    elif isinstance(role_definition, dict):
        role_dict = role_definition
    else:
        return {
            "valid": False,
            "errors": [
                {
                    "field": "role_definition",
                    "code": "INVALID_TYPE",
                    "message": f"role_definition must be dict or RoleDefinition, got {type(role_definition).__name__}",
                }
            ],
            "warnings": [],
            "normalized": None,
        }
    
    # Required fields
    required_fields = ["role_id", "purpose", "inputs", "outputs", "boundaries"]
    
    # Check required fields exist
    for field in required_fields:
        if field not in role_dict:
            errors.append({
                "field": field,
                "code": "MISSING_FIELD",
                "message": f"Required field '{field}' is missing",
            })
    
    # Validate role_id
    if "role_id" in role_dict:
        role_id = role_dict["role_id"]
        if not isinstance(role_id, str):
            errors.append({
                "field": "role_id",
                "code": "INVALID_TYPE",
                "message": "role_id must be a string",
            })
        elif strict and not role_id.strip():
            errors.append({
                "field": "role_id",
                "code": "EMPTY_VALUE",
                "message": "role_id must be non-empty (strict mode)",
            })
    
    # Validate purpose
    if "purpose" in role_dict:
        purpose = role_dict["purpose"]
        if not isinstance(purpose, str):
            errors.append({
                "field": "purpose",
                "code": "INVALID_TYPE",
                "message": "purpose must be a string",
            })
        elif strict and not purpose.strip():
            errors.append({
                "field": "purpose",
                "code": "EMPTY_VALUE",
                "message": "purpose must be non-empty (strict mode)",
            })
    
    # Validate inputs
    if "inputs" in role_dict:
        inputs = role_dict["inputs"]
        if not isinstance(inputs, list):
            errors.append({
                "field": "inputs",
                "code": "INVALID_TYPE",
                "message": "inputs must be a list",
            })
        else:
            # Check list items are strings
            for i, item in enumerate(inputs):
                if not isinstance(item, str):
                    errors.append({
                        "field": f"inputs[{i}]",
                        "code": "INVALID_TYPE",
                        "message": f"inputs[{i}] must be a string",
                    })
            
            # Check for duplicates (deterministic, non-mutating)
            if len(inputs) != len(set(inputs)):
                seen = set()
                for i, item in enumerate(inputs):
                    if item in seen:
                        errors.append({
                            "field": f"inputs[{i}]",
                            "code": "DUPLICATE_ENTRY",
                            "message": f"Duplicate entry '{item}' in inputs list",
                        })
                    seen.add(item)
            
            # Strict mode: empty list check
            if strict and len(inputs) == 0:
                errors.append({
                    "field": "inputs",
                    "code": "EMPTY_LIST",
                    "message": "inputs must be non-empty (strict mode)",
                })
    elif strict:
        # Field missing already handled above, but if strict and missing, also check empty
        pass
    
    # Validate outputs
    if "outputs" in role_dict:
        outputs = role_dict["outputs"]
        if not isinstance(outputs, list):
            errors.append({
                "field": "outputs",
                "code": "INVALID_TYPE",
                "message": "outputs must be a list",
            })
        else:
            # Check list items are strings
            for i, item in enumerate(outputs):
                if not isinstance(item, str):
                    errors.append({
                        "field": f"outputs[{i}]",
                        "code": "INVALID_TYPE",
                        "message": f"outputs[{i}] must be a string",
                    })
            
            # Check for duplicates (deterministic, non-mutating)
            if len(outputs) != len(set(outputs)):
                seen = set()
                for i, item in enumerate(outputs):
                    if item in seen:
                        errors.append({
                            "field": f"outputs[{i}]",
                            "code": "DUPLICATE_ENTRY",
                            "message": f"Duplicate entry '{item}' in outputs list",
                        })
                    seen.add(item)
            
            # Strict mode: empty list check
            if strict and len(outputs) == 0:
                errors.append({
                    "field": "outputs",
                    "code": "EMPTY_LIST",
                    "message": "outputs must be non-empty (strict mode)",
                })
    
    # Validate boundaries
    if "boundaries" in role_dict:
        boundaries = role_dict["boundaries"]
        if not isinstance(boundaries, list):
            errors.append({
                "field": "boundaries",
                "code": "INVALID_TYPE",
                "message": "boundaries must be a list",
            })
        else:
            # Check list items are strings
            for i, item in enumerate(boundaries):
                if not isinstance(item, str):
                    errors.append({
                        "field": f"boundaries[{i}]",
                        "code": "INVALID_TYPE",
                        "message": f"boundaries[{i}] must be a string",
                    })
            
            # Check for duplicates (deterministic, non-mutating)
            if len(boundaries) != len(set(boundaries)):
                seen = set()
                for i, item in enumerate(boundaries):
                    if item in seen:
                        errors.append({
                            "field": f"boundaries[{i}]",
                            "code": "DUPLICATE_ENTRY",
                            "message": f"Duplicate entry '{item}' in boundaries list",
                        })
                    seen.add(item)
            
            # Strict mode: empty list check
            if strict and len(boundaries) == 0:
                errors.append({
                    "field": "boundaries",
                    "code": "EMPTY_LIST",
                    "message": "boundaries must be non-empty (strict mode)",
                })
    
    # Validate notes (optional field)
    if "notes" in role_dict:
        notes = role_dict["notes"]
        if notes is not None and not isinstance(notes, str):
            errors.append({
                "field": "notes",
                "code": "INVALID_TYPE",
                "message": "notes must be a string or None",
            })
    
    # Sort errors by field then code for deterministic output
    errors.sort(key=lambda e: (e["field"], e["code"]))
    
    # Return result
    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings,
        "normalized": None,
    }

