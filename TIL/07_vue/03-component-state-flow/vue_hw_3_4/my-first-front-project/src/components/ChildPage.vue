<template>
  <div>
    <h3>자식 페이지입니다.</h3>
    <p>이름: {{ myInfo.name }}</p>
    <p>나이: {{ myInfo.age }}</p>
    <p>용돈: {{ myInfo.balance }}</p>
    <button @click='giveMeAllowance'>용돈 더 주세요</button>
  </div>
</template>

<script setup>
const props = defineProps({myInfo: Object})

const emit = defineEmits(['giveMeAllowance'])
const giveMeAllowance = function () {
  emit('giveMeAllowance', props.myInfo.name)
}

</script>

<style scoped>
/* div {
  padding: 10px;
  margin-top: 10px;
  border: 1px solid #ccc;
} */
</style>