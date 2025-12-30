// Design-Time Frontend Types
// Authority: DT_FE_REQ_DRAFT.md + DT_FE_DECISION_RECORD_001.md

// DR-03: Only Draft / Frozen states allowed
export type CompanyStatus = 'draft' | 'frozen'

// Company (L1)
export interface Company {
  id: string // COMP-{UUID} format
  name: string
  description: string
  status: CompanyStatus
  createdAt: string
  createdBy: string
  methodology?: Methodology
}

// Cell (L2)
export interface Cell {
  id: string // CELL-{UUID} format
  name: string
  responsibilityWhat: string // What this cell is responsible for
  responsibilityWhatNot: string // What this cell is NOT responsible for
  roles: Role[]
}

// Role (L2 - Cell attached)
export interface Role {
  id: string
  name: string
  constraintType: 'allow' | 'forbid' | 'condition'
  description: string
}

// Topology Relation (L3)
export type RelationType = 'dependency' | 'reference' | 'input-output'

export interface Relation {
  id: string
  sourceCellId: string
  targetCellId: string
  type: RelationType
  description?: string
}

// Methodology (L4)
export interface Methodology {
  name: string
  description: string
  status: 'active' | 'frozen' | 'historical'
}

// Template (L5) - DR-01: Structural copy source only
export interface Template {
  id: string
  name: string
  description: string
  cellCount: number
  relationCount: number
  presetMethodology?: string
  // Template content (for preview/copy)
  company?: Company
  cells?: Cell[]
  relations?: Relation[]
}

