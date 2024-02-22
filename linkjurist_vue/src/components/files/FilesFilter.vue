<script setup>
    import axios from 'axios';
    import { ref } from 'vue';
    import { useFilesStore } from '@/stores/files'

    const filesStore = useFilesStore()
        

    const error = ref({
        field: "",
        message: "",
    });

    const searchForm = ref({
        input: "",
    }) 

    const filterForm = ref({
        locality: "",
        speciality: "",
    }) 

    function submitSearch() {
        error.value = {
            field: "",
            message: "",
        }

        if (searchForm.value.input === "") {
            error.value.field = "search";
            error.value.message = "Introduce texto antes de buscar";
        }

        if (error.value.field === '' && error.value.message === '') {
            axios.post("/api/searchfiles/", searchForm)
                .then(response => {
                    filesStore.files = response.data.files;
                })
                .catch(error => {
                    console.log("Error: ", error);
                })
        }
    }

    function submitFilter() {
        error.value = {
            field: "",
            message: "",
        }

        if (filterForm.value.locality === "" && filterForm.value.speciality === "") {
            error.value.field = "filter";
            error.value.message = "No se ha aplicado ningún filtro";
        }

        if (error.value.field === '' && error.value.message === '') {
            axios.post("/api/filterfiles/", filterForm)
                .then(response => {
                    filesStore.files = response.data.files;
                })
                .catch(error => {
                    console.log("Error: ", error);
                })
        }
    }
</script>

<template>
    <div class="box">
        <form>
            <h1 class="title is-4">Buscar</h1>
            <div class="control my-5">
                <input class="input" type="text" :class="{ 'input-error' : error.field === 'search' }" v-model="searchForm.input">
                <span v-if="error.field === 'search'" class="has-text-danger"> {{ error.message }}</span>         
            </div>   
            <div class="field is-grouped is-grouped-right">
                <div class="control">
                    <a @click.prevent="submitSearch()" class="button secondary-form-button">Buscar</a>
                </div>
            </div>
        </form>
        <form>
            <h1 class="title is-4">Filtros</h1>
            <div class="columns">
                <div class="column is-half">
                    <label class="label">Filtrar por provincia</label>
                    <div class="control is-expanded">
                        <div class="select is-fullwidth">
                            <select v-model="filterForm.locality">
                                <option value="">Nada seleccionado</option>
                                <option value="huelva">Huelva</option>
                                <option value="sevilla">Sevilla</option>
                                <option value="cordoba">Córdoba</option>
                                <option value="jaen">Jaén</option>
                                <option value="malaga">Málaga</option>
                                <option value="almeria">Almería</option>
                                <option value="granada">Granada</option>
                            </select>
                        </div>
                    </div>
                </div>
                <div class="column is-half">
                    <label class="label">Filtrar por especialidad</label>
                    <div class="control is-expanded">
                        <div class="select is-fullwidth">
                            <select v-model="filterForm.speciality">
                                <option value="">Nada seleccionado</option>
                                <option value="1">Derecho penal</option>
                                <option value="2">Derecho civil</option>
                                <option value="3">Derecho laboral</option>
                                <option value="4">Derecho mercantil</option>
                                <option value="5">Derecho administrativo</option>
                                <option value="6">Derecho internacional</option>
                            </select>
                        </div>
                    </div>
                </div>
            </div>
            <span v-if="error.field === 'filter'" class="has-text-danger"> {{ error.message }}</span>         
            <div class="field is-grouped is-grouped-right">
                <div class="control">
                    <a @click.prevent="submitFilter()" class="button secondary-form-button">Filtrar</a>
                </div>
            </div>
        </form>
    </div>
</template>