<script setup>
    import axios from 'axios';
    import { ref } from 'vue'
    import { useAuthStore } from '@/stores/auth';

    const emit = defineEmits(['closeEditPostModal'])
    const props = defineProps(['editPostModal', 'post']);

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
        id: props.post.id,
        content: props.post.content,
        tags: props.post.tags,
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

        console.log("LLEGA");
        if (error.value.field === '' && error.value.message === '') {
            axios.post("/api/editpost/", form)
                .then(response => {
                    if(response.data.message === "success") {
                        this.authStore.setPostsInfo(response.data.posts);

                        form.value.content = response.data.post.content;
                        form.value.tags = response.data.post.tags;

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
        emit('closeEditPostModal');
    }
</script>

<template>
<div class="modal" :class="{'is-active' : editPostModal }">
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
                <h2 class="subtitle mt-3">Añade un usuario a tu cuenta de <span class="secondary-text-color has-text-weight-semibold">Link Jurist</span></h2>
                <div class="field">
                    <div class="control">
                        <textarea class="textarea" :class="{ 'input-error' : error.field === 'content' }" v-model="form.content"></textarea>
                    </div>
                    <span v-if="error.field === 'content'" class="has-text-danger"> {{ error.message }}</span>
                </div>
                <hr>
                Añade especialidades
                <div class="my-1">
                    <a @click="selectTag(1)" class="mr-3 mb-2 button tag-1 black-text" :class="{ 'has-text-weight-semibold selected-tag' : props.post.tags.includes(1) }">Derecho penal</a>
                    <a @click="selectTag(2)" class="mr-3 mb-2 button tag-2 black-text" :class="{ 'has-text-weight-semibold selected-tag' : props.post.tags.includes(2) }">Derecho civil</a>
                    <a @click="selectTag(3)" class="mr-3 mb-2 button tag-3 black-text" :class="{ 'has-text-weight-semibold selected-tag' : props.post.tags.includes(3) }">Derecho laboral</a>
                    <a @click="selectTag(4)" class="mr-3 mb-2 button tag-4 black-text" :class="{ 'has-text-weight-semibold selected-tag' : props.post.tags.includes(4) }">Derecho mercantil</a>
                    <a @click="selectTag(5)" class="mr-3 mb-2 button tag-5 black-text" :class="{ 'has-text-weight-semibold selected-tag' : props.post.tags.includes(5) }">Derecho administrativo</a>
                    <a @click="selectTag(6)" class="mr-3 mb-2 button tag-6 black-text" :class="{ 'has-text-weight-semibold selected-tag' : props.post.tags.includes(6) }">Derecho internacional</a>
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