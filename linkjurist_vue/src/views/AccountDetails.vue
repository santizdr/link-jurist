<script setup>
  import AccountPanel from '@/components/account/AccountPanel.vue'   

  import { useDetailsStore } from '@/stores/details';

  const detailsStore = useDetailsStore();
</script>

<template>
  <main>
    <AccountPanel :viewData="detailsStore" />
  </main>
</template>
