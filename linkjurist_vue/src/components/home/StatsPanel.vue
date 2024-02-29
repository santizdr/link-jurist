<script setup>
    import { useAuthStore } from '@/stores/auth';
    const authStore = useAuthStore();

    const props = defineProps(['stats'])
</script>

<template>
    <div class="box">
        <div class="mb-4">
            <h1 class="is-size-5 has-text-weight-semibold">
                Bienvenido a <span class="secondary-text-color">Link Jurist</span> {{ authStore.user.firstname }}
            </h1>
        </div>
        <hr class="my-3">
        <div class="my-3">
            <h1 class="is-size-6 has-text-weight-semibold my-2">
                Estadísticas de publicaciones:
            </h1>
            <p>Visualizaciones totales: {{ props.stats.post_visualizations }}</p>
            <p>Likes totales: {{ props.stats.post_likes }}</p>
        </div>
        <div class="my-3">
            <h1 class="is-size-6 has-text-weight-semibold my-2">
                Estadísticas de casos:
            </h1>
            <p>Visualizaciones totales: {{ props.stats.case_visualizations }}</p>
            <p>Aplicaciones totales: {{ props.stats.case_applications }}</p>
        </div>
        <div class="my-3">
            <h1 class="is-size-6 has-text-weight-semibold my-2">
                Estadísticas de escritos:
            </h1>
            <p>Descargas totales: {{ props.stats.file_downloads }}</p>
        </div>
    </div>

</template>