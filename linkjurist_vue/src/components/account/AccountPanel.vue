<script setup>
    import { useAuthStore } from '@/stores/auth';
    const store = useAuthStore();
</script>


<template>
    <section class="section mt-4">
    <div v-if="store.authenticated" class="columns is-centered">
    <div class="column is-three-fifths-desktop">
      <div class="box">
        INFORMACION DE MI PERFIL
      </div>
    </div>
  </div>
  </section>
</template>
