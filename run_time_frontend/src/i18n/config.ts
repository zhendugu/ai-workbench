/**
 * i18n Configuration for Run-Time Frontend
 * 
 * Authority: WO-RUNTIME-FRONTEND-I18N-001
 * 
 * Supports:
 * - en (English) - default
 * - zh-Hans (Simplified Chinese)
 * 
 * Language switching is explicit (no auto-detection)
 */

import i18n from 'i18next'
import { initReactI18next } from 'react-i18next'
import enTranslations from './locales/en/common.json'
import zhHansTranslations from './locales/zh-Hans/common.json'

// Get language from localStorage or default to 'en'
const getInitialLanguage = (): string => {
  const saved = localStorage.getItem('rt-fe-language')
  if (saved === 'zh-Hans' || saved === 'en') {
    return saved
  }
  return 'en'
}

i18n
  .use(initReactI18next)
  .init({
    resources: {
      en: {
        translation: enTranslations,
      },
      'zh-Hans': {
        translation: zhHansTranslations,
      },
    },
    lng: getInitialLanguage(),
    fallbackLng: 'en',
    interpolation: {
      escapeValue: false, // React already escapes values
    },
  })

export default i18n

