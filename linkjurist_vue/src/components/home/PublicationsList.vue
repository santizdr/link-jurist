<script setup>
    import PublicationCard from '../home/PublicationCard.vue'

    const publications = [
        {
            "id": 1,
            "title": "Publicacion 1",
            "description": "Lorem ipsum publicaciones",
            "img": "",
            "accImg": "https://bulma.io/images/placeholders/96x96.png",
            "postDate": "2024-01-17",
            "postedBy": "Joaquím Bellmunt",
            "user": "Joaquím Bellmunt",
        },
        {
            "id": 2,
            "title": "Publicacion 2",
            "description": "Lorem ipsum publicaciones",
            "img": "https://bulma.io/images/placeholders/1280x960.png",
            "accImg": "https://bulma.io/images/placeholders/96x96.png",
            "postDate": "2024-01-11",
            "postedBy": "Prudencio Sáez & Asociados",
            "user": "Prudencio Sáez",
        },
        {
            "id": 3,
            "title": "Publicacion 3",
            "description": "Lorem ipsum publicaciones",
            "img": "",
            "accImg": "https://bulma.io/images/placeholders/96x96.png",
            "postDate": "2024-01-9",
            "postedBy": "S&P Asociados",
            "user": "Saúl Pérez",
        },
    ]
</script>

<template>
    <div class="box scrollable-div">

    <h1 class="title">Publicaciones</h1>
    <h2 class="subtitle">Listado de publicaciones de contactos y cuentas relacionadas. </h2>
    <hr>
    <PublicationCard v-for="publication in publications" :key="publication.id" :publication="publication" />
  </div>
</template>