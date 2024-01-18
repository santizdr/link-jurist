<script setup>
  import { useAuthStore } from '@/stores/auth';
  import PublicationsList from './PublicationsList.vue';
  const store = useAuthStore();
</script>


<template>
  <section class="section mt-6">
    <div class="columns is-centered">
      <!-- CARTEL DE BIENVENIDA -->
      <div v-if="!store.authenticated" class="column is-three-fifths-desktop">
        <div class="box">
          <h1 class="title">Bienvenido a <span class="secondary-text-color">Link Jurist</span></h1>
          <h2 class="subtitle mt-3">Lorem ipsum dolor sit am et consectetur, adipisicing elit. Quae soluta dolor maxime adipisci at quos quis quas corrupti voluptatum? Maxime nesciunt quos natus est eligendi quia repellat distinctio odit accusamus!</h2>
          <h2 class="subtitle mt-3">Lorem ipsum dolor sit amet consectetur, adipisicing elit. Quae soluta dolor maxime adipisci at quos quis quas corrupti voluptatum? Maxime nesciunt quos natus est eligendi quia repellat distinctio odit accusamus!</h2>

        </div>
      </div>
      <!-- LISTADO DE PUBLICACIONES -->
      <div v-else class="column is-two-fifths-desktop">
        <PublicationsList />
      </div>
    </div>
  </section>
</template>

<style>

</style>