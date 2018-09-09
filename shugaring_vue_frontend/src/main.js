// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import Vuex from 'vuex'
import App from './App'
import router from './router'
import store from './store'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import '@fortawesome/fontawesome-free/css/all.css'

Vue.use(Vuex)

Vue.use(Vuetify, {
  theme: {
    primary: '#59A193',
    secondary: '#04090D',
    accent: '#59A193'
  },
  iconfont: 'fa',
  icons: {
    'vk': 'fab fa-vk',
    'inst': 'fab fa-instagram',
    'heart': 'fas fa-heart',
    'thumbs': 'far fa-thumbs-up',
    'info': 'fas fa-info',
    'rouble': 'fas fa-ruble-sign',
    'chart': 'fas fa-chart-line',
    'ok': 'far fa-check-circle',
    'search': 'fas fa-search',
    'users': 'fas fa-users'
  }
})

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
