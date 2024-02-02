<script setup>
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
          <p><span class="secondary-text-color">Porcentaje: </span>{{ caso.percent }}</p> 
          <p><span class="secondary-text-color">Fecha de publicación: </span><time :datetime="caso.postDate">{{ caso.postDate }}</time></p>
          <p><span class="secondary-text-color">Fecha de expiración: </span><time :datetime="caso.expiryDate">{{ caso.expiryDate }}</time></p>
          <div class="columns is-vcentered">
            <div class="column">
              <a id="signup_btn" class="button is-rounded secondary-bg-color has-text-weight-semibold white-text is-responsive navbar-button" style="width: 150px;">
                <font-awesome-icon :icon="['fas', 'plus']" class="top-ranking-icon mr-2" />Aplicar
              </a>
            </div>
            <div class="is-narrow">
              <div class="has-text-right case-file-stats mr-4">
                <span class="secondary-text-color mx-3">{{ caso.visualizations }} <font-awesome-icon class="mx-1"  :icon="['fas', 'eye']" /></span>
                <span class="secondary-text-color mx-3">{{ caso.applications }} <font-awesome-icon class="mx-1"  :icon="['fas', 'arrow-right']" /></span>
              </div>
            </div>
           </div>
        </div>
      </div>
    </div>   
</template>
