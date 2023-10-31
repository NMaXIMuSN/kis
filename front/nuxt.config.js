import colors from 'vuetify/es5/util/colors'

export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    titleTemplate: '%s - web',
    title: 'web',
    htmlAttrs: {
      lang: 'en',
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' },
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
  },

  css: [
    '~/assets/global.scss'
  ],

  plugins: [],

  router: {
    middleware: ['auth']
  },  

  components: true,

  buildModules: [
    '@nuxtjs/eslint-module',
    '@nuxtjs/vuetify',
  ],

  modules: [
    '@nuxtjs/axios',
    '@nuxtjs/dayjs',
    '@nuxtjs/auth',
  ],

  dayjs: {
    locales: ['ru'],
    defaultLocale: 'ru',
    plugins: ['duration']
  },

  axios: {
    baseURL: 'http://127.0.0.1:8000/api',
  },

  auth: {
    strategies: {
      local: {
        token: {
          type: 'Token'
        },
        endpoints: {
          login: { url: 'login', method: 'post'},
          logout: { url: 'logout', method: 'get'},
          user: { url: 'user', method: 'get', propertyName: ''},
        },
      },
    },
    redirect: {
      logout: '/login',
      callback: '/login',
      login: '/login',
      home: null,
    }
  },

  // Vuetify module configuration: https://go.nuxtjs.dev/config-vuetify
  vuetify: {
    customVariables: ['~/assets/variables.scss'],
    theme: {
      dark: false,
      themes: {
        light: {
          primary: "#196AA6",
          orange: '#F79420',
          'dark-blue': '#064B66',
          'dark-green': '#0D4F4C',
          'dark-purple': '#123B4F',
          'dark-gold': '#C2912E',
          yellow: '#FAC826',
          'light-yellow': '#FFFACB',
          'light-gold': '#EDD688',
          blue: '#00A0BB',
          accent: colors.grey.darken3,
          secondary: colors.amber.darken3,
          info: colors.teal.lighten1,
          warning: colors.amber.base,
          error: colors.deepOrange.accent4,
          success: colors.green.accent3,
        },
      },
    },
  },

  build: {
    loaders: {
      scss: {
        additionalData: "@import '@/assets/variables.scss';"
      }
    },
  },
}
