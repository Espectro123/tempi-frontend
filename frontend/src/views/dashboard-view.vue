<template>
    <div class="dashboard">
      <div v-for="endpoint in endpoints" :key="endpoint" class="chart-container">
        <temperature-graph :endpoint="endpoint"></temperature-graph>
      </div>
    </div>
  </template>
  
  <script>
  import TemperatureGraph from '../components/TemperatureGraph.vue';
  
  export default {
    name: 'DashboardView',
    components: {
        TemperatureGraph
    },
    setup() {
      const endpoints = ['temperature1', 'temperature2', 'temperature3', 'temperature4', 'temperature5'];
      return { endpoints };
    }
  };
  </script>
  
<style scoped>
.dashboard {
  display: flex;
  flex-direction: column;
  gap: 20px;
  padding: 20px;
}
.chart-container {
  width: 100%;
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
}
</style>

  