<script setup>
  import { ref } from 'vue';
  import FileCard from '@/components/files/FileCard.vue';
  import { useFilesStore } from '@/stores/files';

  const filesStore = ref(useFilesStore());

  function handleUpdateDownloads(file_id) {
    const index = filesStore.value.files.findIndex(file => file.id === file_id);

    if (index !== -1) {
      const downloads = filesStore.value.files[index].downloads;
      filesStore.value.files[index].downloads = downloads + 1;
    }
  }
</script>


<template>
    <div class="box scrollable-div">
    <h1 class="title">Escritos</h1>
    <h2 class="subtitle">Listado de escritos subidos por usuarios de <span class="secondary-text-color">LinkJurist</span>. </h2>
    <hr>
    <FileCard v-for="file in filesStore.files" :key="file.id" :file="file"  @update-downloads="handleUpdateDownloads" />
  </div>
</template>
