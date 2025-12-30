/**
 * Validation Tests
 * 
 * Tests for T-1, T-3, T-4 as specified in WO-AUTH-INTEGRATION-AND-GUARDRAILS-001
 */

import {
  validateCompany,
  validateCell,
  validateRole,
  validateRelationship,
  validateTopology,
  validateMethodology,
  validateFreezeRecord,
  validateFrozenSnapshot,
} from '../validate';
import type { Company, Cell, Role, Relationship, Methodology, FreezeRecord } from '../types';

// ============================================================================
// T-1: Schema Strict Test
// ============================================================================

describe('T-1: Schema Strict Test - Unknown fields must fail validation', () => {
  const validCompany: Company = {
    company_identifier: 'FROZEN-COMP-12345678-1234-1234-1234-123456789012',
    company_name: 'Test Company',
    company_description: 'Test description',
    frozen_at: '2025-12-28T10:00:00Z',
    frozen_by: 'test-user',
  };

  test('should reject Company with unknown field', () => {
    const invalid = { ...validCompany, status: 'active' } as unknown;
    const result = validateCompany(invalid);
    expect(result.valid).toBe(false);
    expect(result.errors.some((e) => e.message.includes('Unknown fields'))).toBe(true);
  });

  test('should reject Company with multiple unknown fields', () => {
    const invalid = { ...validCompany, status: 'active', progress: 50 } as unknown;
    const result = validateCompany(invalid);
    expect(result.valid).toBe(false);
    expect(result.errors.some((e) => e.message.includes('status') && e.message.includes('progress'))).toBe(true);
  });

  test('should accept Company with only allowed fields', () => {
    const result = validateCompany(validCompany);
    expect(result.valid).toBe(true);
    expect(result.errors.length).toBe(0);
  });
});

describe('T-1: Cell Schema Strict Test', () => {
  const validCell: Cell = {
    cell_identifier: 'CELL-12345678-1234-1234-1234-123456789012',
    cell_name: 'Test Cell',
    responsibility_what: 'Test responsibility',
    responsibility_what_not: 'Test boundary',
    role_constraints: [],
  };

  test('should reject Cell with unknown field', () => {
    const invalid = { ...validCell, status: 'active' } as unknown;
    const result = validateCell(invalid);
    expect(result.valid).toBe(false);
    expect(result.errors.some((e) => e.message.includes('Unknown fields'))).toBe(true);
  });

  test('should accept Cell with only allowed fields', () => {
    const result = validateCell(validCell);
    expect(result.valid).toBe(true);
  });
});

// ============================================================================
// T-3: Role Attachment Test
// ============================================================================

describe('T-3: Role Attachment Test - Roles must have attached_to_cell_identifier', () => {
  const validCellId = 'CELL-12345678-1234-1234-1234-123456789012';

  test('should reject Role without attached_to_cell_identifier', () => {
    const invalidRole = {
      role_identifier: 'ROLE-12345678-1234-1234-1234-123456789012',
      role_name: 'Test Role',
      constraint_type: 'allow' as const,
      constraint_description: 'Test constraint',
      // missing attached_to_cell_identifier
    };
    const result = validateRole(invalidRole);
    expect(result.valid).toBe(false);
    expect(
      result.errors.some((e) => e.message.includes('attached_to_cell_identifier') || e.message.includes('G-4'))
    ).toBe(true);
  });

  test('should accept Role with attached_to_cell_identifier', () => {
    const validRole: Role = {
      role_identifier: 'ROLE-12345678-1234-1234-1234-123456789012',
      role_name: 'Test Role',
      constraint_type: 'allow',
      constraint_description: 'Test constraint',
      attached_to_cell_identifier: validCellId,
    };
    const result = validateRole(validRole);
    expect(result.valid).toBe(true);
  });

  test('should reject Role with invalid cell identifier format', () => {
    const invalidRole = {
      role_identifier: 'ROLE-12345678-1234-1234-1234-123456789012',
      role_name: 'Test Role',
      constraint_type: 'allow' as const,
      constraint_description: 'Test constraint',
      attached_to_cell_identifier: 'INVALID-ID',
    };
    const result = validateRole(invalidRole);
    expect(result.valid).toBe(false);
    expect(result.errors.some((e) => e.message.includes('CELL'))).toBe(true);
  });
});

describe('T-3: Role Attachment Cross-Reference Test', () => {
  test('should reject Role attached to non-existent Cell in snapshot', () => {
    const snapshot = {
      company: {
        company_identifier: 'FROZEN-COMP-12345678-1234-1234-1234-123456789012',
        company_name: 'Test',
        company_description: 'Test',
        frozen_at: '2025-12-28T10:00:00Z',
        frozen_by: 'test-user',
      },
      cells: [
        {
          cell_identifier: 'CELL-EXISTING-1234-1234-1234-123456789012',
          cell_name: 'Existing Cell',
          responsibility_what: 'Test',
          responsibility_what_not: 'Test',
          role_constraints: [],
        },
      ],
      roles: [
        {
          role_identifier: 'ROLE-12345678-1234-1234-1234-123456789012',
          role_name: 'Test Role',
          constraint_type: 'allow' as const,
          constraint_description: 'Test',
          attached_to_cell_identifier: 'CELL-NONEXISTENT-1234-1234-1234-123456789012',
        },
      ],
      topology: [],
      methodology: {
        methodology_identifier: 'METH-12345678-1234-1234-1234-123456789012',
        methodology_name: 'Test',
      },
      freeze_record: {
        freeze_record_identifier: 'FREEZE-12345678-1234-1234-1234-123456789012',
        frozen_company_identifier: 'FROZEN-COMP-12345678-1234-1234-1234-123456789012',
        frozen_at: '2025-12-28T10:00:00Z',
        frozen_by: 'test-user',
      },
    };

    const result = validateFrozenSnapshot(snapshot);
    expect(result.valid).toBe(false);
    expect(
      result.errors.some((e) => e.message.includes('not found') || e.message.includes('G-4'))
    ).toBe(true);
  });
});

// ============================================================================
// T-4: Topology Type Enum Test
// ============================================================================

describe('T-4: Topology Type Enum Test - Only 3 types allowed', () => {
  const validRelationship: Relationship = {
    relationship_identifier: 'REL-12345678-1234-1234-1234-123456789012',
    source_cell_identifier: 'CELL-11111111-1111-1111-1111-111111111111',
    target_cell_identifier: 'CELL-22222222-2222-2222-2222-222222222222',
    relationship_type: 'dependency',
    relationship_description: 'Test',
  };

  test('should accept valid relationship types', () => {
    const validTypes: Array<'dependency' | 'reference' | 'input_output'> = [
      'dependency',
      'reference',
      'input_output',
    ];

    validTypes.forEach((type) => {
      const rel = { ...validRelationship, relationship_type: type };
      const result = validateRelationship(rel);
      expect(result.valid).toBe(true);
    });
  });

  test('should reject invalid relationship types', () => {
    const invalidTypes = ['executes', 'triggers', 'flows', 'step', 'order', 'next'];

    invalidTypes.forEach((type) => {
      const invalidRel = { ...validRelationship, relationship_type: type as any };
      const result = validateRelationship(invalidRel);
      expect(result.valid).toBe(false);
      expect(
        result.errors.some(
          (e) =>
            e.message.includes('relationship_type') ||
            e.message.includes('dependency, reference, input_output')
        )
      ).toBe(true);
    });
  });

  test('should reject relationship with unknown field', () => {
    const invalid = { ...validRelationship, execution_order: 1 } as unknown;
    const result = validateRelationship(invalid);
    expect(result.valid).toBe(false);
    expect(result.errors.some((e) => e.message.includes('Unknown fields'))).toBe(true);
  });
});

// ============================================================================
// T-5: Freeze Timestamp Label Test (Partial - Full test in guards.test.ts)
// ============================================================================

describe('T-5: Freeze Timestamp Validation Test', () => {
  test('should accept valid ISO 8601 timestamp', () => {
    const validFreezeRecord: FreezeRecord = {
      freeze_record_identifier: 'FREEZE-12345678-1234-1234-1234-123456789012',
      frozen_company_identifier: 'FROZEN-COMP-12345678-1234-1234-1234-123456789012',
      frozen_at: '2025-12-28T10:00:00Z',
      frozen_by: 'test-user',
    };
    const result = validateFreezeRecord(validFreezeRecord);
    expect(result.valid).toBe(true);
  });

  test('should reject invalid timestamp format', () => {
    const invalidFreezeRecord = {
      freeze_record_identifier: 'FREEZE-12345678-1234-1234-1234-123456789012',
      frozen_company_identifier: 'FROZEN-COMP-12345678-1234-1234-1234-123456789012',
      frozen_at: '2025-12-28 10:00:00', // Invalid format
      frozen_by: 'test-user',
    };
    const result = validateFreezeRecord(invalidFreezeRecord);
    expect(result.valid).toBe(false);
    expect(result.errors.some((e) => e.message.includes('ISO 8601'))).toBe(true);
  });
});

// ============================================================================
// T-6: Snapshot Roundtrip Test
// ============================================================================

describe('T-6: Snapshot Roundtrip Test - Valid snapshot must pass validation', () => {
  const validSnapshot = {
    company: {
      company_identifier: 'FROZEN-COMP-12345678-1234-1234-1234-123456789012',
      company_name: 'Test Company',
      company_description: 'Test description',
      frozen_at: '2025-12-28T10:00:00Z',
      frozen_by: 'test-user',
    },
    cells: [
      {
        cell_identifier: 'CELL-11111111-1111-1111-1111-111111111111',
        cell_name: 'Cell 1',
        responsibility_what: 'Responsibility 1',
        responsibility_what_not: 'Boundary 1',
        role_constraints: ['ROLE-11111111-1111-1111-1111-111111111111'],
      },
      {
        cell_identifier: 'CELL-22222222-2222-2222-2222-222222222222',
        cell_name: 'Cell 2',
        responsibility_what: 'Responsibility 2',
        responsibility_what_not: 'Boundary 2',
        role_constraints: [],
      },
    ],
    roles: [
      {
        role_identifier: 'ROLE-11111111-1111-1111-1111-111111111111',
        role_name: 'Role 1',
        constraint_type: 'allow' as const,
        constraint_description: 'Constraint 1',
        attached_to_cell_identifier: 'CELL-11111111-1111-1111-1111-111111111111',
      },
    ],
    topology: [
      {
        relationship_identifier: 'REL-11111111-1111-1111-1111-111111111111',
        source_cell_identifier: 'CELL-11111111-1111-1111-1111-111111111111',
        target_cell_identifier: 'CELL-22222222-2222-2222-2222-222222222222',
        relationship_type: 'dependency',
        relationship_description: 'Test relationship',
      },
    ],
    methodology: {
      methodology_identifier: 'METH-12345678-1234-1234-1234-123456789012',
      methodology_name: 'Test Methodology',
      methodology_description: 'Test description',
    },
    freeze_record: {
      freeze_record_identifier: 'FREEZE-12345678-1234-1234-1234-123456789012',
      frozen_company_identifier: 'FROZEN-COMP-12345678-1234-1234-1234-123456789012',
      frozen_at: '2025-12-28T10:00:00Z',
      frozen_by: 'test-user',
    },
  };

  test('should accept valid complete snapshot', () => {
    const result = validateFrozenSnapshot(validSnapshot);
    expect(result.valid).toBe(true);
    expect(result.errors.length).toBe(0);
  });

  test('should reject snapshot with missing required field', () => {
    const invalid = {
      ...validSnapshot,
      company: {
        ...validSnapshot.company,
        // @ts-expect-error - missing frozen_by
        frozen_by: undefined,
      },
    };
    const result = validateFrozenSnapshot(invalid);
    expect(result.valid).toBe(false);
    expect(result.errors.length).toBeGreaterThan(0);
  });
});

