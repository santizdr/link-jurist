import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import axios from 'axios'

const pinia = createPinia()
const app = createApp(App)

axios.defaults.baseURL = 'http://localhost:8000'

app.use(router, axios)
app.use(pinia)

app.mount('#app')
