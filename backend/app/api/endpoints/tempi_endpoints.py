from fastapi import APIRouter
from app.domain.entities.temperature_sensor import TemperatureSensor
from app.services.temperature_service import TemperatureService
from app.utils.export_to_excel import export_to_excel
from app.utils.control_tk2000 import set_temperature
from app.utils.read_temperature import read_temperature
from app.repositories.in_memory_experiment import InMemoryExperiment
from app.utils.move_to_usb import move_to_usb
from pydantic import BaseModel
from app.utils.set_start_state_tk2000 import start_tk2000, set_started_temperature
import time
from random import randint

router = APIRouter()

sensor = TemperatureSensor

class Experiment(BaseModel):
    experiment_duration: str
    interval: str
    initial_temperature: str
    target_temperature: str

@router.get("/temperature/{sensor_id}")
def get_temperature(sensor_id: int):
    readings = []
    if InMemoryExperiment.experiment_finish == False:
        TemperatureService.add_temperature_reading(sensor, sensor_id)
        readings = TemperatureService.get_temperature_readings()
        
    if sensor_id == 1 and InMemoryExperiment.is_experiment_ready() == True and InMemoryExperiment.experiment_finish == False:
        InMemoryExperiment.control_intervals()

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
    print("Starting TK 2000")
    start_tk2000()
    time.sleep(3)
    
    print("Setting up initial temperature...")
    set_started_temperature() # Set temperature to 30ºC
    time.sleep(3)
    
    print("Setting experiment temperature....")
    set_temperature(30,experiment.initial_temperature)
    
    print("Setting up the experiment in memory")
    InMemoryExperiment.set_up_experiment(int(experiment.experiment_duration),float(experiment.initial_temperature),float(experiment.target_temperature),int(experiment.interval))
    time.sleep(5) # Time to start things
    return {"message": "Experiment created successfully", "data": experiment.dict()}
