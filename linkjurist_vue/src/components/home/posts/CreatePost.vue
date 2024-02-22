<script setup>
    import { ref } from 'vue'
    import axios from 'axios';

    import { useAuthStore } from '@/stores/auth';
    import { useIndexStore } from '@/stores/index';
    import { useRouter } from 'vue-router'

    import TagsInput from '@/components/home/TagsInput.vue'

    const router = useRouter();

    const authStore = useAuthStore();
    const indexStore = useIndexStore();

    const account = authStore.account.id;
    const user = authStore.user.id;
    
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
        account: account,
        posted_by: user,
        content: '',
        tags: []
    });

    function handleSelectTag(id) {
        const index = form.value.tags.indexOf(id);
        if (index === -1) {
            form.value.tags.push(id);
        } else {
            form.value.tags.splice(index, 1);
        }
    }

    function closeAlert() {
        alert.value.message = "";
        alert.value.class = "";
    }

    function submitForm() {
        error.value = {
            field: "",
            message: "",
        }

        if (form.value.content === "") {
            error.value.field = "content";
            error.value.message = "Introduce contenido a la publicación";
        } 

        if (error.value.field === '' && error.value.message === '') {
            axios.post("/api/createpost", form)
                .then(response => {
                    if(response.data.message === "success") {
                        form.value.content = "";
                        form.value.tags = [];
                        
                        alert.value.message = "Publicación creada correctamente";
                        alert.value.class = "span-success";
                        resetKey.value += 1;

                        this.authStore.setPostsInfo(response.data.posts);
                        if (router.currentRoute.value.fullPath === "/"){
                            this.indexStore.fetchIndexData(this.authStore.account.id);
                        }
                    } else {
                        alert.value.message = "Se ha producido un error crear la publicación";
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
    <form action="" class="box">
        <div v-if="alert.message !== ''" class="my-3">
            <article class="message">
                <div class="message-header"  :class="alert.class">
                    <p>{{ alert.message }}</p>
                    <a @click="closeAlert()" class="delete" aria-label="delete"></a>
                </div>
            </article>  
        </div>    
        <h1 class="is-size-5 has-text-weight-semibold">Crear una publicación</h1>
        <hr>
        <div class="field">
            <div class="control">
                <textarea class="textarea" :class="{ 'input-error' : error.field === 'content' }" v-model="form.content"></textarea>
            </div>
            <span v-if="error.field === 'content'" class="has-text-danger"> {{ error.message }}</span>
        </div>
        <TagsInput :key="resetKey" @handle-select-tag="handleSelectTag"/>
        <div class="field is-grouped is-grouped-right">
            <div class="control">
                <button @click.prevent="submitForm()" class="button secondary-form-button" style="width: 150px;">Crear</button>
            </div>
        </div>
    </form>
</template>