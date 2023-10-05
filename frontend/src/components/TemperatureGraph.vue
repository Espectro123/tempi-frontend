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
      endpoint: String
    },
    setup(props) {
      const reRenderKey = ref(0);
      const chartData = ref({
      labels: [],
      datasets: [{ data: [] }]
      });
      const options = {
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
            min: -10,
            max: 50
          }
        }
      };

      const updateXAxis = () => {
        options.scales.x.min = new Date().getTime() - 30 * 60 * 1000;
        options.scales.x.max = new Date().getTime() + 30 * 60 * 1000;
        console.log('Updated Time Scale:', options.scales.x);
        reRenderKey.value++;
        console.log('Updated reRenderKey:', reRenderKey.value);
      };

      const formatDate = (date) => {
        const d = new Date(date);
        const formattedDate = `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}T${String(d.getHours()).padStart(2, '0')}:${String(d.getMinutes()).padStart(2, '0')}:00.000Z`;
        return formattedDate;
      };

      const fetchData = async () => {
        try {
          const data = await getTemperatureData(props.endpoint);
          console.log('Fetched Data:', data);
          //onst newLabels = [...chartData.value.labels, new Date(data.timestamp).toISOString()];
          const newLabels = [...chartData.value.labels, formatDate(data.timestamp)];
          const newData = [...chartData.value.datasets[0].data, data.temperature];

          chartData.value.labels = newLabels;
          chartData.value.datasets[0].data = newData;

          chartData.value.datasets[0].label = 'Temperature';
          chartData.value.datasets[0].fill = false;
          chartData.value.datasets[0].borderColor = 'rgb(254, 0, 125)';
          chartData.value.datasets[0].tension = 0.1;

          // Set a larger point radius and a different color for the first data point
          chartData.value.datasets[0].pointRadius = newLabels.map((_, index) => index === 0 ? 10 : 5);  // 10 for the first point, 5 for the rest
          chartData.value.datasets[0].pointBackgroundColor = newLabels.map((_, index) => index === 0 ? 'red' : 'blue');  // red for the first point, blue for the rest

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
  