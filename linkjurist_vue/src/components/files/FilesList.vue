<script setup>
  import FileCard from '@/components/files/FileCard.vue'
  import { useFilesStore } from '@/stores/files';

  const filesStore = useFilesStore();
</script>


<template>
    <div class="box scrollable-div">
    <h1 class="title">Escritos</h1>
    <h2 class="subtitle">Listado de escritos subidos por usuarios de <span class="secondary-text-color">LinkJurist</span>. </h2>
    <hr>
    <FileCard v-for="file in filesStore.files" :key="file.id" :file="file" />
  </div>
</template>
