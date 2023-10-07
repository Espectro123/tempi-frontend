from fastapi import APIRouter
from app.domain.entities.temperature_sensor import TemperatureSensor
from app.services.temperature_service import TemperatureService
from app.utils.export_to_excel import export_to_excel

router = APIRouter()

@router.post("/temperature/")
def add_temperature(sensor: TemperatureSensor):
    TemperatureService.add_temperature_reading(sensor)
    return {"msg": "Temperature added"}

@router.get("/temperature/{sensor_number}")
def get_temperature(sensor_number: int):
    readings = TemperatureService.get_temperature_readings()
    return readings[sensor_number]

@router.get("/export/")
def export_data():
    data = TemperatureService.get_temperature_readings()
    export_to_excel(data)
    return {"msg": "Data exported"}
