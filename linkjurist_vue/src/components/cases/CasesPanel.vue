<script setup>
    import { useAuthStore } from '@/stores/auth';

    import CasesFilter from '@/components/cases/CasesFilter.vue'
    import CasesList from '@/components/cases/CasesList.vue'
    import CasesRanking from '@/components/cases/CasesRanking.vue'

    const authStore = useAuthStore();
</script>


<template>
  <section class="section mt-6">
    <div v-if="authStore.user.isAuthenticated" class="columns is-centered">
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