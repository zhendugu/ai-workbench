import { useState } from 'react'
import { useTranslation } from 'react-i18next'
import { Link } from 'react-router-dom'
import { mockCells } from '../mock/data'
import { Plus, Search, Eye, Edit, Trash2 } from 'lucide-react'
import type { Cell } from '../mock/data'

export function CellsManagementPage() {
  const { t, i18n } = useTranslation()
  const isZh = i18n.language === 'zh'
  const [searchTerm, setSearchTerm] = useState('')

  const getCellTypeLabel = (type: Cell['type']) => {
    switch (type) {
      case 'department':
        return t('cells.typeDepartment')
      case 'project':
        return t('cells.typeProject')
      case 'other':
        return t('cells.typeOther')
    }
  }

  const getStatusLabel = (status: Cell['status']) => {
    switch (status) {
      case 'active':
        return t('cells.statusActive')
      case 'paused':
        return t('cells.statusPaused')
      case 'archived':
        return t('cells.statusArchived')
    }
  }

  const getStatusColor = (status: Cell['status']) => {
    switch (status) {
      case 'active':
        return 'bg-green-100 text-green-800'
      case 'paused':
        return 'bg-yellow-100 text-yellow-800'
      case 'archived':
        return 'bg-gray-100 text-gray-800'
    }
  }

  const filteredCells = mockCells.filter((cell) => {
    const name = isZh ? cell.name : cell.nameEn
    return name.toLowerCase().includes(searchTerm.toLowerCase())
  })

  return (
    <div>
      {/* Page Header */}
      <div className="flex items-center justify-between mb-8">
        <div>
          <h1 className="text-3xl font-bold text-gray-900 mb-2">
            {t('cells.title')}
          </h1>
        </div>
        <button className="flex items-center gap-2 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors">
          <Plus className="w-4 h-4" />
          {t('cells.create')}
        </button>
      </div>

      {/* Search and Filter */}
      <div className="flex gap-4 mb-6">
        <div className="flex-1 relative">
          <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 w-5 h-5 text-gray-400" />
          <input
            type="text"
            placeholder={t('cells.search')}
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
          />
        </div>
        <select className="px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent">
          <option>{t('cells.filter')}</option>
        </select>
      </div>

      {/* Cells Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {filteredCells.map((cell) => (
          <div
            key={cell.id}
            className="bg-white rounded-lg shadow-sm border border-gray-200 p-6 hover:shadow-md transition-shadow"
          >
            <div className="flex items-start justify-between mb-4">
              <div className="flex-1">
                <h3 className="text-lg font-semibold text-gray-900 mb-2">
                  {isZh ? cell.name : cell.nameEn}
                </h3>
                <div className="flex gap-2 mb-2">
                  <span className="px-2 py-1 text-xs font-medium bg-blue-100 text-blue-800 rounded">
                    {getCellTypeLabel(cell.type)}
                  </span>
                  <span className={`px-2 py-1 text-xs font-medium rounded ${getStatusColor(cell.status)}`}>
                    {getStatusLabel(cell.status)}
                  </span>
                </div>
              </div>
            </div>

            <div className="space-y-2 mb-4 text-sm text-gray-600">
              {cell.leader && (
                <div>
                  <span className="font-medium">{t('cells.leader')}: </span>
                  {isZh ? cell.leader : cell.leaderEn}
                </div>
              )}
              <div>
                <span className="font-medium">{t('cells.memberCount')}: </span>
                {cell.memberCount}
              </div>
              {cell.description && (
                <div className="text-gray-500 text-xs line-clamp-2">
                  {isZh ? cell.description : cell.descriptionEn}
                </div>
              )}
            </div>

            <div className="flex gap-2 pt-4 border-t border-gray-200">
              <Link
                to={`/cells/${cell.id}`}
                className="flex-1 flex items-center justify-center gap-2 px-3 py-2 text-sm border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors"
              >
                <Eye className="w-4 h-4" />
                {t('cells.view')}
              </Link>
              <button className="flex items-center justify-center gap-2 px-3 py-2 text-sm border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors">
                <Edit className="w-4 h-4" />
                {t('cells.edit')}
              </button>
              <button className="flex items-center justify-center gap-2 px-3 py-2 text-sm border border-red-300 text-red-600 rounded-lg hover:bg-red-50 transition-colors">
                <Trash2 className="w-4 h-4" />
                {t('cells.delete')}
              </button>
            </div>
          </div>
        ))}
      </div>

      {filteredCells.length === 0 && (
        <div className="text-center py-12">
          <p className="text-gray-500">{t('common.noData')}</p>
        </div>
      )}
    </div>
  )
}

