<script setup>
    import axios from 'axios';
    import { ref } from 'vue'
    import { useAuthStore } from '@/stores/auth';
    import { useRouter } from 'vue-router';

    const emit = defineEmits(['closeEditFileModal'])
    const props = defineProps(['editFileModal', 'file']);
    const router = useRouter();

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
        id: props.file.id,
        title: props.file.title,
        description: props.file.description,
        price: props.file.price,
        tags: props.file.tags,
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
            axios.post("/api/editfile/", form)
                .then(response => {
                    if(response.data.message === "success") {
                        this.authStore.setFilesInfo(response.data.files);
                        form.value.title = response.data.file.title;
                        form.value.description = response.data.file.description;
                        form.value.price = response.data.file.price;
                        form.value.tags = response.data.file.tags;

                        router.go();
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
        emit('closeEditFileModal');
    }
</script>

<template>
<div class="modal" :class="{'is-active' : editFileModal }">
  <div class="modal-background"></div>
    <div class="modal-card" style="width: 720px;">
        <form @submit.prevent="submitForm()">    
            <header class="modal-card-head">
                <p class="modal-card-title">Editar escrito</p>
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
                    <label class="label">Precio</label>
                    <p class="control has-icons-right">
                        <input class="input" :class="{ 'input-error' : error.field === 'price' }" type="text" v-model="form.price">
                        <span class="icon is-right">
                            <font-awesome-icon :icon="['fas', 'euro']" class="tabs-icon mr-2" />
                        </span>
                        <span v-if="error.field === 'price'" class="has-text-danger"> {{ error.message }}</span>
                    </p>
                </div>
                <hr>
                Añade especialidades
                <div class="my-1">
                    <a @click="selectTag(1)" class="mr-3 mb-2 button tag-1 black-text" :class="{ 'has-text-weight-semibold selected-tag' : props.file.tags.includes(1) }">Derecho penal</a>
                    <a @click="selectTag(2)" class="mr-3 mb-2 button tag-2 black-text" :class="{ 'has-text-weight-semibold selected-tag' : props.file.tags.includes(2) }">Derecho civil</a>
                    <a @click="selectTag(3)" class="mr-3 mb-2 button tag-3 black-text" :class="{ 'has-text-weight-semibold selected-tag' : props.file.tags.includes(3) }">Derecho laboral</a>
                    <a @click="selectTag(4)" class="mr-3 mb-2 button tag-4 black-text" :class="{ 'has-text-weight-semibold selected-tag' : props.file.tags.includes(4) }">Derecho mercantil</a>
                    <a @click="selectTag(5)" class="mr-3 mb-2 button tag-5 black-text" :class="{ 'has-text-weight-semibold selected-tag' : props.file.tags.includes(5) }">Derecho administrativo</a>
                    <a @click="selectTag(6)" class="mr-3 mb-2 button tag-6 black-text" :class="{ 'has-text-weight-semibold selected-tag' : props.file.tags.includes(6) }">Derecho internacional</a>
                </div>
            </section>
            <footer class="modal-card-foot modal-footer-btns">
                <div class="field is-grouped">
                    <div class="control">
                        <a @click="handleCloseModal()" class="button primary-form-button">Cancelar</a>
                    </div>
                    <div class="control">
                        <a @click="submitForm()" class="button secondary-form-button">Confirmar</a>
                    </div>
                </div>
            </footer>
        </form>
    </div>
</div>
</template>