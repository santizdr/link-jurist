<script setup>
    const { props } = defineProps(['user']);
</script>

<template>
    <div class="card my-5">
        <div class="columns">
            <div class="column is-narrow ml-5 my-2 is-flex is-align-items-center">
                <div class="card-image">
                    <figure class="image is-128x128">
                        <img src="https://bulma.io/images/placeholders/128x128.png">
                    </figure>
                </div>
            </div>
            <div class="column">
                <div class="card-content">
                    <div class="content">
                        <h2 class="title is-4">
                            {{ user.firstname }} {{ user.lastname }}
                        </h2>
                        <hr>
                        <p class="subtitle is-5"><span class="secondary-text-color">Email personal: </span>{{ user.email }}</p>
                        <span class="tag is-medium is-info mr-2">Derecho civil</span>
                        <span class="tag is-medium is-success mr-2">Derecho penal</span>
                        <span class="tag is-medium is-warning mr-2">Derecho laboral</span>
                    </div>
                </div>
            </div>
        </div>
    </div>

</template>