<script setup>
    const { props } = defineProps(['publication']);
</script>

<template>
    <div>
        <div class="card my-5 mx-2">
        <div  v-if="publication.img != ''" class="card-image">
            <figure class="image is-4by3">
            <img :src="publication.img" alt="Placeholder image">
            </figure>
        </div>
        <div class="card-content">
            <div class="media">
            <div class="media-left">
                <figure class="image is-48x48">
                    <img :src="publication.accImg" alt="Placeholder image">
                </figure>
            </div>
            <div class="media-content">
                <p class="title is-4">{{ publication.user }}</p>
                <p class="subtitle is-6">{{ publication.postedBy }}</p>
            </div>
            </div>

            <div class="content">
                {{ publication.description }}
            <br>
            <p><span class="secondary-text-color">Fecha de publicación: </span><time :datetime="publication.postDate">{{ publication.postDate }}</time></p>
            </div>
        </div>
        </div>    
        <hr>   
    </div>
</template>