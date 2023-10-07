from app.domain.entities.temperature_sensor import TemperatureSensor
from app.repositories.in_memory_repository import InMemoryRepository

class TemperatureService:

    @staticmethod
    def add_temperature_reading(sensor: TemperatureSensor):
        InMemoryRepository.add_reading(sensor)

    @staticmethod
    def get_temperature_readings():
        return InMemoryRepository.get_readings()
