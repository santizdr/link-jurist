<script setup>
    import CaseCard from '@/components/cases/CaseCard.vue'
    import { useCasesStore } from '@/stores/cases';

    const casesStore = useCasesStore();
</script>


<template>
    <div class="box scrollable-div">
      <h1 class="title">Casos abiertos</h1>
      <h2 class="subtitle">Listado de oferta y demanda de servicios para todos los casos publicados por los usuarios en la plataforma. </h2>
      <hr>
      <CaseCard v-for="caso in casesStore.cases" :key="caso.id" :caso="caso" />
    </div>
</template>
