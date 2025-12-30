// L4: Methodology View
// Authority: DT_FE_REQ_DRAFT.md Section 2.5

import { useState } from 'react'
import type { Methodology } from '../../types'

interface MethodologySelectorProps {
  methodology: Methodology | null
  onMethodologyChange: (methodology: Methodology | null) => void
  isFrozen: boolean
}

const builtInMethodologies = [
  {
    id: 'none',
    name: 'None',
    description: 'No specific methodology perspective applied',
  },
  {
    id: 'waterfall',
    name: 'Waterfall-Inspired View',
    description: 'Sequential phase organization for understanding',
  },
  {
    id: 'agile',
    name: 'Agile-Inspired View',
    description: 'Iterative sprint-based conceptual grouping',
  },
  {
    id: 'hybrid',
    name: 'Hybrid Approach',
    description: 'Combined perspectives for complex structures',
  },
]

export function MethodologySelector({
  methodology,
  onMethodologyChange,
  isFrozen,
}: MethodologySelectorProps) {
  const [selectedMethodologyId, setSelectedMethodologyId] = useState<string>('none')
  const [customMethodology, setCustomMethodology] = useState('')

  const handleMethodologyChange = (id: string) => {
    setSelectedMethodologyId(id)
    if (id === 'none') {
      onMethodologyChange(null)
    } else {
      const builtIn = builtInMethodologies.find((m) => m.id === id)
      if (builtIn) {
        onMethodologyChange({
          name: builtIn.name,
          description: builtIn.description,
          status: 'active',
        })
      }
    }
  }

  return (
    <div className="bg-white border rounded-lg p-4">
      <div className="flex items-center justify-between mb-4">
        <div>
          <h3 className="text-lg font-semibold">Methodology Perspective</h3>
          <p className="text-sm text-gray-600">Choose a cognitive lens for organizing and viewing structure</p>
        </div>
        <span className="px-2 py-1 text-xs font-mono border rounded bg-gray-100">PERSPECTIVE ONLY</span>
      </div>

      {/* Methodology as Perspective - DT_FE_REQ_DRAFT.md Section 2.5 */}
      <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-3 mb-4">
        <div className="text-sm text-gray-700">
          <p className="font-medium mb-2">Methodology as Perspective:</p>
          <ul className="list-disc list-inside space-y-1 text-xs">
            <li>Methodology is a VIEW, not a system mode</li>
            <li>Changing perspective does NOT change data or structure</li>
            <li>No methodology is recommended or evaluated</li>
            <li>Methodology does NOT drive operations or constraints</li>
            <li>This affects how YOU think, not how the system behaves</li>
          </ul>
        </div>
      </div>

      {/* Built-In Methodologies */}
      <div className="mb-4">
        <label className="block text-xs font-mono text-gray-600 mb-2">Built-In Methodologies</label>
        <div className="space-y-2">
          {builtInMethodologies.map((method) => (
            <label key={method.id} className="flex items-start space-x-3 cursor-pointer">
              <input
                type="radio"
                name="methodology"
                value={method.id}
                checked={selectedMethodologyId === method.id}
                onChange={(e) => handleMethodologyChange(e.target.value)}
                disabled={isFrozen}
                className="mt-1"
              />
              <div className="flex-1">
                <div className="flex items-center gap-2">
                  <span className="font-mono text-sm">{method.name}</span>
                  <span className="px-2 py-1 text-xs border rounded bg-gray-100">available</span>
                </div>
                <p className="text-xs text-gray-600 mt-1">{method.description}</p>
              </div>
            </label>
          ))}
        </div>
      </div>

      {/* Custom Methodology - DT_FE_REQ_DRAFT.md Section 2.5 */}
      <div>
        <label className="block text-xs font-mono text-gray-600 mb-2">
          Custom Methodology (Optional)
        </label>
        <textarea
          value={customMethodology}
          onChange={(e) => setCustomMethodology(e.target.value)}
          disabled={isFrozen}
          placeholder="Describe your custom organizational perspective..."
          className="w-full px-3 py-2 border rounded font-mono text-sm min-h-32"
        />
        <p className="text-xs text-gray-500 mt-1">
          Custom methodologies are saved as draft-only and not shared
        </p>
      </div>
    </div>
  )
}

