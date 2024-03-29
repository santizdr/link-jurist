import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { useIndexStore } from '@/stores/index'
import { useDetailsStore } from '@/stores/details'
import { useCasesStore } from '@/stores/cases'
import { useFilesStore } from '@/stores/files'

import HomeView from '../views/HomeView.vue'
import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'
import CasesView from '../views/CasesView.vue'
import FilesView from '../views/FilesView.vue'
import AccountView from '../views/AccountView.vue'
import UserView from '../views/UserView.vue'
import AccountDetails from '../views/AccountDetails.vue'
import AccountProfile from '../views/AccountProfile.vue'
import { inject } from 'vue'

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
      path: '/account/:id',
      name: 'AccountDetails',
      component: AccountDetails,
    },
    {
      path: '/user/:id',
      name: 'UserView',
      component: UserView,
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
  const authStore = useAuthStore()
  const indexStore = useIndexStore()
  const detailsStore = useDetailsStore()
  const casesStore = useCasesStore()
  const filesStore = useFilesStore()

  if (!authStore.user.isAuthenticated) {
    if (to.path !== '/login' && to.path !== '/signup' && to.path !== '/') {
      next('/login');
    } else {
      next();
    }
  } else {
    if(to.path === '/') {
      indexStore.fetchIndexData(authStore.user.id, authStore.account.id);
    } else if(to.path === '/account' ) {
      detailsStore.clearDetailsInfo();
      authStore.reloadAccountInfo();
    } else if (to.path.match(/^\/account\/\d+$/)) {
      const id = to.params.id; 
      detailsStore.fetchAccountData(authStore.user.id, id);
    } else if (to.path === '/cases') {
      casesStore.fetchCasesData(authStore.account.id);
    } else if (to.path === '/files') {
      filesStore.fetchFilesData(authStore.account.id);
    } else if (to.path.match(/^\/user\/\d+$/)) {
      const id = to.params.id; 
      detailsStore.fetchUserData(id);
    }
    next();
  }
  return false
})

export default router
