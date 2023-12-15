import { createRouter, createWebHistory } from 'vue-router'
import Welcome from '../views/welcome/Welcome.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Welcome
    }
  ]
})

export default router
