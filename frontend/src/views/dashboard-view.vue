 <template>
    <div class="dashboard">
        <header class="header">
            <!-- Header content here -->
        </header>
        <div class="main-content">
            <aside class="sidebar">
              <button class="new-experiment-button">
                <i class="fas fa-plus"></i> New Experiment
              </button>
              <div class="experiment-summary-panel">
                  <h3>Summary</h3>
                  <!-- Panel content here -->
              </div>
              <button class="export-data-button">
                  Export data to USB
              </button>
            </aside>
            <section class="graphs">
                    <div class="row">
                        <temperature-graph v-for="endpoint in endpoints.slice(0, 3)" :key="endpoint" :endpoint="endpoint"></temperature-graph>
                    </div>
                    <div class="row">
                        <temperature-graph v-for="endpoint in endpoints.slice(3)" :key="endpoint" :endpoint="endpoint"></temperature-graph>
                    </div>
                </section>
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

  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;  /* Include padding and border in element's total width and height */
  }

  body, html {
    margin: 0;
    padding: 0;
  }
  
  .dashboard {
      display: flex;
      flex-direction: column;
      height: 100vh;
      margin: 0;
      padding: 0;
  }
  
  .header {
      /* Style for header */
      background-color: #6d83ff;
      color: rgb(117, 172, 255);
      padding: 20px;
      text-align: center;
      width: 100%;
  }
  
  .main-content {
      display: flex;
      flex: 1;
      max-width: 100%;
      margin: 0;
      overflow-x: hidden;
  }
  
  .sidebar {
      /* Style for sidebar */
      background-color: #f4f4f4;
      width: 200px;
      padding: 20px;
      box-shadow: 2px 0 5px rgba(0,0,0,0.1);
  }
  
  .graphs {
      display: flex;
      flex-direction: column;
      flex: 1;
      padding: 20px;
  }
  
  .row {
      display: flex;
      justify-content: space-around;
      margin-bottom: 20px;
      flex-wrap: wrap;
  }
  
  .temperature-graph {
      /* Adjust width as per your requirement */
      width: 30%;
      flex-shrink: 0;
  }

  .new-experiment-button, .export-data-button {
    display: block;
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: none;
    border-radius: 4px;
    background-color: #008CBA; /* Change color as needed */
    color: white;
    cursor: pointer;
    font-size: 16px;
    text-align: left;
  }

  .new-experiment-button i {
    margin-right: 8px; /* Adds some space between the icon and text */
  }

  .experiment-summary-panel {
    padding: 10px;
    background-color: #f9f9f9; /* Change color as needed */
    border: 1px solid #ddd;
    border-radius: 4px;
    margin-bottom: 10px;
  }
  </style>
  

  