<script setup>
    import { useIndexStore } from '@/stores/index';
    import PostCard from '@/components/home/PostCard.vue'

    const indexStore = useIndexStore();
</script>

<template>
    <div class="box scrollable-div">
        <h1 class="title">Publicaciones</h1>
        <div v-if="indexStore.contacts.length > 0">
            <div v-if="indexStore.posts.length === 0">
                <h2 class="subtitle">Tus contactos no han realizado publicaciones. Estas son algunas recomendaciones para tí</h2>
                <hr>
                <PostCard v-for="post in indexStore.post_suggestions" :key="post.id" :post="post" />
            </div>
            <div v-else>
                <h2 class="subtitle">Listado de publicaciones de las cuentas a las que sigues. </h2>
                <hr>
                <PostCard v-for="post in indexStore.posts" :key="post.id" :post="post" />
            </div>

        </div>
        <div v-else>
            <h2 class="subtitle">Aún no tienes contactos. Estas son algunas publicaciones recomendadas para tí</h2>
            <hr>
            <PostCard v-for="post in indexStore.post_suggestions" :key="post.id" :post="post" />
        </div>
  </div>
</template>