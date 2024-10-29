# client.py
import requests

body = {
    "age": 28,
    "gender_male": 1,
    "gender_non_binary": 0,
    "income": 55000,
    "education_level_bachelor": 1,
    "education_level_master": 0,
    "education_level_doctorate": 0,
    "travel_frequency": 3,
    "preferred_activities_hiking": 1,
    "preferred_activities_skiing": 0,
    "preferred_activities_sunbathing": 0,
    "vacation_budget": 2000,
    "location_suburban": 1,
    "location_rural": 0,
    "proximity_to_mountains": 50,
    "proximity_to_beaches": 120,
    "favorite_season_spring": 0,
    "favorite_season_summer": 1,
    "favorite_season_winter": 0,
    "pets": 1,
    "environmental_concerns": 1
}

response = requests.post(url='http://127.0.0.1:8000/score', json=body)
print(response.json())
# Ejemplo de salida esperada: {'preference': 'mountains'}
