<script setup>
    import { ref } from 'vue'
    import { useAuthStore } from '@/stores/auth';
    import axios from 'axios';

    const emit = defineEmits(['closeApplicationModal'])
    const props = defineProps(['showApplicationModal', 'applicationData']);
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
        account: account_id,
        id: props.applicationData.id,
        applicant: props.applicationData.applicant,
        status: '',
    });

    function closeAlert() {
        alert.value.message = "";
        alert.value.class = "";
    }

    function submitForm() {
        error.value = {
            field: "",
            message: "",
        }

        if (form.value.status === "") {
            error.value.field = "status";
            error.value.message = "Elige una opción ";
        }

        if (error.value.field === '' && error.value.message === '') {
            axios.post("/api/assigncase/", form)
            .then(response => {
                if(response.data.message === "success") {
                        form.value.status = "PENDING";

                        this.authStore.setApplicationsInfo(response.data.applications);
                        emit('closeApplicationModal');
                    } else {
                        alert.value.message = "Se ha producido un error al asignar el caso";
                        alert.value.class = "span-error";
                    }            })
            .catch(error => {
                console.log("Error: ", error);
                alert.value.message = "Se ha producido un error al asignar el caso";
                alert.value.class = "span-error";
            })
        }        
    }

    function handleCloseModal() {
        form.value.status = "";
        emit('closeApplicationModal');
    }

    function handleChangeSelect() {
        error.value.field = "";
        error.value.message = "";
    }

</script>

<template>
    <div class="modal" :class="{'is-active' : showApplicationModal }">
      <div class="modal-background"></div>
        <div class="modal-card">
            <form class="mx-3" @submit.prevent="submitForm()">
                <header class="modal-card-head">
                    <p class="modal-card-title">Asignar una solicitud</p>
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
                    <p class="title is-4 my-5">{{ applicationData.case_title }}</p>           
                    <p class="subtitle is-5 my-5">¿Quieres modificar el estado de la solicitud de <span class="secondary-text-color">{{ applicationData.applied_by }} </span> a tu caso?</p> 

                    <div class="field">
                        <label class="label">Estado</label>
                        <div class="select is-fullwidth">
                            <select @change="handleChangeSelect()" :class="{ 'input-error' : error.field === 'status' }" v-model="form.status">
                                <option value="">Nada seleccionado</option>
                                <option value="ACCEPTED">Aceptada</option>
                                <option value="DENIED">Rechazada</option>
                            </select>
                        </div>
                        <span v-if="error.field === 'status'" class="has-text-danger"> {{ error.message }}</span>
                    </div>
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