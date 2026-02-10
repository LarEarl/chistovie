// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  
  modules: [
    '@nuxtjs/tailwindcss',
    '@pinia/nuxt',
  ],

  runtimeConfig: {
    public: {
      apiBase: process.env.NUXT_PUBLIC_API_BASE || 'http://localhost:8000/api'
    }
  },

  app: {
    head: {
      title: 'Чистовье Караганда - Каталог товаров для дома',
      htmlAttrs: {
        lang: 'ru'
      },
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { name: 'description', content: 'Чистовье Караганда - товары для дома, чистящие средства и хозяйственные товары. Быстрая доставка и актуальные цены.' },
        { name: 'robots', content: 'index,follow' },
        { property: 'og:title', content: 'Чистовье Караганда - Каталог товаров для дома' },
        { property: 'og:description', content: 'Чистовье Караганда - товары для дома, чистящие средства и хозяйственные товары.' },
        { property: 'og:type', content: 'website' },
        { property: 'og:url', content: 'https://chistoviekrg.kz/' },
        { property: 'og:site_name', content: 'Чистовье Караганда' },
        { name: 'twitter:card', content: 'summary' }
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
        { rel: 'canonical', href: 'https://chistoviekrg.kz/' }
      ]
    }
  },

  css: [
    '~/assets/css/main.css',
  ],

  compatibilityDate: '2025-12-05',
})
