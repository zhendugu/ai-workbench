/**
 * Guards Tests
 * 
 * Tests for T-2, T-5 (guard aspects) as specified in WO-AUTH-INTEGRATION-AND-GUARDRAILS-001
 */

import {
  guardNoDynamicVocabulary,
  guardNoTemporalVocabulary,
  guardFreezeTimestampLabel,
  guardNoInterpretation,
  guardCopyReadOnly,
  guardRoleAttachment,
  guardTopologyTypeEnum,
  runAllGuards,
} from '../guards';
import type { Role, Relationship } from '../types';

// ============================================================================
// T-2: Forbidden Vocabulary Scan (Guard aspects)
// ============================================================================

describe('T-2: Forbidden Vocabulary Scan - G-2: No Dynamic Vocabulary', () => {
  test('should reject "current" in non-prohibition context', () => {
    expect(guardNoDynamicVocabulary('Current status: active')).toBe(false);
  });

  test('should reject "latest" in non-prohibition context', () => {
    expect(guardNoDynamicVocabulary('Latest update')).toBe(false);
  });

  test('should reject "last updated" in non-prohibition context', () => {
    expect(guardNoDynamicVocabulary('Last updated: 2025-12-28')).toBe(false);
  });

  test('should reject "running" in non-prohibition context', () => {
    expect(guardNoDynamicVocabulary('System is running')).toBe(false);
  });

  test('should allow forbidden words in prohibition context', () => {
    expect(guardNoDynamicVocabulary('Does NOT contain: Current anything')).toBe(true);
    expect(guardNoDynamicVocabulary('Forbidden: latest status')).toBe(true);
    expect(guardNoDynamicVocabulary('Must not use "last updated"')).toBe(true);
  });

  test('should allow normal text without forbidden vocabulary', () => {
    expect(guardNoDynamicVocabulary('Company name: Test')).toBe(true);
    expect(guardNoDynamicVocabulary('Cell responsibility declaration')).toBe(true);
    expect(guardNoDynamicVocabulary('Frozen at: 2025-12-28T10:00:00Z')).toBe(true);
  });
});

describe('T-2: Temporal Vocabulary - G-5: No Temporal Concepts', () => {
  test('should reject temporal vocabulary in relationship description', () => {
    expect(guardNoTemporalVocabulary('This executes before that')).toBe(false);
    expect(guardNoTemporalVocabulary('Step 1: do this')).toBe(false);
    expect(guardNoTemporalVocabulary('Next: trigger action')).toBe(false);
    expect(guardNoTemporalVocabulary('Run after completion')).toBe(false);
  });

  test('should allow temporal vocabulary in prohibition context', () => {
    expect(guardNoTemporalVocabulary('Does NOT express: execution order')).toBe(true);
    expect(guardNoTemporalVocabulary('Forbidden: step, order, next')).toBe(true);
  });

  test('should allow normal relationship descriptions', () => {
    expect(guardNoTemporalVocabulary('Cell A depends on Cell B')).toBe(true);
    expect(guardNoTemporalVocabulary('Structural reference relationship')).toBe(true);
    expect(guardNoTemporalVocabulary(undefined)).toBe(true); // Optional field
  });
});

describe('T-2: Interpretation Vocabulary - G-7: Frontend No Interpretation', () => {
  test('should reject health/risk/completeness scores', () => {
    expect(guardNoInterpretation('Health score: 85%')).toBe(false);
    expect(guardNoInterpretation('Risk level: High')).toBe(false);
    expect(guardNoInterpretation('Completeness indicator: 90%')).toBe(false);
    expect(guardNoInterpretation('Quality score: 4.5/5')).toBe(false);
    expect(guardNoInterpretation('Maturity level: Advanced')).toBe(false);
  });

  test('should reject recommendation vocabulary', () => {
    expect(guardNoInterpretation('Recommended: Add more cells')).toBe(false);
    expect(guardNoInterpretation('Should improve structure')).toBe(false);
    expect(guardNoInterpretation('Best practice: use templates')).toBe(false);
    expect(guardNoInterpretation('Suggestion: optimize topology')).toBe(false);
  });

  test('should allow prohibition contexts', () => {
    expect(guardNoInterpretation('Does NOT provide health scores')).toBe(true);
    expect(guardNoInterpretation('Forbidden: recommendations')).toBe(true);
  });

  test('should allow normal UI labels', () => {
    expect(guardNoInterpretation('Company Name')).toBe(true);
    expect(guardNoInterpretation('Cell Responsibility')).toBe(true);
    expect(guardNoInterpretation('Frozen at: 2025-12-28T10:00:00Z')).toBe(true);
  });
});

// ============================================================================
// T-5: Freeze Timestamp Label Test - G-6
// ============================================================================

describe('T-5: Freeze Timestamp Label Test - G-6: Must use "Frozen at"', () => {
  test('should accept "Frozen at" label', () => {
    expect(guardFreezeTimestampLabel('Frozen at')).toBe(true);
    expect(guardFreezeTimestampLabel('Frozen At')).toBe(true);
    expect(guardFreezeTimestampLabel('frozen at')).toBe(true);
  });

  test('should reject "Last updated" label', () => {
    expect(guardFreezeTimestampLabel('Last updated')).toBe(false);
    expect(guardFreezeTimestampLabel('Updated at')).toBe(false);
  });

  test('should reject other forbidden labels', () => {
    expect(guardFreezeTimestampLabel('Current')).toBe(false);
    expect(guardFreezeTimestampLabel('Latest')).toBe(false);
    expect(guardFreezeTimestampLabel('Recent')).toBe(false);
    expect(guardFreezeTimestampLabel('Modified at')).toBe(false);
    expect(guardFreezeTimestampLabel('Changed at')).toBe(false);
  });

  test('should accept neutral labels', () => {
    expect(guardFreezeTimestampLabel('Timestamp')).toBe(true);
    expect(guardFreezeTimestampLabel('Date')).toBe(true);
  });
});

// ============================================================================
// T-2: Copy Behavior - G-8
// ============================================================================

describe('T-2: Copy Behavior - G-8: Copy Read-Only', () => {
  test('should allow copy actions', () => {
    expect(guardCopyReadOnly('Copy')).toBe(true);
    expect(guardCopyReadOnly('Copy ID')).toBe(true);
    expect(guardCopyReadOnly('Copy Snapshot ID')).toBe(true);
    expect(guardCopyReadOnly('Copy identifier')).toBe(true);
  });

  test('should reject forbidden actions', () => {
    expect(guardCopyReadOnly('Export')).toBe(false);
    expect(guardCopyReadOnly('Publish')).toBe(false);
    expect(guardCopyReadOnly('Deploy')).toBe(false);
    expect(guardCopyReadOnly('Activate')).toBe(false);
    expect(guardCopyReadOnly('Release')).toBe(false);
    expect(guardCopyReadOnly('Recommend')).toBe(false);
    expect(guardCopyReadOnly('Share')).toBe(false);
  });

  test('should reject combined actions with forbidden words', () => {
    expect(guardCopyReadOnly('Copy and Export')).toBe(false);
    expect(guardCopyReadOnly('Export Snapshot')).toBe(false);
    expect(guardCopyReadOnly('Publish to Production')).toBe(false);
  });

  test('should allow neutral actions', () => {
    expect(guardCopyReadOnly('View')).toBe(true);
    expect(guardCopyReadOnly('Show Details')).toBe(true);
    expect(guardCopyReadOnly('Close')).toBe(true);
  });
});

// ============================================================================
// Additional Guard Tests
// ============================================================================

describe('G-4: Role Attachment Guard', () => {
  const validCellIds = new Set(['CELL-11111111-1111-1111-1111-111111111111']);

  test('should accept Role attached to existing Cell', () => {
    const role: Role = {
      role_identifier: 'ROLE-12345678-1234-1234-1234-123456789012',
      role_name: 'Test Role',
      constraint_type: 'allow',
      constraint_description: 'Test',
      attached_to_cell_identifier: 'CELL-11111111-1111-1111-1111-111111111111',
    };
    expect(guardRoleAttachment(role, validCellIds)).toBe(true);
  });

  test('should reject Role attached to non-existent Cell', () => {
    const role: Role = {
      role_identifier: 'ROLE-12345678-1234-1234-1234-123456789012',
      role_name: 'Test Role',
      constraint_type: 'allow',
      constraint_description: 'Test',
      attached_to_cell_identifier: 'CELL-NONEXISTENT-1234-1234-1234-123456789012',
    };
    expect(guardRoleAttachment(role, validCellIds)).toBe(false);
  });
});

describe('G-5: Topology Type Enum Guard', () => {
  test('should accept valid relationship types', () => {
    expect(guardTopologyTypeEnum('dependency')).toBe(true);
    expect(guardTopologyTypeEnum('reference')).toBe(true);
    expect(guardTopologyTypeEnum('input_output')).toBe(true);
  });

  test('should reject invalid relationship types', () => {
    expect(guardTopologyTypeEnum('executes')).toBe(false);
    expect(guardTopologyTypeEnum('triggers')).toBe(false);
    expect(guardTopologyTypeEnum('flows')).toBe(false);
    expect(guardTopologyTypeEnum('step')).toBe(false);
    expect(guardTopologyTypeEnum('order')).toBe(false);
  });
});

describe('runAllGuards Integration Test', () => {
  test('should run all applicable guards and return results', () => {
    const data = {
      company: {
        company_identifier: 'FROZEN-COMP-12345678-1234-1234-1234-123456789012',
        company_name: 'Test',
        company_description: 'Test',
        frozen_at: '2025-12-28T10:00:00Z',
        frozen_by: 'test-user',
      },
      cells: [
        {
          cell_identifier: 'CELL-11111111-1111-1111-1111-111111111111',
          cell_name: 'Test Cell',
          responsibility_what: 'Test',
          responsibility_what_not: 'Test',
          role_constraints: [],
        },
      ],
      roles: [
        {
          role_identifier: 'ROLE-11111111-1111-1111-1111-111111111111',
          role_name: 'Test Role',
          constraint_type: 'allow' as const,
          constraint_description: 'Test',
          attached_to_cell_identifier: 'CELL-11111111-1111-1111-1111-111111111111',
        },
      ],
      relationships: [
        {
          relationship_identifier: 'REL-11111111-1111-1111-1111-111111111111',
          source_cell_identifier: 'CELL-11111111-1111-1111-1111-111111111111',
          target_cell_identifier: 'CELL-11111111-1111-1111-1111-111111111111',
          relationship_type: 'dependency',
        },
      ],
      uiLabels: ['Company Name', 'Cell Responsibility', 'Frozen at: 2025-12-28'],
    };

    const results = runAllGuards(data);
    expect(results.length).toBeGreaterThan(0);
    expect(results.every((r) => r.passed)).toBe(true);
  });

  test('should detect violations in UI labels', () => {
    const data = {
      uiLabels: ['Current status: active', 'Latest update', 'Recommend: improve structure'],
    };

    const results = runAllGuards(data);
    const failedGuards = results.filter((r) => !r.passed);
    expect(failedGuards.length).toBeGreaterThan(0);
  });
});

