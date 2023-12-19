from w1thermsensor import W1ThermSensor, Sensor


SENSOR_DICT = {
    1 : "",
    2 : "",
    3 : "",
    4 : "",
    5 : ""
}

# Read temperature from any sensor
def read_temperature(sensor_id):
    sensor = W1ThermSensor(sensor_type=Sensor.DS18B20, sensor_id=SENSOR_DICT[sensor_id])
    temperature_in_celsius = sensor.get_temperature()
    return temperature_in_celsius




