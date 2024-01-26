<script setup>
  import { useUserStore } from '@/stores/user';
  import PublicationsList from './PublicationsList.vue';
  import StatsPanel from './StatsPanel.vue';

  const store = useUserStore();
</script>


<template>
  <section class="section mt-6">
    <div class="columns is-centered">
      <!-- CARTEL DE BIENVENIDA -->
      <div v-if="store.user.isAuthenticated" class="column is-one-fifth-desktop">
        <StatsPanel />
      </div>
      <div v-if="store.user.isAuthenticated" class="column is-two-fifths-desktop">
        <PublicationsList />
      </div>
      <div v-if="store.user.isAuthenticated" class="column is-one-fifth-desktop"></div>

      <div v-else class="column is-three-fifths-desktop">
        <div class="box">
          <h1 class="title">Bienvenido a <span class="secondary-text-color">Link Jurist</span></h1>
          <h2 class="subtitle mt-3">Lorem ipsum dolor sit am et consectetur, adipisicing elit. Quae soluta dolor maxime adipisci at quos quis quas corrupti voluptatum? Maxime nesciunt quos natus est eligendi quia repellat distinctio odit accusamus!</h2>
          <h2 class="subtitle mt-3">Lorem ipsum dolor sit amet consectetur, adipisicing elit. Quae soluta dolor maxime adipisci at quos quis quas corrupti voluptatum? Maxime nesciunt quos natus est eligendi quia repellat distinctio odit accusamus!</h2>

        </div>
      </div>
      <!-- LISTADO DE PUBLICACIONES -->

    </div>
  </section>
</template>

<style>

</style>