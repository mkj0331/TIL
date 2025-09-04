<template>
  <div class="card">
    <p>이름: {{ account.name }}</p>
    <p>잔액: {{ account.balance }}</p>
    <RouterLink class='btn' :to="{name: 'update', params: {name: account.name}}">updateBalance</RouterLink>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';

defineProps({
  account: {
    type: Object,
    required: true,
  },
})
</script>

<style scoped>
.card {
  border: 1px solid #ddd;
  padding: 16px;
  margin-bottom: 12px;
  border-radius: 6px;
  background-color: #fff;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
}

.btn {
  display: inline-block;
  margin-top: 8px;
  padding: 6px 12px;
  background-color: #007bff;
  color: #fff;
  border-radius: 4px;
  text-decoration: none;
  font-size: 14px;
  font-weight: bold;
  transition: background-color 0.2s ease;
}
</style>