import { createApp } from 'vue';
import App from './App.vue';
import router from './router/index.js';
//import TemperatureGraph from './components/TemperatureGraph.vue';

const app = createApp(App)
//app.component(TemperatureGraph)
app.use(router)
app.mount('#app')


