<script setup>
    import FilesFilter from '../files/FilesFilter.vue'
    import FilesList from '../files/FilesList.vue'
    import FilesRanking from '../files/FilesRanking.vue'

    import { useAuthStore } from '@/stores/auth';
    const store = useAuthStore();
</script>


<template>
  <section class="section mt-6">
    <div v-if="store.authenticated" class="columns is-centered">
        <div class="column is-three-quarters-desktop">
          <div class="columns">
            <div class="column">
              <FilesFilter />
            </div>
          </div>
          <div class="columns">
            <div class="column is-one-quarter">
              <FilesRanking />
            </div>
            <div class="column is-three-quarters">
              <FilesList/>
            </div>
          </div>
        </div>
    </div>
  </section>
</template>

<style>

</style>