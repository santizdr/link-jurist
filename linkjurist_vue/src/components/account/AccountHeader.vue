<script setup>
    import { ref } from 'vue'
    import axios from 'axios'
    import { useAuthStore } from '@/stores/auth';
    import { useDetailsStore } from '@/stores/details';

    const authStore = useAuthStore();
    const detailsStore = useDetailsStore();

    const { props } = defineProps(['account']);
    
    const alert = ref({
        message: "",
        class: "",
    });

    function closeAlert() {
        alert.value.message = "";
        alert.value.class = "";
    }

    function follow() {
        const data = {
            'follower': authStore.account.id,
            'following': detailsStore.account.id,
        };
        axios.post("/api/follow", data)
            .then(response => {
                if(response.data.message === "followed") {
                    detailsStore.setFollow();
                    alert.value.message = "Has seguido a " + detailsStore.account.name;
                    alert.value.class = "span-success";
                } else if (response.data.message === "unfollowed") {
                    detailsStore.setFollow();
                    alert.value.message = "Has dejado de seguir a " + detailsStore.account.name;
                    alert.value.class = "span-success";
                } else {
                    alert.value.message = "Se ha producido un error";
                    alert.value.class = "span-error";
                }
            })
            .catch(error => {
                console.log("Error: ", error);
            })
        
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
            <h1 class="title is-1">{{ account.name }}</h1>
            <h2 class="subtitle">{{ account.slogan }}</h2>
            <div v-if="authStore.account.id !== account.id">
                <a v-if="!detailsStore.follow" @click.prevent="follow()" class="button is-rounded secondary-bg-color has-text-weight-semibold white-text is-responsive navbar-button" style="width: 150px;">
                    <font-awesome-icon :icon="['fas', 'plus']" class="top-ranking-icon mr-2" />Seguir
                </a>
                <a v-else @click.prevent="follow()" class="button is-rounded main-bg-color has-text-weight-semibold white-text is-responsive navbar-button" style="width: 150px;">
                    <font-awesome-icon :icon="['fas', 'minus']" class="top-ranking-icon mr-2" />Dejar de seguir
                </a>
            </div>

        </div>
    </div>

</template>