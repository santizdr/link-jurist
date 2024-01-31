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
          <h1 class="title is-2">Bienvenido a <span class="secondary-text-color">Link Jurist</span></h1>
          <h2 class="subtitle mt-3 mb-1">En <span class="secondary-text-color">Link Jurist</span> podrás acceder a una red de profesionales y publicaciones de ámbito jurídico y establecer contacto con ellos.</h2>
          <h2 class="subtitle mb-1">Podrás acceder a un portal de anuncios en el que los usuarios pueden ofrecer y solicitar servicios jurídicos específicos a cambio de una comisión. </h2>
          <h2 class="subtitle mb-1">Ademas, dispondrás de un mercado de modelos de escritos jurídicos redactados por otros profesionales. Podrás adquirir los escritos de otros usuarios de la plataforma para tu uso propio. </h2>
          <h2 class="subtitle mb-1">Únete a Link Jurist haciendo click <RouterLink to="/signup" class="secondary-text-color">aquí</RouterLink></h2>
        </div>
      </div>
      <!-- LISTADO DE PUBLICACIONES -->

    </div>
  </section>
</template>

<style>

</style>