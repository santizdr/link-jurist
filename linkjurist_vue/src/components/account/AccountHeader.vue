<script setup>
    import { ref } from 'vue'
    import axios from 'axios'
    import { useAuthStore } from '@/stores/auth';
    import { useDetailsStore } from '@/stores/details';
    import EditAccountModal from '@/components/account/EditAccountModal.vue';

    const authStore = useAuthStore();
    const detailsStore = useDetailsStore();

    const { props } = defineProps(['account']);

    const resetKey = ref(0);
    const editAccountModal = ref(false);

    const alert = ref({
        message: "",
        class: "",
    });

    function closeAlert() {
        alert.value.message = "";
        alert.value.class = "";
    }

    function editAccount() {
      editAccountModal.value = true;

      resetKey.value++;
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
            <img :src="account.image" alt="Placeholder image">
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
            <div class="columns">
                <div class="column">
                    <h1 class="title is-1">{{ account.name }}</h1>
                    <h2 class="subtitle">{{ account.slogan }}</h2>
                </div>
                <div v-if="authStore.account.id === account.id" class="column is-narrow">
                    <a v-if="authStore.user.is_manager" @click="editAccount(account.id)" class="button secondary-bg-color has-text-weight-semibold white-text">
                        <span>Editar cuenta <font-awesome-icon :icon="['fas', 'pen']" class="top-ranking-icon mx-1" /></span>
                    </a>
                </div>
            </div>
            <div class="mb-4">
                <span><font-awesome-icon :icon="[account.rating >= 1 ? 'fas' : 'far', 'star']" class="review-icon mr-2" /></span>
                <span><font-awesome-icon :icon="[account.rating >= 2 ? 'fas' : 'far', 'star']" class="review-icon mr-2" /></span>
                <span><font-awesome-icon :icon="[account.rating >= 3 ? 'fas' : 'far', 'star']" class="review-icon mr-2" /></span>
                <span><font-awesome-icon :icon="[account.rating >= 4 ? 'fas' : 'far', 'star']" class="review-icon mr-2" /></span>
                <span><font-awesome-icon :icon="[account.rating >= 5 ? 'fas' : 'far', 'star']" class="review-icon mr-2" /></span>
            </div>
            <div class="my-2" v-if="authStore.account.id !== account.id">
                <a v-if="!detailsStore.follow" @click.prevent="follow()" class="button secondary-bg-color has-text-weight-semibold white-text is-responsive navbar-button" style="width: 150px;">
                    <font-awesome-icon :icon="['fas', 'plus']" class="top-ranking-icon mr-2" />Seguir
                </a>
                <a v-else @click.prevent="follow()" class="button main-bg-color has-text-weight-semibold white-text is-responsive navbar-button" style="width: 150px;">
                    <font-awesome-icon :icon="['fas', 'minus']" class="top-ranking-icon mr-2" />Dejar de seguir
                </a>
            </div>
        </div>
    </div>
    <EditAccountModal :key="resetKey" :editAccountModal="editAccountModal" @close-edit-account-modal="editAccountModal = false" :account="account" />
</template>