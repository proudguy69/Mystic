import { createRouter, createWebHistory } from 'vue-router'
import Welcome from '../views/welcome/Welcome.vue'
import Home from '../views/home/Home.vue'
import Levels from '../views/levels/Levels.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/welcome',
      name: 'welcome',
      component: Welcome
    },
    {
      path: '/levels',
      name: 'levels',
      component: Levels
    },
  ]
})

export default router
