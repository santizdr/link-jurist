<script setup>
    import VuePdfEmbed from 'vue-pdf-embed'
    import 'vue-pdf-embed/dist/style/index.css'
    import 'vue-pdf-embed/dist/style/annotationLayer.css'
    import 'vue-pdf-embed/dist/style/textLayer.css'

    const emit = defineEmits(['closeFileModal'])
    const props = defineProps(['showFileModal', 'file']);
</script>


<template>
    <div class="modal" :class="{'is-active' : showFileModal }">
        <div class="modal-background"></div>
        <div class="modal-card" style="width: 1080px;">
            <header class="modal-card-head">
                <p class="modal-card-title">Vista previa</p>
                <a @click="$emit('closeFileModal')" class="delete" aria-label="close"></a>
            </header>
            <section class="modal-card-body">
                <VuePdfEmbed 
                    annotation-layer text-layer 
                    :source="file"
                />
            </section>
        </div>
    </div>
</template>
