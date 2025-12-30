/**
 * View Model Types for Run-Time Frontend
 * 
 * Authority: These are camelCase view models derived from Authority types.
 * They are display-only transformations with no semantic changes.
 * 
 * Source: Authority types from @ai-workbench/authority (snake_case)
 * Transformation: Pure naming transformation (snake_case -> camelCase) only
 * 
 * These types represent the same Authority facts in a format convenient for UI rendering.
 * They are NOT Authority facts themselves - they are derived views.
 */

/**
 * View model for Company Authority fact
 * Derived from Authority Company type via naming transformation only
 */
export interface CompanyViewModel {
  companyIdentifier: string; // company_identifier
  companyName: string; // company_name
  companyDescription: string; // company_description
  frozenAt: string; // frozen_at
  frozenBy: string; // frozen_by
}

/**
 * View model for Cell Authority fact
 * Derived from Authority Cell type via naming transformation only
 */
export interface CellViewModel {
  cellIdentifier: string; // cell_identifier
  cellName: string; // cell_name
  responsibilityWhat: string; // responsibility_what
  responsibilityWhatNot: string; // responsibility_what_not
  roleConstraints: string[]; // role_constraints (array of role identifiers)
}

/**
 * View model for Role Authority fact
 * Derived from Authority Role type via naming transformation only
 */
export interface RoleViewModel {
  roleIdentifier: string; // role_identifier
  roleName: string; // role_name
  constraintType: 'allow' | 'forbid' | 'condition'; // constraint_type (enum unchanged)
  constraintDescription: string; // constraint_description
  attachedToCellIdentifier: string; // attached_to_cell_identifier
}

/**
 * View model for Relationship Authority fact
 * Derived from Authority Relationship type via naming transformation only
 */
export interface RelationshipViewModel {
  relationshipIdentifier: string; // relationship_identifier
  sourceCellIdentifier: string; // source_cell_identifier
  targetCellIdentifier: string; // target_cell_identifier
  relationshipType: 'dependency' | 'reference' | 'input_output'; // relationship_type (enum unchanged)
  relationshipDescription?: string; // relationship_description (optional)
}

/**
 * View model for Methodology Authority fact
 * Derived from Authority Methodology type via naming transformation only
 */
export interface MethodologyViewModel {
  methodologyIdentifier: string; // methodology_identifier
  methodologyName: string; // methodology_name
  methodologyDescription?: string; // methodology_description (optional)
}

/**
 * View model for FreezeRecord Authority fact
 * Derived from Authority FreezeRecord type via naming transformation only
 */
export interface FreezeRecordViewModel {
  freezeRecordIdentifier: string; // freeze_record_identifier
  frozenCompanyIdentifier: string; // frozen_company_identifier
  frozenAt: string; // frozen_at
  frozenBy: string; // frozen_by
  freezeSummary?: string; // freeze_summary (optional)
  draftIdentifier?: string; // draft_identifier (optional)
}

/**
 * View model bundle for complete frozen snapshot
 * Derived from Authority FrozenSnapshot type
 */
export interface FrozenSnapshotViewModel {
  company: CompanyViewModel;
  cells: CellViewModel[];
  roles: RoleViewModel[];
  topology: RelationshipViewModel[];
  methodology: MethodologyViewModel;
  freezeRecord: FreezeRecordViewModel;
}

