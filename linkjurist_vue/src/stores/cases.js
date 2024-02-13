import { defineStore } from 'pinia'
import axios from 'axios'
import router from '@/router'

export const useCasesStore = defineStore("cases", {
    state: () => ({
        cases: [],
    }),

    actions: {
        async fetchCasesData(id) {
            await axios.get('api/cases', {
                params: {
                  id: id
                }
              })
            .then(response => {
                this.cases = response.data.cases;
            })
            .catch(error => {
                console.log("Error: ", error);
            })
        }
    },
})