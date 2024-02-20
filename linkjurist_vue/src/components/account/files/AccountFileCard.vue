<script setup>
  import { ref } from 'vue'
  import axios from 'axios';
  import ShowFileModal from '@/components/account/files/ShowFileModal.vue';

  const { props } = defineProps(['file']);

  const showFileModal = ref(false);
  const fileSrc = ref(null);

  const tags = {
      1: "Derecho penal",
      2: "Derecho civil",
      3: "Derecho laboral",
      4: "Derecho mercantil",
      5: "Derecho administrativo",
      6: "Derecho internacional",
    }

  function openFile(id) {
      axios.get("/api/getfile/", { 
          responseType: 'blob',
          params: {id: id}
        }
        )
        .then(response => {
          const reader = new FileReader();
          reader.readAsDataURL(response.data); 
          reader.onloadend = () => {
              const base64data = reader.result; 
              fileSrc.value = base64data;
              showFileModal.value = true;
          };
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
          <div>
              <span v-for="tag in file.tags" class="tag is-medium mr-2" :class="'tag-' + tag">{{ tags[tag] }}</span>
          </div>
        </div>
      </div>
      <div class="content">
          <p class="default-font-size"><span class="secondary-text-color">Descripción: </span>{{ file.description }}</p>
          <div class="columns is-vcentered">
          <div class="column">
            <a @click="openFile(file.id)" class="button is-rounded secondary-bg-color has-text-weight-semibold white-text is-responsive navbar-button" style="width: 150px;">
            <!-- <a @click="showFileModal = true" class="button is-rounded secondary-bg-color has-text-weight-semibold white-text is-responsive navbar-button" style="width: 150px;"> -->
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
  <ShowFileModal :file="fileSrc" :showFileModal="showFileModal" @close-file-modal="showFileModal = false" />
</template>