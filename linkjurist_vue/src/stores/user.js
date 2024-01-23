import { defineStore } from 'pinia'
import axios from 'axios'
import router from '@/router'

export const useUserStore = defineStore("user", {
    state: () => ({
        user: {
            isAuthenticated: false,
            id: null,
            firstname: null,
            lastname: null,
            email: null,
            access: null,
            refresh: null,
        }
    }),

    actions: {
        initStore() {
            if(localStorage.getItem('user.access')) {
                this.user.access = localStorage.getItem('user.access');
                this.user.refresh = localStorage.getItem('user.refresh');
                this.user.id = localStorage.getItem('user.id');
                this.user.firstname = localStorage.getItem('user.firstname');
                this.user.lastname = localStorage.getItem('user.lastname');
                this.user.email = localStorage.getItem('user.email');
                this.user.isAuthenticated = true;

                this.refreshToken();

                console.log("Initialised user: ", this.user)

            }
        },
        setToken(data) {
            console.log("Set token: ", data);

            this.user.access = data.access;
            this.user.refresh = data.refresh;
            this.user.isAuthenticated = true;

            localStorage.setItem("user.access", data.access);
            localStorage.setItem("user.refresh", data.refresh);
        },
        removeToken() {
            console.log("Remove token");

            this.user.access = null;
            this.user.refresh = null;
            this.user.id = null;
            this.user.firstname = null;
            this.user.lastname = null;
            this.user.email = null;
            this.user.isAuthenticated = false;

            localStorage.setItem("user.access", "");
            localStorage.setItem("user.refresh", "");
            localStorage.setItem("user.id", "");
            localStorage.setItem("user.firstname", "");
            localStorage.setItem("user.lastname", "");
            localStorage.setItem("user.email", "");
        },
        setUserInfo(user) {
            console.log("Set user info: ", user);

            this.user.id = user.id;
            this.user.firstname = user.firstname;
            this.user.lastname = user.lastname;
            this.user.email = user.email;

            localStorage.setItem("user.id", this.user.id);
            localStorage.setItem("user.firstname", this.user.firstname);
            localStorage.setItem("user.lastname", this.user.lastname);
            localStorage.setItem("user.email", this.user.email);
        },
        refreshToken() {
            axios.post("/api/account/refresh", {
                refresh: this.user.refresh
            })
            .then((response) => {
                this.user.access = response.data.access;
                localStorage.setItem("user.access", response.data.access);
                axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access
            })
            .catch((error) => {
                console.log(error);
                this.removeToken();
            })
        }
    }
})