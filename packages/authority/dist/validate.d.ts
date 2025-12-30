/**
 * Authority Layer Strict Validator
 *
 * Authority: docs/authority/*_FROZEN_001.md
 *
 * G-1: Strict mode validation - unknown fields are rejected
 *
 * This validator ensures that:
 * - All fields match Authority schemas exactly
 * - No additional fields are present (strict mode)
 * - All required fields are present
 * - Field types match schema definitions
 * - Enumeration values are valid
 */
export interface ValidationError {
    field: string;
    message: string;
    path?: string;
}
export interface ValidationResult {
    valid: boolean;
    errors: ValidationError[];
}
export declare function validateCompany(value: unknown, path?: string): ValidationResult;
export declare function validateCell(value: unknown, path?: string): ValidationResult;
export declare function validateRole(value: unknown, path?: string): ValidationResult;
export declare function validateRelationship(value: unknown, path?: string): ValidationResult;
export declare function validateTopology(value: unknown, path?: string): ValidationResult;
export declare function validateMethodology(value: unknown, path?: string): ValidationResult;
export declare function validateFreezeRecord(value: unknown, path?: string): ValidationResult;
export declare function validateFrozenSnapshot(value: unknown): ValidationResult;
