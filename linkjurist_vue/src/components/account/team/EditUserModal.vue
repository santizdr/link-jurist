<script setup>
    import axios from 'axios';
    import { ref } from 'vue'
    import { useAuthStore } from '@/stores/auth';

    const emit = defineEmits(['closeEditUserModal'])
    const props = defineProps(['editUserModal', 'user']);

    const authStore = useAuthStore();
    const account_id = authStore.account.id;

    const alert = ref({
        message: "",
        class: "",
    });

    const error = ref({
        field: "",
        message: "",
    });

    const form = ref({
        id: props.user.id,
        account: account_id,
        email: props.user.email,
        firstname: props.user.firstname,
        lastname: props.user.lastname,
        tags: props.user.tags,
    });

    function closeAlert() {
        alert.value.message = "";
        alert.value.class = "";
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
        } 

        if (error.value.field === '' && error.value.message === '') {
            axios.post("/api/user/", form)
                .then(response => {
                    if(response.data.message === "success") {
                        this.authStore.setTeamInfo(response.data.team);
                        form.value.email = response.data.user.email;
                        form.value.firstname = response.data.user.firstname;
                        form.value.lastname = response.data.user.lastname;
                        form.value.tags = response.data.user.tags;

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

    function selectTag(id) {
        const index = form.value.tags.indexOf(id);
        if (index === -1) {
            form.value.tags.push(id);
        } else {
            form.value.tags.splice(index, 1);
        }
    }

    function handleCloseModal() {        
        emit('closeEditUserModal');
    }
</script>

<template>
<div class="modal" :class="{'is-active' : editUserModal }">
  <div class="modal-background"></div>
    <div class="modal-card" style="width: 720px;">
        <form @submit.prevent="submitForm()">    
            <header class="modal-card-head">
                <p class="modal-card-title">Editar usuario</p>
                <a @click="handleCloseModal()" class="delete" aria-label="close"></a>
            </header>
            <section class="modal-card-body">
                <div v-if="alert.message !== ''" class="my-3">
                    <article class="message">
                        <div class="message-header"  :class="alert.class">
                            <p>{{ alert.message }}</p>
                            <a @click="closeAlert()" class="delete" aria-label="delete"></a>
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

                Añade especialidades
                <div class="my-1">
                    <a @click="selectTag(1)" class="mr-3 mb-2 button tag-1 black-text" :class="{ 'has-text-weight-semibold selected-tag' : props.user.tags.includes(1) }">Derecho penal</a>
                    <a @click="selectTag(2)" class="mr-3 mb-2 button tag-2 black-text" :class="{ 'has-text-weight-semibold selected-tag' : props.user.tags.includes(2) }">Derecho civil</a>
                    <a @click="selectTag(3)" class="mr-3 mb-2 button tag-3 black-text" :class="{ 'has-text-weight-semibold selected-tag' : props.user.tags.includes(3) }">Derecho laboral</a>
                    <a @click="selectTag(4)" class="mr-3 mb-2 button tag-4 black-text" :class="{ 'has-text-weight-semibold selected-tag' : props.user.tags.includes(4) }">Derecho mercantil</a>
                    <a @click="selectTag(5)" class="mr-3 mb-2 button tag-5 black-text" :class="{ 'has-text-weight-semibold selected-tag' : props.user.tags.includes(5) }">Derecho administrativo</a>
                    <a @click="selectTag(6)" class="mr-3 mb-2 button tag-6 black-text" :class="{ 'has-text-weight-semibold selected-tag' : props.user.tags.includes(6) }">Derecho internacional</a>
                </div>
            </section>
            <footer class="modal-card-foot">
                <div class="control">
                    <button @click.prevent="submitForm()" class="button secondary-form-button">Confirmar</button>
                </div> 
            </footer>
        </form>

    </div>
  <button @click="handleCloseModal()" class="modal-close is-large" aria-label="close"></button>
</div>
</template>