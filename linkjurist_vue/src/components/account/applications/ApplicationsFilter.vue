<script setup>
    import { ref } from 'vue'

    const emit = defineEmits(['filterApplications'])
    const applicationType = ref('all')

    function handleApplicationsFilter() {
        emit('filterApplications', applicationType.value);
    }

</script>

<template>
    <div>
        <h1 class="title is-4">Filtrar</h1>
            <div class="field">
                <label class="label">Tipo de solicitud</label>
                <div class="control is-expanded">
                    <div class="select is-fullwidth">
                        <select v-model="applicationType">
                            <option value="all">Todos</option>
                            <option value="request">Mis solicitudes a otros casos</option>
                            <option value="applicant">Solicitudes a mis casos</option>
                        </select>
                    </div>
                </div>
            </div>

        <div class="field is-grouped is-grouped-right">
            <div class="control">
                <a @click="handleApplicationsFilter()" class="button secondary-form-button">Filtrar</a>
            </div>
        </div>
    </div>
    <hr>
</template>