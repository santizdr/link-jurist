<script setup>
import Navbar from './components/Navbar.vue'
import Login from './views//LogIn.vue';
import { useAuthStore } from '@/stores/auth';
const store = useAuthStore();
</script>

<template>
  <header>
    <Navbar></Navbar>
  </header>
  <RouterView />
  <RouterLink to="/"></RouterLink>
  <RouterLink to="/signup"></RouterLink>
</template>

<style scoped></style>
