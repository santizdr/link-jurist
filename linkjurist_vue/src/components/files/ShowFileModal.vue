<script setup>
    import axios from 'axios';
    import VuePdfEmbed from 'vue-pdf-embed';
    import 'vue-pdf-embed/dist/style/index.css';
    import 'vue-pdf-embed/dist/style/annotationLayer.css';
    import 'vue-pdf-embed/dist/style/textLayer.css';

    const emit = defineEmits(['closeFileModal']);
    const props = defineProps(['fileid', 'showFileModal', 'file']);

    function purchaseFile(id) {
        axios.get("/api/purchasefile/" + id, { responseType: 'arraybuffer'})
        .then(response => {
            const file = new Blob([response.data], { type: 'application/pdf' });
            const fileURL = URL.createObjectURL(file);
            window.open(fileURL, '_blank');
            emit('closeFileModal', true)
        })
        .catch(error => {
            console.log("Error: ", error);
        })
    }

    function closeFileModal() {
        emit('closeFileModal', false);
    }
</script>

<template>
    <div class="modal" :class="{'is-active' : showFileModal }">
        <div class="modal-background"></div>
        <div class="modal-card" style="width: 1080px;">
            <header class="modal-card-head">
                <p class="modal-card-title">Vista previa</p>
                <a @click="closeFileModal()" class="delete" aria-label="close"></a>
            </header>
            <section class="modal-card-body">
                <VuePdfEmbed 
                    annotation-layer text-layer 
                    :source="file"
                />
            </section>
            <footer class="modal-card-foot modal-footer-btns">
                <div class="field is-grouped">
                    <div class="control">
                        <a @click="closeFileModal()" class="button primary-form-button">Cancelar</a>
                    </div>
                    <div class="control">
                        <a @click="purchaseFile(props.fileid)" class="button secondary-form-button">Confirmar</a>
                    </div>
                </div>
            </footer>
        </div>
    </div>
</template>
