<script setup>
    import { useAuthStore } from '@/stores/auth';
    import { useDetailsStore } from '@/stores/details';
    import { ref } from 'vue'

    import AccountTeamCard from '../account/team/AccountTeamCard.vue'
    import FileUploadModal from '../account/files/FileUploadModal.vue'
    import AccountFileCard from '../account/files/AccountFileCard.vue'
    import AccountCaseCard from '../account/cases/AccountCaseCard.vue'
    import AccountTeamModal from '../account/team/AccountTeamModal.vue'
    import CaseCreateModal from '../account/cases/CaseCreateModal.vue'

    const { props } = defineProps(['viewData', 'activeTab']);
    const authStore = useAuthStore();
    const detailsStore = useDetailsStore();

    const showUserModal = ref(false);
    const showFileModal = ref(false);
    const showCaseModal = ref(false);
</script>

<template>
    <div id="tab-content">
        <div v-if="activeTab === 'info-tab'">
            <h1 class="title is-3">Resumen</h1>
            <div class="columns">
                <div class="column is-half">
                    <h2 class="subtitle is-4">Contacto</h2>
                    <p class="is-size-5 my-1"><span class="secondary-text-color">Web: </span>{{ viewData.account.web }}</p>
                    <p class="is-size-5 my-1"><span class="secondary-text-color">Email : </span>{{ viewData.account.email }}</p>
                    <p class="is-size-5 my-1"><span class="secondary-text-color">Teléfono : </span>{{ viewData.account.phonenumber }}</p>
                </div>
                <div class="column is-half">
                    <h2 class="subtitle is-4">Dirección</h2>
                    <p class="is-size-5 my-1"><span class="secondary-text-color">Calle: </span>{{ viewData.account.address }}</p>
                    <p class="is-size-5 my-1"><span class="secondary-text-color">Código postal : </span>{{ viewData.account.cp }}</p>
                    <p class="is-size-5 my-1"><span class="secondary-text-color">Provincia : </span>{{ viewData.account.locality }}</p>
                    <p class="is-size-5 my-1"><span class="secondary-text-color">País : </span>{{ viewData.account.country }}</p>
                </div>
            </div>
            <hr>
            <h1 class="title is-3">Sobre nosotros</h1>
            <div class="column is-full">
                <p class="is-size-5 my-1">{{ viewData.account.description }}</p>
            </div>
        </div>
        <div v-if="activeTab === 'team-tab'">
            <div class="columns">
                <div class="column">
                    <h1 class="title is-3">Nuestro equipo</h1>
                </div>
                <div class="column is-narrow is-right">
                    <div class="field is-grouped is-grouped-right">
                        <div class="control">
                            <a v-if="detailsStore.account.id === null || detailsStore.account.id === authStore.account.id" class="button is-rounded secondary-bg-color has-text-weight-semibold white-text is-responsive navbar-button">
                                <span><font-awesome-icon :icon="['fas', 'plus']" class="top-ranking-icon mr-2" />Añadir integrante</span>
                            </a>
                        </div>
                    </div>

                </div>
            </div>
            <AccountTeamCard v-for="user in viewData.team" :user="user" />
        </div>
        <div v-if="activeTab === 'case-tab'">
            <div v-if="detailsStore.account.id === null || detailsStore.account.id === authStore.account.id" class="mx-3">
                <h1 class="title is-3">Crea un caso</h1>
                <a @click="showCaseModal = true" class="button is-rounded secondary-bg-color has-text-weight-semibold white-text is-responsive navbar-button">
                    <span><font-awesome-icon :icon="['fas', 'plus']" class="top-ranking-icon mr-2" />Crear</span>
                </a>
                <hr>
            </div>
            <div class="mx-3">
                <h1 class="title is-3">Nuestros casos</h1>
                <div v-if="viewData.cases.length > 0" class="scrollable-div">
                    <AccountCaseCard v-for="caso in viewData.cases" :key="caso.id" :caso="caso" /> 
                </div>
                <div v-else>
                    <p class="is-size-5 my-1">Aún no has publicado casos</p>
                </div>
            </div>

        </div>
        <div v-if="activeTab === 'file-tab'">
            <div v-if="detailsStore.account.id === null || detailsStore.account.id === authStore.account.id" class="mx-3">
                <h1 class="title is-3">Sube un escrito</h1>
                <a @click="showFileModal = true" class="button is-rounded secondary-bg-color has-text-weight-semibold white-text is-responsive navbar-button">
                    <span><font-awesome-icon :icon="['fas', 'upload']" class="top-ranking-icon mr-2" />Subir archivo</span>
                </a>
                <hr>
            </div>
            <div class="mx-3">
                <h1 class="title is-3">Nuestros escritos</h1>
                <div v-if="viewData.files.length > 0" class="scrollable-div">
                    <AccountFileCard v-for="file in viewData.files" :key="file.id" :file="file" />
                </div>
                <div v-else>
                    <p class="is-size-5 my-1">Aún no hay escritos</p>
                </div>
            </div>
        </div>
    </div>
    <FileUploadModal :showFileModal="showFileModal" @close-file-modal="showFileModal = false" />
    <AccountTeamModal :showUserModal="showUserModal" @close-user-modal="showUserModal = false" />
    <CaseCreateModal :showCaseModal="showCaseModal" @close-case-modal="showCaseModal = false" />

</template>