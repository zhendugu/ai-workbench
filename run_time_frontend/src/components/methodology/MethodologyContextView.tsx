// L4: Methodology Context View (Read-Only)
// Authority: RT_FE_REQ_FROZEN.md Section 3.5

import { useTranslation } from 'react-i18next'
import type { MethodologyViewModel } from '../../types/viewModels'

interface MethodologyContextViewProps {
  methodology: MethodologyViewModel | null
}

export function MethodologyContextView({ methodology }: MethodologyContextViewProps) {
  const { t } = useTranslation()
  
  if (!methodology) {
    return (
      <div className="space-y-6">
        <div className="flex items-center justify-between">
          <div>
            <h2 className="text-2xl font-semibold">{t('methodology.title')}</h2>
            <p className="text-sm text-gray-600 mt-1">
              {t('methodology.description')}
            </p>
          </div>
          <span className="px-2 py-1 text-xs font-mono border rounded read-only-indicator">
            {t('methodology.readOnly')}
          </span>
        </div>
        <div className="bg-white border rounded-lg p-6">
          <p className="text-sm text-gray-400">{t('methodology.noMethodology')}</p>
        </div>
      </div>
    )
  }

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-semibold">{t('methodology.title')}</h2>
          <p className="text-sm text-gray-600 mt-1">
            {t('methodology.description')}
          </p>
        </div>
        <span className="px-2 py-1 text-xs font-mono border rounded read-only-indicator">
          {t('methodology.readOnly')}
        </span>
      </div>

      {/* Anti-Misinterpretation Guardrail - RT_FE_REQ_FROZEN.md Section 6.2 */}
      <div className="bg-blue-50 border border-blue-200 rounded-lg p-4">
        <p className="text-sm text-gray-700">
          {t('methodology.methodologyPerspective')}
        </p>
      </div>

      {/* Methodology Information (Read-Only) */}
      <div className="bg-white border rounded-lg p-6 space-y-4">
        <div>
          <label className="block text-xs font-mono text-gray-600 mb-1">{t('methodology.methodologyIdentifier')}</label>
          <p className="text-sm font-mono text-gray-800">{methodology.methodologyIdentifier}</p>
        </div>

        <div>
          <label className="block text-xs font-mono text-gray-600 mb-1">{t('methodology.methodologyName')}</label>
          <p className="text-sm font-mono text-gray-800">{methodology.methodologyName}</p>
        </div>

        {methodology.methodologyDescription && (
          <div>
            <label className="block text-xs font-mono text-gray-600 mb-1">{t('methodology.methodologyDescription')}</label>
            <p className="text-sm text-gray-800 whitespace-pre-wrap">{methodology.methodologyDescription}</p>
          </div>
        )}

        {/* Explicit Statement - RT_FE_REQ_FROZEN.md Section 3.5 */}
        <div className="bg-gray-50 border border-gray-200 rounded p-3 mt-4">
          <p className="text-xs text-gray-700">
            {t('methodology.methodologyPerspectiveFrozen')}
          </p>
        </div>
      </div>
    </div>
  )
}
