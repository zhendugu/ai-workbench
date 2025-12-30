import { useState } from 'react'
import { useTranslation } from 'react-i18next'
import { mockRoles } from '../mock/data'
import { Plus, Search, Eye, Edit, Trash2, Briefcase } from 'lucide-react'
import type { Role } from '../mock/data'

export function RolesLibraryPage() {
  const { t, i18n } = useTranslation()
  const isZh = i18n.language === 'zh'
  const [searchTerm, setSearchTerm] = useState('')

  const getRoleTypeLabel = (type: Role['type']) => {
    switch (type) {
      case 'technical':
        return t('roles.typeTechnical')
      case 'management':
        return t('roles.typeManagement')
      case 'operations':
        return t('roles.typeOperations')
      case 'design':
        return t('roles.typeDesign')
      case 'other':
        return t('roles.typeOther')
    }
  }

  const getLevelLabel = (level?: Role['level']) => {
    if (!level) return '-'
    switch (level) {
      case 'junior':
        return t('roles.levelJunior')
      case 'intermediate':
        return t('roles.levelIntermediate')
      case 'senior':
        return t('roles.levelSenior')
      case 'expert':
        return t('roles.levelExpert')
    }
  }

  const filteredRoles = mockRoles.filter((role) => {
    const name = isZh ? role.name : role.nameEn
    return name.toLowerCase().includes(searchTerm.toLowerCase())
  })

  return (
    <div>
      {/* Page Header */}
      <div className="flex items-center justify-between mb-8">
        <div>
          <h1 className="text-3xl font-bold text-gray-900 mb-2">
            {t('roles.title')}
          </h1>
        </div>
        <button className="flex items-center gap-2 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors">
          <Plus className="w-4 h-4" />
          {t('roles.create')}
        </button>
      </div>

      {/* Search and Filter */}
      <div className="flex gap-4 mb-6">
        <div className="flex-1 relative">
          <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 w-5 h-5 text-gray-400" />
          <input
            type="text"
            placeholder={t('roles.search')}
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
          />
        </div>
        <select className="px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent">
          <option>{t('roles.filter')}</option>
        </select>
      </div>

      {/* Roles Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {filteredRoles.map((role) => (
          <div
            key={role.id}
            className="bg-white rounded-lg shadow-sm border border-gray-200 p-6 hover:shadow-md transition-shadow"
          >
            <div className="flex items-start gap-3 mb-4">
              <div className="p-3 bg-blue-100 rounded-lg">
                <Briefcase className="w-6 h-6 text-blue-600" />
              </div>
              <div className="flex-1">
                <h3 className="text-lg font-semibold text-gray-900 mb-2">
                  {isZh ? role.name : role.nameEn}
                </h3>
                <span className="inline-block px-2 py-1 text-xs font-medium bg-gray-100 text-gray-800 rounded">
                  {getRoleTypeLabel(role.type)}
                </span>
              </div>
            </div>

            <p className="text-sm text-gray-600 mb-4 line-clamp-3">
              {isZh ? role.description : role.descriptionEn}
            </p>

            {role.level && (
              <div className="mb-4 text-sm text-gray-600">
                <span className="font-medium">{t('roles.level')}: </span>
                {getLevelLabel(role.level)}
              </div>
            )}

            {role.requiredSkills && role.requiredSkills.length > 0 && (
              <div className="mb-4">
                <div className="text-sm font-medium text-gray-700 mb-2">
                  {t('roles.skills')}:
                </div>
                <div className="flex flex-wrap gap-2">
                  {role.requiredSkills.map((skill, idx) => (
                    <span
                      key={idx}
                      className="px-2 py-1 text-xs bg-blue-50 text-blue-700 rounded"
                    >
                      {skill}
                    </span>
                  ))}
                </div>
              </div>
            )}

            <div className="flex gap-2 pt-4 border-t border-gray-200">
              <button className="flex-1 flex items-center justify-center gap-2 px-3 py-2 text-sm border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors">
                <Eye className="w-4 h-4" />
                {t('roles.view')}
              </button>
              <button className="flex items-center justify-center gap-2 px-3 py-2 text-sm border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors">
                <Edit className="w-4 h-4" />
                {t('roles.edit')}
              </button>
              <button className="flex items-center justify-center gap-2 px-3 py-2 text-sm border border-red-300 text-red-600 rounded-lg hover:bg-red-50 transition-colors">
                <Trash2 className="w-4 h-4" />
                {t('roles.delete')}
              </button>
            </div>
          </div>
        ))}
      </div>

      {filteredRoles.length === 0 && (
        <div className="text-center py-12">
          <p className="text-gray-500">{t('common.noData')}</p>
        </div>
      )}
    </div>
  )
}

