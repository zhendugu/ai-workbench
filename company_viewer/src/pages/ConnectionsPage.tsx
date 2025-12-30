import { useState } from 'react'
import { useTranslation } from 'react-i18next'
import { mockConnections, mockCells, mockTaskForces } from '../mock/data'
import { Plus, Network, List } from 'lucide-react'
import type { Connection } from '../mock/data'

export function ConnectionsPage() {
  const { t, i18n } = useTranslation()
  const isZh = i18n.language === 'zh'
  const [viewMode, setViewMode] = useState<'list' | 'graph'>('list')

  const getConnectionTypeLabel = (type: Connection['type']) => {
    switch (type) {
      case 'reporting':
        return t('connections.typeReporting')
      case 'collaboration':
        return t('connections.typeCollaboration')
      case 'support':
        return t('connections.typeSupport')
      case 'dependency':
        return t('connections.typeDependency')
      case 'mentoring':
        return t('connections.typeMentoring')
    }
  }

  const getEntityName = (id: string, type: Connection['sourceEntityType']) => {
    if (type === 'cell') {
      const cell = mockCells.find((c) => c.id === id)
      return cell ? (isZh ? cell.name : cell.nameEn) : id
    } else if (type === 'taskforce') {
      const tf = mockTaskForces.find((t) => t.id === id)
      return tf ? (isZh ? tf.name : tf.nameEn) : id
    }
    return id
  }

  return (
    <div>
      {/* Page Header */}
      <div className="flex items-center justify-between mb-8">
        <div>
          <h1 className="text-3xl font-bold text-gray-900 mb-2">
            {t('connections.title')}
          </h1>
        </div>
        <div className="flex gap-3">
          <div className="flex border border-gray-300 rounded-lg overflow-hidden">
            <button
              onClick={() => setViewMode('list')}
              className={`px-4 py-2 text-sm flex items-center gap-2 transition-colors ${
                viewMode === 'list'
                  ? 'bg-blue-600 text-white'
                  : 'bg-white text-gray-700 hover:bg-gray-50'
              }`}
            >
              <List className="w-4 h-4" />
              {t('connections.viewList')}
            </button>
            <button
              onClick={() => setViewMode('graph')}
              className={`px-4 py-2 text-sm flex items-center gap-2 transition-colors border-l border-gray-300 ${
                viewMode === 'graph'
                  ? 'bg-blue-600 text-white'
                  : 'bg-white text-gray-700 hover:bg-gray-50'
              }`}
            >
              <Network className="w-4 h-4" />
              {t('connections.viewGraph')}
            </button>
          </div>
          <button className="flex items-center gap-2 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors">
            <Plus className="w-4 h-4" />
            {t('connections.create')}
          </button>
        </div>
      </div>

      {/* Graph View */}
      {viewMode === 'graph' && (
        <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6 mb-6">
          <div className="border-2 border-dashed border-gray-300 rounded-lg p-12 text-center min-h-[400px] flex items-center justify-center">
            <div>
              <Network className="w-16 h-16 text-gray-400 mx-auto mb-4" />
              <p className="text-gray-500 mb-2">{t('connections.viewGraph')}</p>
              <p className="text-sm text-gray-400">
                {isZh
                  ? '可交互式节点图 - 可视化展示实体间的关系'
                  : 'Interactive Node Graph - Visualize relationships between entities'}
              </p>
            </div>
          </div>
        </div>
      )}

      {/* List View */}
      {viewMode === 'list' && (
        <div className="bg-white rounded-lg shadow-sm border border-gray-200 overflow-hidden">
          <table className="w-full">
            <thead className="bg-gray-50">
              <tr>
                <th className="px-6 py-3 text-left text-sm font-medium text-gray-700">
                  {t('connections.source')}
                </th>
                <th className="px-6 py-3 text-left text-sm font-medium text-gray-700">
                  {t('connections.type')}
                </th>
                <th className="px-6 py-3 text-left text-sm font-medium text-gray-700">
                  {t('connections.target')}
                </th>
                {mockConnections.some((c) => c.description) && (
                  <th className="px-6 py-3 text-left text-sm font-medium text-gray-700">
                    {t('connections.description')}
                  </th>
                )}
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-200">
              {mockConnections.map((conn) => (
                <tr key={conn.id} className="hover:bg-gray-50">
                  <td className="px-6 py-4 text-sm text-gray-900">
                    {getEntityName(conn.sourceEntityId, conn.sourceEntityType)}
                  </td>
                  <td className="px-6 py-4 text-sm">
                    <span className="inline-block px-2 py-1 text-xs font-medium bg-blue-100 text-blue-800 rounded">
                      {getConnectionTypeLabel(conn.type)}
                    </span>
                  </td>
                  <td className="px-6 py-4 text-sm text-gray-900">
                    {getEntityName(conn.targetEntityId, conn.targetEntityType)}
                  </td>
                  {conn.description && (
                    <td className="px-6 py-4 text-sm text-gray-600">
                      {isZh ? conn.description : conn.descriptionEn}
                    </td>
                  )}
                </tr>
              ))}
            </tbody>
          </table>
          {mockConnections.length === 0 && (
            <div className="text-center py-12">
              <p className="text-gray-500">{t('common.noData')}</p>
            </div>
          )}
        </div>
      )}
    </div>
  )
}

