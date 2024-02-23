<script setup>
  import ConfirmDeleteCase from '@/components/account/cases/ConfirmDeleteCase.vue';

  const { props } = defineProps(['caso']);

  const tags = {
    1: "Derecho penal",
    2: "Derecho civil",
    3: "Derecho laboral",
    4: "Derecho mercantil",
    5: "Derecho administrativo",
    6: "Derecho internacional",
  }

  const deleteCaseModal = ref(false);
  const editCaseModal = ref(false);
  const deleteId = ref(null);

  function deleteCase(id) {
      deleteId.value = id;
      deleteFileModal.value = true;
  }

</script>

<template>
    <div class="card my-3">
      <div class="card-content">
        <div class="media">
          <div class="media-content"> 
            <div>
              <div class="column">
                <p class="title is-4">{{ caso.title }}</p>
                <p class="subtitle is-5 secondary-text-color is-capitalized">{{ caso.type === "OFFER" ? "Oferta"  : "Demanda" }}</p>
              </div>
              <div class="column is-narrow">
                <a @click="editFile(caso.id)" class="button secondary-bg-color has-text-weight-semibold white-text mx-1">
                    <font-awesome-icon :icon="['fas', 'pen']" class="top-ranking-icon" />
                </a>
                <a v-if="authStore.user.is_manager" @click="deleteCase(caso.id)" class="button secondary-bg-color has-text-weight-semibold white-text">
                    <font-awesome-icon :icon="['fas', 'trash']" class="top-ranking-icon" />
                </a>
              </div>
            </div>           

            <div>
              <span v-for="tag in caso.tags" class="tag is-medium mr-2" :class="'tag-' + tag">{{ tags[tag] }}</span>
            </div>
          </div>
        </div>
        <div class="content">
           <p>{{ caso.description }}</p>
           <div class="columns is-vcentered">
            <div class="column">
              <p><span class="secondary-text-color">Fecha de publicación: </span><time :datetime="caso.postDate">{{ caso.post_date }}</time></p>
              <p><span class="secondary-text-color">Fecha de expiración: </span><time :datetime="caso.expiryDate">{{ caso.expiry_date }}</time></p>
            </div>

              <div class="column is-narrow has-text-right case-file-stats mr-4">
                <span class="secondary-text-color mx-3">{{ caso.visualizations }} <font-awesome-icon class="mx-1" :icon="['fas', 'eye']" /></span>
                <span class="secondary-text-color mx-3">{{ caso.applications }} <font-awesome-icon class="mx-1" :icon="['fas', 'arrow-right']" /></span>
              </div>
            </div>
        </div>
      </div>
    </div>   
</template>
