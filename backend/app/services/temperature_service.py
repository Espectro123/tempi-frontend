from app.domain.entities.temperature_sensor import TemperatureSensor
from app.repositories.in_memory_repository import InMemoryRepository
from app.utils.read_temperature import read_temperature
from datetime import datetime
from random import randint
import sys

class TemperatureService:

    @staticmethod
    def add_temperature_reading(sensor: TemperatureSensor, sensor_id):
        sensor.timestamp = datetime.now().isoformat()
        sensor.temperature = read_temperature(sensor_id)
        InMemoryRepository.add_reading(sensor)

    @staticmethod
    def get_temperature_readings():
        return InMemoryRepository.get_readings()
