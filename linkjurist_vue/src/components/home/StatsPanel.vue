<script setup>
    import { useUserStore } from '@/stores/user';
    const store = useUserStore();
</script>

<template>
    <div class="box">
        <div class="mb-4">
            <h1 class="is-size-5 has-text-weight-semibold">
                Bienvenido a <span class="secondary-text-color">Link Jurist</span> {{ store.user.firstname }}
            </h1>
        </div>
        <hr class="my-3">
        <div class="my-3">
            <h1 class="is-size-6 has-text-weight-semibold my-2">
                Estadísticas de publicaciones:
            </h1>
            <p>Visualizaciones totales: 14502</p>
            <p>Likes totales: 9793</p>
        </div>
        <div class="my-3">
            <h1 class="is-size-6 has-text-weight-semibold my-2">
                Estadísticas de casos:
            </h1>
            <p>Visualizaciones totales: 17085</p>
            <p>Aplicaciones totales: 9602</p>
        </div>
        <div class="my-3">
            <h1 class="is-size-6 has-text-weight-semibold my-2">
                Estadísticas de escritos:
            </h1>
            <p>Descargas totales: 8587</p>
        </div>
    </div>

</template>