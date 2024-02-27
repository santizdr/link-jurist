<script setup>
    import { ref } from 'vue'
    import axios from 'axios';
    import { useAuthStore } from '@/stores/auth';

    const authStore = useAuthStore();

    const emit = defineEmits(['closeEditAccountModal'])
    const props = defineProps(['account', 'editAccountModal']);

    function handleCloseModal() {
        emit('closeEditAccountModal');
    }

    const error = ref({
        field: "",
        message: "",
    });

    const form = ref({
        name: props.account.name,
        description: props.account.description,
        slogan: props.account.slogan,
        phonenumber: props.account.phonenumber,
        web: props.account.web,
        email: props.account.email,
        address: props.account.address,
        cp: props.account.cp,
        locality: props.account.locality,
        country: props.account.country,
        account: authStore.account.id,
    });

    async function submitForm() {
        error.value = {
            field: "",
            message: "",
        };

        if (form.value.name === "") {
            error.value.field = "name";
            error.value.message = "El campo título no puede estar vacío";
        } else if (form.value.description === "") {
            error.value.field = "description";
            error.value.message = "El campo descripción no puede estar vacío";
        } else if (form.value.phonenumber === "") {
            error.value.field = "phonenumber";
            error.value.message = "El campo teléfono no puede estar vacío";
        } else if (form.value.web === "") {
            error.value.field = "web";
            error.value.message = "El campo web no puede estar vacío";
        } else if (form.value.email === "") {
            error.value.field = "email";
            error.value.message = "El campo email no puede estar vacío";
        } else if (form.value.address === "") {
            error.value.field = "address";
            error.value.message = "El campo email no puede estar vacío";
        } else if (form.value.cp === "") {
            error.value.field = "cp";
            error.value.message = "El campo código postal no puede estar vacío";
        } else if (form.value.locality === "") {
            error.value.field = "locality";
            error.value.message = "El campo provincia no puede estar vacío";
        } else if (form.value.country === "") {
            error.value.field = "country";
            error.value.message = "El campo país no puede estar vacío";
        }

        if (error.value.field === '' && error.value.message === '') {
            await axios.post("/api/editaccount/", form)
                .then(response => {
                    this.authStore.setAccountInfo(response.data.account);

                    handleCloseModal();
                })
                .catch(error => {
                    console.log("Error: ", error);
                })
        }
    }
</script>

<template>
    <div class="modal" :class="{'is-active' : editAccountModal }">
      <div class="modal-background"></div>
      <div class="modal-card" style="width: 1080px;">
            <form class="mx-3" @submit.prevent="submitForm()">
                <header class="modal-card-head">
                    <p class="modal-card-title">Editar cuenta</p>
                </header>
                <section class="modal-card-body scrollable-div">
                    <div class="columns is-centered">
                        <div class="column is-four-fifths-desktop">
                            <div class="field">
                                <label class="label">Nombre</label>
                                <div class="control">
                                    <input class="input" :class="{ 'input-error' : error.field === 'name' }" type="text" v-model="form.name">
                                </div>
                                <span v-if="error.field === 'name'" class="has-text-danger"> {{ error.message }}</span>
                            </div>
                            <div class="field">
                                <label class="label">Descripción</label>
                                <div class="control">
                                    <textarea class="textarea" :class="{ 'input-error' : error.field === 'description' }" v-model="form.description"></textarea>
                                </div>
                                <span v-if="error.field === 'description'" class="has-text-danger"> {{ error.message }}</span>
                            </div>
                            <div class="field">
                                <label class="label">Eslogan</label>
                                <div class="control">
                                    <input class="input" type="text" v-model="form.slogan">
                                </div>
                            </div>
                            <hr>
                            <div class="field">
                                <label class="label">Teléfono</label>
                                <div class="control">
                                    <input class="input" :class="{ 'input-error' : error.field === 'phonenumber' }" type="tel" v-model="form.phonenumber">
                                </div>
                                <span v-if="error.field === 'phonenumber'" class="has-text-danger"> {{ error.message }}</span>
                            </div>
                            <div class="field">
                                <label class="label">Web</label>
                                <div class="control">
                                    <input class="input" :class="{ 'input-error' : error.field === 'web' }" type="text" v-model="form.web">
                                </div>
                                <span v-if="error.field === 'web'" class="has-text-danger"> {{ error.message }}</span>
                            </div>
                            <div class="field">
                                <label class="label">Email</label>
                                <div class="control">
                                    <input class="input" :class="{ 'input-error' : error.field === 'email' }" type="email" v-model="form.email">
                                </div>
                                <span v-if="error.field === 'email'" class="has-text-danger"> {{ error.message }}</span>
                            </div>
                            <hr>
                            <div class="field">
                                <label class="label">Dirección</label>
                                <div class="control">
                                    <input class="input" :class="{ 'input-error' : error.field === 'address' }" type="text" v-model="form.address">
                                </div>
                                <span v-if="error.field === 'address'" class="has-text-danger"> {{ error.message }}</span>
                            </div>
                            <div class="field">
                                <label class="label">Código Postal</label>
                                <div class="control">
                                    <input class="input" :class="{ 'input-error' : error.field === 'cp' }" type="text" v-model="form.cp">
                                </div>
                                <span v-if="error.field === 'cp'" class="has-text-danger"> {{ error.message }}</span>
                            </div>
                            <div class="field">
                                <label class="label">Provincia</label>
                                <div class="control">
                                    <input class="input" :class="{ 'input-error' : error.field === 'locality' }" type="text" v-model="form.locality">
                                </div>
                                <span v-if="error.field === 'locality'" class="has-text-danger"> {{ error.message }}</span>
                            </div>
                            <div class="field">
                                <label class="label">País</label>
                                <div class="control">
                                    <input class="input" :class="{ 'input-error' : error.field === 'country' }" type="text" v-model="form.country">
                                </div>
                                <span v-if="error.field === 'country'" class="has-text-danger"> {{ error.message }}</span>
                            </div>
                        </div>
                    </div>
                </section>
                <footer class="modal-card-foot modal-footer-btns">
                    <div class="field is-grouped is-grouped-right">
                        <div class="control">
                            <a @click="handleCloseModal()" class="button primary-form-button">Cancelar</a>
                        </div>
                        <div class="control">
                            <a @click="submitForm(id)" class="button secondary-form-button">Confirmar</a>
                        </div>
                    </div>
                </footer>
            </form>
        </div>
    </div>
</template>