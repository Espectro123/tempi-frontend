from fastapi import APIRouter
from app.domain.entities.temperature_sensor import TemperatureSensor
from app.services.temperature_service import TemperatureService
from app.utils.export_to_excel import export_to_excel
from pydantic import BaseModel

router = APIRouter()

sensor = TemperatureSensor

class Experiment(BaseModel):
    duration: str
    temperature: str

@router.get("/temperature/{sensor_id}")
def get_temperature(sensor_id: int):
    TemperatureService.add_temperature_reading(sensor, sensor_id)
    readings = TemperatureService.get_temperature_readings()
    return readings[-1]

@router.get("/export/")
def export_data():
    data = TemperatureService.get_temperature_readings()
    export_to_excel(data)
    return {"msg": "Data exported"}

"""
Get the experiment information that the user input on the frontend
This method also start the heater to heat/cold the water
Params:
@experiment: Experiment model -> Object with the information of the experiment 
"""
@router.post("/experiments")
async def create_experiment(experiment: Experiment):
    return {"message": "Experiment created successfully", "data": experiment.dict()}