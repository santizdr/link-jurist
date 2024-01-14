<script setup>
    import CasesFilter from '../cases/CasesFilter.vue'
    import CasesList from '../cases/CasesList.vue'
    import CasesRanking from '../cases/CasesRanking.vue'

    import { useAuthStore } from '@/stores/auth';
    const store = useAuthStore();
</script>


<template>
  <section class="section mt-6">
    <div v-if="store.authenticated" class="columns is-centered">
        <div class="column is-three-quarters-desktop">
          <div class="columns">
            <div class="column">
              <CasesFilter />
            </div>
          </div>
          <div class="columns">
            <div class="column is-one-quarter">
              <CasesRanking />
            </div>
            <div class="column is-three-quarters">
              <CasesList />
            </div>
          </div>
        </div>
    </div>
  </section>
</template>

<style>

</style>