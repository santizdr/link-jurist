<script setup>
  import { ref } from 'vue';
  import { useAuthStore } from '@/stores/auth';
  import { useIndexStore } from '@/stores/index';

  import WelcomePanel from '@/components/home/WelcomePanel.vue';
  import CreatePost from '@/components/home/posts/CreatePost.vue';
  import PostsList from '@/components/home/posts/PostsList.vue';
  import StatsPanel from '@/components/home/StatsPanel.vue';
  import OtherAccounts from '@/components/home/OtherAccounts.vue';

  const authStore = useAuthStore();
  const indexStore = useIndexStore();

</script>


<template>
  <section class="section mt-6">
    <div class="columns is-centered">
      <!-- CARTEL DE BIENVENIDA -->
      <div v-if="authStore.user.isAuthenticated" class="column is-one-fifth-desktop">
        <StatsPanel :stats="indexStore.stats"/>
      </div>
      <div v-if="authStore.user.isAuthenticated" class="column is-two-fifths-desktop">
        <CreatePost />
        <PostsList />
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