<script setup>
    import { useUserStore } from '@/stores/user';
    const store = useUserStore();

    const { props } = defineProps(['caso']);
</script>

<template>
    <div class="card my-3">
      <div class="card-content">
        <div class="media">
          <div class="media-content">            
            <p class="title is-4">{{ caso.title }} - {{ caso.postedBy }}</p>
            <p class="subtitle is-5 secondary-text-color is-capitalized">{{ caso.type }}</p>
          </div>
        </div>
        <div class="content">
           <p>{{ caso.description }}</p>
           <div class="columns is-vcentered">
            <div class="column">
              <p><span class="secondary-text-color">Fecha de publicación: </span><time :datetime="caso.postDate">{{ caso.postDate }}</time></p>
              <p><span class="secondary-text-color">Fecha de expiración: </span><time :datetime="caso.expiryDate">{{ caso.expiryDate }}</time></p>
            </div>

              <div class="column is-narrow has-text-right case-file-stats mr-4">
                <span class="secondary-text-color mx-3">{{ caso.visualizations }} <font-awesome-icon :icon="['fas', 'eye']" /></span>
                <span class="secondary-text-color mx-3">{{ caso.applications }} <font-awesome-icon :icon="['fas', 'arrow-right']" /></span>
              </div>
            </div>
        </div>
      </div>
    </div>   
</template>
