<template>
  <div>
    <p>자식 페이지</p>
    <p>{{ child.name }}</p>
  </div>
</template>

<script setup>
const props = defineProps({
  child: {
    type: Object,
    required: true
  },
})
</script>

<style scoped>
div {
  background-color: antiquewhite;
  border: 1px solid black;
  padding: 12px;
  text-align: center;
  margin: 12px 0;
}

p:first-of-type {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 8px;
}
</style>