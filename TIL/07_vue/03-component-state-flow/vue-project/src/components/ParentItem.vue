<template>
  <div>
    <p>name: {{ myInfo.name }}</p>
    <p>balance: {{ myInfo.balance }}</p>
    <!-- <button @click="$emit('balanceUpdate', myInfo.name)">+</button> -->
    <button @click="balanceUpdate">+</button>
    <hr>
  </div>
</template>

<script setup>
const props = defineProps({myInfo: Object})
const emit = defineEmits(['balanceUpdate', 'someEvent', 'otherEvent'])
// console.log(props.myInfo)

// 자체적으로, prop받은 데이터를 마음대로 바꾸면 안됨(데이터가 꼬임) -> $emit()
const balanceUpdate = function () {
  // props.myInfo.balance += 1000
  // 엄청 복잡한 로직
  emit('balanceUpdate', props.myInfo.name)
}
</script>

<style scoped>

</style>