<script setup>

</script>

<template>
    <form class="mx-3">
        <h1 class="title is-3">Subir un escrito</h1>
        <div class="columns is-vcentered mx-4">
            <div class="file has-name">
                <label class="file-label">
                    <input class="file-input" type="file" name="resume">
                    <span class="file-cta">
                    <span class="file-icon">
                        <font-awesome-icon :icon="['fas', 'upload']" class="tabs-icon mr-2" />
                    </span>
                    <span class="file-label">
                        Selecciona un archivo
                    </span>
                    </span>
                    <span class="file-name">
                    Screen Shot 2017-07-29 at 15.54.25.png
                    </span>
                </label>
                </div>
            <div class="column is-fout-fifths">
                <p class="is-size-5 mx-4">Haz click y selecciona en un archivo para subir un escrito a tu perfil</p>
            </div>
        </div>
    </form>
</template>
