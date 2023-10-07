 <template>
    <div class="dashboard">
        <header class="header">
          <h2>Tempi</h2>
        </header>
        <div class="main-content">
            <aside class="sidebar">
              <button class="new-experiment-button"  @click="showNewExperimentModal">
                <i class="fas fa-plus"></i> New Experiment
              </button>
              <new-experiment :show="showModal" @close="showModal = false" @experiment-created="handleExperimentCreated"></new-experiment>
              <div class="experiment-summary-panel">
                  <h3>Summary</h3>
                  <!-- Panel content here -->
              </div>
              <div class="experiment-summary-panel">
                <h5>Data points: 0</h5>
                <h5>Started at: 12/11 12:00</h5>
                <h5>End at: 13/11 14:50</h5>
                <h5>Mean (Cº): 22.5</h5>
                <!-- Panel content here -->
              </div>
              <button class="export-data-button">
                <i class="fas fa-download"></i> Download data
              </button>
            </aside>
            <section class="graphs" v-if="experimentCreated">
              <div class="row">
                <div v-for="(endpoint, index) in endpoints.slice(0, 3)" :key="endpoint" class="temperature-graph-container">
                  <div class="graph-title">Pool {{ index + 1 }}</div>
                  <temperature-graph :endpoint="endpoint"></temperature-graph>
                </div>
              </div>
              <div class="row">
                <div v-for="(endpoint, index) in endpoints.slice(3)" :key="endpoint" class="temperature-graph-container">
                  <div class="graph-title">Pool {{ index + 4 }}</div>
                  <temperature-graph :endpoint="endpoint"></temperature-graph>
                </div>
              </div>
            </section>
            <section v-else class="placeholder-section">
              <p class="placeholder-text">Please create a new experiment to view graphs.</p>
            </section>
          </div>
    </div>
</template>

  <script>
  import TemperatureGraph from '../components/TemperatureGraph.vue';
  import NewExperiment from '../components/NewExperiment.vue';
  
  export default {
    name: 'DashboardView',
    components: {
        TemperatureGraph,
        NewExperiment 
    },
    data(){
      return{
        experimentCreated: false,
        showModal: false,
      };
    },
    setup() {
      const endpoints = ['temperature/1', 'temperature/2', 'temperature/3', 'temperature/4', 'temperature/5'];
      return { endpoints };
    },
    methods: {
        showNewExperimentModal() {
            this.showModal = true;
        },
        handleExperimentCreated() {
          this.experimentCreated = true;
        }
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
  
  #app {
    margin: 0 !important;
    padding: 0 !important;
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
      position: fixed;
      top: 0;
      left: 0;
      z-index: 1000; /* High z-index to ensure it stays on top */
  }
  
  .main-content {
      display: flex;
      flex: 1;
      max-width: 100%;
      margin: 0;
      overflow-x: hidden;
      margin-top: 10px;
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
      height: 100%; /* Ensure graphs section takes up all available space */
      overflow-y: auto; /* Allow scrolling within this section if needed */
  }
  
  .row {
      display: flex;
      justify-content: space-around;
      margin-bottom: 20px;
      flex-wrap: wrap;
      margin-bottom: 10px; /* Reduced margin */
  }
  
  .temperature-graph {
      width: 30%;
      flex-shrink: 0;
      height: calc((100% - 10px) / 2); 
  }

  .new-experiment-button, .export-data-button {
    display: block;
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: none;
    border-radius: 4px;
    background-color: #008CBA; 
    color: white;
    cursor: pointer;
    font-size: 15px;
    text-align: left;
  }

  .experiment-summary-panel {
    padding: 10px;
    background-color: #f9f9f9; /* Change color as needed */
    border: 1px solid #ddd;
    border-radius: 4px;
    margin-bottom: 10px;
  }

  .export-data-button i {
    margin-right: 8px;
  }

  
.temperature-graph-container {
  width: 30%;
  height: calc((100% - 10px) / 2);
}


.graph-title {
  text-align: center;
  font-size: 1em; /* Adjusted font size */
  margin-bottom: 5px; /* Reduced margin */
}

.placeholder-section {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  background-color: #e0f7fa;  /* Light blue background */
  border-radius: 8px;  /* Optional: Rounded corners */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);  /* Optional: subtle shadow for depth */
  width: 100%;
}

.placeholder-text {
  font-size: 1.25em;
  color: #00796b;  /* Dark blue text */
  text-align: center;
}
  </style>
  

  