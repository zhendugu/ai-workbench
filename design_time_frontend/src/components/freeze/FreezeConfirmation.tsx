// L6: Freeze Confirmation
// Authority: DT_FE_REQ_DRAFT.md Section 5.2

import { useState } from 'react'
import type { Company, Cell, Relation, Methodology } from '../../types'

interface FreezeConfirmationProps {
  company: Company
  cells: Cell[]
  relations: Relation[]
  methodology: Methodology | null
  onConfirm: () => void
  onCancel: () => void
}

export function FreezeConfirmation({
  company,
  cells,
  relations,
  methodology,
  onConfirm,
  onCancel,
}: FreezeConfirmationProps) {
  const [confirmationText, setConfirmationText] = useState('')
  const [confirmed, setConfirmed] = useState(false)

  // Calculate facts - DT_FE_REQ_DRAFT.md Section 5.2
  const isolatedCells = cells.filter((cell) => {
    const hasRelation = relations.some(
      (r) => r.sourceCellId === cell.id || r.targetCellId === cell.id
    )
    return !hasRelation
  })

  const cellsWithoutBoundary = cells.filter((cell) => !cell.responsibilityWhatNot.trim())

  const canConfirm = confirmed || confirmationText === company.name

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div className="bg-white rounded-lg p-6 max-w-2xl w-full mx-4 max-h-[90vh] overflow-y-auto">
        <h2 className="text-xl font-mono mb-2">Freeze Design Confirmation</h2>
        <p className="text-sm text-gray-600 mb-4">
          This action will convert your design-time draft into a frozen, read-only structure
        </p>

        {/* Consequences - DT_FE_REQ_DRAFT.md Section 5.2 */}
        <div className="bg-red-50 border border-red-200 rounded-lg p-4 mb-4">
          <div className="text-sm">
            <p className="font-semibold mb-2">Consequences of Freezing:</p>
            <ul className="list-disc list-inside space-y-1 text-gray-700 ml-2 text-xs">
              <li>All current structure becomes READ-ONLY</li>
              <li>No further edits, additions, or deletions allowed</li>
              <li>A stable ID will be generated for Run-Time reference</li>
              <li>This frozen structure becomes available to Run-Time and Audit interfaces</li>
              <li>You will need to create a new draft to make further changes</li>
            </ul>
          </div>
        </div>

        {/* Summary Information - DT_FE_REQ_DRAFT.md Section 5.2 */}
        <div className="bg-white border rounded-lg p-4 mb-4">
          <p className="text-sm font-medium mb-3">What will be frozen:</p>
          <div className="space-y-2 text-sm text-gray-600">
            <div className="flex justify-between py-2 border-b">
              <span>Company Metadata</span>
              <span className="font-mono">{company.name || '1 draft'}</span>
            </div>
            <div className="flex justify-between py-2 border-b">
              <span>Defined Cells</span>
              <span className="font-mono">{cells.length} cells</span>
            </div>
            <div className="flex justify-between py-2 border-b">
              <span>Topology Relationships</span>
              <span className="font-mono">{relations.length} relationships</span>
            </div>
            <div className="flex justify-between py-2 border-b">
              <span>Selected Methodology</span>
              <span className="font-mono">{methodology?.name || 'None'}</span>
            </div>
          </div>
        </div>

        {/* Warning Information (Fact Statements) - DT_FE_REQ_DRAFT.md Section 5.2 */}
        {(isolatedCells.length > 0 || cellsWithoutBoundary.length > 0) && (
          <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-4 mb-4">
            <p className="text-sm font-medium mb-2">Facts (not errors):</p>
            <ul className="list-disc list-inside space-y-1 text-xs text-gray-700 ml-2">
              {cellsWithoutBoundary.length > 0 && (
                <li>
                  {cellsWithoutBoundary.length} Cell(s) have no boundary declaration (What NOT)
                </li>
              )}
              {isolatedCells.length > 0 && (
                <li>
                  {isolatedCells.length} Cell(s) have no relations with other cells
                </li>
              )}
            </ul>
            <p className="text-xs text-gray-600 mt-2">
              These are fact statements, not error prompts. They do not prevent Freeze.
            </p>
          </div>
        )}

        {/* Confirmation Text - DT_FE_REQ_DRAFT.md Section 5.2 */}
        <div className="bg-gray-50 border border-dashed rounded-lg p-4 mb-4">
          <p className="text-sm text-gray-700 leading-relaxed">
            Please confirm that you understand this is an irreversible action. Once frozen, this design becomes a
            permanent reference structure for the Run-Time system. No AI assistance or automatic optimization will
            occur.
          </p>
        </div>

        {/* Secondary Confirmation - DT_FE_REQ_DRAFT.md Section 5.2 */}
        <div className="mb-4">
          <label className="block text-sm font-medium mb-2">
            Enter Company name to confirm: <span className="font-mono text-xs">{company.name}</span>
          </label>
          <input
            type="text"
            value={confirmationText}
            onChange={(e) => setConfirmationText(e.target.value)}
            placeholder="Type company name to confirm"
            className="w-full px-3 py-2 border rounded"
          />
          <div className="mt-2">
            <label className="flex items-center space-x-2">
              <input
                type="checkbox"
                checked={confirmed}
                onChange={(e) => setConfirmed(e.target.checked)}
              />
              <span className="text-sm">I confirm I have reviewed all content and take responsibility for this design</span>
            </label>
          </div>
        </div>

        {/* Action Buttons */}
        <div className="flex gap-2">
          <button
            onClick={onCancel}
            className="px-4 py-2 border rounded hover:bg-gray-50"
          >
            Cancel (Keep Editing)
          </button>
          <button
            onClick={onConfirm}
            disabled={!canConfirm}
            className="px-4 py-2 bg-orange-600 text-white rounded hover:bg-orange-700 disabled:bg-gray-300 disabled:cursor-not-allowed"
          >
            Confirm Freeze Design
          </button>
        </div>
      </div>
    </div>
  )
}

