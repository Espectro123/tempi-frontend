<template>
    <div>
      <input type="number" v-model="targetTemp" />
      <button @click="setTemperature">Set Target Temperature</button>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        targetTemp: 20,
      };
    },
    methods: {
      setTemperature() {
        // Make API call to set target temperature in the backend
      },
    },
  };
  </script>
  