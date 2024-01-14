<script setup>
    import { useAuthStore } from '@/stores/auth';
    const store = useAuthStore();
</script>

<template>
<nav class="navbar main-bg-color is-spaced" role="navigation" aria-label="main navigation">
  <div class="navbar-brand">
    <RouterLink to="/" class="navbar-item is-size-4-desktop is-size-5-touch mr-5">
      <img src="../assets/logo.png" width="58" height="112">
      <!-- <i class="fa-solid fa-scale-balanced"></i> -->
      <span class="has-text-weight-medium is-hidden-touch secondary-text-color">Link Jurist</span>
      <span class="has-text-weight-normal is-hidden-desktop secondary-text-color">Link Jurist</span>
    </RouterLink>

    <!-- <a class="navbar-item is-size-4-desktop is-size-5-touch mr-5">
      <img src="../assets/logo.png" width="58" height="112">
      <span class="has-text-weight-medium is-hidden-touch secondary-text-color">Link Jurist</span>
      <span class="has-text-weight-normal is-hidden-desktop secondary-text-color">Link Jurist</span>
    </a> -->

    <a role="button" class="navbar-burger white-text" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample" @click="showMobileMenu = !showMobileMenu">
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
    </a>
  </div>

  <div id="navbarMenu" class="navbar-menu" :class="{ 'is-active': showMobileMenu }">
    <div v-if="store.authenticated" class="navbar-start">
      <!-- ENLACES PARA PANTALLA GRANDE -->
      <RouterLink to="/" class="navbar-item white-text is-hidden-touch mx-3">Inicio</RouterLink>
      <RouterLink to="/cases" class="navbar-item white-text is-hidden-touch mx-3">Casos</RouterLink>
      <RouterLink to="/files" class="navbar-item white-text is-hidden-touch mx-3">Escritos</RouterLink>

      <!-- ENLACES PARA MOVIL -->
      <RouterLink to="/" class="navbar-item is-hidden-desktop">Inicio</RouterLink>
      <RouterLink to="/cases" class="navbar-item is-hidden-desktop">Casos</RouterLink>
      <RouterLink to="/files" class="navbar-item is-hidden-desktop">Escritos</RouterLink>
      <!-- <RouterLink to="/login" class="navbar-item is-hidden-desktop">Identificate</RouterLink> -->
    </div>

    <div v-else class="navbar-start">
      <!-- ENLACES PARA PANTALLA GRANDE -->
      <RouterLink to="/" class="navbar-item white-text is-hidden-touch mx-3">Inicio</RouterLink>
      
      <!-- ENLACES PARA MOVIL -->
      <RouterLink to="/" class="navbar-item is-hidden-desktop">Inicio</RouterLink>
      <RouterLink to="/login" class="navbar-item is-hidden-desktop">Identificate</RouterLink>
    </div>

    <div class="navbar-end">
      <div v-if="store.authenticated" class="navbar-item has-dropdown is-hoverable">
        <a class="navbar-link white-text is-hidden-touch">
          Menú
        </a>
        <a class="navbar-link is-hidden-desktop">
          Menú
        </a>

        <div class="navbar-dropdown is-right">

          <RouterLink to="/account" class="navbar-item">Mi cuenta</RouterLink>
          <a v-on:click="store.changeAuthenticatedVal()" class="navbar-item">Cerrar sesión</a>

        </div>
      </div>
      <div v-else class="buttons buttons are-normal is-hidden-touch">
        <RouterLink id="signup_btn" class="button is-rounded secondary-bg-color has-text-weight-semibold white-text is-responsive navbar-button" to="signup" style="width: 150px;">Registro</RouterLink>
        <RouterLink id="login_btn" class="button is-rounded white-bg-color has-text-weight-semibold is-responsive navbar-button main-text-color" to="login" style="width: 150px;">Iniciar sesión</RouterLink>
      </div>



      <!-- <div class="navbar-item is-hidden-touch">
        <div v-if="!store.authenticated" class="buttons buttons are-normal">
          <RouterLink id="signup_btn" class="button is-rounded secondary-bg-color has-text-weight-semibold white-text is-responsive navbar-button" to="signup" style="width: 150px;">Registro</RouterLink>
          <RouterLink id="login_btn" class="button is-rounded white-bg-color has-text-weight-semibold is-responsive navbar-button main-text-color" to="login" style="width: 150px;">Iniciar sesión</RouterLink>
        </div>
        <div v-else>
          <a v-on:click="store.changeAuthenticatedVal()" class="button is-rounded secondary-bg-color has-text-weight-semibold white-text is-responsive navbar-button">Cerrar sesión</a>
        </div>
      </div> -->

    </div>
  </div>
</nav>
  
</template>

<script>
import { RouterLink } from 'vue-router';

export default {
    data() {
        return {
            showMobileMenu: false,
            handleDropdownMenu: false,
        };
    },
    components: { RouterLink }
}

</script>