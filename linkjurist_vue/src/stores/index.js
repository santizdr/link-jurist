import { defineStore } from 'pinia'
import axios from 'axios'

export const useIndexStore = defineStore("index", {
    state: () => ({
        contacts: [],
        contact_suggestions: [],
        posts: [],
        post_suggestions: [],
        stats: {
          case_applications: null,
          post_likes: null,
          file_downloads: null,
        }
    }),

    actions: {
        async fetchIndexData(me, id) {
          await axios.get("/api/index/", {
            params: {
              me: me, 
              id: id
            }
          })
            .then(response => {
                this.contacts = response.data.contacts;
                this.contact_suggestions = response.data.contact_suggestions;
                this.posts = response.data.posts;
                this.post_suggestions = response.data.post_suggestions;
                this.stats = response.data.stats;
            })
            .catch(error => {
                console.log("Error: ", error);
            })
          }
    },
})