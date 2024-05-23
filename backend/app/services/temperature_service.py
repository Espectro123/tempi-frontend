from app.domain.entities.temperature_sensor import TemperatureSensor
from app.repositories.in_memory_repository import InMemoryRepository
from app.utils.read_temperature import read_temperature
from random import randint
import datetime
import pytz
import sys
import time

"""
Service under ODM. In charge to manage how we add and get data.
"""
class TemperatureService:

    contador = 0
    time = ""

    @classmethod
    def add_temperature_reading(cls, sensor: TemperatureSensor, sensor_id):

        if (cls.contador != 0):
            sensor.timestamp = cls.time
            cls.contador = cls.contador -1
        else:
            cls.time = datetime.datetime.now(pytz.timezone('Europe/Madrid')).strftime('%Y-%m-%dT%H:%M:%S.%f')
            sensor.timestamp = cls.time
            cls.contador = 4

        sensor.temperature = read_temperature(sensor_id)
        InMemoryRepository.add_reading(sensor)

    @staticmethod
    def get_temperature_readings():
        return InMemoryRepository.get_readings()


    @staticmethod
    def read_temperature_and_get_mean(sensor_id):

        readings_list = []
        number_of_measurements = 10
        max_tries = 50
        tries = 0
        mean_temperature = 0
      
        while number_of_measurements != 0 and tries <= max_tries:

            reading = read_temperature(sensor_id)

            if (reading != 0):
                readings_list.append(int(reading))
                number_of_measurements = number_of_measurements - 1

            tries = tries + 1

            time.sleep(0.02)

        if number_of_measurements == 0:
            mean_temperature = sum(readings_list)/len(readings_list)
            return mean_temperature
        else:
            return mean_temperature