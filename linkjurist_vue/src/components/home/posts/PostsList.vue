<script setup>
    import { useIndexStore } from '@/stores/index';
    import { ref } from 'vue';
    import PostCard from '@/components/home/posts/PostCard.vue'

    const indexStore = ref(useIndexStore());

    function handleUpdateLikes(post_id, likes) {
        const index = indexStore.value.post_suggestions.findIndex(post => post.id === post_id);
        
        if (index !== -1) {
            indexStore.value.post_suggestions[index].likes = likes;
        } else {
            indexStore.value.posts[index].likes = likes;
        }
    }
</script>

<template>
    <div class="box scrollable-div">
        <h1 class="title">Publicaciones</h1>
        <div v-if="indexStore.contacts.length > 0">
            <div v-if="indexStore.posts.length === 0">
                <h2 class="subtitle">Tus contactos no han realizado publicaciones. Estas son algunas recomendaciones para tí</h2>
                <hr>
                <PostCard v-for="post in indexStore.post_suggestions" :key="post.id" :post="post" @update-likes="handleUpdateLikes" />
            </div>
            <div v-else>
                <h2 class="subtitle">Listado de publicaciones de las cuentas a las que sigues. </h2>
                <hr>
                <PostCard v-for="post in indexStore.posts" :key="post.id" :post="post" @update-likes="handleUpdateLikes" />
            </div>

        </div>
        <div v-else>
            <h2 class="subtitle">Aún no tienes contactos. Estas son algunas publicaciones recomendadas para tí</h2>
            <hr>
            <PostCard v-for="post in indexStore.post_suggestions" :key="post.id" :post="post" @update-likes="handleUpdateLikes" />
        </div>
  </div>
</template>