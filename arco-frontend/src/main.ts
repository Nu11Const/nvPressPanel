import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router/index'
import VueCookies from 'vue-cookies'
createApp(App).use(router).mount('#app')
App.config.globalProperties.$cookies = VueCookies