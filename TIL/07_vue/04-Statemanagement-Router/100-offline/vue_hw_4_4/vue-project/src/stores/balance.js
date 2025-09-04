import { defineStore } from "pinia";
import { ref } from "vue";

export const useBalanceStore = defineStore('balance', () => {
  const balances = ref([
    {name: '김하나', balance: 100000},
    {name: '김두리', balance: 10000},
    {name: '김서이', balance: 100},
  ])

  function getByName(name) {
    return balances.value.find((acc) => acc.name === name)
  }

  function increaseBalance(name) {
    const account = getByName(name);
    if (account) {
      account.balance += 1000;
    }
  }
  return {balances, getByName, increaseBalance}
})