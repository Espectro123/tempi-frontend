from fastapi import APIRouter
from app.domain.entities.temperature_sensor import TemperatureSensor
from app.services.temperature_service import TemperatureService
from app.utils.export_to_excel import export_to_excel
from app.utils.control_tk2000 import control_tk
from app.utils.read_temperature import read_temperature
from app.utils.manage_intervals import manage_intervals
from app.repositories.in_memory_experiment import InMemoryExperiment
from app.utils.move_to_usb import move_to_usb
from pydantic import BaseModel
import time


router = APIRouter()

sensor = TemperatureSensor

class Experiment(BaseModel):
    experiment_duration: str
    interval: str
    initial_temperature: str
    target_temperature: str

@router.get("/temperature/{sensor_id}")
def get_temperature(sensor_id: int):
    TemperatureService.add_temperature_reading(sensor, sensor_id)
    readings = TemperatureService.get_temperature_readings()
    # Check when a new interval begins
    if sensor_id == 1:
        if InMemoryExperiment.first_check:
            InMemoryExperiment.first()
        manage_intervals(readings[-1])
    return readings[-1]

@router.get("/export/")
def export_data():
    data = TemperatureService.get_temperature_readings()
    export_to_excel(data)
    time.sleep(3)
    move_to_usb()
    return "Data exported"

"""
Get the experiment information that the user input on the frontend
This method also start the heater to heat/cold the water
Params:
@experiment: Experiment model -> Object with the information of the experiment 
"""
@router.post("/experiments")
async def create_experiment(experiment: Experiment):
    control_tk("TurnOn",0.0,0.0)
    control_tk("SetUpTemperature",read_temperature(1),float(experiment.initial_temperature))
    InMemoryExperiment.experiment_duration = int(experiment.experiment_duration)
    InMemoryExperiment.initial_temperature = float(experiment.initial_temperature)
    InMemoryExperiment.target_temperature  = float(experiment.target_temperature)
    InMemoryExperiment.interval            = int(experiment.interval)
    time.sleep(5) # Time to start things
    return {"message": "Experiment created successfully", "data": experiment.dict()}