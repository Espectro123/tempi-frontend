// NewExperiment.vue
<template>
    <div v-if="show" class="new-experiment-modal">
        <div class="modal-content">
            <span class="close" @click="closeModal">&times;</span>
            <form @submit.prevent="handleSubmit">
                <label for="initial_temperature">Initial Temperature:</label>
                <input type="text" id="initial_temperature" v-model="initial_temperature" required>
                <label for="target_temperature">Target Temperature:</label>
                <input type="text" id="target_temperature" v-model="target_temperature" required>
                <label for="experiment_duration">Total experiment Duration:</label>
                <input type="text" id="experiment_duration" v-model="experiment_duration" required>
                <label for="interval">Change interval</label>
                <input type="text" id="interval" v-model="interval" required>
                <button type="submit">Start experiment</button>
            </form>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
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
            try {
                const response = await axios.post('http://localhost:8000/experiments', {
                    experiment_duration: this.experiment_duration,
                    interval: this.interval,
                    initial_temperature: this.initial_temperature,
                    target_temperature: this.target_temperature

                });
                console.log('Response:', response.data);
                this.$emit('close');  // Optionally close the modal upon successful submission
                this.$emit('experiment-created');
            } catch (error) {
                console.error('Error:', error.response ? error.response.data : error.message);
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
