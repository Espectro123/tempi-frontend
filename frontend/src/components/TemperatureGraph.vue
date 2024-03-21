<template>
    <div>
      <line-chart :key="reRenderKey" :chart-data="chartData" :options="options"></line-chart>
    </div>
</template>
  
<script>
  import { ref, onMounted } from 'vue';
  import "chartjs-adapter-date-fns";

  import { Chart, registerables } from 'chart.js';
  import 'chartjs-plugin-zoom';
  Chart.register(...registerables);


  import { LineChart } from 'vue-chart-3';
  import { getTemperatureData } from '../services/temperatureService.js';

  import { format } from 'date-fns';
  
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
        plugins: {
          zoom: {
            pan: {
              enabled: true,
              mode: 'x',
            },
            zoom: {
              wheel: {
                enabled: true,
              },
              pinch: {
                enabled: true,
              },
              mode: 'x',
            },
          },
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

      const formatDate = () => {
        
        const currentDate = new Date();
        const formattedDate = format(currentDate, "yyyy-MM-dd'T'HH:mm:ss.SSS'Z'");
        console.log(formattedDate);

        return formattedDate;
      };

      const fetchData = async () => {
        try {
          const data = await getTemperatureData(props.endpoint);
          const newLabels = [...chartData.value.labels, formatDate(data.timestamp)];
          const newData = [...chartData.value.datasets[0].data, data.temperature];
          options.value.title.text = props.label;

          chartData.value.labels = newLabels;
          chartData.value.datasets[0].data = newData;

          chartData.value.datasets[0].label = 'Temperature';
          chartData.value.datasets[0].fill = false;
          chartData.value.datasets[0].borderColor = 'rgb(0, 126, 254)';
          chartData.value.datasets[0].backgroundColor = 'rgb(0, 126, 254)';
          chartData.value.datasets[0].tension = 0.1;
          chartData.value.datasets[0].pointRadius = 2;  
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
  
