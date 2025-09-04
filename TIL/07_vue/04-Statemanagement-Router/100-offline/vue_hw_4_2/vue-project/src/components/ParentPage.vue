<template>
  <div>
    <p>부모 컴포넌트</p>
    <p>{{  family.father  }}</p>
    <p>{{  family.mother  }}</p>
    <ChildPage v-for="child in family.children" :child="child"/>
  </div>
</template>

<script setup>
import ChildPage from './ChildPage.vue';

const props = defineProps({
  family: {
    type: Object,
    required: true,
  }
})
</script>

<style scoped>
div {
  background-color: #f9f9f9;
  padding: 24px;
  margin-bottom: 24px;
  border: 1px solid black;
  text-align: center;
}

p:first-of-type {
  font-weight: bold;
  font-size: 24px;
  text-align: center;
  margin-bottom: 12px;
}
</style>