import { useState } from 'react'
import { useTranslation } from 'react-i18next'
import { mockTaskForces } from '../mock/data'
import { Plus, Search, Eye, Edit, Target } from 'lucide-react'
import type { TaskForce } from '../mock/data'

export function TaskForcesPage() {
  const { t, i18n } = useTranslation()
  const isZh = i18n.language === 'zh'
  const [searchTerm, setSearchTerm] = useState('')

  const getStatusLabel = (status: TaskForce['status']) => {
    switch (status) {
      case 'planning':
        return t('taskForces.statusPlanning')
      case 'active':
        return t('taskForces.statusActive')
      case 'completed':
        return t('taskForces.statusCompleted')
      case 'cancelled':
        return t('taskForces.statusCancelled')
    }
  }

  const getStatusColor = (status: TaskForce['status']) => {
    switch (status) {
      case 'planning':
        return 'bg-gray-100 text-gray-800'
      case 'active':
        return 'bg-green-100 text-green-800'
      case 'completed':
        return 'bg-blue-100 text-blue-800'
      case 'cancelled':
        return 'bg-red-100 text-red-800'
    }
  }

  const filteredTaskForces = mockTaskForces.filter((tf) => {
    const name = isZh ? tf.name : tf.nameEn
    return name.toLowerCase().includes(searchTerm.toLowerCase())
  })

  return (
    <div>
      {/* Page Header */}
      <div className="flex items-center justify-between mb-8">
        <div>
          <h1 className="text-3xl font-bold text-gray-900 mb-2">
            {t('taskForces.title')}
          </h1>
        </div>
        <button className="flex items-center gap-2 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors">
          <Plus className="w-4 h-4" />
          {t('taskForces.create')}
        </button>
      </div>

      {/* Search and Filter */}
      <div className="flex gap-4 mb-6">
        <div className="flex-1 relative">
          <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 w-5 h-5 text-gray-400" />
          <input
            type="text"
            placeholder={t('taskForces.search')}
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
          />
        </div>
        <select className="px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent">
          <option>{t('taskForces.filter')}</option>
        </select>
      </div>

      {/* Task Forces List */}
      <div className="space-y-4">
        {filteredTaskForces.map((tf) => (
          <div
            key={tf.id}
            className="bg-white rounded-lg shadow-sm border border-gray-200 p-6 hover:shadow-md transition-shadow"
          >
            <div className="flex items-start justify-between mb-4">
              <div className="flex items-start gap-4 flex-1">
                <div className="p-3 bg-purple-100 rounded-lg">
                  <Target className="w-6 h-6 text-purple-600" />
                </div>
                <div className="flex-1">
                  <div className="flex items-center gap-3 mb-2">
                    <h3 className="text-xl font-semibold text-gray-900">
                      {isZh ? tf.name : tf.nameEn}
                    </h3>
                    <span className={`px-2 py-1 text-xs font-medium rounded ${getStatusColor(tf.status)}`}>
                      {getStatusLabel(tf.status)}
                    </span>
                  </div>
                  <p className="text-gray-600 mb-3">
                    {isZh ? tf.objective : tf.objectiveEn}
                  </p>
                  <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-sm text-gray-600">
                    <div>
                      <span className="font-medium">{t('taskForces.leader')}: </span>
                      {isZh ? tf.leader : tf.leaderEn}
                    </div>
                    <div>
                      <span className="font-medium">{t('taskForces.startDate')}: </span>
                      {tf.startDate}
                    </div>
                    {tf.endDate && (
                      <div>
                        <span className="font-medium">{t('taskForces.endDate')}: </span>
                        {tf.endDate}
                      </div>
                    )}
                    <div>
                      <span className="font-medium">{t('taskForces.members')}: </span>
                      {tf.memberIds.length} {isZh ? '人' : 'people'}
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <div className="flex gap-2 pt-4 border-t border-gray-200">
              <button className="flex items-center gap-2 px-4 py-2 text-sm border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors">
                <Eye className="w-4 h-4" />
                {t('taskForces.view')}
              </button>
              <button className="flex items-center gap-2 px-4 py-2 text-sm border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors">
                <Edit className="w-4 h-4" />
                {t('taskForces.edit')}
              </button>
            </div>
          </div>
        ))}
      </div>

      {filteredTaskForces.length === 0 && (
        <div className="text-center py-12">
          <p className="text-gray-500">{t('common.noData')}</p>
        </div>
      )}
    </div>
  )
}

