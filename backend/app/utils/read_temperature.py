from w1thermsensor import W1ThermSensor, Sensor
from random import randint

SENSOR_DICT = {
    1 : "000000024604",
    2 : "000000028fda",
    3 : "00000002c848",
    4 : "00000002e27e",
    5 : "0000000460d5"
}

# Read temperature from any sensor
def read_temperature(sensor_id):
    temperature_in_celsius = 0
    try:
        sensor = W1ThermSensor(sensor_type=Sensor.DS18B20, sensor_id=SENSOR_DICT[sensor_id])
        temperature_in_celsius = sensor.get_temperature()
        return temperature_in_celsius
    except:
        return temperature_in_celsius
    

