import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router/index'
import VueCookies from 'vue-cookies'
import { useRoute, useRouter } from 'vue-router'
const vm = createApp(App)
vm.config.globalProperties.$http =VueCookies;
vm.use(router)
vm.use(VueCookies)
vm.mount('#app')