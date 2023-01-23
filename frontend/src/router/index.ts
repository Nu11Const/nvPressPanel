import {createRouter, createWebHashHistory} from 'vue-router'
import nvPress from '../components/nvpress.vue'
//在Vue-router新版本中，需要使用createRouter来创建路由
export default createRouter({
  //指定路由的模式，此处只用的是hash模式
  history: createWebHashHistory(),
  //路由地址
  routes: [
    {
      //设置根目录
      path: '/',
      //import里边写组件地址
      component: () => import('../components/home.vue')
    },
    {
        path: '/caddy',
        component: () => import('../components/caddy.vue')
    },
    {
        path: '/nvpress',
        component: nvPress
    },
    {
        path: '/ftp',
        component: () => import('../components/ftp.vue')
    },
    {
        path: '/docker',
        component: () => import('../components/docker.vue')
    },
    {
      path: '/login',
      component: () => import("../components/login.vue")
    },
    {
      path: '/error/403',
      component: () => import("../errors/403.vue")
    },
    {
      path: '/:catchAll(.*)',
      component: () => import("../errors/404.vue")
    }
  ]
})
