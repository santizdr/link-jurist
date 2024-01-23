<script setup>
    import { useUserStore } from '@/stores/user';
    const store = useUserStore();
</script>

<template>
    <form class="box">
        <h1 class="title is-4">Filtros</h1>
        <div class="columns">
            <div class="column is-half">
                <label class="label">Filtrar por provincia</label>
                <div class="control is-expanded">
                    <div class="select is-fullwidth">
                        <select>
                            <option>Nada seleccionado</option>
                            <option>Huelva</option>
                            <option>Sevilla</option>
                            <option>Córdoba</option>
                            <option>Jaén</option>
                            <option>Málaga</option>
                            <option>Almería</option>
                            <option>Granada</option>
                        </select>
                    </div>
                </div>
            </div>
            <div class="column is-half">
                <label class="label">Filtrar por especialidad</label>
                <div class="control is-expanded">
                    <div class="select is-fullwidth">
                        <select>
                            <option>Nada seleccionado</option>
                            <option>Derecho civil</option>
                            <option>Derecho penal</option>
                            <option>Derecho laboral</option>
                            <option>Derecho mercantil</option>
                            <option>Derecho administrativo</option>
                            <option>Derecho internacional</option>
                        </select>
                    </div>
                </div>
            </div>
        </div>
        <div class="field is-grouped is-grouped-right">
            <div class="control">
                <button class="button is-rounded secondary-form-button">Filtrar</button>
            </div>
        </div>
    </form>
</template>