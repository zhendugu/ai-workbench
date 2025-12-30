import { useTranslation } from 'react-i18next'
import { mockCompany, mockCells, mockRoles, mockTaskForces, mockMethodologies } from '../mock/data'
import { Edit, Download, Plus } from 'lucide-react'

export function CompanyViewPage() {
  const { t, i18n } = useTranslation()
  const isZh = i18n.language === 'zh'

  return (
    <div>
      {/* Page Header */}
      <div className="flex items-center justify-between mb-8">
        <div>
          <h1 className="text-3xl font-bold text-gray-900 mb-2">
            {t('company.title')}
          </h1>
        </div>
        <div className="flex gap-3">
          <button className="flex items-center gap-2 px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors">
            <Edit className="w-4 h-4" />
            {t('company.edit')}
          </button>
          <button className="flex items-center gap-2 px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors">
            <Download className="w-4 h-4" />
            {t('company.export')}
          </button>
          <button className="flex items-center gap-2 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors">
            <Plus className="w-4 h-4" />
            {t('company.addCell')}
          </button>
        </div>
      </div>

      {/* Basic Information Card */}
      <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6 mb-6">
        <h2 className="text-xl font-semibold text-gray-900 mb-4">
          {t('company.name')}
        </h2>
        <div className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              {t('company.name')}
            </label>
            <p className="text-gray-900">{isZh ? mockCompany.name : mockCompany.nameEn}</p>
          </div>
          {mockCompany.foundedDate && (
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                {t('company.foundedDate')}
              </label>
              <p className="text-gray-900">{mockCompany.foundedDate}</p>
            </div>
          )}
          {mockCompany.description && (
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                {t('company.description')}
              </label>
              <p className="text-gray-700">{isZh ? mockCompany.description : mockCompany.descriptionEn}</p>
            </div>
          )}
          {mockCompany.vision && (
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                {t('company.vision')}
              </label>
              <p className="text-gray-700">{isZh ? mockCompany.vision : mockCompany.visionEn}</p>
            </div>
          )}
          {mockCompany.mission && (
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                {t('company.mission')}
              </label>
              <p className="text-gray-700">{isZh ? mockCompany.mission : mockCompany.missionEn}</p>
            </div>
          )}
        </div>
      </div>

      {/* Organization Structure */}
      <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6 mb-6">
        <h2 className="text-xl font-semibold text-gray-900 mb-4">
          {t('company.structure')}
        </h2>
        <div className="border-2 border-dashed border-gray-300 rounded-lg p-12 text-center">
          <p className="text-gray-500 mb-4">
            {t('company.structure')}
          </p>
          <p className="text-sm text-gray-400">
            {isZh
              ? '可视化树形结构图 - 显示所有小组及其层级关系'
              : 'Visual Tree Structure - Showing all Cells and hierarchy'}
          </p>
        </div>
      </div>

      {/* Related Content */}
      <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
        <h2 className="text-xl font-semibold text-gray-900 mb-4">
          {isZh ? '关联内容' : 'Related Content'}
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
          <div className="p-4 border border-gray-200 rounded-lg">
            <div className="text-2xl font-bold text-gray-900 mb-1">
              {mockCells.length}
            </div>
            <div className="text-sm text-gray-600">{t('company.cellsCount')}</div>
          </div>
          <div className="p-4 border border-gray-200 rounded-lg">
            <div className="text-2xl font-bold text-gray-900 mb-1">
              {mockRoles.length}
            </div>
            <div className="text-sm text-gray-600">{t('company.rolesCount')}</div>
          </div>
          <div className="p-4 border border-gray-200 rounded-lg">
            <div className="text-2xl font-bold text-gray-900 mb-1">
              {mockTaskForces.filter((tf) => tf.status === 'active').length}
            </div>
            <div className="text-sm text-gray-600">{t('company.taskForcesCount')}</div>
          </div>
          <div className="p-4 border border-gray-200 rounded-lg">
            <div className="text-2xl font-bold text-gray-900 mb-1">
              {mockMethodologies.length}
            </div>
            <div className="text-sm text-gray-600">{t('company.methodologiesCount')}</div>
          </div>
        </div>
      </div>
    </div>
  )
}

