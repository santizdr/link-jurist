<script setup>
  import axios from 'axios';
  
  const { props } = defineProps(['file']);

  function openFile(id) {
      axios.get("/api/getfile/", { 
          responseType: 'arraybuffer',
          params: {id: id}
        }
        )
        .then(response => {
            const file = new Blob([response.data], { type: 'application/pdf' });
            const fileURL = URL.createObjectURL(file);
            window.open(fileURL, '_blank');
        })
        .catch(error => {
            console.log("Error: ", error);
        })
  }
</script>

<template>
  <div class="card my-4 mx-4">
    <div class="card-content">
      <div class="media">
        <div class="media-content">            
          <p class="title is-4">{{ file.title }}</p>
          <p class="subtitle is-5 secondary-text-color"></p>
        </div>
      </div>
      <div class="content">
          <p class="default-font-size"><span class="secondary-text-color">Descripción: </span>{{ file.description }}</p>
          <div class="columns is-vcentered">
          <div class="column">
            <a @click="openFile(file.id)" class="button is-rounded secondary-bg-color has-text-weight-semibold white-text is-responsive navbar-button" style="width: 150px;">
              <font-awesome-icon :icon="['fas', 'file']" class="top-ranking-icon mr-2" />Abrir
            </a>
          </div>
          <div class="is-narrow">
            <div class="has-text-right case-file-stats mr-4">
              <span class="secondary-text-color">{{ file.downloads }} <font-awesome-icon class="mx-1" :icon="['fas', 'download']" /></span>
            </div>
          </div>
          </div>
      </div>
    </div>
  </div>  
</template>