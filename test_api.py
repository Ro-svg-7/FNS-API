from dotenv import load_dotenv
import requests
from pprint import pprint
import json

import os

load_dotenv()

calories = None
fat = None
carbohydrates = None
protein = None

API_KEY = os.getenv("API_KEY")

SEARCH_URL = f"https://api.nal.usda.gov/fdc/v1/foods/search?api_key={API_KEY}&query=Apple"

search_response = requests.get(SEARCH_URL)
print(search_response.status_code)
data = search_response.json()
fdcId = data["foods"][0]["fdcId"]

NUTRITION_URL = f"https://api.nal.usda.gov/fdc/v1/food/{fdcId}?api_key={API_KEY}"

nutrition_response = requests.get(NUTRITION_URL)
print(nutrition_response.status_code)
nut_data = nutrition_response.json()
# pprint(json.dumps(nut_data, indent=4))
for nutrient in nut_data["foodNutrients"]:
    name = nutrient["nutrient"]["name"]
    amount = nutrient["amount"]

    if name == "Energy":
        calories = amount
    elif name == "Total lipid (fat)":
        fat = amount    
    elif name == "Carbohydrate, by difference":
        carbohydrates = amount
    elif name == "Protein":
        protein = amount
print(f"Calories: {calories} kcal")
print(f"Fat: {fat} g")
print(f"Carbohydrates: {carbohydrates} g")
print(f"Protein: {protein} g")