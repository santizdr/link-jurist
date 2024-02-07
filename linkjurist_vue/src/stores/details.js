import { defineStore } from 'pinia'
import axios from 'axios'
import router from '@/router'

export const useDetailsStore = defineStore("details", {
    state: () => ({
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
        follow: null,
        team: [],    
        cases: [],      
        files: [],        
    }),

    actions: {
        setFollow() {
            this.follow = !this.follow;
        },
        async fetchAccountData(me, id) {
          await axios.get("/api/accountdetails/" + me + "/" + id)
                .then(response => {
                    this.account = response.data.account;
                    this.follow = response.data.follow;
                    this.team = response.data.team;
                    this.cases = response.data.cases;
                    this.files = response.data.files;

                })
                .catch(error => {
                    console.log("Error: ", error);
                })
          }
    },
})