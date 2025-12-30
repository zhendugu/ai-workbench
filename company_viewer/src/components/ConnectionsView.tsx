import { useTranslation } from 'react-i18next'
import type { Connection, Team } from '../services/dataLoader'

interface ConnectionsViewProps {
  connections: Connection[]
  teams: Team[]
}

export function ConnectionsView({ connections, teams }: ConnectionsViewProps) {
  const { t } = useTranslation()

  const getTeamName = (teamId: string) => {
    const team = teams.find((t) => t.id === teamId)
    return team?.name || teamId
  }

  const getConnectionTypeLabel = (type: Connection['type']) => {
    switch (type) {
      case 'depends-on':
        return t('connections.dependsOn')
      case 'references':
        return t('connections.references')
      case 'provides-to':
        return t('connections.providesTo')
      default:
        return type
    }
  }

  if (connections.length === 0) {
    return (
      <div className="space-y-6">
        <div>
          <h2 className="text-2xl font-semibold text-gray-900 mb-2">{t('connections.title')}</h2>
          <p className="text-gray-600">{t('connections.subtitle')}</p>
        </div>
        <div className="bg-white rounded-lg border border-gray-200 shadow-sm p-8 text-center">
          <p className="text-gray-500 text-lg">{t('connections.noConnections')}</p>
        </div>
      </div>
    )
  }

  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-2xl font-semibold text-gray-900 mb-2">{t('connections.title')}</h2>
        <p className="text-gray-600">{t('connections.subtitle')}</p>
      </div>

      <div className="bg-white rounded-lg border border-gray-200 shadow-sm p-6">
        <div className="space-y-4">
          {connections.map((connection) => (
            <div key={connection.id} className="border-b border-gray-200 last:border-b-0 pb-4 last:pb-0">
              <div className="flex items-center gap-3 flex-wrap">
                <span className="font-medium text-gray-900">{getTeamName(connection.fromTeam)}</span>
                <span className="text-gray-500">•</span>
                <span className="text-sm text-gray-600">{getConnectionTypeLabel(connection.type)}</span>
                <span className="text-gray-500">•</span>
                <span className="font-medium text-gray-900">{getTeamName(connection.toTeam)}</span>
              </div>
              {connection.description && (
                <p className="text-sm text-gray-600 mt-2 ml-0">{connection.description}</p>
              )}
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}

