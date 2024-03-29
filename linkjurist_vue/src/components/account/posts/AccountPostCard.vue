<script setup>
    import axios from 'axios';
    import { ref } from 'vue'
    import { useAuthStore } from '@/stores/auth';
    import ConfirmDeletePost from '@/components/account/posts/ConfirmDeletePost.vue';
    import EditPostModal from '@/components/account/posts/EditPostModal.vue';
    import { useRouter } from 'vue-router'

    const authStore = useAuthStore();
    const props = defineProps(['post']);
    const emit = defineEmits(['updateLikes'])

    const tags = {
        1: "Derecho penal",
        2: "Derecho civil",
        3: "Derecho laboral",
        4: "Derecho mercantil",
        5: "Derecho administrativo",
        6: "Derecho internacional",
    }

    const resetKey = ref(0);

    const deletePostModal = ref(false);
    const editPostModal = ref(false);
    const deleteId = ref(null);

    function deletePost(id) {
        deleteId.value = id;
        deletePostModal.value = true;
    }

    function editPost() {
        editPostModal.value = true;
    }

    function handleCloseEditModal() {
        editPostModal.value = false;
    }

    const alert = ref({
        message: "",
        class: "",
    });

    function closeAlert() {
        alert.value.message = "";
        alert.value.class = "";
    }

    function like(id) {
        const data = {
            'id': id,
            'me': authStore.user.id,
        };

        const counter = ref(props.post.likes)
        
        axios.post("/api/likepost", data)
        .then(response => {
            if(response.data.message === "liked") {
                counter.value++;
                alert.value.message = "Te gusta esta publicación";
                alert.value.class = "span-success";
            } else if (response.data.message === "delete") {
                counter.value--;
                alert.value.message = "Me gusta eliminado";
                alert.value.class = "span-error";
            } else {
                console.log("Se ha producido un error");
                alert.value.message = "Se ha producido un error al asignar el me gusta";
                alert.value.class = "span-error";
            }
            emit('updateLikes', id, counter.value);
        })
        .catch(error => {
            console.log("Error: ", error);
            alert.value.message = "Se ha producido un error al asignar el me gusta";
            alert.value.class = "span-error";
        })
    }
</script>

<template>
    <div>
        <div class="card my-5 mx-2">
            <div class="card-content">
                <div v-if="alert.message !== ''" class="my-3">
                    <article class="message">
                        <div class="message-header"  :class="alert.class">
                            <p>{{ alert.message }}</p>
                            <a @click="closeAlert()" class="delete" aria-label="delete"></a>
                        </div>
                    </article>  
                </div> 
                <div class="media">
                    <!-- <div class="media-left">
                        <figure class="image is-48x48">
                            <img :src="post.accImg" alt="Placeholder image">
                        </figure>
                    </div> -->
                    <div class="media-content">
                        <div class="columns">
                            <div class="column">
                                <p class="title is-4">{{ post.account_name }}</p>
                                <p class="subtitle is-6">{{ post.posted_by_name }}</p>
                            </div>
                            <div class="column is-narrow">
                                <div v-if="post.account === authStore.account.id">
                                    <a v-if="post.posted_by === authStore.user.id || authStore.user.is_manager" @click="editPost(post.id)" class="button secondary-bg-color has-text-weight-semibold white-text mx-1">
                                        <font-awesome-icon :icon="['fas', 'pen']" class="top-ranking-icon" />
                                    </a>
                                    <a v-if="post.posted_by === authStore.user.id || authStore.user.is_manager" @click="deletePost(post.id)" class="button secondary-bg-color has-text-weight-semibold white-text">
                                        <font-awesome-icon :icon="['fas', 'trash']" class="top-ranking-icon" />
                                    </a>
                                </div>
                            </div>
                        </div>
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
                                <span @click="like(post.id)" class="secondary-text-color mx-3">{{ post.likes }} <font-awesome-icon class="mx-1"  :icon="['fas', 'heart']" /></span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>    
        <hr>   
    </div>
    <ConfirmDeletePost :deletePostModal="deletePostModal" @close-delete-post-modal="deletePostModal = false" :id="deleteId" />
    <EditPostModal :key="resetKey" :editPostModal="editPostModal" @close-edit-post-modal="handleCloseEditModal()" :post="post"/>
</template>