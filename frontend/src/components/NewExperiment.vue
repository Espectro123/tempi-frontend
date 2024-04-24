<template>
    <div v-if="show" class="new-experiment-modal">
        <div class="modal-content">
            <span class="close" @click="closeModal">&times;</span>
            <form @submit.prevent="handleSubmit">
                <label for="initial_temperature">Initial temperature
                    <i class="fas fa-question-circle" title="Starting temperature of a cycle. Range [10.0, 30.0]ºC"></i>
                </label>
                <input type="text" id="initial_temperature" placeholder="Intial Temperature on celsius [10.0, 30.0]" v-model="initial_temperature" required>
                
                <label for="target_temperature">Target temperature
                    <i class="fas fa-question-circle" title="Maximun or minimum temperature of a cycle. Range [10.0, 30.0]ºC"></i>
                </label>
                <input type="text" id="target_temperature" placeholder="Target Temperature on celsius [10.0, 30.0]" v-model="target_temperature" required>
                
                <label for="experiment_duration">Experiment duration
                    <i class="fas fa-question-circle" title="Duration of the experiment in hours. Minimum value: 1.0"></i>
                </label>
                <input type="text" id="experiment_duration" placeholder="Duration of the experiment in hours... 1.0" v-model="experiment_duration" required>
                
                <label for="interval">Cycle duration
                    <i class="fas fa-question-circle" title="Indicates the duration of a cycle in hours. Minimum value: 0.1. Must be lower than Experiment duration."></i>
                </label>
                <input type="text" id="interval" placeholder="Duration of each cycle in hours... 1.0" v-model="interval" required>
                
                <button type="submit" :disabled="isLoading">
                    <span v-if="isLoading">Creating experiment... <i class="fas fa-spinner fa-spin"></i></span>
                    <span v-else>Start experiment</span>
                </button>
            </form>
        </div>
    </div>
</template>


<script>
import axios from 'axios';

export default {
    data() {
        return {
            isLoading: false
        };
    },
    props: {
        show: {
            type: Boolean,
            required: true
        }
    },
    methods: {
        closeModal() {
            this.$emit('close');
        },
        async handleSubmit() {
            this.isLoading = true; // Step 2: Set isLoading to true when submission starts
            try {
                const response = await axios.post('http://localhost:8000/experiments', {
                    experiment_duration: this.experiment_duration,
                    interval: this.interval,
                    initial_temperature: this.initial_temperature,
                    target_temperature: this.target_temperature
                });
                console.log('Response:', response.data);
                this.$emit('experiment-created', {
                    initial_temperature: this.initial_temperature,
                    target_temperature: this.target_temperature,
                    experiment_duration: this.experiment_duration,
                    interval: this.interval,
                });
            } catch (error) {
                console.error('Error:', error.response ? error.response.data : error.message);
            } finally {
                this.isLoading = false; // Reset loading state
                this.$emit('close'); // Close modal
            }
        }
    }
};
</script>

<style scoped>
.new-experiment-modal {
    /* Style for modal */
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1001; 
}

.modal-content {
    /* Style for modal content */
    background-color: white;
    padding: 20px;
    border-radius: 4px;
    width: 300px;
    text-align: left;
    position: relative;
}

.close {
    /* Style for close button */
    position: absolute;
    top: 10px;
    right: 10px;
    cursor: pointer;
}

form {
    /* Form styles */
    display: flex;
    flex-direction: column;
}
</style>
