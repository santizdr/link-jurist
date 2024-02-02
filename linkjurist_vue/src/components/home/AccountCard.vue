<script setup>
    const { props } = defineProps(['account']);
</script>

<template>
    <div>
        <div class="card my-5 mx-2">
            <div class="card-content">
                <div class="media">
                    <div class="media-content">
                        <p class="title is-5">{{ account.name }}</p>
                        <p class="subtitle is-6">{{ account.locality }}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>    
</template>