<script setup>
    import { useAuthStore } from '@/stores/auth';

    const authStore = useAuthStore();
    const { props } = defineProps(['application']);
</script>

<template>
    <div class="card my-3">
      <div class="card-content">
        <div class="media">
          <div class="media-content"> 
            <p class="title is-4 my-5">{{ application.case_title }}</p>           
            <p class="subtitle is-5 my-5"><span class="secondary-text-color">{{ application.applied_by }} </span> ha aplicado a tu caso</p> 

            <span v-if="application.status === 'PENDING'" class="tag is-medium is-light mr-2">Pendiente<font-awesome-icon class="ml-2" :icon="['fas', 'clock']" /></span>
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
                <span class="secondary-text-color mx-3">{{ application.case_visualizations }} <font-awesome-icon class="mx-1" :icon="['fas', 'eye']" /></span>
                <span class="secondary-text-color mx-3">{{ application.case_applications }} <font-awesome-icon class="mx-1" :icon="['fas', 'arrow-right']" /></span>
              </div>
            </div>
        </div>
      </div>
    </div>   
</template>
