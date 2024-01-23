<script setup>
    import axios from 'axios';
    import { ref } from 'vue'
    import { useUserStore } from '@/stores/user';

    const store = useUserStore();

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
        firstname: "",
        lastname: "",
        password1: "",
        password2: "",
    });

    function submitForm() {
        error.value = {
            field: "",
            message: "",
        };
        if(form.value.firstname === "") {
            error.value.field = "firstname";
            error.value.message = "El campo nombre no puede estar vacío";
        } else if (form.value.lastname === "") {
            error.value.field = "lastname";
            error.value.message = "El campo apellido no puede estar vacío";
        } else if (form.value.email === "") {
            error.value.field = "email";
            error.value.message = "Introduce un email válido";
        } else if (form.value.password1 === "") {
            error.value.field = "password1";
            error.value.message = "La contraseña no puede estar vacía";
        } else if (form.value.password2 === "") {
            error.value.field = "password2";
            error.value.message = "La contraseña no puede estar vacía";
        } else if (form.value.password1 !== form.value.password2) {
            error.value.field = "password2";
            error.value.message = "Las contraseñas no coinciden";
        }

        if (error.value.field === '' && error.value.message === '') {
            axios.post("/api/signup/", form)
                .then(response => {
                    if(response.data.message === "success") {
                        alert.value.message = "Registro completado con éxito. Por favor inicie sesión";
                        alert.value.class = "span-success";

                        form.value.email = "";
                        form.value.firstname = "";
                        form.value.lastname = "";
                        form.value.password1 = "";
                        form.value.password2= "";
                    } else {
                        alert.value.status = "error";
                        alert.value.message = "Se ha producido un error en el registro";
                        alert.value.class = "span-error";
                    }
                })
                .catch(error => {
                    console.log("Error: ", error);
                })
        }
    }
</script>


<template>
    <div class="signup-page">
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
                        <h1 class="title">Registro</h1>
                        <h2 class="subtitle mt-3">Crea usuario para tu cuenta de <span class="secondary-text-color has-text-weight-semibold">Link Jurist</span> y empieza a disfrutar sus beneficios</h2>
                        <div class="field">
                            <label class="label">Nombre</label>
                            <div class="control">
                                <input class="input" :class="{ 'input-error' : error.field === 'firstname' }" type="text" v-model="form.firstname">
                            </div>
                            <span v-if="error.field === 'firstname'" class="has-text-danger"> {{ error.message }}</span>
                        </div>

                        <div class="field">
                            <label class="label">Apellido</label>
                            <div class="control">
                                <input class="input" :class="{ 'input-error' : error.field === 'lastname' }" type="text" v-model="form.lastname">
                                <span v-if="error.field === 'lastname'" class="has-text-danger"> {{ error.message }}</span>
                            </div>
                        </div>

                        <div class="field">
                            <label class="label">Correo electrónico</label>
                            <div class="control">
                                <input class="input" :class="{ 'input-error' : error.field === 'email' }" type="email" v-model="form.email">
                                <span v-if="error.field === 'email'" class="has-text-danger"> {{ error.message }}</span>
                            </div>
                        </div>

                        <div class="field">
                            <label class="label">Contraseña</label>
                            <div class="control">
                                <input class="input" :class="{ 'input-error' : error.field === 'password1' }" type="password" v-model="form.password1">
                                <span v-if="error.field === 'password1'" class="has-text-danger"> {{ error.message }}</span>
                            </div>
                        </div> 
                        <div class="field">
                            <label class="label">Repetir contraseña</label>
                            <div class="control">
                                <input class="input" :class="{ 'input-error' : error.field === 'password2' }" type="password" v-model="form.password2">
                                <span v-if="error.field === 'password2'" class="has-text-danger"> {{ error.message }}</span>
                            </div>
                        </div>
                        <div class="field is-grouped is-grouped-right mt-1">
                            <div class="control">
                                <button class="button is-rounded secondary-form-button">Confirmar</button>
                            </div>
                            <div class="control">
                                <RouterLink to="/" class="button is-rounded main-form-button">Cancelar</RouterLink>
                            </div>
                        </div>
                        <p class="mt-3">Ya tienes cuenta de <span class="secondary-text-color has-text-weight-semibold">Link Jurist</span>? Inicia sesión haciendo click <RouterLink to="login">aquí</RouterLink></p>
                    </form>
                </div>
            </div>
        </section>
    </div>
</template>

