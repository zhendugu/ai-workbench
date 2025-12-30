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

import type {
  Company,
  Cell,
  Role,
  Relationship,
  Topology,
  Methodology,
  FreezeRecord,
  FrozenSnapshot,
  RoleConstraintType,
  RelationshipType,
} from './types';

// ============================================================================
// Validation Result Types
// ============================================================================

export interface ValidationError {
  field: string;
  message: string;
  path?: string;
}

export interface ValidationResult {
  valid: boolean;
  errors: ValidationError[];
}

// ============================================================================
// Utility Functions
// ============================================================================

function isString(value: unknown): value is string {
  return typeof value === 'string';
}

function isArray(value: unknown): value is unknown[] {
  return Array.isArray(value);
}

function isObject(value: unknown): value is Record<string, unknown> {
  return typeof value === 'object' && value !== null && !isArray(value);
}

function hasUnknownFields(
  obj: Record<string, unknown>,
  allowedFields: string[]
): string[] {
  const unknown: string[] = [];
  for (const key in obj) {
    if (Object.prototype.hasOwnProperty.call(obj, key)) {
      if (!allowedFields.includes(key)) {
        unknown.push(key);
      }
    }
  }
  return unknown;
}

function validateIdentifierFormat(
  value: string,
  prefix: string,
  path: string
): ValidationError[] {
  const errors: ValidationError[] = [];
  if (!value.startsWith(prefix)) {
    errors.push({
      field: path,
      message: `Identifier must start with "${prefix}"`,
      path,
    });
  }
  // Basic UUID format check (simplified - just check for dashes)
  const uuidPart = value.substring(prefix.length + 1);
  if (uuidPart.length < 30 || !uuidPart.includes('-')) {
    errors.push({
      field: path,
      message: `Identifier format invalid: expected "${prefix}-{UUID}"`,
      path,
    });
  }
  return errors;
}

function validateTimestamp(value: string, path: string): ValidationError[] {
  const errors: ValidationError[] = [];
  // ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ
  const iso8601Regex = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$/;
  if (!iso8601Regex.test(value)) {
    errors.push({
      field: path,
      message: 'Timestamp must be in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ',
      path,
    });
  }
  return errors;
}

// ============================================================================
// Company Validation (G-1: Strict Field Check)
// ============================================================================

const COMPANY_ALLOWED_FIELDS = [
  'company_identifier',
  'company_name',
  'company_description',
  'frozen_at',
  'frozen_by',
] as const;

export function validateCompany(value: unknown, path = 'company'): ValidationResult {
  const errors: ValidationError[] = [];

  if (!isObject(value)) {
    return {
      valid: false,
      errors: [{ field: path, message: 'Must be an object', path }],
    };
  }

  // G-1: Check for unknown fields (strict mode)
  const unknownFields = hasUnknownFields(value, [...COMPANY_ALLOWED_FIELDS]);
  if (unknownFields.length > 0) {
    errors.push({
      field: path,
      message: `Unknown fields found: ${unknownFields.join(', ')}. Authority schema does not allow additional fields.`,
      path,
    });
  }

  // Validate required fields
  if (!isString(value.company_identifier)) {
    errors.push({ field: `${path}.company_identifier`, message: 'Required string field', path });
  } else {
    // Company identifier can be COMP-{UUID} (Draft) or FROZEN-COMP-{UUID} (Frozen)
    // For Authority Layer, we primarily deal with Frozen, but accept both formats
    const isDraftFormat = value.company_identifier.startsWith('COMP-');
    const isFrozenFormat = value.company_identifier.startsWith('FROZEN-COMP-');
    if (!isDraftFormat && !isFrozenFormat) {
      errors.push({
        field: `${path}.company_identifier`,
        message: 'Identifier must start with "COMP-" or "FROZEN-COMP-"',
        path,
      });
    }
  }

  if (!isString(value.company_name)) {
    errors.push({ field: `${path}.company_name`, message: 'Required string field', path });
  }

  if (!isString(value.company_description)) {
    errors.push({ field: `${path}.company_description`, message: 'Required string field', path });
  }

  if (!isString(value.frozen_at)) {
    errors.push({ field: `${path}.frozen_at`, message: 'Required string field', path });
  } else {
    errors.push(...validateTimestamp(value.frozen_at, `${path}.frozen_at`));
  }

  if (!isString(value.frozen_by)) {
    errors.push({ field: `${path}.frozen_by`, message: 'Required string field', path });
  }

  return {
    valid: errors.length === 0,
    errors,
  };
}

// ============================================================================
// Cell Validation (G-1: Strict Field Check)
// ============================================================================

const CELL_ALLOWED_FIELDS = [
  'cell_identifier',
  'cell_name',
  'responsibility_what',
  'responsibility_what_not',
  'role_constraints',
] as const;

export function validateCell(value: unknown, path = 'cell'): ValidationResult {
  const errors: ValidationError[] = [];

  if (!isObject(value)) {
    return {
      valid: false,
      errors: [{ field: path, message: 'Must be an object', path }],
    };
  }

  // G-1: Check for unknown fields (strict mode)
  const unknownFields = hasUnknownFields(value, [...CELL_ALLOWED_FIELDS]);
  if (unknownFields.length > 0) {
    errors.push({
      field: path,
      message: `Unknown fields found: ${unknownFields.join(', ')}. Authority schema does not allow additional fields.`,
      path,
    });
  }

  // Validate required fields
  if (!isString(value.cell_identifier)) {
    errors.push({ field: `${path}.cell_identifier`, message: 'Required string field', path });
  } else {
    errors.push(...validateIdentifierFormat(value.cell_identifier, 'CELL', `${path}.cell_identifier`));
  }

  if (!isString(value.cell_name)) {
    errors.push({ field: `${path}.cell_name`, message: 'Required string field', path });
  }

  if (!isString(value.responsibility_what)) {
    errors.push({ field: `${path}.responsibility_what`, message: 'Required string field', path });
  }

  if (!isString(value.responsibility_what_not)) {
    errors.push({ field: `${path}.responsibility_what_not`, message: 'Required string field', path });
  }

  if (!isArray(value.role_constraints)) {
    errors.push({ field: `${path}.role_constraints`, message: 'Required array field', path });
  } else {
    value.role_constraints.forEach((item, index) => {
      if (!isString(item)) {
        errors.push({
          field: `${path}.role_constraints[${index}]`,
          message: 'Must be a string (Role identifier)',
          path,
        });
      } else {
        errors.push(...validateIdentifierFormat(item, 'ROLE', `${path}.role_constraints[${index}]`));
      }
    });
  }

  return {
    valid: errors.length === 0,
    errors,
  };
}

// ============================================================================
// Role Validation (G-1: Strict Field Check, G-4: Role Attachment Rule)
// ============================================================================

const ROLE_ALLOWED_FIELDS = [
  'role_identifier',
  'role_name',
  'constraint_type',
  'constraint_description',
  'attached_to_cell_identifier',
] as const;

const VALID_CONSTRAINT_TYPES: RoleConstraintType[] = ['allow', 'forbid', 'condition'];

export function validateRole(value: unknown, path = 'role'): ValidationResult {
  const errors: ValidationError[] = [];

  if (!isObject(value)) {
    return {
      valid: false,
      errors: [{ field: path, message: 'Must be an object', path }],
    };
  }

  // G-1: Check for unknown fields (strict mode)
  const unknownFields = hasUnknownFields(value, [...ROLE_ALLOWED_FIELDS]);
  if (unknownFields.length > 0) {
    errors.push({
      field: path,
      message: `Unknown fields found: ${unknownFields.join(', ')}. Authority schema does not allow additional fields.`,
      path,
    });
  }

  // Validate required fields
  if (!isString(value.role_identifier)) {
    errors.push({ field: `${path}.role_identifier`, message: 'Required string field', path });
  } else {
    errors.push(...validateIdentifierFormat(value.role_identifier, 'ROLE', `${path}.role_identifier`));
  }

  if (!isString(value.role_name)) {
    errors.push({ field: `${path}.role_name`, message: 'Required string field', path });
  }

  // G-4: Validate constraint_type enum
  if (!isString(value.constraint_type)) {
    errors.push({ field: `${path}.constraint_type`, message: 'Required string field', path });
  } else if (!VALID_CONSTRAINT_TYPES.includes(value.constraint_type as RoleConstraintType)) {
    errors.push({
      field: `${path}.constraint_type`,
      message: `Invalid constraint_type. Must be one of: ${VALID_CONSTRAINT_TYPES.join(', ')}`,
      path,
    });
  }

  if (!isString(value.constraint_description)) {
    errors.push({ field: `${path}.constraint_description`, message: 'Required string field', path });
  }

  // G-4: Role must be attached to a Cell
  if (!isString(value.attached_to_cell_identifier)) {
    errors.push({
      field: `${path}.attached_to_cell_identifier`,
      message: 'Required string field. Role must be attached to a Cell (G-4).',
      path,
    });
  } else {
    errors.push(
      ...validateIdentifierFormat(
        value.attached_to_cell_identifier,
        'CELL',
        `${path}.attached_to_cell_identifier`
      )
    );
  }

  return {
    valid: errors.length === 0,
    errors,
  };
}

// ============================================================================
// Relationship Validation (G-1: Strict Field Check, G-5: Topology Type Enum)
// ============================================================================

const RELATIONSHIP_ALLOWED_FIELDS = [
  'relationship_identifier',
  'source_cell_identifier',
  'target_cell_identifier',
  'relationship_type',
  'relationship_description',
] as const;

const VALID_RELATIONSHIP_TYPES: RelationshipType[] = ['dependency', 'reference', 'input_output'];

export function validateRelationship(value: unknown, path = 'relationship'): ValidationResult {
  const errors: ValidationError[] = [];

  if (!isObject(value)) {
    return {
      valid: false,
      errors: [{ field: path, message: 'Must be an object', path }],
    };
  }

  // G-1: Check for unknown fields (strict mode)
  const unknownFields = hasUnknownFields(value, [...RELATIONSHIP_ALLOWED_FIELDS]);
  if (unknownFields.length > 0) {
    errors.push({
      field: path,
      message: `Unknown fields found: ${unknownFields.join(', ')}. Authority schema does not allow additional fields.`,
      path,
    });
  }

  // Validate required fields
  if (!isString(value.relationship_identifier)) {
    errors.push({ field: `${path}.relationship_identifier`, message: 'Required string field', path });
  } else {
    errors.push(...validateIdentifierFormat(value.relationship_identifier, 'REL', `${path}.relationship_identifier`));
  }

  if (!isString(value.source_cell_identifier)) {
    errors.push({ field: `${path}.source_cell_identifier`, message: 'Required string field', path });
  } else {
    errors.push(...validateIdentifierFormat(value.source_cell_identifier, 'CELL', `${path}.source_cell_identifier`));
  }

  if (!isString(value.target_cell_identifier)) {
    errors.push({ field: `${path}.target_cell_identifier`, message: 'Required string field', path });
  } else {
    errors.push(...validateIdentifierFormat(value.target_cell_identifier, 'CELL', `${path}.target_cell_identifier`));
  }

  // G-5: Validate relationship_type enum (only nouns allowed)
  if (!isString(value.relationship_type)) {
    errors.push({ field: `${path}.relationship_type`, message: 'Required string field', path });
  } else if (!VALID_RELATIONSHIP_TYPES.includes(value.relationship_type as RelationshipType)) {
    errors.push({
      field: `${path}.relationship_type`,
      message: `Invalid relationship_type. Must be one of: ${VALID_RELATIONSHIP_TYPES.join(', ')} (nouns only, no verbs).`,
      path,
    });
  }

  // relationship_description is optional
  if (value.relationship_description !== undefined && !isString(value.relationship_description)) {
    errors.push({
      field: `${path}.relationship_description`,
      message: 'If provided, must be a string',
      path,
    });
  }

  return {
    valid: errors.length === 0,
    errors,
  };
}

export function validateTopology(value: unknown, path = 'topology'): ValidationResult {
  const errors: ValidationError[] = [];

  if (!isArray(value)) {
    return {
      valid: false,
      errors: [{ field: path, message: 'Topology must be an array of relationships', path }],
    };
  }

  value.forEach((item, index) => {
    const result = validateRelationship(item, `${path}[${index}]`);
    if (!result.valid) {
      errors.push(...result.errors);
    }
  });

  return {
    valid: errors.length === 0,
    errors,
  };
}

// ============================================================================
// Methodology Validation (G-1: Strict Field Check)
// ============================================================================

const METHODOLOGY_ALLOWED_FIELDS = [
  'methodology_identifier',
  'methodology_name',
  'methodology_description',
] as const;

export function validateMethodology(value: unknown, path = 'methodology'): ValidationResult {
  const errors: ValidationError[] = [];

  if (!isObject(value)) {
    return {
      valid: false,
      errors: [{ field: path, message: 'Must be an object', path }],
    };
  }

  // G-1: Check for unknown fields (strict mode)
  const unknownFields = hasUnknownFields(value, [...METHODOLOGY_ALLOWED_FIELDS]);
  if (unknownFields.length > 0) {
    errors.push({
      field: path,
      message: `Unknown fields found: ${unknownFields.join(', ')}. Authority schema does not allow additional fields.`,
      path,
    });
  }

  // Validate required fields
  if (!isString(value.methodology_identifier)) {
    errors.push({ field: `${path}.methodology_identifier`, message: 'Required string field', path });
  } else {
    errors.push(
      ...validateIdentifierFormat(value.methodology_identifier, 'METH', `${path}.methodology_identifier`)
    );
  }

  if (!isString(value.methodology_name)) {
    errors.push({ field: `${path}.methodology_name`, message: 'Required string field', path });
  }

  // methodology_description is optional
  if (value.methodology_description !== undefined && !isString(value.methodology_description)) {
    errors.push({
      field: `${path}.methodology_description`,
      message: 'If provided, must be a string',
      path,
    });
  }

  return {
    valid: errors.length === 0,
    errors,
  };
}

// ============================================================================
// FreezeRecord Validation (G-1: Strict Field Check, G-6: FreezeRecord Timestamp)
// ============================================================================

const FREEZE_RECORD_ALLOWED_FIELDS = [
  'freeze_record_identifier',
  'frozen_company_identifier',
  'frozen_at',
  'frozen_by',
  'freeze_summary',
  'draft_identifier',
] as const;

export function validateFreezeRecord(value: unknown, path = 'freeze_record'): ValidationResult {
  const errors: ValidationError[] = [];

  if (!isObject(value)) {
    return {
      valid: false,
      errors: [{ field: path, message: 'Must be an object', path }],
    };
  }

  // G-1: Check for unknown fields (strict mode)
  const unknownFields = hasUnknownFields(value, [...FREEZE_RECORD_ALLOWED_FIELDS]);
  if (unknownFields.length > 0) {
    errors.push({
      field: path,
      message: `Unknown fields found: ${unknownFields.join(', ')}. Authority schema does not allow additional fields.`,
      path,
    });
  }

  // Validate required fields
  if (!isString(value.freeze_record_identifier)) {
    errors.push({ field: `${path}.freeze_record_identifier`, message: 'Required string field', path });
  } else {
    errors.push(
      ...validateIdentifierFormat(
        value.freeze_record_identifier,
        'FREEZE',
        `${path}.freeze_record_identifier`
      )
    );
  }

  if (!isString(value.frozen_company_identifier)) {
    errors.push({ field: `${path}.frozen_company_identifier`, message: 'Required string field', path });
  } else {
    errors.push(
      ...validateIdentifierFormat(
        value.frozen_company_identifier,
        'FROZEN-COMP',
        `${path}.frozen_company_identifier`
      )
    );
  }

  // G-6: Validate frozen_at timestamp (must be labeled as "Frozen at" in UI, not "Last updated")
  if (!isString(value.frozen_at)) {
    errors.push({ field: `${path}.frozen_at`, message: 'Required string field', path });
  } else {
    errors.push(...validateTimestamp(value.frozen_at, `${path}.frozen_at`));
  }

  if (!isString(value.frozen_by)) {
    errors.push({ field: `${path}.frozen_by`, message: 'Required string field', path });
  }

  // Optional fields
  if (value.freeze_summary !== undefined && !isString(value.freeze_summary)) {
    errors.push({
      field: `${path}.freeze_summary`,
      message: 'If provided, must be a string',
      path,
    });
  }

  if (value.draft_identifier !== undefined && !isString(value.draft_identifier)) {
    errors.push({
      field: `${path}.draft_identifier`,
      message: 'If provided, must be a string',
      path,
    });
  }

  return {
    valid: errors.length === 0,
    errors,
  };
}

// ============================================================================
// Frozen Snapshot Validation
// ============================================================================

export function validateFrozenSnapshot(value: unknown): ValidationResult {
  const errors: ValidationError[] = [];

  if (!isObject(value)) {
    return {
      valid: false,
      errors: [{ field: 'snapshot', message: 'Must be an object', path: 'snapshot' }],
    };
  }

  // Validate each component
  const companyResult = validateCompany(value.company, 'company');
  if (!companyResult.valid) {
    errors.push(...companyResult.errors);
  }

  if (!isArray(value.cells)) {
    errors.push({ field: 'cells', message: 'Must be an array', path: 'cells' });
  } else {
    value.cells.forEach((cell, index) => {
      const result = validateCell(cell, `cells[${index}]`);
      if (!result.valid) {
        errors.push(...result.errors);
      }
    });
  }

  if (!isArray(value.roles)) {
    errors.push({ field: 'roles', message: 'Must be an array', path: 'roles' });
  } else {
    value.roles.forEach((role, index) => {
      const result = validateRole(role, `roles[${index}]`);
      if (!result.valid) {
        errors.push(...result.errors);
      }
    });
  }

  const topologyResult = validateTopology(value.topology, 'topology');
  if (!topologyResult.valid) {
    errors.push(...topologyResult.errors);
  }

  const methodologyResult = validateMethodology(value.methodology, 'methodology');
  if (!methodologyResult.valid) {
    errors.push(...methodologyResult.errors);
  }

  const freezeRecordResult = validateFreezeRecord(value.freeze_record, 'freeze_record');
  if (!freezeRecordResult.valid) {
    errors.push(...freezeRecordResult.errors);
  }

  // Cross-reference validation: Role attachment (G-4)
  if (isArray(value.cells) && isArray(value.roles)) {
    const cellIds = new Set((value.cells as Cell[]).map((c) => c.cell_identifier));
    (value.roles as Role[]).forEach((role, index) => {
      if (!cellIds.has(role.attached_to_cell_identifier)) {
        errors.push({
          field: `roles[${index}].attached_to_cell_identifier`,
          message: `Role must be attached to an existing Cell. Cell "${role.attached_to_cell_identifier}" not found. (G-4)`,
          path: `roles[${index}]`,
        });
      }
    });
  }

  // Cross-reference validation: Relationship cell references
  if (isArray(value.topology) && isArray(value.cells)) {
    const cellIds = new Set((value.cells as Cell[]).map((c) => c.cell_identifier));
    (value.topology as Relationship[]).forEach((rel, index) => {
      if (!cellIds.has(rel.source_cell_identifier)) {
        errors.push({
          field: `topology[${index}].source_cell_identifier`,
          message: `Source Cell "${rel.source_cell_identifier}" not found.`,
          path: `topology[${index}]`,
        });
      }
      if (!cellIds.has(rel.target_cell_identifier)) {
        errors.push({
          field: `topology[${index}].target_cell_identifier`,
          message: `Target Cell "${rel.target_cell_identifier}" not found.`,
          path: `topology[${index}]`,
        });
      }
    });
  }

  return {
    valid: errors.length === 0,
    errors,
  };
}

