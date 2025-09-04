<template>
  <div>
    <p>pinia 연습하기</p>
    <ParentPage v-for="fam in familyStore.familyInfo" :family="fam"/>
  </div>
</template>

<script setup>
import ParentPage from './ParentPage.vue';
import { useFamilyStore } from '@/stores/family';

const familyStore = useFamilyStore()

</script>

<style scoped>
p {
  font-size: 28px;
  font-weight: bold;
  margin-bottom: 20px;
}
</style>

