// Run-Time Frontend Main Application
// Authority: RT_FE_REQ_FROZEN.md
// Mode: RUN-TIME (FROZEN) ONLY - Read-only viewing interface

import { useState, useEffect } from 'react'
import { useTranslation } from 'react-i18next'
import { CompanyIdentityView } from './components/company/CompanyIdentityView'
import { StructureView } from './components/cell/StructureView'
import { TopologyView } from './components/topology/TopologyView'
import { MethodologyContextView } from './components/methodology/MethodologyContextView'
import { FreezeRecordView } from './components/freeze/FreezeRecordView'
import { loadSnapshotById } from './services/authorityLoader'
import type { FrozenSnapshotViewModel } from './types/viewModels'

function App() {
  const { t, i18n } = useTranslation()
  // Get frozenId from URL - RT_FE_REQ_FROZEN.md Section 4.3: Deep linking support
  const [snapshot, setSnapshot] = useState<FrozenSnapshotViewModel | null>(null)
  const [error, setError] = useState<string | null>(null)
  const [loading, setLoading] = useState(true)
  const [activeView, setActiveView] = useState<
    'company' | 'structure' | 'topology' | 'methodology' | 'freeze-record'
  >('company')

  // Language switcher handler
  const handleLanguageChange = (lang: string) => {
    i18n.changeLanguage(lang)
    localStorage.setItem('rt-fe-language', lang)
  }

  // Load frozen company data on mount (one-time load)
  // MANDATORY: Uses Authority validation via authorityLoader
  useEffect(() => {
    // Extract frozenId from URL (e.g., /frozen/FROZEN-COMP-123)
    const pathParts = window.location.pathname.split('/')
    const idFromUrl = pathParts[pathParts.length - 1] || pathParts[pathParts.length - 2]
    
    const frozenId = (idFromUrl && idFromUrl !== 'frozen' && idFromUrl !== '') 
      ? idFromUrl 
      : 'FROZEN-COMP-DEFAULT' // Default for development

    loadSnapshotById(frozenId)
      .then((result) => {
        if (result.success && result.data) {
          setSnapshot(result.data)
          setError(null)
        } else {
          setError(result.error || 'Failed to load snapshot')
          setSnapshot(null)
        }
      })
      .catch((err) => {
        setError(err instanceof Error ? err.message : 'Unknown error')
        setSnapshot(null)
      })
      .finally(() => {
        setLoading(false)
      })
  }, [])

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <p className="text-gray-600">{t('errors.loading')}</p>
        </div>
      </div>
    )
  }

  if (error || !snapshot) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center max-w-md">
          <h1 className="text-xl font-semibold text-red-600 mb-2">{t('errors.invalidSnapshot')}</h1>
          <p className="text-gray-600 mb-4">{error || t('errors.snapshotValidationFailed')}</p>
          <p className="text-sm text-gray-500">
            {t('errors.snapshotDoesNotConform')}
          </p>
        </div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* PHASE 1: Global Frozen Banner - RT_FE_REQ_FROZEN.md Section 6.1 */}
      <div className="sticky top-0 z-50 border-b bg-white shadow-sm">
        <div className="container mx-auto px-4 py-3">
          {/* Language Switcher */}
          <div className="flex justify-end mb-2">
            <div className="flex gap-2">
              <button
                onClick={() => handleLanguageChange('en')}
                className={`px-3 py-1 text-xs border rounded ${
                  i18n.language === 'en' ? 'bg-gray-200 border-gray-400' : 'bg-white border-gray-300'
                }`}
              >
                {t('language.english')}
              </button>
              <button
                onClick={() => handleLanguageChange('zh-Hans')}
                className={`px-3 py-1 text-xs border rounded ${
                  i18n.language === 'zh-Hans' ? 'bg-gray-200 border-gray-400' : 'bg-white border-gray-300'
                }`}
              >
                {t('language.chinese')}
              </button>
            </div>
          </div>

          {/* Global Banner - MUST be displayed at top of all pages */}
          <div className="bg-blue-50 border border-blue-200 rounded-lg p-3 mb-3">
            <div className="flex items-center gap-2 mb-2">
              <span className="px-2 py-1 text-xs font-mono font-semibold border rounded bg-gray-100 text-gray-800">
                {t('banner.runtimeReadOnly')}
              </span>
            </div>
            <p className="text-sm text-gray-700">
              {t('banner.frozenCannotModify')}
              <br />
              {t('banner.nothingRunning')}
              <br />
              {t('banner.readOnlyView')}
            </p>
          </div>

          {/* Company Status Banner - RT_FE_REQ_FROZEN.md Section 6.1 */}
          <div className="bg-gray-50 border border-gray-200 rounded-lg p-3">
            <div className="flex items-center justify-between">
              <div>
                <div className="flex items-center gap-2 mb-1">
                  <span className="text-lg font-mono font-semibold">{t('company.frozenCompany')}</span>
                  <span className="px-2 py-1 text-xs font-mono border rounded frozen-indicator">
                    {t('company.frozenReadOnly')}
                  </span>
                </div>
                <div className="text-sm text-gray-600 space-y-1">
                  <p>
                    <span className="font-mono">{t('company.frozenAt')}:</span> {new Date(snapshot.company.frozenAt).toLocaleString()}
                  </p>
                  <p>
                    <span className="font-mono">{t('company.frozenBy')}:</span> {snapshot.company.frozenBy}
                  </p>
                  <p>
                    <span className="font-mono">{t('company.companyIdentifier')}:</span> {snapshot.company.companyIdentifier}
                  </p>
                  <p className="text-gray-700 font-medium">{t('company.cannotModify')}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* PHASE 3: View Navigation - RT_FE_REQ_FROZEN.md Section 4.1 */}
      {/* Important: Navigation is view switching only, not task flow */}
      <div className="container mx-auto px-4 py-4">
        <div className="mb-6">
          <div className="flex items-center gap-2 mb-2">
            <span className="text-xs font-mono text-gray-500">{t('navigation.viewNavigation')}</span>
          </div>
          <div className="flex gap-2 border-b">
            <button
              onClick={() => setActiveView('company')}
              className={`px-4 py-2 text-sm font-mono ${
                activeView === 'company'
                  ? 'border-b-2 border-gray-600 text-gray-800'
                  : 'text-gray-600 hover:text-gray-800'
              }`}
            >
              {t('navigation.companyOverview')}
            </button>
            <button
              onClick={() => setActiveView('structure')}
              className={`px-4 py-2 text-sm font-mono ${
                activeView === 'structure'
                  ? 'border-b-2 border-gray-600 text-gray-800'
                  : 'text-gray-600 hover:text-gray-800'
              }`}
            >
              {t('navigation.structureView')}
            </button>
            <button
              onClick={() => setActiveView('topology')}
              className={`px-4 py-2 text-sm font-mono ${
                activeView === 'topology'
                  ? 'border-b-2 border-gray-600 text-gray-800'
                  : 'text-gray-600 hover:text-gray-800'
              }`}
            >
              {t('navigation.topologyView')}
            </button>
            <button
              onClick={() => setActiveView('methodology')}
              className={`px-4 py-2 text-sm font-mono ${
                activeView === 'methodology'
                  ? 'border-b-2 border-gray-600 text-gray-800'
                  : 'text-gray-600 hover:text-gray-800'
              }`}
            >
              {t('navigation.methodologyContext')}
            </button>
            <button
              onClick={() => setActiveView('freeze-record')}
              className={`px-4 py-2 text-sm font-mono ${
                activeView === 'freeze-record'
                  ? 'border-b-2 border-gray-600 text-gray-800'
                  : 'text-gray-600 hover:text-gray-800'
              }`}
            >
              {t('navigation.freezeRecord')}
            </button>
          </div>
        </div>

        {/* PHASE 2: View Implementation - RT_FE_REQ_FROZEN.md Section 3 */}
        {activeView === 'company' && (
          <CompanyIdentityView company={snapshot.company} />
        )}

        {activeView === 'structure' && (
          <StructureView cells={snapshot.cells} roles={snapshot.roles} />
        )}

        {activeView === 'topology' && (
          <TopologyView cells={snapshot.cells} relations={snapshot.topology} />
        )}

        {activeView === 'methodology' && (
          <MethodologyContextView methodology={snapshot.methodology} />
        )}

        {activeView === 'freeze-record' && (
          <FreezeRecordView freezeRecord={snapshot.freezeRecord} />
        )}
      </div>
    </div>
  )
}

export default App
