import { defineStore } from 'pinia'
import router from '@/router'

export const useAuthStore = defineStore("auth", {
    state() {
        return {
            authenticated: false,
            team: [
                {
                    "uuid": "e66a04be-e729-4431-8d10-29f6d40888dd",
                    "firstname": "Prudencio",
                    "lastname": "Sáez",
                    "email": "psaez@pys.es",
                },
                {
                    "uuid": "c9587843-f53b-48fe-b71e-4f10608101b4",
                    "firstname": "Antonio",
                    "lastname": "Mairena",
                    "email": "amairena@pys.es",
                },
                {
                    "uuid": "8175dec5-2884-422e-a6ad-3da20be6e3f2",
                    "firstname": "Daniel",
                    "lastname": "Casares",
                    "email": "dcasares@pys.es",
                },

            ],
        }
    },

    actions: {
        changeAuthenticatedVal() {
            this.authenticated = !this.authenticated;
            router.push("/");

            if(router.currentRoute !== "/" && !this.authenticated) {
                router.push("/");
            }
        }
    }
})