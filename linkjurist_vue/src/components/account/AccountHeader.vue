<script setup>
    import { useAuthStore } from '@/stores/auth';
    const store = useAuthStore();

    const { props } = defineProps(['account']);

</script>

<template>
    <div class="columns">
        <div class="column is-one-fifth">
            <figure class="image is-256x256">
            <img :src="account.accImg" alt="Placeholder image">
            </figure>
        </div>
        <div class="column is-four-fifth">
            <h1 class="title is-1">{{ account.name }}</h1>
            <h2 class="subtitle">{{ account.slogan }}</h2>
            <a id="signup_btn" class="button is-rounded secondary-bg-color has-text-weight-semibold white-text is-responsive navbar-button" style="width: 150px;">
                <font-awesome-icon :icon="['fas', 'plus']" class="top-ranking-icon mr-2" />Seguir
            </a>
        </div>
    </div>

</template>