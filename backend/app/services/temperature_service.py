from app.domain.entities.temperature_sensor import TemperatureSensor
from app.repositories.in_memory_repository import InMemoryRepository
from app.utils.read_temperature import read_temperature
from datetime import datetime
from random import randint
from app.api.endpoints.tempi_endpoints_data_preprocesed import DataDigest
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

    def check_data():
        digest = DataDigest(InMemoryRepository.get_readings())

        if digest.validate_data():
            if digest.remove_errors():
                pass
        else:
            sys.exit()