<script setup>
    import UserPanel from '@/components/user/UserPanel.vue'
    import { useDetailsStore } from '@/stores/details';

    const detailsStore = useDetailsStore();
</script>

<template>
  <main>
    <UserPanel :user="detailsStore.user"/>
  </main>
</template>
