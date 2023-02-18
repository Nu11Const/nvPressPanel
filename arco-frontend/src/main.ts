import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router/index'
import VueCookies from 'vue-cookies'
import { useRoute, useRouter } from 'vue-router'
createApp(App).use(router).mount('#app')
App.config.globalProperties.$cookies = VueCookies