import requests
import json
from animals_web_generator import read_animals_template, write_animals_html, serialize_animal

API_KEY = 'EAtgdsUVitcqpX3n18bJ5A==puIXjoF4t4EqYkyU'

def fetch_data(animal_name):
  """
  Fetches the animals data for the animal 'animal_name'.
  Returns: a list of animals, each animal is a dictionary.
  """
  api_url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
  response = requests.get(api_url, headers={'X-Api-Key': API_KEY})

  if response.status_code == 200:
    data = response.json()
    # save the data in a JSON file
    with open("animals_data.json", "w") as file:
      json.dump(data, file, indent=4)

    # read the animals_template.html
    animals_template = read_animals_template("animals_template.html")
    # if the list ist empty
    if not data:
        output = f"<h2>The animal '{animal_name}' doesn't exist.</h2>"
        print(f"Error: The animal '{animal_name}' cannot be found on the website.")
    else:
      # convert data to html
      output = "".join(serialize_animal(animal) for animal in data)
      print("Website was successfully generated to the file animals.html.")
    write_animals_html(animals_template, output, animal_name)
  else:
    # if response.status_code != 200
    print(f"Error: API request failed with status code {response.status_code}")
  return data