import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_food_image(food_item):

    headers = {
        "Authorization": os.getenv("PIXABY_API_KEY")
    }
    SEARCH_URL = "https://api.pexels.com/v1/search"

    params = {
        "query": food_item,
        "per_page": 1
    }

    response = requests.get(SEARCH_URL, headers=headers, params=params)

    print(response.status_code)
    data = response.json()
    if data["photos"]:
        image_url = data["photos"][0]["src"]["medium"]
        return image_url
    else:
        print("No image found for the food item.")
        return None
