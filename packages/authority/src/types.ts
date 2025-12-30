/**
 * Authority Layer TypeScript Types
 * 
 * Authority: docs/authority/*_FROZEN_001.md
 * Highest Authority: docs/frontend/DT_FE_DECISION_RECORD_001.md
 * 
 * These types represent the authoritative fact models as defined in the Authority Layer.
 * No additional fields or semantics may be added without extending the Authority schemas.
 */

// ============================================================================
// Company (AUTH_COMPANY_SCHEMA_FROZEN_001.md)
// ============================================================================

/**
 * Company Authority Schema
 * Total Fields: 5
 * - Identity Fields: company_identifier, company_name
 * - Descriptive Fields: company_description
 * - Provenance Fields: frozen_at, frozen_by
 */
export interface Company {
  /** Format: `COMP-{UUID}` (for Draft) or `FROZEN-COMP-{UUID}` (for Frozen) */
  company_identifier: string;
  company_name: string;
  company_description: string;
  /** Format: ISO 8601 `YYYY-MM-DDTHH:MM:SSZ` - immutable freeze timestamp */
  frozen_at: string;
  /** Human identifier (name, username, or ID) */
  frozen_by: string;
}

// ============================================================================
// Cell (AUTH_CELL_SCHEMA_FROZEN_001.md)
// ============================================================================

/**
 * Cell Authority Schema
 * Total Fields: 5
 * - Identity Fields: cell_identifier, cell_name
 * - Responsibility Declaration Fields: responsibility_what, responsibility_what_not
 * - Constraint Attachment: role_constraints (array of Role identifier references)
 */
export interface Cell {
  /** Format: `CELL-{UUID}` */
  cell_identifier: string;
  cell_name: string;
  responsibility_what: string;
  responsibility_what_not: string;
  /** Array of Role identifiers (references to Role facts) */
  role_constraints: string[]; // Array of role_identifier strings
}

// ============================================================================
// Role (AUTH_ROLE_SCHEMA_FROZEN_001.md)
// ============================================================================

/**
 * Role Authority Schema
 * Total Fields: 5
 * - Identity Fields: role_identifier, role_name
 * - Constraint Fields: constraint_type (enumeration), constraint_description
 * - Attachment Field: attached_to_cell_identifier (required reference)
 * 
 * Role is a constraint attached to a Cell. It cannot exist independently.
 */
export type RoleConstraintType = 'allow' | 'forbid' | 'condition';

export interface Role {
  /** Format: `ROLE-{UUID}` */
  role_identifier: string;
  role_name: string;
  constraint_type: RoleConstraintType;
  constraint_description: string;
  /** Format: `CELL-{UUID}` - Required reference to parent Cell */
  attached_to_cell_identifier: string;
}

// ============================================================================
// Topology (AUTH_TOPOLOGY_SCHEMA_FROZEN_001.md)
// ============================================================================

/**
 * Topology Relationship Type Enumeration
 * Relationship types are **nouns**, not verbs.
 * No execution semantics are implied.
 */
export type RelationshipType = 'dependency' | 'reference' | 'input_output';

/**
 * Topology Authority Schema (per relationship fact)
 * Total Fields: 5 (4 required, 1 optional)
 * - Identity Fields: relationship_identifier
 * - Reference Fields: source_cell_identifier, target_cell_identifier
 * - Type Declaration: relationship_type (enumeration)
 * - Descriptive Fields: relationship_description (optional)
 */
export interface Relationship {
  /** Format: `REL-{UUID}` */
  relationship_identifier: string;
  /** Format: `CELL-{UUID}` */
  source_cell_identifier: string;
  /** Format: `CELL-{UUID}` */
  target_cell_identifier: string;
  relationship_type: RelationshipType;
  /** Optional descriptive text */
  relationship_description?: string;
}

/**
 * Topology is a collection of relationship facts
 */
export type Topology = Relationship[];

// ============================================================================
// Methodology (AUTH_METHODOLOGY_SCHEMA_FROZEN_001.md)
// ============================================================================

/**
 * Methodology Authority Schema
 * Total Fields: 3 (2 required, 1 optional)
 * - Identity Fields: methodology_identifier, methodology_name
 * - Descriptive Fields: methodology_description (optional)
 * 
 * Methodology is perspective metadata for human understanding only.
 * It does not change facts, create conflicts, or affect Freeze legality.
 */
export interface Methodology {
  /** Format: `METH-{UUID}` */
  methodology_identifier: string;
  methodology_name: string;
  /** Optional descriptive text */
  methodology_description?: string;
}

// ============================================================================
// FreezeRecord (AUTH_FREEZE_RECORD_SCHEMA_FROZEN_001.md)
// ============================================================================

/**
 * Freeze Record Authority Schema
 * Total Fields: 6 (4 required, 2 optional)
 * - Identity Fields: freeze_record_identifier
 * - Reference Fields: frozen_company_identifier, draft_identifier (optional)
 * - Timestamp Fields: frozen_at
 * - Declarer Fields: frozen_by
 * - Summary Fields: freeze_summary (optional)
 * 
 * Freeze Record is an immutable provenance record (not event, not activation).
 * It documents when and by whom a Company was frozen.
 */
export interface FreezeRecord {
  /** Format: `FREEZE-{UUID}` */
  freeze_record_identifier: string;
  /** Format: `FROZEN-COMP-{UUID}` */
  frozen_company_identifier: string;
  /** Format: ISO 8601 `YYYY-MM-DDTHH:MM:SSZ` - immutable freeze timestamp */
  frozen_at: string;
  /** Human identifier (name, username, or ID) */
  frozen_by: string;
  /** Optional human-provided summary or notes */
  freeze_summary?: string;
  /** Optional: Format `COMP-{UUID}` - original Draft identifier */
  draft_identifier?: string;
}

// ============================================================================
// Frozen Snapshot Bundle
// ============================================================================

/**
 * Complete frozen snapshot bundle containing all authority facts
 * for a single frozen Company.
 */
export interface FrozenSnapshot {
  company: Company;
  cells: Cell[];
  roles: Role[];
  topology: Topology;
  methodology: Methodology;
  freeze_record: FreezeRecord;
}

