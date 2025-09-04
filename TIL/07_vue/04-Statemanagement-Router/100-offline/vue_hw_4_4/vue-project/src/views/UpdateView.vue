<template>
  <div>
    <p>데이터 수정 페이지</p>
    <p>이름: {{ name }}</p>
    <p>잔고: {{ account.balance }}</p>
    <button @click="addBalance">+</button>
  </div>
</template>

<script setup>
import { useBalanceStore } from '@/stores/balance';
import { computed } from 'vue';

const props = defineProps({
  name: {
    type: String,
    required: true,
  }
})

const name = props.name

const store = useBalanceStore()

const account = computed(() => store.getByName(name))

function addBalance() {
  store.increaseBalance(name)
}
</script>

<style scoped>
p:first-of-type {
  font-size: 18px;
  font-weight: bold;
}
</style>