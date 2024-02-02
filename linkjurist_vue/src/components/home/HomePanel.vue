<script setup>
  import { useAuthStore } from '@/stores/auth';
  
  import WelcomePanel from './WelcomePanel.vue';
  import CreatePost from './CreatePost.vue';
  import PublicationsList from './PublicationsList.vue';
  import StatsPanel from './StatsPanel.vue';
  import OtherAccounts from './OtherAccounts.vue';

  const authStore = useAuthStore();
</script>


<template>
  <section class="section mt-6">
    <div class="columns is-centered">
      <!-- CARTEL DE BIENVENIDA -->
      <div v-if="authStore.user.isAuthenticated" class="column is-one-fifth-desktop">
        <StatsPanel />
      </div>
      <div v-if="authStore.user.isAuthenticated" class="column is-two-fifths-desktop">
        <CreatePost />
        <PublicationsList />
      </div>
      <div v-if="authStore.user.isAuthenticated" class="column is-one-fifth-desktop">
        <OtherAccounts />
      </div>

      <div v-else class="column is-three-fifths-desktop">
        <WelcomePanel />
      </div>
      <!-- LISTADO DE PUBLICACIONES -->

    </div>
  </section>
</template>

<style>

</style>