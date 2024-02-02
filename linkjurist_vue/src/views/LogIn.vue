<script setup>
    import axios from 'axios';
    import { ref } from 'vue'
    import { useAuthStore } from '@/stores/auth';
    import { useRouter } from 'vue-router'

    const router = useRouter()
    const authStore = useAuthStore();

    const alert = ref({
        message: "",
        class: "",
    });

    const error = ref({
        field: "",
        message: "",
    });

    const form = ref({
        email: "",
        password: "",
    });

    async function submitForm() {
        error.value = {
            field: "",
            message: "",
        };

        if (form.value.email === "") {
            error.value.field = "email";
            error.value.message = "Introduce un email válido";
        } else if (form.value.password === "") {
            error.value.field = "password";
            error.value.message = "Introduce una contraseña válida";
        }

        if (error.value.field === '' && error.value.message === '') {
            await axios.post("/api/login/", form._rawValue)
                .then(response => {
                    this.authStore.setToken(response.data);

                    axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access;
                })
                .catch(error => {
                    alert.value.message = "Se ha producido un error al iniciar sesión";
                    alert.value.class = "span-error";
                })

            await axios.get("/api/me")
                .then(response => {
                    this.authStore.setStoreInfo(response.data);
                    if(response.data.account === '') {
                        router.push("accountprofile")
                    } else {
                        router.push("/");
                    }
                })
                .catch(error => {
                    console.log("Error: ", error);
                })
        }
    }

</script>

<template>
    <div class="login-page">
        <section class="section mt-6">
            <div class="columns is-centered">
                <div class="column is-three-fifths-desktop">
                    <form class="box" @submit.prevent="submitForm()">
                        <div v-if="alert.message !== ''" class="my-3">
                            <article class="message">
                                <div class="message-header"  :class="alert.class">
                                    <p>{{ alert.message }}</p>
                                    <button class="delete" aria-label="delete"></button>
                                </div>
                            </article>  
                        </div> 
                        <h1 class="title">Inicio de sesión</h1>
                        <h2 class="subtitle mt-3">Inicia sesión en tu cuenta de <span class="secondary-text-color has-text-weight-semibold">Link Jurist</span></h2>
                        <div class="field">
                            <label class="label">Correo electrónico</label>
                            <div class="control">
                                <input class="input" :class="{ 'input-error' : error.field === 'email' }" type="email" v-model="form.email">
                            </div>
                            <span v-if="error.field === 'email'" class="has-text-danger"> {{ error.message }}</span>
                        </div>

                        <div class="field">
                            <label class="label">Contraseña</label>
                            <div class="control">
                                <input class="input" :class="{ 'input-error' : error.field === 'password' }" type="password" v-model="form.password">
                            </div>
                            <span v-if="error.field === 'password'" class="has-text-danger"> {{ error.message }}</span>
                        </div> 
                        <div class="field is-grouped is-grouped-right mt-1">
                            <div class="control">
                                <button class="button is-rounded secondary-form-button">Confirmar</button>
                            </div>
                            <div class="control">
                                <RouterLink to="/" class="button is-rounded main-form-button">Cancelar</RouterLink>
                            </div>
                        </div>
                        <p class="mt-3">No tienes cuenta de <span class="secondary-text-color has-text-weight-semibold">Link Jurist</span>? Crea tu cuenta haciendo click <RouterLink to="signup">aquí</RouterLink></p>
                    </form>
                </div>
            </div>
        </section>
    </div>
</template>
>