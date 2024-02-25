<script setup>
    import { ref } from 'vue'
    import { useAuthStore } from '@/stores/auth';
    import { useDetailsStore } from '@/stores/details';

    const authStore = useAuthStore();
    const detailsStore = useDetailsStore();

    const { props } = defineProps(['user']);
    
    const alert = ref({
        message: "",
        class: "",
    });

    function closeAlert() {
        alert.value.message = "";
        alert.value.class = "";
    }
</script>

<template>
    <div class="columns">
        <div class="column is-one-fifth">
            <figure class="image is-256x256">
            <img src="https://bulma.io/images/placeholders/256x256.png" alt="Placeholder image">
            </figure>
        </div>
        <div class="column is-four-fifth">
            <div v-if="alert.message !== ''" class="my-3">
                <article class="message">
                    <div class="message-header"  :class="alert.class">
                        <p>{{ alert.message }}</p>
                        <a @click="closeAlert()" class="delete" aria-label="delete"></a>
                    </div>
                </article>  
            </div> 
            <h1 class="title is-1">{{ user.firstname }} {{ user.lastname }}</h1>
            <h2 class="subtitle">
                <RouterLink :to="'/account/' + user.account" class="secondary-text-color has-text-weight-semibold">{{ user.account_name }}</RouterLink>
            </h2>
            <hr>
        </div>
    </div>
</template>