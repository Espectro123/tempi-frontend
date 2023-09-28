<template>
  <div>
    <h3>{{ poolName }}</h3>
    <LineChart ref="chartInstance" :data="chartData" :options="chartOptions" />
  </div>
</template>

<script>
import { Chart } from 'chart.js';
import 'chartjs-adapter-date-fns';
import { ref } from 'vue';
import { LineChart } from 'vue-chart-3';
import { CategoryScale, LinearScale, Title, TimeScale  } from 'chart.js';

Chart.register(CategoryScale, LinearScale, Title, TimeScale );

export default {
  props: {
    poolName: { type: String, required: true },
    chartData: { type: Object, required: true }
  },
  components: { LineChart },
  setup() {
    const chartInstance = ref(null);

    const chartOptions = ref({
      scales: {
        x: { 
          type: 'time',
          time: { unit: 'minute', displayFormats: { minute: 'HH:mm' }},
          title: { display: true, text: 'Time' },
          min: new Date(Date.now() - 60 * 60 * 1000),
          max: new Date(),
        },
        y: { 
          type: 'linear',
          title: { display: true, text: 'Temperature' },
          min: 0,
          max: 50
        }
      }
    });

    function updateChartOptions() {
      chartOptions.value.scales.x.min = new Date(Date.now() - 60 * 60 * 1000);
      chartOptions.value.scales.x.max = new Date();
      if (chartInstance.value) {
        chartInstance.value.update('none');
      }
    }

    setInterval(updateChartOptions, 60000);

    return { chartOptions, chartInstance };
  },
  mounted() {
    this.chartInstance = this.$refs.chartInstance;
  }
};
</script>
