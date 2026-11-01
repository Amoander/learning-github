"""Search USDA FoodData Central for a food and print its calories."""
import requests

API_URL = "https://api.nal.usda.gov/fdc/v1/foods/search"
KEY_FILE = "usda_key.txt"
CALORIES_ID = 1008


def load_key():
    """Read the API key from usda_key.txt."""
    with open(KEY_FILE) as file:
        return file.read().strip()


def search_foods(query, api_key):
    """Ask USDA for foods matching query. Return a list of foods."""
    params = {"query": query, "api_key": api_key, "pageSize": 5}
    response = requests.get(API_URL, params=params, timeout=15)
    response.raise_for_status()
    return response.json()["foods"]


def calories(food):
    """Find the calories (per 100 g) in a food's nutrient list."""
    for nutrient in food["foodNutrients"]:
        if nutrient["nutrientId"] == CALORIES_ID:
            return nutrient["value"]
    return None


def main():
    api_key = load_key()
    query = input("Search for a food: ")
    foods = search_foods(query, api_key)
    if not foods:
        print("No matches.")
        return
    for food in foods:
        kcal = calories(food)
        kcal_text = f"{kcal:.0f} kcal" if kcal is not None else "— kcal"
        print(f"{food['description']}: {kcal_text} per 100 g")


if __name__ == "__main__":
    main()