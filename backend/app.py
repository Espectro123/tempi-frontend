from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from random import randint
from datetime import datetime

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI"}

@app.get("/welcome")
def welcome():
    return {"message": "Welcome to Tempi idiot idiot"}


@app.get("/temperature1")
async def read_temperature():
    timestamp = datetime.now().isoformat()
    temperature = randint(20,35)
    print("Temperature; ", temperature, "Time: ", timestamp)
    return {"temperature": temperature, "timestamp": timestamp}

@app.get("/temperature2")
async def read_temperature():
    timestamp = datetime.now().isoformat()
    temperature = randint(20,35)
    print("Temperature; ", temperature, "Time: ", timestamp)
    return {"temperature": temperature, "timestamp": timestamp}

@app.get("/temperature3")
async def read_temperature():
    timestamp = datetime.now().isoformat()
    temperature = randint(20,35)
    print("Temperature; ", temperature, "Time: ", timestamp)
    return {"temperature": temperature, "timestamp": timestamp}

@app.get("/temperature4")
async def read_temperature():
    timestamp = datetime.now().isoformat()
    temperature = randint(20,35)
    print("Temperature; ", temperature, "Time: ", timestamp)
    return {"temperature": temperature, "timestamp": timestamp}

@app.get("/temperature5")
async def read_temperature():
    timestamp = datetime.now().isoformat()
    temperature = randint(20,35)
    print("Temperature; ", temperature, "Time: ", timestamp)
    return {"temperature": temperature, "timestamp": timestamp}