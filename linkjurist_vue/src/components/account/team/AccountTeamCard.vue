<script setup>
    const { props } = defineProps(['user']);

    const tags = {
        1: "Derecho penal",
        2: "Derecho civil",
        3: "Derecho laboral",
        4: "Derecho mercantil",
        5: "Derecho administrativo",
        6: "Derecho internacional",
    }
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
                            <RouterLink :to="'/user/' + user.id" class="black-text ">{{ user.firstname }} {{ user.lastname }}</RouterLink>
                        </h2>
                        <hr>
                        <p class="subtitle is-5"><span class="secondary-text-color">Email personal: </span>{{ user.email }}</p>
                        <div>
                            <span v-for="tag in user.tags" class="tag is-medium mr-2" :class="'tag-' + tag">{{ tags[tag] }}</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

</template>