from app.domain.entities.temperature_sensor import TemperatureSensor
from app.repositories.in_memory_repository import InMemoryRepository
from app.utils.read_temperature import read_temperature
from random import randint
import datetime
import pytz
import sys

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

        sensor.temperature = randint(15,30) #read_temperature(sensor_id)
        InMemoryRepository.add_reading(sensor)

    @staticmethod
    def get_temperature_readings():
        return InMemoryRepository.get_readings()
