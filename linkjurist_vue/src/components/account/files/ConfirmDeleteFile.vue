<script setup>
    import { ref } from 'vue'
    import axios from 'axios';
    import { useAuthStore } from '@/stores/auth';
    import { useRouter } from 'vue-router'

    const router = useRouter();
    const authStore = useAuthStore();

    const emit = defineEmits(['closeDeleteFileModal'])
    const props = defineProps(['id', 'deleteFileModal']);

    const alert = ref({
        message: "",
        class: "",
    });

    function handleCloseModal() {
        emit('closeDeleteFileModal');
    }

    function confirmDelete(id) {
        axios.post("/api/deletefile/", {
            id: id
        })
        .then(response => {
            if(response.data.message === "success") {
                authStore.files = response.data.file;
                alert.value.message = "Has eliminado al usuario";
                alert.value.class = "span-success";
                if (router.currentRoute.value.fullPath.includes("user")){
                    this.detailsStore.fetchUserData(this.authStore.user.id);
                }
                handleCloseModal();
            } else {
                alert.value.message = "Se ha producido un error";
                alert.value.class = "span-error";
            }
        })
        .catch(error => {
            console.log("Error: ", error);
        })
    }
</script>

<template>
    <div class="modal" :class="{'is-active' : deleteFileModal }">
      <div class="modal-background"></div>
        <div class="modal-card">
            <form class="mx-3" @submit.prevent="submitForm()">
                <header class="modal-card-head">
                    <p class="modal-card-title">Ventana de confirmación</p>
                    <a @click="handleCloseModal()" class="delete" aria-label="close"></a>
                </header>
                <section class="modal-card-body">    
                    <p class="subtitle is-5 my-2">¿Estas seguro de que quieres eliminar el escrito?</p>
                </section>
                <footer class="modal-card-foot">
                    <div class="field is-grouped">
                        <div class="control">
                            <a @click="handleCloseModal()" class="button primary-form-button">Cancelar</a>
                        </div>
                        <div class="control">
                            <a @click="confirmDelete(id)" class="button secondary-form-button">Confirmar</a>
                        </div>
                    </div>
                </footer>
            </form>
        </div>
    </div>
</template>