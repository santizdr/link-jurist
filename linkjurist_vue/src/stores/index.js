import { defineStore } from 'pinia'
import axios from 'axios'

export const useIndexStore = defineStore("index", {
    state: () => ({
        contacts: [],
        contact_suggestions: [],
        posts: [],
        post_suggestions: [],
        stats: {
          case_visualizations: null,
          case_applications: null,
          post_likes: null,
          cases_visualizations: null,
          cases_likes: null,
          downloads: null,
        }
    }),

    actions: {
        async fetchIndexData(id) {
          await axios.get("/api/index/", {
            params: {id: id}
          })
            .then(response => {

                this.contacts = response.data.contacts;
                this.contact_suggestions = response.data.contact_suggestions;
                this.posts = response.data.posts;
                this.post_suggestions = response.data.post_suggestions;
                this.stats = response.data.stats;
                console.log("STORE")
                console.log(this.stats)
            })
            .catch(error => {
                console.log("Error: ", error);
            })
          }
    },
})