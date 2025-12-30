import { useTranslation } from 'react-i18next'
import { Link } from 'react-router-dom'
import { Building2, Users, Briefcase, UsersRound, Network, BookOpen, ArrowRight } from 'lucide-react'
import { mockCompany, mockCells, mockRoles, mockTaskForces, mockMethodologies } from '../mock/data'

export function DashboardPage() {
  const { t, i18n } = useTranslation()
  const isZh = i18n.language === 'zh'

  const stats = [
    {
      icon: Users,
      label: t('company.cellsCount'),
      count: mockCells.length,
      link: '/cells',
      color: 'bg-blue-500',
    },
    {
      icon: Briefcase,
      label: t('company.rolesCount'),
      count: mockRoles.length,
      link: '/roles',
      color: 'bg-green-500',
    },
    {
      icon: UsersRound,
      label: t('company.taskForcesCount'),
      count: mockTaskForces.filter((tf) => tf.status === 'active').length,
      link: '/task-forces',
      color: 'bg-purple-500',
    },
    {
      icon: BookOpen,
      label: t('company.methodologiesCount'),
      count: mockMethodologies.length,
      link: '/methodologies',
      color: 'bg-orange-500',
    },
  ]

  return (
    <div>
      {/* Page Header */}
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-2">
          {t('dashboard.title')}
        </h1>
        <p className="text-gray-600">{t('dashboard.subtitle')}</p>
      </div>

      {/* Company Info Card */}
      <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6 mb-8">
        <div className="flex items-center gap-3 mb-4">
          <Building2 className="w-8 h-8 text-blue-600" />
          <div>
            <h2 className="text-xl font-semibold text-gray-900">
              {isZh ? mockCompany.name : mockCompany.nameEn}
            </h2>
            {mockCompany.foundedDate && (
              <p className="text-sm text-gray-600">
                {t('company.foundedDate')}: {mockCompany.foundedDate}
              </p>
            )}
          </div>
        </div>
        {mockCompany.description && (
          <p className="text-gray-700 mb-4">
            {isZh ? mockCompany.description : mockCompany.descriptionEn}
          </p>
        )}
        <Link
          to="/company"
          className="inline-flex items-center gap-2 text-blue-600 hover:text-blue-700 font-medium"
        >
          {t('navigation.company')} <ArrowRight className="w-4 h-4" />
        </Link>
      </div>

      {/* Statistics Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
        {stats.map((stat) => {
          const Icon = stat.icon
          return (
            <Link
              key={stat.link}
              to={stat.link}
              className="bg-white rounded-lg shadow-sm border border-gray-200 p-6 hover:shadow-md transition-shadow"
            >
              <div className="flex items-center justify-between mb-4">
                <div className={`${stat.color} p-3 rounded-lg`}>
                  <Icon className="w-6 h-6 text-white" />
                </div>
                <ArrowRight className="w-5 h-5 text-gray-400" />
              </div>
              <div className="text-3xl font-bold text-gray-900 mb-1">
                {stat.count}
              </div>
              <div className="text-sm text-gray-600">{stat.label}</div>
            </Link>
          )
        })}
      </div>

      {/* Quick Links */}
      <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
        <h2 className="text-xl font-semibold text-gray-900 mb-4">
          {t('navigation.dashboard')}
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <Link
            to="/company"
            className="flex items-center gap-3 p-4 border border-gray-200 rounded-lg hover:bg-gray-50 transition-colors"
          >
            <Building2 className="w-5 h-5 text-gray-600" />
            <span className="font-medium text-gray-900">
              {t('navigation.company')}
            </span>
          </Link>
          <Link
            to="/cells"
            className="flex items-center gap-3 p-4 border border-gray-200 rounded-lg hover:bg-gray-50 transition-colors"
          >
            <Users className="w-5 h-5 text-gray-600" />
            <span className="font-medium text-gray-900">
              {t('navigation.cells')}
            </span>
          </Link>
          <Link
            to="/roles"
            className="flex items-center gap-3 p-4 border border-gray-200 rounded-lg hover:bg-gray-50 transition-colors"
          >
            <Briefcase className="w-5 h-5 text-gray-600" />
            <span className="font-medium text-gray-900">
              {t('navigation.roles')}
            </span>
          </Link>
          <Link
            to="/task-forces"
            className="flex items-center gap-3 p-4 border border-gray-200 rounded-lg hover:bg-gray-50 transition-colors"
          >
            <UsersRound className="w-5 h-5 text-gray-600" />
            <span className="font-medium text-gray-900">
              {t('navigation.taskForces')}
            </span>
          </Link>
          <Link
            to="/connections"
            className="flex items-center gap-3 p-4 border border-gray-200 rounded-lg hover:bg-gray-50 transition-colors"
          >
            <Network className="w-5 h-5 text-gray-600" />
            <span className="font-medium text-gray-900">
              {t('navigation.connections')}
            </span>
          </Link>
          <Link
            to="/methodologies"
            className="flex items-center gap-3 p-4 border border-gray-200 rounded-lg hover:bg-gray-50 transition-colors"
          >
            <BookOpen className="w-5 h-5 text-gray-600" />
            <span className="font-medium text-gray-900">
              {t('navigation.methodologies')}
            </span>
          </Link>
        </div>
      </div>
    </div>
  )
}

