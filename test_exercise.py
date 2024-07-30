import pytest
import pandas as pd
from Pets import fetch_sold_pets
from pet_counter import PetCounter, get_sold_pets_from_api

def test_fetch_sold_pets():
    df_sold_pets = fetch_sold_pets()
    assert not df_sold_pets.empty, "La tabla de mascotas vendidas está vacía."
    # Imprimir el DataFrame en un formato legible en la consola
    print(df_sold_pets.to_string(index=False))

def test_count_pets_by_name():
    sold_pets = get_sold_pets_from_api()
    pet_counter = PetCounter(sold_pets)
    name_counts = pet_counter.count_pets_by_name()
    df_name_counts = pd.DataFrame(list(name_counts.items()), columns=['Name', 'Count'])
    assert not df_name_counts.empty, "La tabla de conteo de nombres de mascotas está vacía."
    # Imprimir el DataFrame en un formato legible en la consola
    print(df_name_counts.to_string(index=False))
