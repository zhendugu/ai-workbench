import { ReactNode } from 'react'
import { Link, useLocation } from 'react-router-dom'
import { useTranslation } from 'react-i18next'
import {
  LayoutDashboard,
  Building2,
  Users,
  Briefcase,
  UsersRound,
  Network,
  BookOpen,
} from 'lucide-react'

interface LayoutProps {
  children: ReactNode
}

export function Layout({ children }: LayoutProps) {
  const { t, i18n } = useTranslation()
  const location = useLocation()

  const handleLanguageChange = (lang: string) => {
    i18n.changeLanguage(lang)
    localStorage.setItem('company-viewer-language', lang)
  }

  const navItems = [
    { path: '/', icon: LayoutDashboard, key: 'dashboard' },
    { path: '/company', icon: Building2, key: 'company' },
    { path: '/cells', icon: Users, key: 'cells' },
    { path: '/roles', icon: Briefcase, key: 'roles' },
    { path: '/task-forces', icon: UsersRound, key: 'taskForces' },
    { path: '/connections', icon: Network, key: 'connections' },
    { path: '/methodologies', icon: BookOpen, key: 'methodologies' },
  ]

  const isActive = (path: string) => {
    if (path === '/') {
      return location.pathname === '/'
    }
    return location.pathname.startsWith(path)
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Top Navigation Bar */}
      <header className="bg-white border-b border-gray-200 sticky top-0 z-50 shadow-sm">
        <div className="container mx-auto px-4 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-4">
              <h1 className="text-2xl font-semibold text-gray-900">
                {t('app.title')}
              </h1>
              <p className="text-sm text-gray-600 hidden sm:block">
                {t('app.subtitle')}
              </p>
            </div>

            {/* Language Switcher */}
            <div className="flex gap-2">
              <button
                onClick={() => handleLanguageChange('en')}
                className={`px-4 py-2 text-sm border rounded transition-colors ${
                  i18n.language === 'en'
                    ? 'bg-gray-100 border-gray-400 text-gray-900'
                    : 'bg-white border-gray-300 text-gray-700 hover:bg-gray-50'
                }`}
              >
                {t('language.english')}
              </button>
              <button
                onClick={() => handleLanguageChange('zh')}
                className={`px-4 py-2 text-sm border rounded transition-colors ${
                  i18n.language === 'zh'
                    ? 'bg-gray-100 border-gray-400 text-gray-900'
                    : 'bg-white border-gray-300 text-gray-700 hover:bg-gray-50'
                }`}
              >
                {t('language.chinese')}
              </button>
            </div>
          </div>
        </div>
      </header>

      <div className="flex">
        {/* Left Sidebar */}
        <aside className="w-64 bg-white border-r border-gray-200 min-h-[calc(100vh-73px)]">
          <nav className="p-4">
            <ul className="space-y-1">
              {navItems.map((item) => {
                const Icon = item.icon
                const active = isActive(item.path)
                return (
                  <li key={item.path}>
                    <Link
                      to={item.path}
                      className={`flex items-center gap-3 px-4 py-3 rounded-lg transition-colors ${
                        active
                          ? 'bg-blue-50 text-blue-600 font-medium'
                          : 'text-gray-700 hover:bg-gray-50'
                      }`}
                    >
                      <Icon className="w-5 h-5" />
                      <span>{t(`navigation.${item.key}`)}</span>
                    </Link>
                  </li>
                )
              })}
            </ul>
          </nav>
        </aside>

        {/* Main Content Area */}
        <main className="flex-1 container mx-auto px-4 py-8 max-w-7xl">
          {children}
        </main>
      </div>
    </div>
  )
}

