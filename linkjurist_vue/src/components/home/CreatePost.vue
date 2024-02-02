<script setup>
    import { useAuthStore } from '@/stores/auth';
    import { ref } from 'vue'
    import axios from 'axios';

    const authStore = useAuthStore();
    const account = authStore.account.id;
    const user = authStore.user.id;

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
    });

    function submitForm() {
        error.value = {
            field: "",
            message: "",
        }

        if (form.value.content === "") {
            error.value.field = "content";
            error.value.message = "Introduce contenido a la publicación";
        } 
        console.log(form.value);

        if (error.value.field === '' && error.value.message === '') {
            axios.post("/api/createpost", form)
                .then(response => {
                    if(response.data.message === "success") {
                            form.value.content = "";

                            alert.value.message = "Publicación creada correctamente";
                            alert.value.class = "span-success";
                        } else {
                            alert.value.message = "Se ha producido un error crear la publicación";
                            alert.value.class = "span-error";
                        }            })
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
                    <button class="delete" aria-label="delete"></button>
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
        <div class="field is-grouped is-grouped-right">
                <div class="control">
                    <button @click.prevent="submitForm()" class="button is-rounded secondary-form-button" style="width: 150px;">Crear</button>
                </div>
            </div>
    </form>
</template>