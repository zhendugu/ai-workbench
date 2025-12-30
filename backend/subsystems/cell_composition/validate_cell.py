"""
Cell validation for Cell Composition Subsystem.

C-CELL-3: Validate Cell Completeness implementation

Phase-2 Semantic Reduction: Cell is a static declarative composition, not a runtime entity.
Cell has no state, no lifecycle, no execution semantics in Phase-2.
"""

from typing import Any, Dict, List, Union

from .models import CellDefinition


def validate_cell_definition(
    cell_definition: Union[Dict[str, Any], CellDefinition],
    strict: bool = True,
    check_role_references: bool = False,
) -> Dict[str, Any]:
    """
    C-CELL-3: Validate Cell Completeness (PURE VALIDATION, NO STATE)
    
    Checks whether a CellDefinition is "complete" per schema rules.
    This is a PURE FUNCTION with NO I/O, NO file reads/writes, NO global state mutation.
    
    THIS IS NOT EXECUTION
    THIS IS NOT STATE MANAGEMENT
    THIS IS NOT LIFECYCLE MANAGEMENT
    
    Phase-2 Semantic Reduction:
    - Cell has no state, no lifecycle, no execution semantics
    - Validates only static composition definition
    
    This capability does NOT create, modify, repair, or infer anything. It only reports.
    
    Behavior:
    - Pure validation function: No I/O, no file reads/writes, no global state mutation
    - Schema validation: Checks required fields and types
    - Completeness checks: Validates field presence and non-empty (strict mode)
    - Role reference check: Optional read-only check via C-ROLE-2 (if check_role_references=True)
    - Deterministic output: Same input always produces same output
    - Structured errors: Returns structured error list
    
    Args:
        cell_definition: Cell definition to validate (dict or CellDefinition instance)
        strict: If True, requires all required fields present and non-empty (default: True)
                If False, allows empty lists but still requires keys present
        check_role_references: If True, checks that referenced roles exist via C-ROLE-2 (read-only)
                              Default: False (to keep function pure by default)
    
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
    - Query cell by id (that is C-CELL-2)
    - Write/repair/normalize cell
    - Auto-fill missing fields
    - Generate suggestions beyond structured errors/warnings
    - Validate Cell state structure
    - Validate Cell state transitions
    - Validate Cell lifecycle rules
    - Validate Cell execution semantics
    """
    errors: List[Dict[str, str]] = []
    warnings: List[Dict[str, str]] = []
    
    # Convert CellDefinition instance to dict if needed
    if isinstance(cell_definition, CellDefinition):
        cell_dict = {
            "cell_id": cell_definition.cell_id,
            "role_ids": cell_definition.role_ids,
            "input_contract": cell_definition.input_contract,
            "output_format": cell_definition.output_format,
        }
    elif isinstance(cell_definition, dict):
        cell_dict = cell_definition
    else:
        return {
            "valid": False,
            "errors": [
                {
                    "field": "cell_definition",
                    "code": "INVALID_TYPE",
                    "message": f"cell_definition must be dict or CellDefinition, got {type(cell_definition).__name__}",
                }
            ],
            "warnings": [],
            "normalized": None,
        }
    
    # Explicitly check for forbidden fields (Phase-2 constraint)
    forbidden_fields = ["state", "status", "lifecycle", "state_transitions",
                       "execution_history", "runtime_info", "activation_time",
                       "deactivation_time", "current_state", "previous_state"]
    for field in forbidden_fields:
        if field in cell_dict:
            errors.append({
                "field": field,
                "code": "FORBIDDEN_FIELD",
                "message": f"Forbidden field '{field}' detected. Phase-2 Cell definitions must not contain state or lifecycle fields.",
            })
    
    # Required fields
    required_fields = ["cell_id", "role_ids", "input_contract", "output_format"]
    
    # Check required fields exist
    for field in required_fields:
        if field not in cell_dict:
            errors.append({
                "field": field,
                "code": "MISSING_FIELD",
                "message": f"Required field '{field}' is missing",
            })
    
    # Validate cell_id
    if "cell_id" in cell_dict:
        cell_id = cell_dict["cell_id"]
        if not isinstance(cell_id, str):
            errors.append({
                "field": "cell_id",
                "code": "INVALID_TYPE",
                "message": "cell_id must be a string",
            })
        elif strict and not cell_id.strip():
            errors.append({
                "field": "cell_id",
                "code": "EMPTY_VALUE",
                "message": "cell_id must be non-empty (strict mode)",
            })
    
    # Validate role_ids
    if "role_ids" in cell_dict:
        role_ids = cell_dict["role_ids"]
        if not isinstance(role_ids, list):
            errors.append({
                "field": "role_ids",
                "code": "INVALID_TYPE",
                "message": "role_ids must be a list",
            })
        else:
            # Check list items are strings
            for i, role_id in enumerate(role_ids):
                if not isinstance(role_id, str):
                    errors.append({
                        "field": f"role_ids[{i}]",
                        "code": "INVALID_TYPE",
                        "message": f"role_ids[{i}] must be a string",
                    })
            
            # Check for duplicates (deterministic, non-mutating)
            if len(role_ids) != len(set(role_ids)):
                seen = set()
                for i, role_id in enumerate(role_ids):
                    if role_id in seen:
                        errors.append({
                            "field": f"role_ids[{i}]",
                            "code": "DUPLICATE_ENTRY",
                            "message": f"Duplicate role_id '{role_id}' in role_ids list",
                        })
                    seen.add(role_id)
            
            # Strict mode: empty list check
            if strict and len(role_ids) == 0:
                errors.append({
                    "field": "role_ids",
                    "code": "EMPTY_LIST",
                    "message": "role_ids must be non-empty (strict mode)",
                })
            
            # Optional: Check role references exist (read-only via C-ROLE-2)
            if check_role_references and len(errors) == 0:  # Only check if no other errors
                try:
                    from ..role_management.query_role import query_role_definition
                    
                    for role_id in role_ids:
                        # Read-only check: query role definition
                        role_result = query_role_definition(role_id, "cell_validation")
                        if role_result.get("status") != "found":
                            warnings.append({
                                "field": "role_ids",
                                "code": "ROLE_NOT_FOUND",
                                "message": f"Referenced role '{role_id}' not found",
                            })
                except Exception:
                    # If C-ROLE-2 is not available or fails, skip role reference check
                    # This keeps the function pure and doesn't fail validation
                    pass
    
    # Validate input_contract
    if "input_contract" in cell_dict:
        input_contract = cell_dict["input_contract"]
        if not isinstance(input_contract, dict):
            errors.append({
                "field": "input_contract",
                "code": "INVALID_TYPE",
                "message": "input_contract must be a dict",
            })
        elif strict and len(input_contract) == 0:
            errors.append({
                "field": "input_contract",
                "code": "EMPTY_DICT",
                "message": "input_contract must be non-empty (strict mode)",
            })
    
    # Validate output_format
    if "output_format" in cell_dict:
        output_format = cell_dict["output_format"]
        if not isinstance(output_format, dict):
            errors.append({
                "field": "output_format",
                "code": "INVALID_TYPE",
                "message": "output_format must be a dict",
            })
        elif strict and len(output_format) == 0:
            errors.append({
                "field": "output_format",
                "code": "EMPTY_DICT",
                "message": "output_format must be non-empty (strict mode)",
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

