import { useTranslation } from 'react-i18next'
import type { Team } from '../services/dataLoader'

interface TeamsViewProps {
  teams: Team[]
}

export function TeamsView({ teams }: TeamsViewProps) {
  const { t } = useTranslation()

  if (teams.length === 0) {
    return (
      <div className="bg-white rounded-lg border border-gray-200 shadow-sm p-8 text-center">
        <p className="text-gray-500 text-lg">{t('teams.noTeams')}</p>
      </div>
    )
  }

  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-2xl font-semibold text-gray-900 mb-2">{t('teams.title')}</h2>
        <p className="text-gray-600">{t('teams.subtitle')}</p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {teams.map((team) => (
          <div key={team.id} className="bg-white rounded-lg border border-gray-200 shadow-sm p-6">
            <h3 className="text-xl font-semibold text-gray-900 mb-4">{team.name}</h3>

            <div className="space-y-4">
              {team.purpose && (
                <div>
                  <h4 className="text-sm font-medium text-gray-700 mb-2">{t('teams.teamPurpose')}</h4>
                  <p className="text-gray-800 whitespace-pre-wrap leading-relaxed">{team.purpose}</p>
                </div>
              )}

              {team.boundaries && (
                <div>
                  <h4 className="text-sm font-medium text-gray-700 mb-2">{t('teams.teamBoundaries')}</h4>
                  <p className="text-gray-800 whitespace-pre-wrap leading-relaxed">{team.boundaries}</p>
                </div>
              )}

              {team.responsibilities.length > 0 && (
                <div>
                  <h4 className="text-sm font-medium text-gray-700 mb-3">{t('teams.responsibilities')}</h4>
                  <div className="space-y-3">
                    {team.responsibilities.map((resp) => (
                      <div key={resp.id} className="bg-gray-50 border border-gray-200 rounded-lg p-4">
                        <div className="flex items-center gap-2 mb-2">
                          <span className={`px-2 py-1 text-xs font-medium rounded ${
                            resp.type === 'allowed' 
                              ? 'bg-green-100 text-green-800'
                              : resp.type === 'forbidden'
                              ? 'bg-red-100 text-red-800'
                              : 'bg-yellow-100 text-yellow-800'
                          }`}>
                            {resp.type === 'allowed' && t('teams.responsibilityTypeAllowed')}
                            {resp.type === 'forbidden' && t('teams.responsibilityTypeForbidden')}
                            {resp.type === 'conditional' && t('teams.responsibilityTypeConditional')}
                          </span>
                          <span className="text-sm font-medium text-gray-900">{resp.name}</span>
                        </div>
                        {resp.description && (
                          <p className="text-sm text-gray-700 mt-2">{resp.description}</p>
                        )}
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}

