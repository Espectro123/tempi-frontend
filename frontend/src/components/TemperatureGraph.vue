<template>
  <div>
    <line-chart :key="reRenderKey" :chart-data="chartData" :options="options"></line-chart>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import "chartjs-adapter-date-fns";

import { Chart, registerables } from 'chart.js';
Chart.register(...registerables);


import { LineChart } from 'vue-chart-3';
import { getTemperatureData } from '../services/temperatureService.js';


export default {
  name: 'TemperatureGraph',
  components: {
    LineChart
  },
  props: {
    endpoint: String,
    label: String
  },
  setup(props) {
    const reRenderKey = ref(0);
    const chartData = ref({
    labels: [],
    datasets: [{ data: [] }]
    });
    const options = ref({
      title: {
        display: true,
        text: props.label
      },
      scales: {
        x: {
          type: 'time',
          adapters: {
            date: {
              library: 'date-fns', // specify the library here
            },
          },
          time: {
            unit: 'minute',
            displayFormats: {
              minute: 'HH:mm'
            }
          },
          min: new Date().getTime() - 30 * 60 * 1000,
          max: new Date().getTime() + 30 * 60 * 1000
        },
        y: {
          min: 5,
          max: 35,
          ticks: {
            stepSize: 5  // This will cause the y-axis to increment by 5
          }
        }
      }
    });

    const updateXAxis = () => {
      options.value.scales.x.min = new Date().getTime() - 30 * 60 * 1000;
      options.value.scales.x.max = new Date().getTime() + 30 * 60 * 1000;
      reRenderKey.value++;
    };

    const fetchData = async () => {
      try {
        const [temperatureData, timestamp] = await getTemperatureData(props.endpoint);
        const newLabels = [...chartData.value.labels, timestamp];
        const newData = [...chartData.value.datasets[0].data, temperatureData];
        options.value.title.text = props.label;

        chartData.value.labels = newLabels;
        chartData.value.datasets[0].data = newData;

        chartData.value.datasets[0].label = 'Temperature';
        chartData.value.datasets[0].fill = false;
        chartData.value.datasets[0].borderColor = 'rgb(0, 126, 254)';
        chartData.value.datasets[0].backgroundColor = 'rgb(0, 126, 254)';
        chartData.value.datasets[0].tension = 0.2;
        chartData.value.datasets[0].pointRadius = 4;  
        chartData.value.datasets[0].pointBackgroundColor = 'blue';


        console.log('Updated Chart Data:', chartData.value);
        updateXAxis();

      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    onMounted(() => {
        console.log('Component Mounted');
        fetchData();
        setInterval(fetchData, 60000);
      });

      return { chartData, options, reRenderKey };
    }
  };
</script>