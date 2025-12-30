/**
 * Run-Time Frontend Type Exports
 * 
 * Authority: Run-Time Frontend now uses Authority types via view models.
 * 
 * All Authority-like types have been removed and replaced with:
 * 1. Direct imports from @ai-workbench/authority (for validation boundaries)
 * 2. View models (camelCase transformations) for UI rendering
 * 
 * This file re-exports view models for convenience.
 * The actual Authority types are imported from @ai-workbench/authority where needed.
 */

// Re-export Authority types (for validation and data loading)
export type {
  FrozenSnapshot,
  Company,
  Cell,
  Role,
  Relationship,
  Topology,
  Methodology,
  FreezeRecord,
} from '@ai-workbench/authority';

// Re-export view models (for UI rendering)
export type {
  FrozenSnapshotViewModel,
  CompanyViewModel,
  CellViewModel,
  RoleViewModel,
  RelationshipViewModel,
  MethodologyViewModel,
  FreezeRecordViewModel,
} from './viewModels';
