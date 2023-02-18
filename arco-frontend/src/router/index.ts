import {createRouter, createWebHashHistory} from 'vue-router'
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
      component: () => import('../pages/Home.vue')
    },
    {
      path: '/auth/login',
      component: () => import('../pages/Login.vue')
    },
    {
      path: '/nvpress',
      component: () => import("../pages/nvPress.vue")
    },
    {
      path: '/ftp',
      component: () => import("../pages/FTP.vue")
    },
    {
      path: '/caddy',
      component: () => import("../pages/Caddy.vue")
    },
    {
      path: '/docker',
      component: () => import("../pages/Docker.vue")
    },
    {
      path: '/settings/caddy',
      component: () => import("../pages/Caddy_settings.vue")
    },
    {
      path: '/settings/docker',
      component: () => import("../pages/Docker_settings.vue")
    },
    {
      path: '/settings/system',
      component: () => import("../pages/System_settings.vue")
    },
    {
      path: '/:catchAll(.*)',
      component: () => import("../errors/404.vue")
    }
  ]
})
