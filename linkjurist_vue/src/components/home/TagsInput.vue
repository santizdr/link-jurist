<script setup>
    import { ref } from 'vue'

    const emit = defineEmits(['handleSelectTag'])
    const props = defineProps(['formTags'])

    const initialTagValues = {
        1: false,
        2: false,
        3: false,
        4: false,
        5: false,
        6: false,
    };

    const selectedTags = ref(initialTagValues);

    function selectTag(id) {
        switch (id) {
            case 1:
                selectedTags.value[1] = !selectedTags.value[1];
                break;
            case 2:
                selectedTags.value[2] = !selectedTags.value[2];
                break;
            case 3:
                selectedTags.value[3] = !selectedTags.value[3];
                break;
            case 4:
                selectedTags.value[4] = !selectedTags.value[4];
                break;
            case 5:
                selectedTags.value[5] = !selectedTags.value[5];
                break;
            case 6:
                selectedTags.value[6] = !selectedTags.value[6];
                break;
        }

        emit('handleSelectTag', id);
    }
</script>

<template>
    Añade especialidades
    <div class="my-1">
        <a @click="selectTag(1)" class="mr-3 mb-2 button is-rounded tag-1 black-text" :class="{ 'has-text-weight-semibold selected-tag' : selectedTags[1] }">Derecho penal</a>
        <a @click="selectTag(2)" class="mr-3 mb-2 button is-rounded tag-2 black-text" :class="{ 'has-text-weight-semibold selected-tag' : selectedTags[2] }">Derecho civil</a>
        <a @click="selectTag(3)" class="mr-3 mb-2 button is-rounded tag-3 black-text" :class="{ 'has-text-weight-semibold selected-tag' : selectedTags[3] }">Derecho laboral</a>
        <a @click="selectTag(4)" class="mr-3 mb-2 button is-rounded tag-4 black-text" :class="{ 'has-text-weight-semibold selected-tag' : selectedTags[4] }">Derecho mercantil</a>
        <a @click="selectTag(5)" class="mr-3 mb-2 button is-rounded tag-5 black-text" :class="{ 'has-text-weight-semibold selected-tag' : selectedTags[5] }">Derecho administrativo</a>
        <a @click="selectTag(6)" class="mr-3 mb-2 button is-rounded tag-6 black-text" :class="{ 'has-text-weight-semibold selected-tag' : selectedTags[6] }">Derecho internacional</a>
    </div>
</template>