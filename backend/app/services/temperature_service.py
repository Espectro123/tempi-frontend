from app.domain.entities.temperature_sensor import TemperatureSensor
from app.repositories.in_memory_repository import InMemoryRepository
from random import randint
from datetime import datetime

class TemperatureService:

    # Here I should add the way to read data from sensors. Must use sensor id
    @staticmethod
    def add_temperature_reading(sensor: TemperatureSensor, sensor_id):
        sensor.timestamp = datetime.now().isoformat()
        sensor.temperature = str(randint(20,35))
        InMemoryRepository.add_reading(sensor)

    @staticmethod
    def get_temperature_readings():
        return InMemoryRepository.get_readings()
