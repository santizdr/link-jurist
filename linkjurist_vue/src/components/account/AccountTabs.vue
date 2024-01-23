<script setup>
    import { ref } from 'vue'
    import { useUserStore } from '@/stores/user';
    import AccountTabContent from '../account/AccountTabContent.vue'

    const store = useUserStore();

    const { props } = defineProps(['account']);

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
                    <li :class="{'is-active': activeTab === 'team-tab'}" @click="handleActiveTab('team-tab')">
                        <a>
                            <font-awesome-icon :icon="['fas', 'user']" class="tabs-icon mr-2" /><span>Equipo</span>
                        </a>
                    </li>
                    <li :class="{'is-active': activeTab === 'case-tab'}" @click="handleActiveTab('case-tab')">
                        <a>
                            <font-awesome-icon :icon="['fas', 'scale-balanced']" class="tabs-icon mr-2" /><span>Casos</span>
                        </a>
                    </li>
                    <li :class="{'is-active': activeTab === 'file-tab'}" @click="handleActiveTab('file-tab')">
                        <a>
                            <font-awesome-icon :icon="['fas', 'file']" class="tabs-icon mr-2" /><span>Escritos</span>
                        </a>
                    </li>

                </ul>
            </div>
                <AccountTabContent :activeTab="activeTab" :account="account" />
        </div>
    </div>

</template>