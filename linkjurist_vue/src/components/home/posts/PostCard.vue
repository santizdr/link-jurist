<script setup>
    const { props } = defineProps(['post']);

    const tags = {
        1: "Derecho penal",
        2: "Derecho civil",
        3: "Derecho laboral",
        4: "Derecho mercantil",
        5: "Derecho administrativo",
        6: "Derecho internacional",
    }
</script>

<template>
    <div>
        <div class="card my-5 mx-2">
            <div class="card-content">
                <div class="media">
                    <!-- <div class="media-left">
                        <figure class="image is-48x48">
                            <img :src="post.accImg" alt="Placeholder image">
                        </figure>
                    </div> -->
                    <div class="media-content">
                        <p class="title is-4">
                            <RouterLink :to="'/user/' + post.posted_by" class="black-text ">{{ post.posted_by_name }}</RouterLink>
                        </p>
                        <p class="subtitle is-6">
                            <RouterLink :to="'/account/' + post.account" class="black-text ">{{ post.account_name }}</RouterLink>
                        </p>
                        <div>
                            <span v-for="tag in post.tags" class="tag is-medium mr-2" :class="'tag-' + tag">{{ tags[tag] }}</span>
                        </div>
                    </div>
                </div>

                <div class="content">
                    {{ post.content }}
                    <br>
                    <div class="columns is-vcentered">
                        <div class="column">
                            <p class="my-2"><span class="secondary-text-color">Fecha de publicación: </span><time :datetime="post.post_date">{{ post.post_date }}</time></p>
                        </div>
                        <div class="is-narrow">
                            <div class="has-text-right case-file-stats mr-4">
                                <span class="secondary-text-color mx-3">{{ post.likes }} <font-awesome-icon class="mx-1"  :icon="['fas', 'heart']" /></span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>    
        <hr>   
    </div>
</template>