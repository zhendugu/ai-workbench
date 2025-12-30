// L1: Company Context
// Authority: DT_FE_REQ_DRAFT.md Section 2.1

import { useState, useEffect } from 'react'
import type { Company } from '../../types'

interface CompanyContextProps {
  company: Company | null
  onCompanyChange: (company: Company | null) => void
  isFrozen: boolean
}

export function CompanyContext({ company, onCompanyChange, isFrozen }: CompanyContextProps) {
  const [name, setName] = useState('')
  const [description, setDescription] = useState('')

  useEffect(() => {
    if (company) {
      setName(company.name)
      setDescription(company.description)
    }
  }, [company])

  const handleSave = () => {
    if (!name.trim() || !description.trim()) return

    const newCompany: Company = {
      id: company?.id || `COMP-${Date.now()}`,
      name: name.trim(),
      description: description.trim(),
      status: company?.status || 'draft',
      createdAt: company?.createdAt || new Date().toISOString(),
      createdBy: company?.createdBy || 'user-unknown',
      methodology: company?.methodology,
    }

    onCompanyChange(newCompany)
  }

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-semibold">Company Metadata</h2>
          <p className="text-sm text-gray-600 mt-1">
            Define the identity and purpose of this virtual company structure
          </p>
        </div>
        <span className={`px-3 py-1 text-xs font-mono border rounded ${
          isFrozen ? 'bg-gray-200 text-gray-600' : 'bg-blue-100 text-blue-700'
        }`}>
          {isFrozen ? 'FROZEN' : 'DRAFT'}
        </span>
      </div>

      <div className="bg-white border rounded-lg p-6">
        <div className="mb-4">
          <h3 className="text-lg font-mono mb-2">DESIGN-TIME COMPANY</h3>
          <p className="text-sm text-gray-600">This is a structural declaration, not an executable entity</p>
        </div>

        {/* Company ID - DR-02: Technical identifier only */}
        <div className="mb-4">
          <label className="block text-xs font-mono text-gray-600 mb-1">
            Company ID (Auto-generated)
          </label>
          <input
            type="text"
            value={company?.id || 'Not created yet'}
            disabled
            className="w-full px-3 py-2 border rounded bg-gray-100 font-mono text-sm"
          />
          <p className="text-xs text-gray-500 mt-1">Technical identifier for persistence and reference</p>
        </div>

        {/* Company Name */}
        <div className="mb-4">
          <label className="block text-xs font-mono text-gray-600 mb-1">
            Company Name (Required)
          </label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            disabled={isFrozen}
            placeholder="Enter a human-readable name..."
            className="w-full px-3 py-2 border rounded font-mono"
          />
        </div>

        {/* Description */}
        <div className="mb-4">
          <label className="block text-xs font-mono text-gray-600 mb-1">
            Human-Readable Description (Required)
          </label>
          <textarea
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            disabled={isFrozen}
            placeholder="Describe what this company structure is designed to accomplish..."
            className="w-full px-3 py-2 border rounded font-mono text-sm min-h-32"
          />
        </div>

        {/* Important Notes - DT_FE_REQ_DRAFT.md Section 2.1 */}
        <div className="mt-6 pt-4 border-t">
          <div className="text-sm text-gray-600">
            <p className="font-medium mb-2">Important Notes:</p>
            <ul className="list-disc list-inside space-y-1 text-xs">
              <li>Company does NOT execute or run</li>
              <li>Company does NOT have operational states</li>
              <li>Company is a semantic anchor for structure grouping</li>
              <li>Freezing converts this to a read-only reference for Run-Time use</li>
            </ul>
          </div>
        </div>

        {/* Save Button */}
        {!isFrozen && (
          <div className="mt-6">
            <button
              onClick={handleSave}
              disabled={!name.trim() || !description.trim()}
              className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 disabled:bg-gray-300 disabled:cursor-not-allowed"
            >
              Save Company
            </button>
          </div>
        )}

        {/* Frozen State Display */}
        {isFrozen && company && (
          <div className="mt-6 pt-4 border-t">
            <div className="text-sm text-gray-600">
              <p className="font-medium mb-2">Frozen Information:</p>
              <p className="text-xs">Frozen at: {company.createdAt}</p>
              <p className="text-xs">Frozen by: {company.createdBy}</p>
            </div>
          </div>
        )}
      </div>
    </div>
  )
}

