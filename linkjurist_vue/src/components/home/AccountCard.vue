<script setup>
    const { props } = defineProps(['account']);
</script>

<template>
    <div>
        <div class="card my-5 mx-2">
            <div class="card-content">
                <div class="media">
                    <div class="media-content">
                        <RouterLink :to="'/account/' + account.id" class="black-text account-card-title has-text-weight-semibold">{{ account.name }}</RouterLink>
                        <p class="subtitle is-6">{{ account.locality }}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>    
</template>