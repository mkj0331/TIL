<template>
  <RouterLink to="/">main</RouterLink>
  <div>
    <p>pinia + router 연습하기</p>
    <RouterView />
  </div>
</template>

<script setup>
import { RouterView } from 'vue-router';


</script>

<style scoped>
p {
  font-size: 28px;
  font-weight: bold;
}
</style>