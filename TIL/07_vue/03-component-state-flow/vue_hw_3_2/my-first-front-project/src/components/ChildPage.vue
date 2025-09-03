<template>
  <div>
    <h3>자식 페이지입니다.</h3>
    <p>name: {{ myInfo.name }}</p>
    <p>age: {{ myInfo.age }}</p>
  </div>
</template>

<script setup>
const props = defineProps({myInfo: Object})
</script>

<style scoped>
div {
  padding: 10px;
  margin-top: 10px;
  border: 1px solid #ccc;
}
</style>