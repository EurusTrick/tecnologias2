# app.py
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from joblib import load
import pathlib
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI(title='Mountains vs Beaches Preference Prediction')
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Cargar el modelo entrenado
model = load(pathlib.Path('model/mountains_vs_beaches-v1.joblib'))

# Definir el modelo de entrada
class InputData(BaseModel):
    age: int
    gender_male: int = 0
    gender_non_binary: int = 0
    income: float
    education_level_bachelor: int = 0
    education_level_master: int = 0
    education_level_doctorate: int = 0
    travel_frequency: int
    preferred_activities_hiking: int = 0
    preferred_activities_skiing: int = 0
    preferred_activities_sunbathing: int = 0
    vacation_budget: float
    location_suburban: int = 0
    location_rural: int = 0
    proximity_to_mountains: float
    proximity_to_beaches: float
    favorite_season_spring: int = 0
    favorite_season_summer: int = 0
    favorite_season_winter: int = 0
    pets: int
    environmental_concerns: int

class ProbabilityOutput(BaseModel):
    probability_mountains: float
    probability_beaches: float

@app.post('/score', response_model=ProbabilityOutput)
def score(data: InputData):
    model_input = np.array([v for k, v in data.dict().items()]).reshape(1, -1)
    probabilities = model.predict_proba(model_input)[0]
    return {
        'probability_mountains': probabilities[1],  # Probabilidad de preferencia por "montañas"
        'probability_beaches': probabilities[0]     # Probabilidad de preferencia por "playas"
    }
