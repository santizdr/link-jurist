<script setup>
    import { ref } from 'vue'
    import axios from 'axios';

    import { useAuthStore } from '@/stores/auth';
    import { useRouter } from 'vue-router'

    const router = useRouter();
    const props = defineProps(['account'])
    const emit = defineEmits(['updateReviews']);
    const authStore = useAuthStore();
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
        account: router.currentRoute.value.params['id'],
        posted_by: user,
        rating: '',
    });

    function closeAlert() {
        alert.value.message = "";
        alert.value.class = "";
    }

    function setRating(rating) {
        form.value.rating = rating;
    }

    function submitForm() {
        error.value = {
            field: "",
            message: "",
        }

        if (form.value.rating === "") {
            error.value.field = "rating";
            error.value.message = "Selecciona una puntuación";
        } 

        if (error.value.field === '' && error.value.message === '') {
            axios.post("/api/review", form)
                .then(response => {
                    if(response.data.message === "success") {
                        form.value.rating = "";
                        
                        alert.value.message = "Valoración creada correctamente";
                        alert.value.class = "span-success";
                    } else {
                        alert.value.message = "Se ha producido un error publicar la valoración";
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
    <form action="">
        <div v-if="alert.message !== ''" class="my-3">
            <article class="message">
                <div class="message-header"  :class="alert.class">
                    <p>{{ alert.message }}</p>
                    <a @click="closeAlert()" class="delete" aria-label="delete"></a>
                </div>
            </article>  
        </div>    
        <h1 class="is-size-5 has-text-weight-semibold my-3">Añade una valoración</h1>
        <div class="columns">
            <div class="column mt-3 mb-2 ">
                <span @click="setRating(1)"><font-awesome-icon :icon="[form.rating >= 1 ? 'fas' : 'far', 'star']" class="review-icon mr-2" /></span>
                <span @click="setRating(2)"><font-awesome-icon :icon="[form.rating >= 2 ? 'fas' : 'far', 'star']" class="review-icon mr-2" /></span>
                <span @click="setRating(3)"><font-awesome-icon :icon="[form.rating >= 3 ? 'fas' : 'far', 'star']" class="review-icon mr-2" /></span>
                <span @click="setRating(4)"><font-awesome-icon :icon="[form.rating >= 4 ? 'fas' : 'far', 'star']" class="review-icon mr-2" /></span>
                <span @click="setRating(5)"><font-awesome-icon :icon="[form.rating >= 5 ? 'fas' : 'far', 'star']" class="review-icon mr-2" /></span>
                <div class="mt-3">
                    <span v-if="error.field === 'rating'" class="default-font-size has-text-danger has-text-weight-medium"> {{ error.message }}</span>
                </div>
            </div>

            <div class="column field is-grouped is-grouped-right">
                <div class="control">
                    <button @click.prevent="submitForm()" class="button secondary-form-button" style="width: 150px;">Publicar</button>
                </div>
            </div>
        </div>
    </form>
</template>