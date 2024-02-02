<script setup>
    import { useIndexStore } from '@/stores/index';
    import PublicationCard from '../home/PublicationCard.vue'

    const indexStore = useIndexStore();
</script>

<template>
    <div class="box scrollable-div">
        <h1 class="title">Publicaciones</h1>
        <div v-if="indexStore.contacts.length > 0">
            <div v-if="indexStore.publications.length === 0">
                <h2 class="subtitle">Tus contactos no han realizado publicaciones. Estas son algunas recomendaciones para tí</h2>
                <hr>
                <PublicationCard v-for="publication in indexStore.publication_suggestions" :key="publication.id" :publication="publication" />
            </div>
            <div v-else>
                <h2 class="subtitle">Listado de publicaciones de las cuentas a las que sigues. </h2>
                <hr>
                <PublicationCard v-for="publication in indexStore.publications" :key="publication.id" :publication="publication" />
            </div>

        </div>
        <div v-else>
            <h2 class="subtitle">Aún no tienes contactos. Estas son algunas publicaciones recomendadas para tí</h2>
            <hr>
            <PublicationCard v-for="publication in indexStore.publication_suggestions" :key="publication.id" :publication="publication" />
        </div>
  </div>
</template>