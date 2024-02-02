<script setup>
import Navbar from './components/Navbar.vue'
import { useAuthStore } from '@/stores/auth';
const authStore = useAuthStore();
</script>

<template>
  <header>
    <Navbar></Navbar>
  </header>
  <RouterView />
</template>

<style scoped></style>
