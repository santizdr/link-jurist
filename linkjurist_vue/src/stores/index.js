import { defineStore } from 'pinia'
import axios from 'axios'
import router from '@/router'

export const useIndexStore = defineStore("index", {
    state: () => ({
        contacts: [],
        contact_suggestions: [],
        posts: [],
        post_suggestions: [],
    }),

    actions: {
        async fetchIndexData(id) {
          await axios.get("/api/index/" + id)
                .then(response => {
                    this.contacts = response.data.contacts;
                    this.contact_suggestions = response.data.contact_suggestions;
                    this.posts = response.data.posts;
                    this.post_suggestions = response.data.post_suggestions;

                })
                .catch(error => {
                    console.log("Error: ", error);
                })
          }
    },
})