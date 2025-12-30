// L5: Freeze Record View (Read-Only)
// Authority: RT_FE_REQ_FROZEN.md Section 3.6

import { useTranslation } from 'react-i18next'
import type { FreezeRecordViewModel } from '../../types/viewModels'

interface FreezeRecordViewProps {
  freezeRecord: FreezeRecordViewModel
}

export function FreezeRecordView({ freezeRecord }: FreezeRecordViewProps) {
  const { t } = useTranslation()
  
  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-semibold">{t('freezeRecord.title')}</h2>
          <p className="text-sm text-gray-600 mt-1">
            {t('freezeRecord.description')}
          </p>
        </div>
        <span className="px-2 py-1 text-xs font-mono border rounded frozen-indicator">
          {t('freezeRecord.immutable')}
        </span>
      </div>

      {/* Anti-Misinterpretation Guardrail - RT_FE_REQ_FROZEN.md Section 6.2 */}
      <div className="bg-blue-50 border border-blue-200 rounded-lg p-4">
        <p className="text-sm text-gray-700">
          {t('freezeRecord.immutableRecord')}
        </p>
      </div>

      {/* Freeze Record Information (Read-Only) */}
      <div className="bg-white border rounded-lg p-6 space-y-4">
        {/* Time Stamp - MUST be labeled as "Frozen at" - RT_FE_REQ_FROZEN.md Section 3.6 */}
        <div>
          <label className="block text-xs font-mono text-gray-600 mb-1">{t('freezeRecord.frozenAt')}</label>
          <p className="text-sm font-mono text-gray-800">
            {new Date(freezeRecord.frozenAt).toLocaleString()}
          </p>
          <p className="text-xs text-gray-500 mt-1">
            {t('freezeRecord.frozenAtDescription')}
          </p>
        </div>

        <div>
          <label className="block text-xs font-mono text-gray-600 mb-1">{t('freezeRecord.frozenBy')}</label>
          <p className="text-sm font-mono text-gray-800">{freezeRecord.frozenBy}</p>
        </div>

        <div>
          <label className="block text-xs font-mono text-gray-600 mb-1">{t('freezeRecord.frozenCompanyIdentifier')}</label>
          <p className="text-sm font-mono text-gray-800">{freezeRecord.frozenCompanyIdentifier}</p>
          <button
            onClick={() => {
              navigator.clipboard.writeText(freezeRecord.frozenCompanyIdentifier)
            }}
            className="mt-1 text-xs text-blue-600 hover:text-blue-800"
          >
            {t('freezeRecord.copyCompanyIdentifier')}
          </button>
        </div>

        <div>
          <label className="block text-xs font-mono text-gray-600 mb-1">{t('freezeRecord.freezeRecordIdentifier')}</label>
          <p className="text-sm font-mono text-gray-800">{freezeRecord.freezeRecordIdentifier}</p>
        </div>

        {freezeRecord.draftIdentifier && (
          <div>
            <label className="block text-xs font-mono text-gray-600 mb-1">{t('freezeRecord.previousDraftId')}</label>
            <p className="text-sm font-mono text-gray-800">{freezeRecord.draftIdentifier}</p>
          </div>
        )}

        {freezeRecord.freezeSummary && (
          <div>
            <label className="block text-xs font-mono text-gray-600 mb-1">{t('freezeRecord.freezeSummary')}</label>
            <p className="text-sm text-gray-800 whitespace-pre-wrap">{freezeRecord.freezeSummary}</p>
          </div>
        )}

        {/* Explicit Statement - RT_FE_REQ_FROZEN.md Section 3.6 */}
        <div className="bg-gray-50 border border-gray-200 rounded p-3 mt-4">
          <p className="text-xs text-gray-700">
            {t('freezeRecord.immutableStatement')}
          </p>
        </div>
      </div>
    </div>
  )
}
