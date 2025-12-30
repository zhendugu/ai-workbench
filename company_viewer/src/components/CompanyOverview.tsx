import { useTranslation } from 'react-i18next'
import type { Company } from '../services/dataLoader'

interface CompanyOverviewProps {
  company: Company
}

export function CompanyOverview({ company }: CompanyOverviewProps) {
  const { t } = useTranslation()

  const formatDate = (dateString: string) => {
    try {
      const date = new Date(dateString)
      return date.toLocaleDateString(undefined, {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
      })
    } catch {
      return dateString
    }
  }

  return (
    <div className="space-y-6">
      <div className="bg-white rounded-lg border border-gray-200 shadow-sm p-8">
        <div className="space-y-6">
          <div>
            <h2 className="text-xl font-semibold text-gray-900 mb-2">{t('company.name')}</h2>
            <p className="text-2xl text-gray-800">{company.name}</p>
          </div>

          {company.description && (
            <div>
              <h2 className="text-xl font-semibold text-gray-900 mb-2">{t('company.description')}</h2>
              <p className="text-gray-700 whitespace-pre-wrap leading-relaxed">{company.description}</p>
            </div>
          )}

          <div className="grid grid-cols-1 md:grid-cols-2 gap-6 pt-6 border-t border-gray-200">
            <div>
              <h3 className="text-sm font-medium text-gray-500 mb-1">{t('company.created')}</h3>
              <p className="text-gray-900">{formatDate(company.createdAt)}</p>
            </div>

            {company.createdBy && (
              <div>
                <h3 className="text-sm font-medium text-gray-500 mb-1">{t('company.createdBy')}</h3>
                <p className="text-gray-900">{company.createdBy}</p>
              </div>
            )}
          </div>

          <div className="bg-blue-50 border border-blue-200 rounded-lg p-4 mt-6">
            <p className="text-sm text-blue-900">{t('company.cannotChange')}</p>
          </div>
        </div>
      </div>
    </div>
  )
}

