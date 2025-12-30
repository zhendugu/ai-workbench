// L2: Structure View (Read-Only)
// Authority: RT_FE_REQ_FROZEN.md Section 3.2, 3.3

import { useState } from 'react'
import { useTranslation } from 'react-i18next'
import type { CellViewModel, RoleViewModel } from '../../types/viewModels'

interface StructureViewProps {
  cells: CellViewModel[]
  roles: RoleViewModel[] // Roles provided separately (indexed by identifier)
}

export function StructureView({ cells, roles }: StructureViewProps) {
  const { t } = useTranslation()
  const [selectedCellId, setSelectedCellId] = useState<string | null>(null)
  const selectedCell = cells.find((c) => c.cellIdentifier === selectedCellId)
  
  // Get roles for selected cell
  const selectedCellRoles = selectedCell
    ? roles.filter((r) => r.attachedToCellIdentifier === selectedCell.cellIdentifier)
    : []

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-semibold">{t('structure.title')}</h2>
          <p className="text-sm text-gray-600 mt-1">
            {t('structure.description')}
          </p>
        </div>
        <span className="px-2 py-1 text-xs font-mono border rounded read-only-indicator">
          {t('structure.readOnly')}
        </span>
      </div>

      {/* Anti-Misinterpretation Guardrail - RT_FE_REQ_FROZEN.md Section 6.2 */}
      <div className="bg-blue-50 border border-blue-200 rounded-lg p-4">
        <p className="text-sm text-gray-700">
          {t('structure.frozenDeclarations')}
        </p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Cell List (Read-Only) */}
        <div className="bg-white border rounded-lg p-6">
          <h3 className="text-base font-mono mb-4">{t('structure.cells')} ({cells.length})</h3>
          {cells.length === 0 ? (
            <p className="text-sm text-gray-400">{t('structure.noCells')}</p>
          ) : (
            <div className="space-y-2">
              {cells.map((cell) => (
                <div
                  key={cell.cellIdentifier}
                  onClick={() => setSelectedCellId(cell.cellIdentifier)}
                  className={`p-3 border rounded cursor-pointer ${
                    selectedCellId === cell.cellIdentifier ? 'border-gray-600 bg-gray-50' : 'border-gray-200'
                  }`}
                >
                  <div className="flex items-center justify-between mb-1">
                    <span className="text-sm font-mono font-medium">{cell.cellName}</span>
                    <span className="text-xs font-mono text-gray-500">{cell.cellIdentifier}</span>
                  </div>
                  <p className="text-xs text-gray-600 line-clamp-2">
                    {cell.responsibilityWhat}
                  </p>
                </div>
              ))}
            </div>
          )}
        </div>

        {/* Cell Detail (Read-Only) */}
        <div className="bg-white border rounded-lg p-6">
          {selectedCell ? (
            <>
              <h3 className="text-base font-mono mb-4">{t('structure.cellDetail')}</h3>
              
              {/* Explicit Statement - RT_FE_REQ_FROZEN.md Section 3.2 */}
              <div className="bg-gray-50 border border-gray-200 rounded p-3 mb-4">
                <p className="text-xs text-gray-700">
                  {t('structure.cellIsDeclaration')}
                </p>
              </div>

              <div className="space-y-4">
                <div>
                  <label className="block text-xs font-mono text-gray-600 mb-1">{t('structure.cellIdentifier')}</label>
                  <p className="text-sm font-mono text-gray-800">{selectedCell.cellIdentifier}</p>
                </div>

                <div>
                  <label className="block text-xs font-mono text-gray-600 mb-1">{t('structure.cellName')}</label>
                  <p className="text-sm text-gray-800">{selectedCell.cellName}</p>
                </div>

                <div>
                  <label className="block text-xs font-mono text-gray-600 mb-1">{t('structure.responsibilityWhat')}</label>
                  <p className="text-sm text-gray-800 whitespace-pre-wrap">
                    {selectedCell.responsibilityWhat}
                  </p>
                </div>

                <div>
                  <label className="block text-xs font-mono text-gray-600 mb-1">{t('structure.responsibilityWhatNot')}</label>
                  <p className="text-sm text-gray-800 whitespace-pre-wrap">
                    {selectedCell.responsibilityWhatNot}
                  </p>
                </div>

                {/* Roles (Read-Only) - RT_FE_REQ_FROZEN.md Section 3.3 */}
                <div>
                  <label className="block text-xs font-mono text-gray-600 mb-2">{t('structure.roleConstraints')}</label>
                  {selectedCellRoles.length === 0 ? (
                    <p className="text-sm text-gray-400">{t('structure.noRoleConstraints')}</p>
                  ) : (
                    <div className="space-y-2">
                      {selectedCellRoles.map((role) => (
                        <div key={role.roleIdentifier} className="bg-gray-50 border border-gray-200 rounded p-3">
                          <div className="flex items-center justify-between mb-1">
                            <span className="text-sm font-mono font-medium">{role.roleName}</span>
                            <span className="px-2 py-1 text-xs font-mono border rounded bg-gray-100">
                              {role.constraintType}
                            </span>
                          </div>
                          <p className="text-xs text-gray-700 mt-1">{role.constraintDescription}</p>
                        </div>
                      ))}
                    </div>
                  )}
                  
                  {/* Explicit Statement for Roles - RT_FE_REQ_FROZEN.md Section 3.3 */}
                  {selectedCellRoles.length > 0 && (
                    <div className="bg-gray-50 border border-gray-200 rounded p-2 mt-2">
                      <p className="text-xs text-gray-700">
                        {t('structure.roleIsConstraint')}
                      </p>
                    </div>
                  )}
                </div>
              </div>
            </>
          ) : (
            <div className="text-center text-gray-400">
              <p className="text-sm">{t('structure.selectCell')}</p>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}
