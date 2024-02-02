<script setup>
    const { props } = defineProps(['publication']);
</script>

<template>
    <div>
        <div class="card my-5 mx-2">

            <div class="card-content">
                <div class="media">
                    <!-- <div class="media-left">
                        <figure class="image is-48x48">
                            <img :src="publication.accImg" alt="Placeholder image">
                        </figure>
                    </div> -->
                    <div class="media-content">
                        <p class="title is-4">{{ publication.posted_by_name }}</p>
                        <p class="subtitle is-6">{{ publication.account_name }}</p>
                    </div>
                </div>

                <div class="content">
                    {{ publication.content }}
                <br>

                <div class="columns is-vcentered">
                    <div class="column">
                        <p class="my-2"><span class="secondary-text-color">Fecha de publicación: </span><time :datetime="publication.post_date">{{ publication.post_date }}</time></p>
                    </div>
                    <div class="is-narrow">
                        <div class="has-text-right case-file-stats mr-4">
                            <span class="secondary-text-color mx-3">{{ publication.likes }} <font-awesome-icon class="mx-1"  :icon="['fas', 'heart']" /></span>
                        </div>
                    </div>
                </div>



                </div>
            </div>
        </div>    
        <hr>   
    </div>
</template>