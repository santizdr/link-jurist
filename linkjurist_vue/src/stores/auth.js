import { defineStore } from 'pinia'
import axios from 'axios'


export const useAuthStore = defineStore("auth", {
    
    state: () => ({
        accInStorage: localStorage.getItem('account.id'),
        user: {
            isAuthenticated: false,
            id: null,
            firstname: null,
            lastname: null,
            email: null,
            description: null,
            access: null,
            refresh: null,
            is_manager: null,
            tags: [],
        },
        account: {
            id: null,
            name: null,
            rating: null,
            description: null,
            slogan: null,
            web: null,
            email: null,
            phonenumber: null,
            address: null,
            cp: null,
            locality: null,
            country: null,
            image: null,
        },
        team: [],
        posts: [],
        files: [],
        cases: [],
        applications: []
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
                this.user.description = localStorage.getItem('user.description');
                this.user.is_manager = localStorage.getItem('user.is_manager');
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
            this.user.description = null;
            this.user.isAuthenticated = false;
            this.user.is_manager = false;
            this.user.tags = []

            localStorage.setItem("user.access", "");
            localStorage.setItem("user.refresh", "");
            localStorage.setItem("user.id", "");
            localStorage.setItem("user.firstname", "");
            localStorage.setItem("user.lastname", "");
            localStorage.setItem("user.email", "");
            localStorage.setItem("user.description", "");
            localStorage.setItem("user.is_manager", "");
            localStorage.setItem("user.tags", []);
        },
        setStoreInfo(data) {
            console.log("Set user info: ", data.user);

            this.user.id = data.user.id;
            this.user.firstname = data.user.firstname;
            this.user.lastname = data.user.lastname;
            this.user.email = data.user.email;
            this.user.description = data.user.description.replace(/\n/g, '<br>');
            this.user.is_manager = data.user.is_manager;
            this.user.tags = data.user.tags;

            if(data.account !== '') {
                this.setAccountInfo(data.account);
            }

            if (data.team.length > 0 ) {
                this.setTeamInfo(data.team);
            }

            if (data.posts.length > 0 ) {
                this.setPostsInfo(data.posts);
            }

            if (data.cases.length > 0 ) {
                this.setCasesInfo(data.cases);
            }

            if (data.files.length > 0 ) {
                this.setFilesInfo(data.files);
            }

            if (data.applications.length > 0 ) {
                this.setApplicationsInfo(data.applications);
            }

            localStorage.setItem("user.id", this.user.id);
            localStorage.setItem("user.firstname", this.user.firstname);
            localStorage.setItem("user.lastname", this.user.lastname);
            localStorage.setItem("user.email", this.user.email);
            localStorage.setItem("user.description", this.user.description);
            localStorage.setItem("user.is_manager", this.user.is_manager);
            localStorage.setItem("user.tags", this.user.tags);
        },
        setAccountInfo(account) {
            console.log("Set account info: ", account);

            this.account.id = account.id;
            this.account.name = account.name;
            this.account.rating = parseInt(account.rating);
            this.account.description = account.description.replace(/\n/g, '<br>');
            this.account.slogan = account.slogan;
            this.account.web = account.web;
            this.account.email = account.email;
            this.account.phonenumber = account.phonenumber;
            this.account.address = account.address;
            this.account.cp = account.cp;
            this.account.locality = account.locality;
            this.account.country = account.country;
            this.account.image = account.image;

            localStorage.setItem("account.id", this.account.id);
            localStorage.setItem("account.name", this.account.name);
            localStorage.setItem("account.rating", this.account.rating);
            localStorage.setItem("account.description", this.account.description);
            localStorage.setItem("account.slogan", this.account.slogan);
            localStorage.setItem("account.web", this.account.web);
            localStorage.setItem("account.email", this.account.email);
            localStorage.setItem("account.phonenumber", this.account.phonenumber);
            localStorage.setItem("account.address", this.account.address);
            localStorage.setItem("account.cp", this.account.cp);
            localStorage.setItem("account.locality", this.account.locality);
            localStorage.setItem("account.country", this.account.country);
            localStorage.setItem("account.image", this.account.image);
        },
        setTeamInfo(team) {
            console.log("Set team info: ", team);

            this.team = team;
            localStorage.setItem("team", team)
        },
        setPostsInfo(posts) {
            console.log("Set posts info: ", posts);

            this.posts = posts;
            localStorage.setItem("posts", posts)
        },
        setCasesInfo(cases) {
            console.log("Set cases info: ", cases);

            this.cases = cases;
            localStorage.setItem("cases", cases)
        },
        setFilesInfo(files) {
            console.log("Set files info: ", files);

            this.files = files;
            localStorage.setItem("files", files)
        },
        setApplicationsInfo(applications) {
            console.log("Set applications info: ", applications);

            for (let application of applications) {
                if(this.account.id === application.applicant) {
                    application["type"] = "applicant"; 
                } else {
                    application["type"] = "request";
                }
              }            
            this.applications = applications;
            localStorage.setItem("applications", applications)
        },
        refreshToken() {
            axios.post("/api/refresh/", {
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
        },
        logOut() {
            this.removeToken();

            this.account.id = null;
            this.account.name = null;
            this.account.rating = null;
            this.account.description = null;
            this.account.slogan = null;
            this.account.web = null;
            this.account.email = null;
            this.account.phonenumber = null;
            this.account.address = null;
            this.account.cp = null;
            this.account.locality = null;
            this.account.country = null;
      
            this.team = [];
            this.posts = [];
            this.files = [];
            this.cases = [];
            this.applications = [];

            localStorage.setItem("account.id", "");
            localStorage.setItem("account.name", "");
            localStorage.setItem("account.rating", "");
            localStorage.setItem("account.description", "");
            localStorage.setItem("account.slogan", "");
            localStorage.setItem("account.web", "");
            localStorage.setItem("account.email", "");
            localStorage.setItem("account.phonenumber", "");
            localStorage.setItem("account.address", "");
            localStorage.setItem("account.cp", "");
            localStorage.setItem("account.locality", "");
            localStorage.setItem("account.country", "");

            localStorage.setItem("team", []);
            localStorage.setItem("posts", []);
            localStorage.setItem("files", []);
            localStorage.setItem("cases", []);
            localStorage.setItem("applications", []);
        },
        reloadAccountInfo() {
            axios.get("/api/me")
            .then(response => {
                this.setStoreInfo(response.data);
            })
            .catch(error => {
                console.log("Error: ", error);
            })
        }
    }
})