<script setup>
    import { ref } from 'vue'
    import UserTabContent from '@/components/user/UserTabContent.vue';
    
    const { props } = defineProps(['user']);
    const activeTab = ref("info-tab");

    function handleActiveTab(id) {
        activeTab.value = id;
    }
</script>

<template>
    <div class="columns">
        <div class="column is-full">
            <div class="tabs is-centered is-boxed">
                <ul>
                    <li :class="{'is-active': activeTab === 'info-tab'}" @click="handleActiveTab('info-tab')" >
                        <a>
                            <font-awesome-icon :icon="['fas', 'info']" class="tabs-icon mr-2" /><span>Información</span>
                        </a>
                    </li>
                    <li :class="{'is-active': activeTab === 'posts-tab'}" @click="handleActiveTab('posts-tab')">
                        <a>
                            <font-awesome-icon :icon="['fas', 'keyboard']" class="tabs-icon mr-2" /><span>Publicaciones</span>
                        </a>
                    </li>
                    <li :class="{'is-active': activeTab === 'file-tab'}" @click="handleActiveTab('file-tab')">
                        <a>
                            <font-awesome-icon :icon="['fas', 'file']" class="tabs-icon mr-2" /><span>Escritos</span>
                        </a>
                    </li>
                </ul>
            </div>
            <UserTabContent :activeTab="activeTab" :user="user" />
        </div>
    </div>

</template>