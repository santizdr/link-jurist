<script setup>
import { ref } from 'vue'
import { useUserStore } from '@/stores/user';
import axios from 'axios';

const emit = defineEmits(['closeCaseModal'])
const { props } = defineProps(['showCaseModal']);

const store = useUserStore();

function handleCloseModal() {
    form.value.title = "";
    form.value.description = "";
    form.value.type = "";
    form.value.expiryDate = "";
    form.value.percent = "";

    emit('closeCaseModal');
}

const account_id = store.account.id;

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
    title: '',
    description: '',
    type: '',
    expiryDate: '',
    percent: "",
});

function submitForm() {
    error.value = {
        field: "",
        message: "",
    }

    if (form.value.title === "") {
        error.value.field = "title";
        error.value.message = "El campo título no puede estar vacío";
    } else if (form.value.description === "") {
        error.value.field = "description";
        error.value.message = "El campo descripción no puede estar vacío";
    } else if (form.value.type === '') {
        error.value.field = "type";
        error.value.message = "Selecciona un tipo para la publicación";
    }else if (form.value.expiryDate === '') {
        error.value.field = "expiryDate";
        error.value.message = "El campo fecha de expiración no puede estar vacío";
    } else if (form.value.percent === '') {
        error.value.field = "percent";
        error.value.message = "El campo comisión no puede estar vacío";
    }

    if (error.value.field === '' && error.value.message === '') {
        console.log("Todo bien");
        console.log(form.value);
    }

    axios.post("/api/postcase/", form)
            .then(response => {
                if(response.data.message === "success") {
                        form.value.title = "";
                        form.value.description = "";
                        form.value.type = "";
                        form.value.date = "";
                        form.value.percent= "";

                        this.store.setCasesInfo(response.data.cases);
                        emit('closeCaseModal');
                    } else {
                        alert.value.status = "error";
                        alert.value.message = "Se ha producido un error al publicar el caso";
                        alert.value.class = "span-error";
                    }            })
            .catch(error => {
                console.log("Error: ", error);
            })
}

</script>

<template>
    <div class="modal" :class="{'is-active' : showCaseModal }">
      <div class="modal-background"></div>
        <div class="modal-card">
            <form class="mx-3" @submit.prevent="submitForm()">
                <header class="modal-card-head">
                    <p class="modal-card-title">Publicar un caso</p>
                    <a @click="handleCloseModal()" class="delete" aria-label="close"></a>
                </header>
                <section class="modal-card-body">    
                    <div class="field">
                        <label class="label">Título</label>
                        <div class="control">
                            <input class="input" :class="{ 'input-error' : error.field === 'title' }" type="text" v-model="form.title">
                        </div>
                        <span v-if="error.field === 'title'" class="has-text-danger"> {{ error.message }}</span>
                    </div>
                    <div class="field">
                        <label class="label">Descripción</label>
                        <div class="control">
                            <textarea class="textarea" :class="{ 'input-error' : error.field === 'title' }" v-model="form.description"></textarea>
                        </div>
                        <span v-if="error.field === 'description'" class="has-text-danger"> {{ error.message }}</span>
                    </div>
                    <div class="field">
                        <label class="label">Tipo</label>
                        <div class="select is-fullwidth">
                            <select v-model="form.type">
                                <option value="">Nada seleccionado</option>
                                <option value="OFFER">Oferta</option>
                                <option value="DEMAND">Demanda</option>
                            </select>
                        </div>
                    </div>
                    <div class="field">
                        <label class="label">Fecha de expiración</label>
                        <div class="control">
                            <input class="input" :class="{ 'input-error' : error.field === 'expiryDate' }" type="date" v-model="form.expiryDate">
                        </div>
                        <span v-if="error.field === 'expiryDate'" class="has-text-danger"> {{ error.message }}</span>
                    </div>
                    <div class="field">
                        <label class="label">Comisión</label>
                        <p class="control has-icons-right">
                            <input class="input" :class="{ 'input-error' : error.field === 'percent' }" type="text" v-model="form.percent">
                            <span class="icon is-right">
                                <font-awesome-icon :icon="['fas', 'percent']" class="tabs-icon mr-2" />
                            </span>
                            <span v-if="error.field === 'percent'" class="has-text-danger"> {{ error.message }}</span>
                        </p>
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