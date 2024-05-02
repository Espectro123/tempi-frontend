from w1thermsensor import W1ThermSensor, Sensor
from random import randint
import time

SENSOR_DICT = {
    1 : "000000024604",
    2 : "000000028fda",
    3 : "00000002c848",
    4 : "00000002e27e",
    5 : "0000000460d5"
}

# Read temperature from any sensor
def read_temperature(sensor_id):
    sensor = W1ThermSensor(sensor_type=Sensor.DS18B20, sensor_id=SENSOR_DICT[sensor_id])
    temperature_in_celsius = sensor.get_temperature()
    return temperature_in_celsius



while(True):
    try:
        print("Sensor 1 Temp: ", read_temperature(1))
        print("Sensor 2 Temp: ", read_temperature(2))
        print("Sensor 3 Temp: ", read_temperature(3))
        print("Sensor 4 Temp: ", read_temperature(4))
        print("Sensor 5 Temp: ", read_temperature(5))
        time.sleep(5)
    except:
        print("couldn't read from sensor")
