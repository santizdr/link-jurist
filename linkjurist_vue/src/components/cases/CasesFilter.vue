<script setup>
    import axios from 'axios';
    import { ref } from 'vue';
    import { useCasesStore } from '@/stores/cases'

    const casesStore = useCasesStore()

    const error = ref({
        field: "",
        message: "",
    });

    const searchForm = ref({
        input: "",
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
            axios.post("/api/searchcases/", searchForm)
                .then(response => {
                    casesStore.cases = response.data.cases;
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
                    <a @click.prevent="submitSearch()" class="button is-rounded secondary-form-button">Buscar</a>
                </div>
            </div>
        </form>
        <form>
            <h1 class="title is-4">Filtros</h1>
            <div class="columns">
                <div class="column is-one-third">
                    <label class="label">Filtrar por tipo de anuncio</label>
                    <div class="control is-expanded">
                        <div class="select is-fullwidth">
                            <select>
                                <option>Nada seleccionado</option>
                                <option>Oferta</option>
                                <option>Demanda</option>
                            </select>
                        </div>
                    </div>
                </div>
                <div class="column is-one-third">
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
                <div class="column is-one-third">
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
    </div>
</template>