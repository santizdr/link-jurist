<script setup>
    import axios from 'axios';
    import { ref } from 'vue'
    import { useAuthStore } from '@/stores/auth';
    import TagsInput from '@/components/home/TagsInput.vue'

    const emit = defineEmits(['closeUserModal'])
    const { props } = defineProps(['showUserModal']);

    const authStore = useAuthStore();
    const account_id = authStore.account.id;

    const resetKey = ref(0);

    const alert = ref({
        message: "",
        class: "",
    });

    const error = ref({
        field: "",
        message: "",
    });

    const form = ref({
        account: account_id,
        email: "",
        firstname: "",
        lastname: "",
        password1: "",
        password2: "",
        tags: [],
    });

    function handleSelectTag(id) {
        const index = form.value.tags.indexOf(id);
        if (index === -1) {
            form.value.tags.push(id);
        } else {
            form.value.tags.splice(index, 1);
        }
    }
    
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
            axios.post("/api/adduser/", form)
                .then(response => {
                    if(response.data.message === "success") {
                        this.authStore.setTeamInfo(response.data.team);
                        handleCloseModal();
                    } else {
                        alert.value.message = "Se ha producido un error al añadir el usuario";
                        alert.value.class = "span-error";
                    }
                })
                .catch(error => {
                    console.log("Error: ", error);
                })
        }
    }

    function handleCloseModal() {
        form.value.email = "";
        form.value.firstname = "";
        form.value.lastname = "";
        form.value.password1 = "";
        form.value.password2 = "";
        form.value.tags = [];
        
        resetKey.value += 1;
        emit('closeUserModal');
    }
</script>

<template>
<div class="modal" :class="{'is-active' : showUserModal }">
  <div class="modal-background"></div>
    <div class="modal-card" style="width: 720px;">
        <form @submit.prevent="submitForm()">    
            <header class="modal-card-head">
                <p class="modal-card-title">Añadir usuario</p>
                <a @click="handleCloseModal()" class="delete" aria-label="close"></a>
            </header>
            <section class="modal-card-body">
                <div v-if="alert.message !== ''" class="my-3">
                    <article class="message">
                        <div class="message-header"  :class="alert.class">
                            <p>{{ alert.message }}</p>
                            <button class="delete" aria-label="delete"></button>
                        </div>
                    </article>  
                </div>          
                <h2 class="subtitle mt-3">Añade un usuario a tu cuenta de <span class="secondary-text-color has-text-weight-semibold">Link Jurist</span></h2>
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
                <TagsInput :key="resetKey" @handle-select-tag="handleSelectTag"/>
            </section>
            <footer class="modal-card-foot">
                <div class="control">
                    <button @click.prevent="submitForm()" class="button is-rounded secondary-form-button">Confirmar</button>
                </div> 
            </footer>
        </form>

    </div>
  <button @click="handleCloseModal()" class="modal-close is-large" aria-label="close"></button>
</div>
</template>