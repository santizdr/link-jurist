<script setup>
import Navbar from './components/Navbar.vue'
import { useUserStore } from '@/stores/user';
const store = useUserStore();
</script>

<template>
  <header>
    <Navbar></Navbar>
  </header>
  <RouterView />
</template>

<style scoped></style>
