import logging
from collections import Counter
import requests
import pandas as pd

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PetCounter:
    def __init__(self, pets):
        if not isinstance(pets, list) or not all(isinstance(p, tuple) and len(p) == 2 for p in pets):
            raise ValueError("Invalid pets data. Expected a list of tuples (id, name).")
        self.pets = pets
        logging.info("PetCounter initialized with %d pets.", len(pets))

    def count_pets_by_name(self):
        name_count = Counter()
        for pet_id, pet_name in self.pets:
            if pet_name:
                normalized_name = pet_name.lower().strip()
                name_count[normalized_name] += 1
        logging.info("Counted pet names: %s", name_count)
        return name_count

def get_sold_pets_from_api():
    url = "https://petstore.swagger.io/v2/pet/findByStatus"
    params = {"status": "sold"}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses
        pets_data = response.json()
        sold_pets = [(pet.get("id"), pet.get("name")) for pet in pets_data if pet.get("name")]
        return sold_pets
    except requests.exceptions.RequestException as e:
        logging.error("An error occurred while fetching sold pets data: %s", e)
        return []

# Uso de PetCounter para mostrar la tabla de conteo de nombres
sold_pets = get_sold_pets_from_api()
if sold_pets:
    try:
        counter = PetCounter(sold_pets)
        name_counts = counter.count_pets_by_name()
        df_name_counts = pd.DataFrame(list(name_counts.items()), columns=['Name', 'Count'])
        print(df_name_counts)
    except ValueError as e:
        logging.error("An error occurred: %s", e)
