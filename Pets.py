import requests
import pandas as pd

def fetch_sold_pets():
    url = "https://petstore.swagger.io/v2/pet/findByStatus"
    params = {"status": "sold"}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        pets = response.json()
        sold_pets = [(pet.get("id"), pet.get("name")) for pet in pets]
        df_sold_pets = pd.DataFrame(sold_pets, columns=['ID', 'Name'])
        # print(df_sold_pets.to_string(index=False))  # Comentar o remover esta línea
        return df_sold_pets
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener las mascotas vendidas: {e}")
        return pd.DataFrame()  # Retorna un DataFrame vacío en caso de error

if __name__ == "__main__":
    fetch_sold_pets()
