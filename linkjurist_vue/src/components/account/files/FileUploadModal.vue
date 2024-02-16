<script setup>
    import { ref, watch } from 'vue'
    import { useAuthStore } from '@/stores/auth';
    import axios from 'axios';
    import TagsInput from '@/components/home/TagsInput.vue'

    const emit = defineEmits(['closeFileModal'])
    const props = defineProps(['showFileModal']);
    const authStore = useAuthStore();

    const account_id = authStore.account.id;
    const user_id = authStore.user.id;
    const selectedFileName = ref('');
    const file = ref(null);

    const error = ref({
        field: "",
        message: "",
    });

    const form = ref({
        account: account_id,
        uploaded_by: user_id,
        title: '',
        file: file,
        description: "",
        price: "",
        tags: [],
    });

    const resetKey = ref(0);

    function forceRerender() {
        resetKey.value += 1;
    };

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
        }
        
        if (form.value.file === "" || form.value.file === null) {
            error.value.field = "file";
            error.value.message = "Selecciona un archivo";
        } else if (form.value.title === "") {
            error.value.field = "title";
            error.value.message = "El campo título no puede estar vacío";
        } else if (form.value.price === "") {
            error.value.field = "price";
            error.value.message = "El campo precio no puede estar vacío";
        } else if (!validatePrice(form.value.price)) {
            error.value.field = "price";
            error.value.message = "El precio debe tener dos dígitos decimales y estar separado por un punto";
        }

        if (error.value.field === '' && error.value.message === '') {
            const formData = new FormData();

            // Agrega cada campo de tu formulario a formData
            formData.append('title', form.value.title);
            formData.append('account', form.value.account);
            formData.append('uploaded_by', form.value.uploaded_by);
            formData.append('description', form.value.description);
            formData.append('price', form.value.price);
            formData.append('file', form.value.file);
            formData.append('tags', JSON.stringify(form.value.tags));

            axios.post("/api/uploadfile/", formData)
                .then(response => {

                    if(response.data.message === "success") {
                        this.authStore.setFilesInfo(response.data.files);

                        handleCloseModal();
                        emit('closeFileModal');
                    } else {
                        alert.value.message = "Se ha producido un error subir el escrito";
                        alert.value.class = "span-error";
                    }
                })
                .catch(error => {
                    console.log("Error: ", error);
                })
        }
    }

    function handleCloseModal() {
        form.value.title = "";
        form.value.description = "";
        form.value.price = "";
        form.value.tags = [];
        file.value = null;
        selectedFileName.value = "";
        forceRerender();

        emit('closeFileModal');
    }

    function handleFileChange(event) {
        file.value = event.target.files[0];
        selectedFileName.value = file.value ? file.value.name : '';
    }

    function validatePrice(price) {
        var regex = /^\d{1,3}(\.\d{2})$/;
        return regex.test(price)
    }
</script>

<template>
    <div class="modal" :class="{'is-active' : showFileModal }">
      <div class="modal-background"></div>
        <div class="modal-card" style="width: 720px;">
            <form class="mx-3" enctype="multipart/form-data" @submit.prevent="submitForm()">
                <header class="modal-card-head">
                    <p class="modal-card-title">Subir escrito</p>
                    <a @click="handleCloseModal()" class="delete" aria-label="close"></a>
                </header>
                <section class="modal-card-body">    
                    <div class="field">
                        <label class="label">Selecciona un archivo</label>
                        <div class="file has-name mx-4">
                            <label class="file-label">
                                <input class="file-input" type="file" name="resume" @change="handleFileChange">
                                <span class="file-cta">
                                <span class="file-icon">
                                    <font-awesome-icon :icon="['fas', 'upload']" class="tabs-icon mr-2" />
                                </span>
                                <span class="file-label">
                                    Selecciona un archivo
                                </span>
                                </span>
                                <span v-if="selectedFileName === ''" class="file-name" >
                                    Ningún archivo seleccionado
                                </span>
                                <span v-else class="file-name" >
                                    {{ selectedFileName }}
                                </span>
                            </label>
                        </div>
                        <span v-if="error.field === 'file'" class="has-text-danger"> {{ error.message }}</span>
                    </div>
                    <div class="field">
                        <label class="label">Título</label>
                        <div class="control">
                            <input class="input" :class="{ 'input-error' : error.field === 'title' }" type="text" v-model="form.title">
                            <span v-if="error.field === 'title'" class="has-text-danger"> {{ error.message }}</span>
                        </div>
                    </div>
                    <div class="field">
                        <label class="label">Descripción</label>
                        <div class="control">
                            <textarea class="textarea" v-model="form.description"></textarea>
                        </div>
                    </div>

                    <div class="field">
                        <label class="label">Precio</label>
                        <p class="control has-icons-right">
                            <input class="input" :class="{ 'input-error' : error.field === 'price' }" type="text" v-model="form.price">
                            <span class="icon is-right">
                                <font-awesome-icon :icon="['fas', 'euro-sign']" class="tabs-icon mr-2" />
                            </span>
                            <span v-if="error.field === 'price'" class="has-text-danger"> {{ error.message }}</span>
                        </p>
                    </div>
                    <TagsInput :key="resetKey" :formTags="form.tags" @handle-select-tag="handleSelectTag" />
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