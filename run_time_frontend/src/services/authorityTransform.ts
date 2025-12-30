/**
 * Authority to View Model Transformation
 * 
 * Authority: One-way transformation from Authority types (snake_case) to View Models (camelCase)
 * 
 * Rules:
 * - Field name only: Transform snake_case to camelCase
 * - No semantic changes: Field meaning must remain identical
 * - No field additions: Cannot add fields not in Authority type
 * - No field removal: Cannot remove required Authority fields
 * - Enum values unchanged: Enum values remain as-is
 */

import type {
  Company,
  Cell,
  Role,
  Relationship,
  Methodology,
  FreezeRecord,
  FrozenSnapshot,
} from '@ai-workbench/authority';

import type {
  CompanyViewModel,
  CellViewModel,
  RoleViewModel,
  RelationshipViewModel,
  MethodologyViewModel,
  FreezeRecordViewModel,
  FrozenSnapshotViewModel,
} from '../types/viewModels';

/**
 * Transform Authority Company to View Model
 */
export function transformCompany(authority: Company): CompanyViewModel {
  return {
    companyIdentifier: authority.company_identifier,
    companyName: authority.company_name,
    companyDescription: authority.company_description,
    frozenAt: authority.frozen_at,
    frozenBy: authority.frozen_by,
  };
}

/**
 * Transform Authority Cell to View Model
 */
export function transformCell(authority: Cell): CellViewModel {
  return {
    cellIdentifier: authority.cell_identifier,
    cellName: authority.cell_name,
    responsibilityWhat: authority.responsibility_what,
    responsibilityWhatNot: authority.responsibility_what_not,
    roleConstraints: authority.role_constraints, // Array of identifiers (unchanged)
  };
}

/**
 * Transform Authority Role to View Model
 */
export function transformRole(authority: Role): RoleViewModel {
  return {
    roleIdentifier: authority.role_identifier,
    roleName: authority.role_name,
    constraintType: authority.constraint_type, // Enum unchanged
    constraintDescription: authority.constraint_description,
    attachedToCellIdentifier: authority.attached_to_cell_identifier,
  };
}

/**
 * Transform Authority Relationship to View Model
 */
export function transformRelationship(authority: Relationship): RelationshipViewModel {
  return {
    relationshipIdentifier: authority.relationship_identifier,
    sourceCellIdentifier: authority.source_cell_identifier,
    targetCellIdentifier: authority.target_cell_identifier,
    relationshipType: authority.relationship_type, // Enum unchanged
    relationshipDescription: authority.relationship_description,
  };
}

/**
 * Transform Authority Methodology to View Model
 */
export function transformMethodology(authority: Methodology): MethodologyViewModel {
  return {
    methodologyIdentifier: authority.methodology_identifier,
    methodologyName: authority.methodology_name,
    methodologyDescription: authority.methodology_description,
  };
}

/**
 * Transform Authority FreezeRecord to View Model
 */
export function transformFreezeRecord(authority: FreezeRecord): FreezeRecordViewModel {
  return {
    freezeRecordIdentifier: authority.freeze_record_identifier,
    frozenCompanyIdentifier: authority.frozen_company_identifier,
    frozenAt: authority.frozen_at,
    frozenBy: authority.frozen_by,
    freezeSummary: authority.freeze_summary,
    draftIdentifier: authority.draft_identifier,
  };
}

/**
 * Transform Authority FrozenSnapshot to View Model
 */
export function transformFrozenSnapshot(authority: FrozenSnapshot): FrozenSnapshotViewModel {
  return {
    company: transformCompany(authority.company),
    cells: authority.cells.map(transformCell),
    roles: authority.roles.map(transformRole),
    topology: authority.topology.map(transformRelationship),
    methodology: transformMethodology(authority.methodology),
    freezeRecord: transformFreezeRecord(authority.freeze_record),
  };
}

