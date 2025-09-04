<template>
  <div>
    <p>메인 페이지</p>

    <MainPage v-for="account in store.balances" :account="account" />
  </div>
</template>

<script setup>
import { useBalanceStore } from '@/stores/balance';
import MainPage from '@/components/MainPage.vue';

const store = useBalanceStore()

</script>

<style scoped>
p {
  font-size: 20px;
  font-weight: bold;
}
</style>