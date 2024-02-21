<script setup>
    import AccountFileCard from '@/components/account/files/AccountFileCard.vue'
    import AccountPostCard from '@/components/account/posts/AccountPostCard.vue'

    const tags = {
        1: "Derecho penal",
        2: "Derecho civil",
        3: "Derecho laboral",
        4: "Derecho mercantil",
        5: "Derecho administrativo",
        6: "Derecho internacional",
    }

    const props  = defineProps(['user', 'activeTab']);
</script>

<template>
    <div id="tab-content">
        <div v-if="activeTab === 'info-tab'">
            <h1 class="title is-3">Resumen</h1>
            <div class="">
                <p class="is-size-5 my-1">{{ user.description }}</p>
            </div> 
            <hr>
            <p class="is-size-5 my-1"><span class="secondary-text-color">Email personal: </span>{{ user.email }}</p>
            <div v-if="user.tags.length > 0">
                <p class="is-size-5 my-1"><span class="secondary-text-color">Especialidades: </span></p>
                <div class="mx-2">
                    <span v-for="tag in user.tags" class="tag is-medium mr-2" :class="'tag-' + tag">{{ tags[tag] }}</span>
                </div>
            </div>
        </div>

        <div v-if="activeTab === 'posts-tab'">
            <div class="columns">
                <div class="column">
                    <h1 class="title is-3">Posts</h1>
                </div>
            </div>
            <div v-if="user.posts.length > 0">
                <AccountPostCard v-for="post in user.posts" :key="post.id" :post="post" /> 
            </div>
            <div v-else>
                <p class="is-size-5 my-1">Aún no se ha realizado ninguna publicación</p>
            </div>
        </div>

        <div v-if="activeTab === 'file-tab'">
            <div class="columns">
                <div class="column">
                    <h1 class="title is-3">Escritos</h1>
                </div>
            </div>
            <div v-if="user.files.length > 0">
                <AccountFileCard v-for="file in user.files" :key="file.id" :file="file" />
            </div>
            <div v-else>
                <p class="is-size-5 my-1">Aún no se han publicado escritos</p>
            </div>
        </div>
    </div>
</template>
