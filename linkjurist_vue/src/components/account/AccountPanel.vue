<script setup>
    const { props } = defineProps(['viewData']);

    import AccountHeader from '../account/AccountHeader.vue'
    import AccountTabs from '../account/AccountTabs.vue'
</script>


<template>
  <section class="section mt-4">
    <div class="columns is-centered">
      <div class="column is-three-quarters-desktop">
        <div class="box">
          <AccountHeader :account="viewData.account" />
          <AccountTabs :viewData="viewData" />
        </div>
      </div>
    </div>
  </section>
</template>
