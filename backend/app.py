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


@app.get("/temperature")
async def read_temperature():
    timestamp = datetime.now().isoformat()
    temperature = randint(0,1)
    print("Temperature; ", temperature, "Time: ", timestamp)
    return {"temperature": temperature, "timestamp": timestamp}

