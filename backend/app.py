from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from random import randint
from datetime import datetime
from pydantic import BaseModel

app = FastAPI()

# Add CORS middleware. Allow all since it will run on localhost.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Experiment(BaseModel):
    duration: str
    temperature: str


"""
Get the experiment information that the user input on the frontend
This method also start the heater to heat/cold the water
Params:
@experiment: Experiment model -> Object with the information of the experiment 
"""
@app.post("/experiments")
async def create_experiment(experiment: Experiment):
    return {"message": "Experiment created successfully", "data": experiment.dict()}

"""
This endpoint get the data from the sensor, store it and send it to the frontend.
Params:
@sensor_number: int -> Reprensent the number of the sensor from which the information will be collected
"""
@app.get("/temperature/{sensor_number}")
async def read_sensor_data(sensor_number):
    timestamp = datetime.now().isoformat()
    temperature = randint(20,35)
    print("Temperature; ", temperature, "Time: ", timestamp, "Sensor number: ", sensor_number)
    return {"temperature": temperature, "timestamp": timestamp}