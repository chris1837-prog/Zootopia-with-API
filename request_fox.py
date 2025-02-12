import requests
import json

"""Create the JSON file animal_fox_data.json, which in the first exercise My-Zootopia was already given as "animal_data.json" """
name = 'fox'
api_url = f'https://api.api-ninjas.com/v1/animals?name={name}'
response = requests.get(api_url, headers={'X-Api-Key': 'EAtgdsUVitcqpX3n18bJ5A==puIXjoF4t4EqYkyU'})

if response.status_code == requests.codes.ok:
  data = response.json()
  with open("animal_fox_data.json", "w") as file:
    json.dump(data, file, indent=4)
else:
    print("Error:", response.status_code, response.json())
