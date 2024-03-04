<script setup>
    import { ref } from 'vue'
    import HandleApplicationModal from '@/components/account/applications/HandleApplicationModal.vue'

    const showApplicationModal = ref(false);
    const { props } = defineProps(['application', 'filter']);
</script>

<template>
  <div v-if="filter === 'all' || application.type === filter">
    <div v-if="application.type === 'applicant'" class="card my-3">
      <div class="card-content">
        <div class="media">
          <div class="media-content"> 
            <p class="title is-4 my-5">
              <RouterLink :to="'/account/' + application.applicant" class="secondary-text-color has-text-weight-semibold">{{ application.applied_by }}</RouterLink> ha aplicado a tu caso
            </p> 
            <p class="subtitle is-5 my-5">{{ application.case_title }}</p>
            <span class="secondary-text-color">Estado: </span>
            <span v-if="application.status === 'PENDING'" class="tag is-medium is-light mr-2"><a @click="showApplicationModal = true" class="black-text">Pendiente<font-awesome-icon class="ml-2" :icon="['fas', 'clock']" /></a></span>
            <span v-else-if="application.status === 'DENIED'" class="tag is-medium is-danger mr-2">Rechazada<font-awesome-icon class="ml-2" :icon="['fas', 'xmark']" /></span>
            <span v-else class="tag is-medium is-success mr-2">Aceptada<font-awesome-icon class="ml-2" :icon="['fas', 'check']" /></span>
          </div>
        </div>
        <div class="content">
           <div class="columns is-vcentered">
            <div class="column">
              <p><span class="secondary-text-color">Fecha de publicación: </span><time :datetime="application.case_post_date">{{ application.case_post_date }}</time></p>
              <p><span class="secondary-text-color">Fecha de expiración: </span><time :datetime="application.case_expiry_date">{{ application.case_expiry_date }}</time></p>
            </div>

              <div class="column is-narrow has-text-right case-file-stats mr-4">
                <span class="secondary-text-color mx-3">{{ application.case_applications }} <font-awesome-icon class="mx-1" :icon="['fas', 'arrow-right']" /></span>
              </div>
            </div>
        </div>
      </div>
    </div>   

    <div class="card my-3" v-else>
      <div class="card-content">
        <div class="media">
          <div class="media-content"> 
            <p class="title is-4 my-5">
              Has aplicado al caso de <RouterLink :to="'/account/' + application.applicant" class="secondary-text-color has-text-weight-semibold">{{ application.applied_by }}</RouterLink>
            </p> 
            <p class="subtitle is-5 my-5">{{ application.case_title }}</p>       
            <span class="secondary-text-color">Estado: </span>
            <span v-if="application.status === 'PENDING'" class="tag is-medium is-light mr-2"><a class="black-text">Pendiente<font-awesome-icon class="ml-2" :icon="['fas', 'clock']" /></a></span>
            <span v-else-if="application.status === 'DENIED'" class="tag is-medium is-danger mr-2">Rechazada<font-awesome-icon class="ml-2" :icon="['fas', 'xmark']" /></span>
            <span v-else class="tag is-medium is-success mr-2">Aceptada<font-awesome-icon class="ml-2" :icon="['fas', 'check']" /></span>
          </div>
        </div>
        <div class="content">
           <div class="columns is-vcentered">
            <div class="column">
              <p><span class="secondary-text-color">Fecha de publicación: </span><time :datetime="application.case_post_date">{{ application.case_post_date }}</time></p>
              <p><span class="secondary-text-color">Fecha de expiración: </span><time :datetime="application.case_expiry_date">{{ application.case_expiry_date }}</time></p>
            </div>
              <div class="column is-narrow has-text-right case-file-stats mr-4">
                <span class="secondary-text-color mx-3">{{ application.case_applications }} <font-awesome-icon class="mx-1" :icon="['fas', 'arrow-right']" /></span>
              </div>
            </div>
        </div>
      </div>
    </div>   
  </div>
  <HandleApplicationModal :showApplicationModal="showApplicationModal" :applicationData="application" @close-application-modal="showApplicationModal = false" />

</template>
