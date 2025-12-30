// Design-Time Frontend Main Application
// Authority: DT_FE_REQ_DRAFT.md + DT_FE_DECISION_RECORD_001.md

import { useState } from 'react'
import { CompanyContext } from './components/company/CompanyContext'
import { CellManagement } from './components/cell/CellManagement'
import { TopologyCanvas } from './components/topology/TopologyCanvas'
import { MethodologySelector } from './components/methodology/MethodologySelector'
import { TemplateLibrary } from './components/template/TemplateLibrary'
import { FreezeConfirmation } from './components/freeze/FreezeConfirmation'
import type { Company, Cell, Relation, Methodology } from './types'

function App() {
  const [company, setCompany] = useState<Company | null>(null)
  const [cells, setCells] = useState<Cell[]>([])
  const [relations, setRelations] = useState<Relation[]>([])
  const [methodology, setMethodology] = useState<Methodology | null>(null)
  const [activeTab, setActiveTab] = useState<'company' | 'cells' | 'topology' | 'templates'>('company')
  const [showFreezeDialog, setShowFreezeDialog] = useState(false)

  const isFrozen = company?.status === 'frozen'

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Global Design-Time Indicator - DT_FE_REQ_DRAFT.md Section 1.1 */}
      <div className="sticky top-0 z-50 border-b bg-white shadow-sm">
        <div className="container mx-auto px-4 py-3">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-4">
              <div className="flex items-center gap-2">
                <span className="text-lg font-mono font-semibold">AI Virtual Company</span>
              </div>
              <span className="px-2 py-1 text-xs font-mono border rounded bg-gray-100">
                {company?.status === 'frozen' ? 'RUN-TIME - READ ONLY' : 'DESIGN-TIME'}
              </span>
            </div>
            <div className="flex items-center gap-2">
              {company && (
                <span className="text-sm text-gray-600 font-mono">
                  {company.status === 'frozen' ? 'FROZEN (READ-ONLY)' : 'DRAFT'}
                </span>
              )}
              {!isFrozen && company && (
                <button
                  onClick={() => setShowFreezeDialog(true)}
                  className="px-4 py-2 text-sm font-mono bg-blue-600 text-white rounded hover:bg-blue-700"
                >
                  Freeze Design
                </button>
              )}
            </div>
          </div>
        </div>
      </div>

      {/* Information Banner - DT_FE_REQ_DRAFT.md Section 1.1 */}
      {!isFrozen && (
        <div className="border-b bg-yellow-50">
          <div className="container mx-auto px-4 py-3">
            <div className="flex items-start gap-2 text-sm text-gray-700">
              <span className="font-medium">You are in DESIGN-TIME mode</span>
              <span className="text-xs">
                All content here is structural declaration. No execution, automation, or AI behavior occurs in this
                interface. This is for constructing company structures from zero, not running them.
              </span>
            </div>
          </div>
        </div>
      )}

      {/* Main Navigation - DT_FE_REQ_DRAFT.md Section 3.2 */}
      <div className="container mx-auto px-4 py-4">
        <div className="flex gap-2 border-b mb-6">
          <button
            onClick={() => setActiveTab('company')}
            className={`px-4 py-2 text-sm font-mono ${
              activeTab === 'company' ? 'border-b-2 border-blue-600 text-blue-600' : 'text-gray-600'
            }`}
          >
            Company
          </button>
          <button
            onClick={() => setActiveTab('cells')}
            className={`px-4 py-2 text-sm font-mono ${
              activeTab === 'cells' ? 'border-b-2 border-blue-600 text-blue-600' : 'text-gray-600'
            }`}
          >
            Cells
          </button>
          <button
            onClick={() => setActiveTab('topology')}
            className={`px-4 py-2 text-sm font-mono ${
              activeTab === 'topology' ? 'border-b-2 border-blue-600 text-blue-600' : 'text-gray-600'
            }`}
          >
            Topology
          </button>
          <button
            onClick={() => setActiveTab('templates')}
            className={`px-4 py-2 text-sm font-mono ${
              activeTab === 'templates' ? 'border-b-2 border-blue-600 text-blue-600' : 'text-gray-600'
            }`}
          >
            Templates
          </button>
        </div>

        {/* Methodology Selector - Global Control - DT_FE_REQ_DRAFT.md Section 3.2 */}
        <div className="mb-6">
          <MethodologySelector
            methodology={methodology}
            onMethodologyChange={setMethodology}
            isFrozen={isFrozen}
          />
        </div>

        {/* Main Content */}
        {activeTab === 'company' && (
          <CompanyContext
            company={company}
            onCompanyChange={setCompany}
            isFrozen={isFrozen}
          />
        )}

        {activeTab === 'cells' && (
          <CellManagement
            cells={cells}
            onCellsChange={setCells}
            isFrozen={isFrozen}
          />
        )}

        {activeTab === 'topology' && (
          <TopologyCanvas
            cells={cells}
            relations={relations}
            onRelationsChange={setRelations}
            isFrozen={isFrozen}
          />
        )}

        {activeTab === 'templates' && (
          <TemplateLibrary
            onTemplateUse={(template) => {
              // DR-01: Create NEW Draft, fully independent
              if (template.company) setCompany(template.company)
              if (template.cells) setCells(template.cells)
              if (template.relations) setRelations(template.relations)
              setActiveTab('company')
            }}
            isFrozen={isFrozen}
          />
        )}
      </div>

      {/* Freeze Confirmation Dialog - DT_FE_REQ_DRAFT.md Section 5.2 */}
      {showFreezeDialog && company && (
        <FreezeConfirmation
          company={company}
          cells={cells}
          relations={relations}
          methodology={methodology}
          onConfirm={() => {
            setCompany({ ...company, status: 'frozen' })
            setShowFreezeDialog(false)
          }}
          onCancel={() => setShowFreezeDialog(false)}
        />
      )}
    </div>
  )
}

export default App

