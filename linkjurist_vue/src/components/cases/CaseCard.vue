<script setup>
    import { useAuthStore } from '@/stores/auth';
    const store = useAuthStore();

    const { props } = defineProps(['caso']);

    function toCapitalNoun(str) {
        return str.charAt(0).toUpperCase() + str.slice(1);
    }
</script>

<template>
    <div class="card my-3">
      <div class="card-content">
        <div class="media">
          <div class="media-content">            
            <p class="title is-4">{{ caso.title }} - {{ caso.postedBy }}</p>
            <p class="subtitle is-5 secondary-text-color">{{ toCapitalNoun(caso.type) }}</p>
          </div>
        </div>
        <div class="content">
           <p>{{ caso.description }}</p>
          <p><span class="secondary-text-color">Fecha de publicación: </span><time :datetime="caso.postDate">{{ caso.postDate }}</time></p>
          <p><span class="secondary-text-color">Fecha de expiración: </span><time :datetime="caso.expiryDate">{{ caso.expiryDate }}</time></p>
        </div>
      </div>
    </div>   
</template>
