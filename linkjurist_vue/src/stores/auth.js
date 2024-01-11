import { defineStore } from 'pinia'
import router from '@/router'

export const useAuthStore = defineStore("auth", {
    state() {
        return {
            authenticated: false,
        }
    },

    actions: {
        changeAuthenticatedVal() {
            this.authenticated = !this.authenticated;
            router.push('/');

        }
    }
})