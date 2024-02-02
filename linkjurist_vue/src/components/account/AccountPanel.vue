<script setup>
    import AccountHeader from '../account/AccountHeader.vue'
    import AccountTabs from '../account/AccountTabs.vue'
    import { useAuthStore } from '@/stores/auth';
    
    const authStore = useAuthStore();

</script>


<template>
    <section class="section mt-4">
      <div v-if="authStore.user.isAuthenticated" class="columns is-centered">
      <div class="column is-three-quarters-desktop">
          <div class="box">
            <AccountHeader :account="authStore.account" />
            <AccountTabs :account="authStore.account" />
        </div>
      </div>
  </div>
  </section>
</template>
