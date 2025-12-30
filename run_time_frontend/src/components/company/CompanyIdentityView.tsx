// L1: Company Identity View (Read-Only)
// Authority: RT_FE_REQ_FROZEN.md Section 3.1

import { useTranslation } from 'react-i18next'
import type { CompanyViewModel } from '../../types/viewModels'

interface CompanyIdentityViewProps {
  company: CompanyViewModel
}

export function CompanyIdentityView({ company }: CompanyIdentityViewProps) {
  const { t } = useTranslation()
  
  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-semibold">{t('company.companyIdentity')}</h2>
          <p className="text-sm text-gray-600 mt-1">
            {t('company.frozenStructureIdentity')}
          </p>
        </div>
        <span className="px-2 py-1 text-xs font-mono border rounded frozen-indicator">
          {t('company.frozenCompanyReadOnly')}
        </span>
      </div>

      {/* Explicit Statement - RT_FE_REQ_FROZEN.md Section 3.1 */}
      <div className="bg-blue-50 border border-blue-200 rounded-lg p-4">
        <p className="text-sm text-gray-700">
          {t('company.frozenStructuralDeclaration')}
        </p>
      </div>

      {/* Company Information (Read-Only) */}
      <div className="bg-white border rounded-lg p-6 space-y-4">
        <div>
          <label className="block text-xs font-mono text-gray-600 mb-1">{t('company.companyIdentifier')}</label>
          <p className="text-sm font-mono text-gray-800">{company.companyIdentifier}</p>
        </div>

        <div>
          <label className="block text-xs font-mono text-gray-600 mb-1">{t('company.companyName')}</label>
          <p className="text-sm text-gray-800">{company.companyName}</p>
        </div>

        <div>
          <label className="block text-xs font-mono text-gray-600 mb-1">{t('company.companyDescription')}</label>
          <p className="text-sm text-gray-800 whitespace-pre-wrap">{company.companyDescription}</p>
        </div>

        <div>
          <label className="block text-xs font-mono text-gray-600 mb-1">{t('company.frozenAt')}</label>
          <p className="text-sm font-mono text-gray-800">
            {new Date(company.frozenAt).toLocaleString()}
          </p>
        </div>

        <div>
          <label className="block text-xs font-mono text-gray-600 mb-1">{t('company.frozenBy')}</label>
          <p className="text-sm font-mono text-gray-800">{company.frozenBy}</p>
        </div>
      </div>
    </div>
  )
}
