import { useParams, Link } from 'react-router-dom'
import { useTranslation } from 'react-i18next'
import { mockCells } from '../mock/data'
import { ArrowLeft, Plus, Edit, Trash2 } from 'lucide-react'
import type { Cell } from '../mock/data'

export function CellDetailPage() {
  const { id } = useParams<{ id: string }>()
  const { t, i18n } = useTranslation()
  const isZh = i18n.language === 'zh'

  const cell = mockCells.find((c) => c.id === id)

  if (!cell) {
    return (
      <div className="text-center py-12">
        <p className="text-gray-500">{t('common.noData')}</p>
        <Link to="/cells" className="mt-4 text-blue-600 hover:text-blue-700">
          {t('cellDetail.back')}
        </Link>
      </div>
    )
  }

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

  return (
    <div>
      {/* Page Header */}
      <div className="flex items-center justify-between mb-8">
        <div className="flex items-center gap-4">
          <Link
            to="/cells"
            className="flex items-center gap-2 text-gray-600 hover:text-gray-900"
          >
            <ArrowLeft className="w-5 h-5" />
            {t('cellDetail.back')}
          </Link>
          <div>
            <h1 className="text-3xl font-bold text-gray-900">
              {isZh ? cell.name : cell.nameEn}
            </h1>
          </div>
        </div>
        <div className="flex gap-3">
          <button className="flex items-center gap-2 px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors">
            <Edit className="w-4 h-4" />
            {t('common.edit')}
          </button>
          <button className="flex items-center gap-2 px-4 py-2 border border-red-300 text-red-600 rounded-lg hover:bg-red-50 transition-colors">
            <Trash2 className="w-4 h-4" />
            {t('common.delete')}
          </button>
        </div>
      </div>

      {/* Basic Information */}
      <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6 mb-6">
        <h2 className="text-xl font-semibold text-gray-900 mb-4">
          {t('cellDetail.basicInfo')}
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              {t('cells.name')}
            </label>
            <p className="text-gray-900">{isZh ? cell.name : cell.nameEn}</p>
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              {t('cells.type')}
            </label>
            <p className="text-gray-900">{getCellTypeLabel(cell.type)}</p>
          </div>
          {cell.leader && (
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                {t('cells.leader')}
              </label>
              <p className="text-gray-900">{isZh ? cell.leader : cell.leaderEn}</p>
            </div>
          )}
          {cell.parentCellId && (
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                {t('cellDetail.parent')}
              </label>
              <p className="text-gray-900">
                {mockCells.find((c) => c.id === cell.parentCellId)
                  ? isZh
                    ? mockCells.find((c) => c.id === cell.parentCellId)!.name
                    : mockCells.find((c) => c.id === cell.parentCellId)!.nameEn
                  : cell.parentCellId}
              </p>
            </div>
          )}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              {t('cells.status')}
            </label>
            <span className={`inline-block px-2 py-1 text-sm font-medium rounded ${getStatusColor(cell.status)}`}>
              {getStatusLabel(cell.status)}
            </span>
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              {t('cellDetail.createdAt')}
            </label>
            <p className="text-gray-900">
              {new Date(cell.createdAt).toLocaleDateString()}
            </p>
          </div>
          {cell.description && (
            <div className="md:col-span-2">
              <label className="block text-sm font-medium text-gray-700 mb-1">
                {t('cells.description')}
              </label>
              <p className="text-gray-700">{isZh ? cell.description : cell.descriptionEn}</p>
            </div>
          )}
        </div>
      </div>

      {/* Members List */}
      <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6 mb-6">
        <div className="flex items-center justify-between mb-4">
          <h2 className="text-xl font-semibold text-gray-900">
            {t('cellDetail.members')}
          </h2>
          <button className="flex items-center gap-2 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors">
            <Plus className="w-4 h-4" />
            {t('cellDetail.addMember')}
          </button>
        </div>
        <div className="border border-gray-200 rounded-lg overflow-hidden">
          <table className="w-full">
            <thead className="bg-gray-50">
              <tr>
                <th className="px-4 py-3 text-left text-sm font-medium text-gray-700">
                  {isZh ? '姓名' : 'Name'}
                </th>
                <th className="px-4 py-3 text-left text-sm font-medium text-gray-700">
                  {isZh ? '职责' : 'Role'}
                </th>
                <th className="px-4 py-3 text-right text-sm font-medium text-gray-700">
                  {t('common.delete')}
                </th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-200">
              <tr>
                <td className="px-4 py-3 text-sm text-gray-900">{isZh ? '张三' : 'Zhang San'}</td>
                <td className="px-4 py-3 text-sm text-gray-600">{isZh ? '开发工程师' : 'Developer'}</td>
                <td className="px-4 py-3 text-right">
                  <button className="text-red-600 hover:text-red-700 text-sm">
                    {t('cellDetail.remove')}
                  </button>
                </td>
              </tr>
              <tr>
                <td className="px-4 py-3 text-sm text-gray-900">{isZh ? '李四' : 'Li Si'}</td>
                <td className="px-4 py-3 text-sm text-gray-600">{isZh ? '设计师' : 'Designer'}</td>
                <td className="px-4 py-3 text-right">
                  <button className="text-red-600 hover:text-red-700 text-sm">
                    {t('cellDetail.remove')}
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      {/* Roles List */}
      <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6 mb-6">
        <div className="flex items-center justify-between mb-4">
          <h2 className="text-xl font-semibold text-gray-900">
            {t('cellDetail.roles')}
          </h2>
          <button className="flex items-center gap-2 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors">
            <Plus className="w-4 h-4" />
            {t('cellDetail.linkRole')}
          </button>
        </div>
        <div className="border border-gray-200 rounded-lg overflow-hidden">
          <table className="w-full">
            <thead className="bg-gray-50">
              <tr>
                <th className="px-4 py-3 text-left text-sm font-medium text-gray-700">
                  {t('roles.name')}
                </th>
                <th className="px-4 py-3 text-left text-sm font-medium text-gray-700">
                  {t('roles.type')}
                </th>
                <th className="px-4 py-3 text-right text-sm font-medium text-gray-700">
                  {t('common.view')}
                </th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-200">
              <tr>
                <td className="px-4 py-3 text-sm text-gray-900">{isZh ? '前端开发' : 'Frontend Development'}</td>
                <td className="px-4 py-3 text-sm text-gray-600">{t('roles.typeTechnical')}</td>
                <td className="px-4 py-3 text-right">
                  <button className="text-blue-600 hover:text-blue-700 text-sm">
                    {t('common.view')}
                  </button>
                </td>
              </tr>
              <tr>
                <td className="px-4 py-3 text-sm text-gray-900">{isZh ? 'UI设计' : 'UI Design'}</td>
                <td className="px-4 py-3 text-sm text-gray-600">{t('roles.typeDesign')}</td>
                <td className="px-4 py-3 text-right">
                  <button className="text-blue-600 hover:text-blue-700 text-sm">
                    {t('common.view')}
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      {/* Connections */}
      <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
        <div className="flex items-center justify-between mb-4">
          <h2 className="text-xl font-semibold text-gray-900">
            {t('cellDetail.connections')}
          </h2>
          <button className="flex items-center gap-2 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors">
            <Plus className="w-4 h-4" />
            {t('cellDetail.addConnection')}
          </button>
        </div>
        <div className="border border-gray-200 rounded-lg overflow-hidden">
          <table className="w-full">
            <thead className="bg-gray-50">
              <tr>
                <th className="px-4 py-3 text-left text-sm font-medium text-gray-700">
                  {t('connections.target')}
                </th>
                <th className="px-4 py-3 text-left text-sm font-medium text-gray-700">
                  {t('connections.type')}
                </th>
                <th className="px-4 py-3 text-right text-sm font-medium text-gray-700">
                  {t('common.view')}
                </th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-200">
              <tr>
                <td className="px-4 py-3 text-sm text-gray-900">{isZh ? '设计小组' : 'Design Team'}</td>
                <td className="px-4 py-3 text-sm text-gray-600">{t('connections.typeCollaboration')}</td>
                <td className="px-4 py-3 text-right">
                  <button className="text-blue-600 hover:text-blue-700 text-sm">
                    {t('common.view')}
                  </button>
                </td>
              </tr>
              <tr>
                <td className="px-4 py-3 text-sm text-gray-900">{isZh ? '产品小组' : 'Product Team'}</td>
                <td className="px-4 py-3 text-sm text-gray-600">{t('connections.typeReporting')}</td>
                <td className="px-4 py-3 text-right">
                  <button className="text-blue-600 hover:text-blue-700 text-sm">
                    {t('common.view')}
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  )
}

