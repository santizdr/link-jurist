<script setup>
    import { ref } from 'vue'

    const selected = ref([]);
    const emit = defineEmits(['handleSelectTag'])

    function selectTag(id) {
        const index = selected.value.indexOf(id);
        if (index === -1) {
            selected.value.push(id);
        } else {
            selected.value.splice(index, 1);
        }
        emit('handleSelectTag', id);
    }

</script>

<template>
    Añade especialidades
    <div class="my-1">
        <a @click="selectTag(1)" class="mr-3 mb-2 button is-rounded tag-1 black-text" :class="{ 'has-text-weight-semibold': selected.includes(1) }">Derecho penal</a>
        <a @click="selectTag(2)" class="mr-3 mb-2 button is-rounded tag-2 black-text" :class="{ 'has-text-weight-semibold': selected.includes(2) }">Derecho civil</a>
        <a @click="selectTag(3)" class="mr-3 mb-2 button is-rounded tag-3 black-text" :class="{ 'has-text-weight-semibold': selected.includes(3) }">Derecho laboral</a>
        <a @click="selectTag(4)" class="mr-3 mb-2 button is-rounded tag-4 black-text" :class="{ 'has-text-weight-semibold': selected.includes(4) }">Derecho mercantil</a>
        <a @click="selectTag(5)" class="mr-3 mb-2 button is-rounded tag-5 black-text" :class="{ 'has-text-weight-semibold': selected.includes(5) }">Derecho administrativo</a>
        <a @click="selectTag(6)" class="mr-3 mb-2 button is-rounded tag-6 black-text" :class="{ 'has-text-weight-semibold': selected.includes(6) }">Derecho internacional</a>
    </div>
</template>