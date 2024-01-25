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
        },
        account: {
            id: null,
            name: null,
            description: null,
            slogan: null,
            web: null,
            email: null,
            phonenumber: null,
            address: null,
            cp: null,
            locality: null,
            country: null,
        },
        team: [],
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
        setStoreInfo(data) {
            console.log("Set user info: ", data.user);

            this.user.id = data.user.id;
            this.user.firstname = data.user.firstname;
            this.user.lastname = data.user.lastname;
            this.user.email = data.user.email;

            if(data.account !== '') {
                this.setAccountInfo(data.account);
            }

            if (data.team.length > 0 ) {
                this.setTeamInfo(data.team);
            }

            localStorage.setItem("user.id", this.user.id);
            localStorage.setItem("user.firstname", this.user.firstname);
            localStorage.setItem("user.lastname", this.user.lastname);
            localStorage.setItem("user.email", this.user.email);
        },
        setAccountInfo(account) {
            console.log("Set account info: ", account);

            this.account.id = account.id;
            this.account.name = account.name;
            this.account.description = account.description;
            this.account.slogan = account.slogan;
            this.account.web = account.web;
            this.account.email = account.email;
            this.account.phonenumber = account.phonenumber;
            this.account.address = account.address;
            this.account.cp = account.cp;
            this.account.locality = account.locality;
            this.account.country = account.country;

            localStorage.setItem("account.id", this.account.id);
            localStorage.setItem("account.name", this.account.name);
            localStorage.setItem("account.description", this.account.description);
            localStorage.setItem("account.slogan", this.account.slogan);
            localStorage.setItem("account.web", this.account.web);
            localStorage.setItem("account.email", this.account.email);
            localStorage.setItem("account.phonenumber", this.account.phonenumber);
            localStorage.setItem("account.address", this.account.address);
            localStorage.setItem("account.cp", this.account.cp);
            localStorage.setItem("account.locality", this.account.locality);
            localStorage.setItem("account.country", this.account.country);
        },
        setTeamInfo(team) {
            console.log("Set team info: ", team);

            this.team = team;
            localStorage.setItem("team", team)
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