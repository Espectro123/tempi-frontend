from typing import List
from app.domain.entities.temperature_sensor import TemperatureSensor

class InMemoryRepository:
    data = []

    @classmethod
    def add_reading(cls, sensor: TemperatureSensor):
        cls.data.append(sensor.dict())

    @classmethod
    def get_readings(cls) -> List[TemperatureSensor]:
        return cls.data
