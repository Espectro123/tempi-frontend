from pydantic import BaseModel
from datetime import datetime

class TemperatureSensor(BaseModel):
    temperature: str
    timestamp: datetime
