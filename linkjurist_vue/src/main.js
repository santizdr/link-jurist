import './assets/main.css'

import { createApp, setTransitionHooks } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import axios from 'axios'

import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { library } from '@fortawesome/fontawesome-svg-core'

import { fa1, fa2, fa3, fa4, fa5, faGlobe, faEnvelope, faPlus, faInfo, faFile, faUser, faScaleBalanced, faUpload, faDownload, faEye, faArrowRight, faEuroSign, faPercent, faHeart, faMinus, faClock, faCheck, faXmark, faPen, faTrash, faKeyboard} from '@fortawesome/free-solid-svg-icons'

library.add(fa1, fa2, fa3, fa4, fa5, faGlobe, faEnvelope, faPlus, faInfo, faFile, faUser, faScaleBalanced, faUpload, faDownload, faEye, faArrowRight, faEuroSign, faPercent, faHeart, faMinus, faClock, faCheck, faXmark, faPen, faTrash, faKeyboard )

const pinia = createPinia()

pinia.use((context) => {
    const accessToken = window.localStorage.getItem("user.access");
    const refreshToken = window.localStorage.getItem("user.refresh");

    if (accessToken && refreshToken) {
        if(context.store.$id === "auth") {
            axios.defaults.headers.common["Authorization"] = "Bearer " + accessToken;
            context.store.initStore();
            axios.get("/api/me")
                .then(response => {
                    console.log(response);
                    context.store.setStoreInfo(response.data);
                })
                .catch(error => {
                    console.log("Error: ", error);
                })
        }
    }
})

const app = createApp(App).component('font-awesome-icon', FontAwesomeIcon)

axios.defaults.baseURL = 'http://localhost:8000'

app.use(router, axios)
app.use(pinia)

app.mount('#app')
