<script setup>
    import { ref } from 'vue'
    import ConfirmDeleteUser from '@/components/account/team/ConfirmDeleteUser.vue'
    
    const { props } = defineProps(['user']);

    const tags = {
        1: "Derecho penal",
        2: "Derecho civil",
        3: "Derecho laboral",
        4: "Derecho mercantil",
        5: "Derecho administrativo",
        6: "Derecho internacional",
    }

    const deleteUserModal = ref(false);
    const editUserModal = ref(false);
    const deleteId = ref(null);

    function deleteUser(id) {
        deleteId.value = id;
        deleteUserModal.value = true;
    }
</script>

<template>
    <div class="card my-5">
        <div class="columns">
            <div class="column is-narrow ml-5 my-2 is-flex is-align-items-center">
                <div class="card-image">
                    <figure class="image is-128x128">
                        <img src="https://bulma.io/images/placeholders/128x128.png">
                    </figure>
                </div>
            </div>
            <div class="column">
                <div class="card-content">
                    <div class="content">
                        <div class="columns">
                            <div class="column">
                                <h2 class="title is-4">
                                    <RouterLink :to="'/user/' + user.id" class="black-text ">{{ user.firstname }} {{ user.lastname }}</RouterLink>
                                </h2>
                                <p class="subtitle is-5 mb-3"><span class="secondary-text-color">Email personal: </span>{{ user.email }}</p>
                                <div>
                                    <span v-for="tag in user.tags" class="tag is-medium mr-2" :class="'tag-' + tag">{{ tags[tag] }}</span>
                                </div>
                            </div>
                            <div class="column is-narrow">
                                <a @click="editUser(user.id)" class="button secondary-bg-color has-text-weight-semibold white-text mx-1">
                                    <font-awesome-icon :icon="['fas', 'pen']" class="top-ranking-icon" />
                                </a>
                                <a v-if="!user.is_manager" @click="deleteUser(user.id)" class="button secondary-bg-color has-text-weight-semibold white-text">
                                    <font-awesome-icon :icon="['fas', 'trash']" class="top-ranking-icon" />
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <ConfirmDeleteUser :deleteUserModal="deleteUserModal" @close-delete-user-modal="deleteUserModal = false" :id="deleteId" />
</template>