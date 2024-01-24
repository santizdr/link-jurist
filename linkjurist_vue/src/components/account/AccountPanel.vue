<script setup>
    import AccountHeader from '../account/AccountHeader.vue'
    import AccountTabs from '../account/AccountTabs.vue'

    import { useUserStore } from '@/stores/user';
    const store = useUserStore();

</script>


<template>
    <section class="section mt-4">
      <div v-if="store.user.isAuthenticated" class="columns is-centered">
      <div class="column is-three-quarters-desktop">
          <div class="box">
            <AccountHeader :account="store.account" />
            <AccountTabs :account="store.account" />
        </div>
      </div>
  </div>
  </section>
</template>
