import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/ROI.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/faq',
    name: 'FAQ',
    component: () => import(/* webpackChunkName: "about" */ '../views/FAQ.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
