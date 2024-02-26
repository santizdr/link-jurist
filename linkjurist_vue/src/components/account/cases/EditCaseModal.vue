<script setup>
    import axios from 'axios';
    import { ref } from 'vue'
    import { useAuthStore } from '@/stores/auth';

    const emit = defineEmits(['closeEditCaseModal'])
    const props = defineProps(['editCaseModal', 'caso']);

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
        id: props.caso.id,
        title: props.caso.title,
        description: props.caso.description,
        type: props.caso.type,
        expiryDate: props.caso.expiry_date,
        percent: props.caso.percent,
        tags: props.caso.tags,
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

        if(form.value.content === "") {
            error.value.field = "content";
            error.value.message = "El contenido de la publicación no puede estar vacío";
        } 

        if (error.value.field === '' && error.value.message === '') {
            axios.post("/api/editcase/", form)
                .then(response => {
                    if(response.data.message === "success") {
                        this.authStore.setCasesInfo(response.data.cases);
                        form.value.title = response.data.case.title;
                        form.value.description = response.data.case.description;
                        form.value.type = response.data.case.type;
                        form.value.expiryDate = response.data.case.expiry_date;
                        form.value.percent = response.data.case.percent;

                        form.value.tags = response.data.case.tags;

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

    function handleChangeSelect() {
        error.value.field = "";
        error.value.message = "";
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
        emit('closeEditCaseModal');
    }
</script>

<template>
<div class="modal" :class="{'is-active' : editCaseModal }">
  <div class="modal-background"></div>
    <div class="modal-card" style="width: 720px;">
        <form @submit.prevent="submitForm()">    
            <header class="modal-card-head">
                <p class="modal-card-title">Editar publicación</p>
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
                        <textarea class="textarea" :class="{ 'input-error' : error.field === 'description' }" v-model="form.description"></textarea>
                    </div>
                    <span v-if="error.field === 'description'" class="has-text-danger"> {{ error.message }}</span>
                </div>
                <div class="field">
                    <label class="label">Tipo</label>
                    <div class="select is-fullwidth">
                        <select @change="handleChangeSelect()" :class="{ 'input-error' : error.field === 'type' }" v-model="form.type">
                            <option value="">Nada seleccionado</option>
                            <option value="OFFER">Oferta</option>
                            <option value="DEMAND">Demanda</option>
                        </select>
                    </div>
                    <span v-if="error.field === 'type'" class="has-text-danger"> {{ error.message }}</span>
                </div>
                <div class="field">
                    <label class="label">Fecha de expiración</label>
                    <div class="control">
                        <input class="input is-fullwidth" :class="{ 'input-error' : error.field === 'expiryDate' }" type="date" v-model="form.expiryDate">
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
                <hr>
                Añade especialidades
                <div class="my-1">
                    <a @click="selectTag(1)" class="mr-3 mb-2 button tag-1 black-text" :class="{ 'has-text-weight-semibold selected-tag' : props.caso.tags.includes(1) }">Derecho penal</a>
                    <a @click="selectTag(2)" class="mr-3 mb-2 button tag-2 black-text" :class="{ 'has-text-weight-semibold selected-tag' : props.caso.tags.includes(2) }">Derecho civil</a>
                    <a @click="selectTag(3)" class="mr-3 mb-2 button tag-3 black-text" :class="{ 'has-text-weight-semibold selected-tag' : props.caso.tags.includes(3) }">Derecho laboral</a>
                    <a @click="selectTag(4)" class="mr-3 mb-2 button tag-4 black-text" :class="{ 'has-text-weight-semibold selected-tag' : props.caso.tags.includes(4) }">Derecho mercantil</a>
                    <a @click="selectTag(5)" class="mr-3 mb-2 button tag-5 black-text" :class="{ 'has-text-weight-semibold selected-tag' : props.caso.tags.includes(5) }">Derecho administrativo</a>
                    <a @click="selectTag(6)" class="mr-3 mb-2 button tag-6 black-text" :class="{ 'has-text-weight-semibold selected-tag' : props.caso.tags.includes(6) }">Derecho internacional</a>
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