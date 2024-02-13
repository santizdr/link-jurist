<script setup>
    import AccountPanel from '@/components/account/AccountPanel.vue'   

    import { useAuthStore } from '@/stores/auth';

    const authStore = useAuthStore();
</script>

<template>
  <main>
    <AccountPanel :viewData="authStore" />
  </main>
</template>
