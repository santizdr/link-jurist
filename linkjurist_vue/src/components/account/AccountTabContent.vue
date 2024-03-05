<script setup>
    import { useAuthStore } from '@/stores/auth';
    import { useDetailsStore } from '@/stores/details';
    import { ref } from 'vue'

    import AccountTeamCard from '@/components/account/team/AccountTeamCard.vue'
    import FileUploadModal from '@/components/account/files/FileUploadModal.vue'
    import AccountFileCard from '@/components/account/files/AccountFileCard.vue'
    import AccountCaseCard from '@/components/account/cases/AccountCaseCard.vue'
    import AccountPostCard from '@/components/account/posts/AccountPostCard.vue'
    import CreateUserModal from '@/components/account/team/CreateUserModal.vue'
    import CaseCreateModal from '@/components/account/cases/CaseCreateModal.vue'
    import CaseCard from '@/components/cases/CaseCard.vue'
    import PostCard from '@/components/home/posts/PostCard.vue'
    import CreatePost from '@/components/home/posts/CreatePost.vue'
    import ApplicationCard from '@/components/account/applications/ApplicationCard.vue'
    import ApplicationsFilter from '@/components/account/applications/ApplicationsFilter.vue'

    const props  = defineProps(['viewData', 'activeTab']);
    const authStore = useAuthStore();
    const detailsStore = useDetailsStore();

    const showUserModal = ref(false);
    const showFileModal = ref(false);
    const showCaseModal = ref(false);
    const applicationsType = ref("all");

    function filterApplications(val) {
        applicationsType.value = val;
    }

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
                <p class="is-size-5 my-1" v-html="viewData.account.description"></p>
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
                            <a @click="showUserModal = true" v-if="detailsStore.account.id === null || detailsStore.account.id === authStore.account.id" class="button secondary-bg-color has-text-weight-semibold white-text is-responsive navbar-button">
                                <span><font-awesome-icon :icon="['fas', 'plus']" class="top-ranking-icon mr-2" />Añadir integrante</span>
                            </a>
                        </div>
                    </div>

                </div>
            </div>
            <AccountTeamCard v-for="user in viewData.team" :user="user" />
        </div>

        <div v-if="activeTab === 'posts-tab'">
            <div v-if="detailsStore.account.id === null || detailsStore.account.id === authStore.account.id" class="mx-3">
                <CreatePost />
                <hr>
            </div>
            <div class="mx-3">
                <h1 class="title is-3">Nuestras publicaciones</h1>
                <div v-if="authStore.account.id === viewData.account.id">
                    <div v-if="viewData.posts.length > 0" class="scrollable-div">
                        <AccountPostCard v-for="post in viewData.posts" :key="post.id" :post="post" /> 
                    </div>
                    <div v-else>
                        <p class="is-size-5 my-1">Aún no has realizado ninguna publicación</p>
                    </div>
                </div>
                <div v-else>
                    <div v-if="viewData.posts.length > 0" class="scrollable-div">
                        <PostCard v-for="post in viewData.posts" :key="post.id" :post="post" /> 
                    </div>
                    <div v-else>
                        <p class="is-size-5 my-1">Aún no hay publicaciones en esta cuenta</p>
                    </div>
                </div>
            </div>
        </div>

        <div v-if="activeTab === 'case-tab'">
            <div v-if="detailsStore.account.id === null || detailsStore.account.id === authStore.account.id" class="mx-3">
                <h1 class="title is-3">Crea un caso</h1>
                <a @click="showCaseModal = true" class="button secondary-bg-color has-text-weight-semibold white-text is-responsive navbar-button">
                    <span><font-awesome-icon :icon="['fas', 'plus']" class="top-ranking-icon mr-2" />Crear</span>
                </a>
                <hr>
            </div>
            <div class="mx-3">
                <h1 class="title is-3">Nuestros casos</h1>
                <div v-if="viewData.cases.length > 0" class="scrollable-div">
                    <div v-if="authStore.account.id === viewData.account.id">
                        <AccountCaseCard v-for="caso in viewData.cases" :key="caso.id" :caso="caso" /> 
                    </div>
                    <div v-else>
                        <CaseCard v-for="caso in viewData.cases" :key="caso.id" :caso="caso" /> 
                    </div>
                </div>
                <div v-else>
                    <p class="is-size-5 my-1">Aún no has publicado casos</p>
                </div>
            </div>
        </div>

        <div v-if="activeTab === 'file-tab'">
            <div v-if="detailsStore.account.id === null || detailsStore.account.id === authStore.account.id" class="mx-3">
                <h1 class="title is-3">Sube un escrito</h1>
                <a @click="showFileModal = true" class="button secondary-bg-color has-text-weight-semibold white-text is-responsive navbar-button">
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

        <div v-if="activeTab === 'applications-tab'">
            <div class="mx-3">
                <ApplicationsFilter @filter-applications="filterApplications" />
                <h1 class="title is-3">Estado de solicitudes. </h1>
                <div v-if="viewData.applications.length > 0" class="scrollable-div">
                    <ApplicationCard v-for="application in viewData.applications" :key="application.id" :application="application" :filter="applicationsType" />
                </div>
                <div v-else>
                    <p class="is-size-5 my-1">Aún no hay solicitudes</p>
                </div>
            </div>
        </div>
    </div>
    <FileUploadModal :showFileModal="showFileModal" @close-file-modal="showFileModal = false" />
    <CreateUserModal :acc="authStore.account.id" :showUserModal="showUserModal" @close-user-modal="showUserModal = false" />
    <CaseCreateModal :showCaseModal="showCaseModal" @close-case-modal="showCaseModal = false" />
</template>