<script setup>
    import UserHeader from '@/components/user/UserHeader.vue'
    import UserTabs from '@/components/user/UserTabs.vue'

    const { props } = defineProps(['user']);
</script>

<template>
  <section class="section mt-4">
    <div class="columns is-centered">
      <div class="column is-three-quarters-desktop">
        <div class="box">
          <UserHeader :user="user" />
          <UserTabs :user="user" />
        </div>
      </div>
    </div>
  </section>
</template>

