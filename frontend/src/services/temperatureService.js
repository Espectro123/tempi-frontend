import axios from 'axios';

const BASE_URL = 'http://localhost:8000';

export const getTemperatureData = async (endpoint) => {
  try {
    // Fetch temperature data
    const temperatureResponse = await axios.get(`${BASE_URL}/${endpoint}`);
    const temperatureData = temperatureResponse.data;
    console.log('Temperature Data:', temperatureData);
    console.log('Temperature Endpoint called:', `${BASE_URL}/${endpoint}`);

    // Fetch timestamp data
    const timeResponse = await axios.get(`${BASE_URL}/time`);
    const timestamp = timeResponse.data;
    console.log('Timestamp:', timestamp);
    console.log('Time Endpoint called:', `${BASE_URL}/time`);

    // Combine results into an array
    return [temperatureData, timestamp];
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error;
  }
};