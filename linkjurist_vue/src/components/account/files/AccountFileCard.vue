<script setup>
  import { ref } from 'vue'
  import axios from 'axios';
  import { useAuthStore } from '@/stores/auth';
  import { useRouter } from 'vue-router'
  import AccountShowFileModal from '@/components/account/files/AccountShowFileModal.vue';
  import ConfirmDeleteFile from '@/components/account/files/ConfirmDeleteFile.vue';
  import EditFileModal from '@/components/account/files/EditFileModal.vue';

  const router = useRouter();

  const authStore = useAuthStore();

  const emit = defineEmits(['updateDownloads']);
  const props = defineProps(['file']);

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

  const resetKey = ref(0);

  const deleteFileModal = ref(false);
  const editFileModal = ref(false);
  const deleteId = ref(null);

  function openFile(id, account) {
      axios.get("/api/getfile/", { 
          responseType: 'blob',
          params: {id: id, account: account}
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

  function handleCloseModal(purchased) {
    showFileModal.value = false;
    if(purchased) {
      emit('updateDownloads', props.file.id)
    }
  }

  function deleteFile(id) {
      deleteId.value = id;
      deleteFileModal.value = true;
  }

  function editFile() {
      editFileModal.value = true;
  }
</script>

<template>
  <div class="card my-4 mx-4">
    <div class="card-content">
      <div class="media">
        <div class="media-content">     
          <div class="columns">
            <div class="column">
              <p class="title is-4">{{ file.title }}</p>
            </div>
            <div class="column is-narrow">
              <div v-if="file.account === authStore.account.id">
                  <a @click="editFile(file.id)" class="button secondary-bg-color has-text-weight-semibold white-text mx-1">
                      <font-awesome-icon :icon="['fas', 'pen']" class="top-ranking-icon" />
                  </a>
                  <a v-if="file.uploaded_by === authStore.user.id || authStore.user.is_manager" @click="deleteFile(file.id)" class="button secondary-bg-color has-text-weight-semibold white-text">
                      <font-awesome-icon :icon="['fas', 'trash']" class="top-ranking-icon" />
                  </a>
                </div>
            </div>
          </div>
          <div>
              <span v-for="tag in file.tags" class="tag is-medium mr-2" :class="'tag-' + tag">{{ tags[tag] }}</span>
          </div>
        </div>
      </div>
      <div class="content">
          <p class="default-font-size"><span class="secondary-text-color">Descripción: </span>{{ file.description }}</p>
          <div class="columns is-vcentered">
          <div class="column">
            <a @click="openFile(file.id, authStore.account.id)" class="button secondary-bg-color has-text-weight-semibold white-text is-responsive navbar-button" style="width: 150px;">
            <!-- <a @click="showFileModal = true" class="button secondary-bg-color has-text-weight-semibold white-text is-responsive navbar-button" style="width: 150px;"> -->
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
  <AccountShowFileModal :fileid="file.id" :file="fileSrc" :showFileModal="showFileModal" @close-file-modal="handleCloseModal" />
  <ConfirmDeleteFile :deleteFileModal="deleteFileModal" @close-delete-file-modal="deleteFileModal = false" :id="deleteId" />
  <EditFileModal :key="resetKey" :editFileModal="editFileModal" @close-edit-file-modal="editFileModal = false" :file="file"/>
</template>