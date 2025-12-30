import { useTranslation } from 'react-i18next'
import type { Approach } from '../services/dataLoader'

interface ApproachViewProps {
  approach: Approach | null
}

export function ApproachView({ approach }: ApproachViewProps) {
  const { t } = useTranslation()

  if (!approach) {
    return (
      <div className="space-y-6">
        <div>
          <h2 className="text-2xl font-semibold text-gray-900 mb-2">{t('approach.title')}</h2>
          <p className="text-gray-600">{t('approach.subtitle')}</p>
        </div>
        <div className="bg-white rounded-lg border border-gray-200 shadow-sm p-8 text-center">
          <p className="text-gray-500 text-lg">{t('approach.noApproach')}</p>
        </div>
      </div>
    )
  }

  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-2xl font-semibold text-gray-900 mb-2">{t('approach.title')}</h2>
        <p className="text-gray-600">{t('approach.subtitle')}</p>
      </div>

      <div className="bg-white rounded-lg border border-gray-200 shadow-sm p-8">
        <div className="space-y-6">
          <div>
            <h3 className="text-lg font-medium text-gray-700 mb-2">{t('approach.name')}</h3>
            <p className="text-xl text-gray-900">{approach.name}</p>
          </div>

          {approach.description && (
            <div>
              <h3 className="text-lg font-medium text-gray-700 mb-2">{t('approach.description')}</h3>
              <p className="text-gray-800 whitespace-pre-wrap leading-relaxed">{approach.description}</p>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}

