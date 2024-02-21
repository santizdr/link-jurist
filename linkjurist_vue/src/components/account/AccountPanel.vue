<script setup>
    import AccountHeader from '@/components/account/AccountHeader.vue'
    import AccountTabs from '@/components/account/AccountTabs.vue'

    const { props } = defineProps(['viewData']);
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
