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

    @staticmethod
    def add_temperature_reading(sensor: TemperatureSensor, sensor_id):
        sensor.timestamp = datetime.datetime.now(pytz.timezone('Europe/Madrid')).isoformat()
        sensor.temperature = read_temperature(sensor_id)
        InMemoryRepository.add_reading(sensor)

    @staticmethod
    def get_temperature_readings():
        return InMemoryRepository.get_readings()
