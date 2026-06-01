from dotenv import load_dotenv
import requests
from pprint import pprint
import json

import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

def get_nutrition_info(food_item):
    SEARCH_URL = f"https://api.nal.usda.gov/fdc/v1/foods/search?api_key={API_KEY}&query={food_item}"
    search_response = requests.get(SEARCH_URL)
    if search_response.status_code != 200:
        print(f"Error: {search_response.status_code}")
        return None
    data = search_response.json()
    if not data["foods"]:
        print("Food item not found.")
        return None
    fdcId = data["foods"][0]["fdcId"]
    
    NUTRITION_URL = f"https://api.nal.usda.gov/fdc/v1/food/{fdcId}?api_key={API_KEY}"
    nutrition_response = requests.get(NUTRITION_URL)
    if nutrition_response.status_code != 200:
        print(f"Error: {nutrition_response.status_code}")
        return None
    nut_data = nutrition_response.json()
    
    calories = None
    fat = None
    carbohydrates = None
    protein = None

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

    return {
        "calories": calories,
        "fat": fat,
        "carbohydrates": carbohydrates,
        "protein": protein
    }