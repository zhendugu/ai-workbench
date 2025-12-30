// L2: Structure Layer - Cell Management
// Authority: DT_FE_REQ_DRAFT.md Section 2.2

import { useState } from 'react'
import type { Cell, Role } from '../../types'

interface CellManagementProps {
  cells: Cell[]
  onCellsChange: (cells: Cell[]) => void
  isFrozen: boolean
}

export function CellManagement({ cells, onCellsChange, isFrozen }: CellManagementProps) {
  const [showCreateDialog, setShowCreateDialog] = useState(false)
  const [editingCell, setEditingCell] = useState<Cell | null>(null)
  const [newCell, setNewCell] = useState<Partial<Cell>>({
    name: '',
    responsibilityWhat: '',
    responsibilityWhatNot: '',
    roles: [],
  })

  const handleCreateCell = () => {
    if (!newCell.name || !newCell.responsibilityWhat || !newCell.responsibilityWhatNot) return

    const cell: Cell = {
      id: `CELL-${Date.now()}`,
      name: newCell.name,
      responsibilityWhat: newCell.responsibilityWhat,
      responsibilityWhatNot: newCell.responsibilityWhatNot,
      roles: newCell.roles || [],
    }

    onCellsChange([...cells, cell])
    setNewCell({ name: '', responsibilityWhat: '', responsibilityWhatNot: '', roles: [] })
    setShowCreateDialog(false)
  }

  const handleDeleteCell = (id: string) => {
    if (confirm('Are you sure you want to delete this Cell? This action cannot be undone.')) {
      onCellsChange(cells.filter((cell) => cell.id !== id))
    }
  }

  const handleAddRole = (cellId: string) => {
    const cell = cells.find((c) => c.id === cellId)
    if (!cell) return

    const newRole: Role = {
      id: `ROLE-${Date.now()}`,
      name: '',
      constraintType: 'allow',
      description: '',
    }

    const updatedCells = cells.map((c) =>
      c.id === cellId ? { ...c, roles: [...c.roles, newRole] } : c
    )
    onCellsChange(updatedCells)
  }

  const handleUpdateRole = (cellId: string, roleId: string, updates: Partial<Role>) => {
    const updatedCells = cells.map((cell) => {
      if (cell.id !== cellId) return cell
      return {
        ...cell,
        roles: cell.roles.map((role) => (role.id === roleId ? { ...role, ...updates } : role)),
      }
    })
    onCellsChange(updatedCells)
  }

  const handleDeleteRole = (cellId: string, roleId: string) => {
    const updatedCells = cells.map((cell) => {
      if (cell.id !== cellId) return cell
      return {
        ...cell,
        roles: cell.roles.filter((role) => role.id !== roleId),
      }
    })
    onCellsChange(updatedCells)
  }

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-semibold">Cell Management</h2>
          <p className="text-sm text-gray-600 mt-1">Define minimum responsibility units and their boundaries</p>
        </div>
        {!isFrozen && (
          <button
            onClick={() => setShowCreateDialog(true)}
            className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
          >
            New Cell
          </button>
        )}
      </div>

      {/* Cell Design Constraints - DT_FE_REQ_DRAFT.md Section 2.2 */}
      <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-4">
        <div className="text-sm text-gray-700">
          <p className="font-medium mb-2">Cell Design Constraints (DESIGN-TIME ONLY):</p>
          <ul className="list-disc list-inside space-y-1 text-xs">
            <li>Cell is a responsibility declaration, NOT an executor</li>
            <li>Cell does NOT bind to AI, humans, or agents</li>
            <li>Cell does NOT contain execution logic</li>
            <li>Cell does NOT imply "who does the work"</li>
            <li>Role constraints define allowed/prohibited behaviors only</li>
          </ul>
        </div>
      </div>

      {/* Cell List */}
      {cells.length === 0 ? (
        <div className="bg-white border rounded-lg p-12 text-center text-gray-500">
          <p>No cells defined yet</p>
          <p className="text-xs mt-1">Create your first responsibility unit to begin</p>
        </div>
      ) : (
        <div className="space-y-4">
          {cells.map((cell) => (
            <div key={cell.id} className="bg-white border rounded-lg p-6">
              <div className="flex items-start justify-between mb-4">
                <div>
                  <div className="flex items-center gap-2 mb-2">
                    <h3 className="text-base font-mono">{cell.id}</h3>
                    <span className="px-2 py-1 text-xs font-mono border rounded bg-gray-100">
                      Responsibility Declaration
                    </span>
                  </div>
                  <p className="text-sm font-semibold">{cell.name}</p>
                </div>
                {!isFrozen && (
                  <button
                    onClick={() => handleDeleteCell(cell.id)}
                    className="px-3 py-1 text-sm text-red-600 border border-red-300 rounded hover:bg-red-50"
                  >
                    Delete
                  </button>
                )}
              </div>

              <div className="space-y-4">
                <div>
                  <label className="block text-xs font-mono text-gray-600 mb-1">
                    Responsibility Description (What)
                  </label>
                  {isFrozen ? (
                    <p className="text-sm">{cell.responsibilityWhat}</p>
                  ) : (
                    <textarea
                      value={cell.responsibilityWhat}
                      onChange={(e) => {
                        const updated = cells.map((c) =>
                          c.id === cell.id ? { ...c, responsibilityWhat: e.target.value } : c
                        )
                        onCellsChange(updated)
                      }}
                      className="w-full px-3 py-2 border rounded font-mono text-sm min-h-20"
                    />
                  )}
                </div>

                <div>
                  <label className="block text-xs font-mono text-gray-600 mb-1">
                    Responsibility Boundary (What NOT)
                  </label>
                  {isFrozen ? (
                    <p className="text-sm">{cell.responsibilityWhatNot}</p>
                  ) : (
                    <textarea
                      value={cell.responsibilityWhatNot}
                      onChange={(e) => {
                        const updated = cells.map((c) =>
                          c.id === cell.id ? { ...c, responsibilityWhatNot: e.target.value } : c
                        )
                        onCellsChange(updated)
                      }}
                      className="w-full px-3 py-2 border rounded font-mono text-sm min-h-20"
                    />
                  )}
                </div>

                {/* Role Constraints - DT_FE_REQ_DRAFT.md Section 2.3 */}
                <div className="mt-4 pt-4 border-t">
                  <div className="flex items-center justify-between mb-2">
                    <label className="text-xs font-mono text-gray-600">Attached Role Constraints</label>
                    {!isFrozen && (
                      <button
                        onClick={() => handleAddRole(cell.id)}
                        className="text-xs text-blue-600 hover:underline"
                      >
                        Add Role
                      </button>
                    )}
                  </div>
                  <p className="text-xs text-gray-500 mb-2">Role is a Cell constraint, not an independent entity.</p>

                  {cell.roles.length === 0 ? (
                    <p className="text-xs text-gray-400">No roles defined</p>
                  ) : (
                    <div className="space-y-2">
                      {cell.roles.map((role) => (
                        <div key={role.id} className="bg-gray-50 border rounded p-3">
                          <div className="flex items-start justify-between mb-2">
                            {isFrozen ? (
                              <p className="text-sm font-semibold">{role.name}</p>
                            ) : (
                              <input
                                type="text"
                                value={role.name}
                                onChange={(e) => handleUpdateRole(cell.id, role.id, { name: e.target.value })}
                                placeholder="Role name"
                                className="flex-1 px-2 py-1 border rounded text-sm font-mono"
                              />
                            )}
                            {!isFrozen && (
                              <button
                                onClick={() => handleDeleteRole(cell.id, role.id)}
                                className="ml-2 text-xs text-red-600 hover:underline"
                              >
                                Remove
                              </button>
                            )}
                          </div>
                          {isFrozen ? (
                            <div className="text-xs text-gray-600">
                              <p>Type: {role.constraintType}</p>
                              <p>{role.description}</p>
                            </div>
                          ) : (
                            <div className="space-y-2">
                              <select
                                value={role.constraintType}
                                onChange={(e) =>
                                  handleUpdateRole(cell.id, role.id, {
                                    constraintType: e.target.value as 'allow' | 'forbid' | 'condition',
                                  })
                                }
                                className="w-full px-2 py-1 border rounded text-xs"
                              >
                                <option value="allow">Allow</option>
                                <option value="forbid">Forbid</option>
                                <option value="condition">Condition</option>
                              </select>
                              <textarea
                                value={role.description}
                                onChange={(e) => handleUpdateRole(cell.id, role.id, { description: e.target.value })}
                                placeholder="Constraint description"
                                className="w-full px-2 py-1 border rounded text-xs min-h-16"
                              />
                            </div>
                          )}
                        </div>
                      ))}
                    </div>
                  )}
                </div>
              </div>
            </div>
          ))}
        </div>
      )}

      {/* Create Cell Dialog */}
      {showCreateDialog && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
          <div className="bg-white rounded-lg p-6 max-w-2xl w-full mx-4 max-h-[90vh] overflow-y-auto">
            <h3 className="text-lg font-mono mb-4">Create New Cell</h3>
            <p className="text-sm text-gray-600 mb-4">Define a minimum responsibility unit with explicit boundaries</p>

            <div className="space-y-4">
              <div>
                <label className="block text-xs font-mono text-gray-600 mb-1">
                  Cell Name (Required)
                </label>
                <input
                  type="text"
                  value={newCell.name || ''}
                  onChange={(e) => setNewCell({ ...newCell, name: e.target.value })}
                  placeholder="Cell name"
                  className="w-full px-3 py-2 border rounded font-mono"
                />
              </div>

              <div>
                <label className="block text-xs font-mono text-gray-600 mb-1">
                  Responsibility Description (What) (Required)
                </label>
                <textarea
                  value={newCell.responsibilityWhat || ''}
                  onChange={(e) => setNewCell({ ...newCell, responsibilityWhat: e.target.value })}
                  placeholder="What is this cell responsible for?"
                  className="w-full px-3 py-2 border rounded font-mono text-sm min-h-24"
                />
              </div>

              <div>
                <label className="block text-xs font-mono text-gray-600 mb-1">
                  Responsibility Boundary (What NOT) (Required)
                </label>
                <textarea
                  value={newCell.responsibilityWhatNot || ''}
                  onChange={(e) => setNewCell({ ...newCell, responsibilityWhatNot: e.target.value })}
                  placeholder="What are the explicit boundaries of this responsibility?"
                  className="w-full px-3 py-2 border rounded font-mono text-sm min-h-24"
                />
              </div>
            </div>

            <div className="flex gap-2 mt-6">
              <button
                onClick={() => setShowCreateDialog(false)}
                className="px-4 py-2 border rounded hover:bg-gray-50"
              >
                Cancel
              </button>
              <button
                onClick={handleCreateCell}
                disabled={!newCell.name || !newCell.responsibilityWhat || !newCell.responsibilityWhatNot}
                className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 disabled:bg-gray-300 disabled:cursor-not-allowed"
              >
                Create Cell
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  )
}

