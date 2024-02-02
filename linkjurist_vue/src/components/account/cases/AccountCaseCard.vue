<script setup>
    import { useAuthStore } from '@/stores/auth';

    const authStore = useAuthStore();
    const { props } = defineProps(['caso']);
</script>

<template>
    <div class="card my-3">
      <div class="card-content">
        <div class="media">
          <div class="media-content">            
            <p class="title is-4">{{ caso.title }}</p>
            <p class="subtitle is-5 secondary-text-color is-capitalized">{{ caso.type === "OFFER" ? "Oferta"  : "Demanda" }}</p>
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
