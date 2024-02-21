import { defineStore } from 'pinia'
import axios from 'axios'

export const useFilesStore = defineStore("files", {
    state: () => ({
        files: [],
    }),

    actions: {
        async fetchFilesData(id) {
            await axios.get('api/files', {
                params: {
                  id: id
                }
              })
            .then(response => {
                this.files = response.data.files;
            })
            .catch(error => {
                console.log("Error: ", error);
            })
        }
    },
})