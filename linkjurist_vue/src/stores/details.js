import { defineStore } from 'pinia'
import axios from 'axios'

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
        user: {
            id: null,
            email: null,
            firstname: null,
            lastname: null,
            description: null,
            account_name: null,
            tags: [],
        },
        follow: null,
        team: [],   
        posts: [], 
        cases: [],      
        files: [],        
    }),

    actions: {
        setFollow() {
            this.follow = !this.follow;
        },
        async fetchAccountData(me, id) {
          await axios.get("/api/accountdetails/", 
            {
                params: {
                    id: id,
                    me: me
                }
            }
          ).then(response => {
                this.account = response.data.account;
                this.follow = response.data.follow;
                this.team = response.data.team;
                this.posts = response.data.posts;
                this.cases = response.data.cases;
                this.files = response.data.files;

            })
            .catch(error => {
                console.log("Error: ", error);
            })
        },
        async fetchUserData(id) {
            await axios.get("/api/userdetails/", 
              {
                params: {id: id}
              }
            ).then(response => {
                console.log(response.data)
                this.user = response.data.user;
              })
              .catch(error => {
                console.log("Error: ", error);
              })
          },
        clearDetailsInfo() {
            this.account.id = null;
            this.account.name = null;
            this.account.description = null;
            this.account.slogan = null;
            this.account.web = null;
            this.account.email = null;
            this.account.phonenumber = null;
            this.account.address = null;
            this.account.cp = null;
            this.account.locality = null;
            this.account.country = null;
      
            this.user.id = null;
            this.user.account_name = null;
            this.user.email = null;
            this.user.firstname = null;
            this.user.lastname = null;
            this.user.description = null;
            this.user.tags = [];

            this.team = [];
            this.posts = [];
            this.files = [];
            this.cases = [];

            localStorage.setItem("account.id", "");
            localStorage.setItem("account.name", "");
            localStorage.setItem("account.description", "");
            localStorage.setItem("account.slogan", "");
            localStorage.setItem("account.web", "");
            localStorage.setItem("account.email", "");
            localStorage.setItem("account.phonenumber", "");
            localStorage.setItem("account.address", "");
            localStorage.setItem("account.cp", "");
            localStorage.setItem("account.locality", "");
            localStorage.setItem("account.country", "");

            localStorage.setItem("user.id", "");
            localStorage.setItem("user.email", "");
            localStorage.setItem("user.fisrtname", "");
            localStorage.setItem("user.lastname", "");
            localStorage.setItem("user.description", "");
            localStorage.setItem("user.account_name", "");
            localStorage.setItem("user.tags", []);

            localStorage.setItem("team", []);
            localStorage.setItem("posts", []);
            localStorage.setItem("files", []);
            localStorage.setItem("cases", []);
            localStorage.setItem("applications", []);
        },
    },
})