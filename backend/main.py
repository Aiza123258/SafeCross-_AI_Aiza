from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

from utils.predictor import predict_severity


app = FastAPI(
    title="SafeCross AI Backend",
    description="AI-powered road accident prediction and safety backend",
    version="1.0.0"
)


class SeverityRequest(BaseModel):
    weather: str
    road_condition: str
    accident_cause: str
    traffic_density: str
    vehicles_involved: int
    nearby_accidents: int
    hour: int
    day_of_week: int
    is_night: int
    latitude: Optional[float] = 0.0
    longitude: Optional[float] = 0.0
    month: Optional[int] = 6


@app.get("/")
def root():
    return {
        "message": "SafeCross AI Backend is running",
        "status": "success"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/predict/severity")
def predict_severity_api(data: SeverityRequest):

    result = predict_severity(
        weather=data.weather,
        road_condition=data.road_condition,
        accident_cause=data.accident_cause,
        traffic_density=data.traffic_density,
        vehicles_involved=data.vehicles_involved,
        nearby_accidents=data.nearby_accidents,
        hour=data.hour,
        day_of_week=data.day_of_week,
        is_night=data.is_night,
        latitude=data.latitude,
        longitude=data.longitude,
        month=data.month
    )

    return {
        "status": "success",
        "prediction": result
    }