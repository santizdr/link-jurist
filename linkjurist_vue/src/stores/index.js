import { defineStore } from 'pinia'
import axios from 'axios'
import router from '@/router'

export const useIndexStore = defineStore("index", {
    state: () => ({
        contacts: [],
        contact_suggestions: [],
        publications: [],
        publications_suggestions: [],
    }),

    actions: {
        async fetchIndexData(id) {
          await axios.get("/api/index/" + id)
                .then(response => {
                    console.log(response.data)
                    this.contacts = response.data.contacts;
                    this.contact_suggestions = response.data.contact_suggestions;
                    this.publications = response.data.publications;
                    this.publications_suggestions = response.data.publications_suggestions;

                })
                .catch(error => {
                    console.log("Error: ", error);
                })
          }
    },
})