/**
 * i18n Configuration for Company Viewer
 */

import i18n from 'i18next'
import { initReactI18next } from 'react-i18next'
import enTranslations from './locales/en/common.json'
import zhTranslations from './locales/zh/common.json'

const getInitialLanguage = (): string => {
  const saved = localStorage.getItem('company-viewer-language')
  if (saved === 'zh' || saved === 'en') {
    return saved
  }
  // Default to browser language or 'en'
  const browserLang = navigator.language.toLowerCase()
  if (browserLang.startsWith('zh')) {
    return 'zh'
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
      zh: {
        translation: zhTranslations,
      },
    },
    lng: getInitialLanguage(),
    fallbackLng: 'en',
    interpolation: {
      escapeValue: false,
    },
  })

export default i18n

