/**
 * Data Loader for Company Viewer
 * 
 * Loads company data from snapshots.
 * This is a simplified, human-friendly interface that hides technical details.
 */

export interface Company {
  name: string
  description: string
  createdAt: string
  createdBy: string
}

export interface Team {
  id: string
  name: string
  purpose: string
  boundaries: string
  responsibilities: Responsibility[]
}

export interface Responsibility {
  id: string
  name: string
  type: 'allowed' | 'forbidden' | 'conditional'
  description: string
}

export interface Connection {
  id: string
  fromTeam: string
  toTeam: string
  type: 'depends-on' | 'references' | 'provides-to'
  description?: string
}

export interface Approach {
  id: string
  name: string
  description?: string
}

export interface CompanyData {
  company: Company
  teams: Team[]
  connections: Connection[]
  approach: Approach | null
}

/**
 * Load company data from snapshot files
 */
export async function loadCompanyData(companyId: string = 'FROZEN-COMP-DEFAULT'): Promise<CompanyData | null> {
  try {
    const baseUrl = '/snapshots/authority'
    const snapshotDir = `${baseUrl}/${companyId}`

    // Load all data files
    const [companyRes, cellsRes, rolesRes, topologyRes, methodologyRes] = await Promise.all([
      fetch(`${snapshotDir}/company.json`),
      fetch(`${snapshotDir}/cells.json`),
      fetch(`${snapshotDir}/roles.json`),
      fetch(`${snapshotDir}/topology.json`),
      fetch(`${snapshotDir}/methodology.json`),
    ])

    if (!companyRes.ok || !cellsRes.ok || !rolesRes.ok || !topologyRes.ok) {
      return null
    }

    const companyData = await companyRes.json()
    const cellsData = await cellsRes.json()
    const rolesData = await rolesRes.json()
    const topologyData = await topologyRes.json()
    const methodologyData = methodologyRes.ok ? await methodologyRes.json() : null

    // Transform to human-friendly format
    const company: Company = {
      name: companyData.company_name || '',
      description: companyData.company_description || '',
      createdAt: companyData.frozen_at || '',
      createdBy: companyData.frozen_by || '',
    }

    // Transform cells to teams
    const cellsArray = Array.isArray(cellsData) ? cellsData : cellsData.cells || []
    const teams: Team[] = cellsArray.map((cell: any) => {
      // Find roles for this cell
      const rolesArray = Array.isArray(rolesData) ? rolesData : rolesData.roles || []
      const cellRoles = rolesArray.filter(
        (role: any) => role.attached_to_cell_identifier === cell.cell_identifier
      )

      const responsibilities: Responsibility[] = cellRoles.map((role: any) => ({
        id: role.role_identifier || '',
        name: role.role_name || '',
        type: role.constraint_type === 'allow' ? 'allowed' 
            : role.constraint_type === 'forbid' ? 'forbidden' 
            : 'conditional',
        description: role.constraint_description || '',
      }))

      return {
        id: cell.cell_identifier || '',
        name: cell.cell_name || '',
        purpose: cell.responsibility_what || '',
        boundaries: cell.responsibility_what_not || '',
        responsibilities,
      }
    })

    // Transform relationships to connections
    const connections: Connection[] = (Array.isArray(topologyData) ? topologyData : topologyData.relationships || []).map((rel: any) => ({
      id: rel.relationship_identifier || '',
      fromTeam: rel.source_cell_identifier || '',
      toTeam: rel.target_cell_identifier || '',
      type: rel.relationship_type === 'dependency' ? 'depends-on'
          : rel.relationship_type === 'reference' ? 'references'
          : 'provides-to',
      description: rel.relationship_description,
    }))

    // Transform methodology to approach
    const approach: Approach | null = methodologyData ? {
      id: methodologyData.methodology_identifier || '',
      name: methodologyData.methodology_name || '',
      description: methodologyData.methodology_description,
    } : null

    return {
      company,
      teams,
      connections,
      approach,
    }
  } catch (error) {
    console.error('Error loading company data:', error)
    return null
  }
}

