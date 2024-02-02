<script setup>
    import { useIndexStore } from '@/stores/index';
    import AccountCard from '../home/AccountCard.vue'

    const indexStore = useIndexStore();
</script>

<template>
    <div class="box">
        <div v-if="indexStore.contacts.length > 0">
            <div class="mb-4">
                <h1 class="is-size-5 has-text-weight-semibold">
                    Tus contactos
                </h1>
            </div>
            <hr class="my-3">
            <div class="my-3">
                <AccountCard v-for="account in indexStore.contacts" :key="account.id" :account="account" />
            </div>
        </div>

        <div v-else>
            <div class="mb-4">
                <h1 class="is-size-5 has-text-weight-semibold">
                    Cuentas recomendadas
                </h1>
            </div>
            <hr class="my-3">
            <div class="my-3">
                <AccountCard v-for="account in indexStore.contact_suggestions" :key="account.id" :account="account" />
            </div>
        </div>




    </div>
</template>