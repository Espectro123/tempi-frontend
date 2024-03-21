from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints.tempi_endpoints import router as temperature_router

app = FastAPI()

origins = [
    "http://localhost:8080",
    "http://localhost:8000",
]

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API routes
app.include_router(temperature_router)
