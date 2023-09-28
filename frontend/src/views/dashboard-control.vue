<template>
  <div>
    <TemperatureControl />
    <div v-for="pool in pools" :key="pool.id">
      <TemperatureGraph v-if="pool.chartData" :chartData="pool.chartData" :poolName="pool.name" />
    </div>    
  </div>
</template>

<script>
import axios from 'axios';
import TemperatureControl from '@/components/TemperatureControl.vue';
import TemperatureGraph from '@/components/TemperatureGraph.vue';

export default {
  components: {
    TemperatureControl,
    TemperatureGraph,
  },
  data() {
    return {
      pools: [
        { id: 1, name: 'Pool 1', temperature: null, chartData: null },
        { id: 2, name: 'Pool 2', temperature: null, chartData: null },
        { id: 3, name: 'Pool 3', temperature: null, chartData: null },
        { id: 4, name: 'Pool 4', temperature: null, chartData: null },
        { id: 5, name: 'Pool 5', temperature: null, chartData: null },
      ],
    };
  },
  async mounted() {
    this.pools.forEach((pool) => {
      pool.chartData = {
        labels: [], 
        datasets: [{ label: 'Temperature', data: [] }]
      };
      setInterval(async () => {
        try {
          const response = await axios.get('http://localhost:8000/temperature');
          pool.temperature = response.data.temperature;
          pool.chartData.labels.push(response.data.timestamp);
          pool.chartData.datasets[0].data.push(pool.temperature);
          if (pool.chartData.labels.length > 600) {
            pool.chartData.labels.shift();
            pool.chartData.datasets[0].data.shift();
          }
        } catch (error) {
          console.error(error);
        }
      }, 1000);
    });
  },
};
</script>
