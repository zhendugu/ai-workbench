// L5: Template Library
// Authority: DT_FE_REQ_DRAFT.md Section 2.6 + DR-01

import type { Template } from '../../types'

interface TemplateLibraryProps {
  onTemplateUse: (template: Template) => void
  isFrozen: boolean
}

// DR-01: Template is structural copy source only, no recommendations
const templates: Template[] = [
  {
    id: 'research-company',
    name: 'Research Company',
    description: 'Complete structure for investigation and analysis tasks',
    cellCount: 3,
    relationCount: 2,
    presetMethodology: 'None',
    // For MVP: Empty structure, actual copy would come from backend
  },
  {
    id: 'consulting-company',
    name: 'Consulting Company',
    description: 'Complete structure for advisory and recommendation services',
    cellCount: 4,
    relationCount: 3,
    presetMethodology: 'None',
  },
]

export function TemplateLibrary({ onTemplateUse, isFrozen }: TemplateLibraryProps) {
  const handleUseTemplate = (template: Template) => {
    // DR-01: Create NEW Draft, fully independent
    // In real implementation, this would call backend API to create new Company from template
    // For MVP, we just trigger the callback
    onTemplateUse(template)
  }

  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-2xl font-semibold">Template Library</h2>
        <p className="text-sm text-gray-600 mt-1">
          Reusable structural patterns for faster design iteration
        </p>
      </div>

      {/* Template Usage Rules - DT_FE_REQ_DRAFT.md Section 2.6 + DR-01 */}
      <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-4">
        <div className="text-sm text-gray-700">
          <p className="font-medium mb-2">Template Usage Rules:</p>
          <ul className="list-disc list-inside space-y-1 text-xs">
            <li>Templates are structural starting points, not auto-generated solutions</li>
            <li>Using a template requires explicit human confirmation</li>
            <li>Templates can be edited after application (if not frozen)</li>
            <li>Templates do NOT include execution logic or judgment points</li>
            <li>Templates do NOT carry best practices, recommendations, or quality implications</li>
          </ul>
        </div>
      </div>

      {/* Template List - DR-01: No scoring, recommendation, or matching */}
      <div className="space-y-4">
        {templates.map((template) => (
          <div key={template.id} className="bg-white border rounded-lg p-6">
            <div className="flex items-start justify-between">
              <div className="flex-1">
                <div className="flex items-center gap-2 mb-2">
                  <h3 className="text-base font-mono">{template.name}</h3>
                  <span className="px-2 py-1 text-xs font-mono border rounded bg-gray-100">built-in</span>
                </div>
                <p className="text-sm text-gray-600 mb-2">{template.description}</p>
                <div className="text-xs text-gray-500 space-y-1">
                  <p>Cells: {template.cellCount}</p>
                  <p>Relations: {template.relationCount}</p>
                  {template.presetMethodology && <p>Methodology: {template.presetMethodology}</p>}
                </div>
              </div>
              <button
                onClick={() => handleUseTemplate(template)}
                disabled={isFrozen}
                className="px-4 py-2 border rounded hover:bg-gray-50 disabled:bg-gray-100 disabled:text-gray-400 disabled:cursor-not-allowed text-sm"
              >
                Use Template
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}

