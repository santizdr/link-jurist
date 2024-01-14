<script setup>
    import { useAuthStore } from '@/stores/auth';
    const store = useAuthStore();
</script>


<template>
  <section class="section mt-6">
    <div class="columns is-centered">
      <!-- CARTEL DE BIENVENIDA -->
      <div v-if="!store.authenticated" class="column is-three-fifths-desktop">
        <div class="box">
          <h1 class="title">Bienvenido a <span class="secondary-text-color">Link Jurist</span></h1>
          <h2 class="subtitle mt-3">Lorem ipsum dolor sit am et consectetur, adipisicing elit. Quae soluta dolor maxime adipisci at quos quis quas corrupti voluptatum? Maxime nesciunt quos natus est eligendi quia repellat distinctio odit accusamus!</h2>
          <h2 class="subtitle mt-3">Lorem ipsum dolor sit amet consectetur, adipisicing elit. Quae soluta dolor maxime adipisci at quos quis quas corrupti voluptatum? Maxime nesciunt quos natus est eligendi quia repellat distinctio odit accusamus!</h2>

        </div>
      </div>
      <!-- LISTADO DE PUBLICACIONES -->
      <div v-else class="column is-two-fifths-desktop">
        <div class="box">
          <div class="card">
            <div class="card-image">
              <figure class="image is-4by3">
                <img src="https://bulma.io/images/placeholders/1280x960.png" alt="Placeholder image">
              </figure>
            </div>
            <div class="card-content">
              <div class="media">
                <div class="media-left">
                  <figure class="image is-48x48">
                    <img src="https://bulma.io/images/placeholders/96x96.png" alt="Placeholder image">
                  </figure>
                </div>
                <div class="media-content">
                  <p class="title is-4">John Smith</p>
                  <p class="subtitle is-6">@johnsmith</p>
                </div>
              </div>

              <div class="content">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                Phasellus nec iaculis mauris. <a>@bulmaio</a>.
                <a href="#">#css</a> <a href="#">#responsive</a>
                <br>
                <time datetime="2016-1-1">11:09 PM - 1 Jan 2016</time>
              </div>
            </div>
          </div>       
        </div>
      </div>
    </div>
  </section>
</template>

<style>

</style>