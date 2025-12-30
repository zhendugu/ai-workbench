import { useState } from 'react'
import { useTranslation } from 'react-i18next'
import { mockMethodologies, mockCells, mockRoles } from '../mock/data'
import { Plus, Search, Eye, Edit, BookOpen } from 'lucide-react'
import type { Methodology } from '../mock/data'

export function MethodologiesPage() {
  const { t, i18n } = useTranslation()
  const isZh = i18n.language === 'zh'
  const [searchTerm, setSearchTerm] = useState('')

  const getCategoryLabel = (category: Methodology['category']) => {
    switch (category) {
      case 'development':
        return t('methodologies.categoryDevelopment')
      case 'design':
        return t('methodologies.categoryDesign')
      case 'management':
        return t('methodologies.categoryManagement')
      case 'other':
        return t('methodologies.categoryOther')
    }
  }

  const filteredMethodologies = mockMethodologies.filter((method) => {
    const name = isZh ? method.name : method.nameEn
    return name.toLowerCase().includes(searchTerm.toLowerCase())
  })

  const getAppliedCellCount = (methodId: string) => {
    return mockMethodologies.find((m) => m.id === methodId)?.appliedToCellIds?.length || 0
  }

  const getAppliedRoleCount = (methodId: string) => {
    return mockMethodologies.find((m) => m.id === methodId)?.appliedToRoleIds?.length || 0
  }

  return (
    <div>
      {/* Page Header */}
      <div className="flex items-center justify-between mb-8">
        <div>
          <h1 className="text-3xl font-bold text-gray-900 mb-2">
            {t('methodologies.title')}
          </h1>
        </div>
        <button className="flex items-center gap-2 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors">
          <Plus className="w-4 h-4" />
          {t('methodologies.create')}
        </button>
      </div>

      {/* Search and Filter */}
      <div className="flex gap-4 mb-6">
        <div className="flex-1 relative">
          <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 w-5 h-5 text-gray-400" />
          <input
            type="text"
            placeholder={t('methodologies.search')}
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
          />
        </div>
        <select className="px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent">
          <option>{t('methodologies.filter')}</option>
        </select>
      </div>

      {/* Methodologies Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {filteredMethodologies.map((method) => (
          <div
            key={method.id}
            className="bg-white rounded-lg shadow-sm border border-gray-200 p-6 hover:shadow-md transition-shadow"
          >
            <div className="flex items-start gap-4 mb-4">
              <div className="p-3 bg-orange-100 rounded-lg">
                <BookOpen className="w-6 h-6 text-orange-600" />
              </div>
              <div className="flex-1">
                <div className="flex items-center gap-3 mb-2">
                  <h3 className="text-xl font-semibold text-gray-900">
                    {isZh ? method.name : method.nameEn}
                  </h3>
                  <span className="px-2 py-1 text-xs font-medium bg-gray-100 text-gray-800 rounded">
                    {getCategoryLabel(method.category)}
                  </span>
                </div>
                <p className="text-sm text-gray-600 line-clamp-2">
                  {isZh ? method.description : method.descriptionEn}
                </p>
              </div>
            </div>

            <div className="mb-4 text-sm text-gray-600">
              <div className="mb-1">
                <span className="font-medium">{t('methodologies.appliedToCells')}: </span>
                {getAppliedCellCount(method.id)} {isZh ? '个小组' : 'cells'}
              </div>
              <div>
                <span className="font-medium">{t('methodologies.appliedToRoles')}: </span>
                {getAppliedRoleCount(method.id)} {isZh ? '个职责' : 'roles'}
              </div>
            </div>

            <div className="flex gap-2 pt-4 border-t border-gray-200">
              <button className="flex-1 flex items-center justify-center gap-2 px-3 py-2 text-sm border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors">
                <Eye className="w-4 h-4" />
                {t('methodologies.view')}
              </button>
              <button className="flex items-center justify-center gap-2 px-3 py-2 text-sm border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors">
                <Edit className="w-4 h-4" />
                {t('methodologies.edit')}
              </button>
            </div>
          </div>
        ))}
      </div>

      {filteredMethodologies.length === 0 && (
        <div className="text-center py-12">
          <p className="text-gray-500">{t('common.noData')}</p>
        </div>
      )}
    </div>
  )
}

