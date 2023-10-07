from pydantic import BaseModel
from datetime import datetime

class TemperatureSensor(BaseModel):
    temperature: str
    timestamp: datetime

    @classmethod
    def return_values_as_dict(cls):
        return {"temperature": cls.temperature, "timestamp": cls.timestamp}
