import { createRouter, createWebHistory } from 'vue-router'
import { useUserStore } from '@/stores/user'

import HomeView from '../views/HomeView.vue'
import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'
import CasesView from '../views/CasesView.vue'
import FilesView from '../views/FilesView.vue'
import AccountView from '../views/AccountView.vue'
import AccountProfile from '../views/AccountProfile.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'HomeView',
      component: HomeView,
    },
    {
      path: '/accountprofile',
      name: 'AccountProfile',
      component: AccountProfile,
    },
    {
      path: '/signup',
      name: 'SignUp',
      component: SignUp,
    },
    {
      path: '/login',
      name: 'LogIn',
      component: LogIn,
    },
    {
      path: '/cases',
      name: 'CasesView',
      component: CasesView,
    },
    {
      path: '/files',
      name: 'FilesView',
      component: FilesView,
    },
    {
      path: '/account',
      name: 'AccountView',
      component: AccountView,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    }
  ]
})

router.beforeEach((to, from, next) => {
  const store = useUserStore()

  if (!store.user.isAuthenticated) {
    if (to.path !== '/login' && to.path !== '/signup' && to.path !== '/') {
      next('/login');
    } else {
      next();
    }
  } else {
    next();
  }
  return false
})

export default router