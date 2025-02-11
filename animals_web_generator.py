import json
import requests

def load_data(file_path):
  """Loads a JSON file from given file path
  and returns the parsed data."""
  with open(file_path, "r") as handle:
    return json.load(handle)


def print_animals(animals_data):
  """Prints animal details such as name, diet, first location
  and type if available."""
  for item in animals_data:
    if "name" in item:
      print("Name: ", item["name"])
    if "characteristics" in item and "diet" in item["characteristics"]:
      print("Diet: ", item["characteristics"]["diet"])
    if "locations" in item and item["locations"] != []:
      print("Location: ", item["locations"][0])
    if "characteristics" in item and "type" in item["characteristics"]:
      print("Type: ", item["characteristics"]["type"])
    else:
      print()
    print()

def read_animals_template (file_path):
  """Reads the HTML template file and
  returns its content as a string."""
  with open(file_path, "r") as file:
    return file.read()


def write_animals_html(animals_template, output, user_input):
  """Replaces a placeholder in the HTML template
  with formatted animal data and writes it to 'animals.html'."""
  with open("animals.html", "w") as file:
    if output:
      my_html = animals_template.replace("__REPLACE_ANIMALS_INFO__", output)
    else:
      my_html = animals_template.replace("__REPLACE_ANIMALS_INFO__",
                                         f'<h2>The animal "{user_input}" doesn\'t exist.</h2>')
    return file.write(my_html)


def serialize_animal(animal_obj):
  """Formats an animal object's details into an HTML list item string."""
  output = "" # define an empty string
  output += '<li class="cards__item">'
  output += f'<div class="card__title"> {animal_obj["name"]}</div><br/>'
  output += f'<p class="card__text"> <strong> Diet: </strong> {animal_obj["characteristics"]["diet"]}<br/></p>'
  output += f'<p class="card__text"> <strong> Location: </strong>{animal_obj["locations"][0] if animal_obj["locations"] else ""}<br/></p>'

  if "type" in animal_obj["characteristics"]:
    output += f'<p class="card__text"> <strong> Type: </strong> {animal_obj["characteristics"]["type"] if "type" in animal_obj["characteristics"] else ''}<br/></p>'
  output += '</li>'
  return output

def main():
  user_input = input("Enter a name of an animal: ")
  api_url = f'https://api.api-ninjas.com/v1/animals?name={user_input}'
  response = requests.get(api_url, headers={'X-Api-Key': 'EAtgdsUVitcqpX3n18bJ5A==puIXjoF4t4EqYkyU'})

  if response.status_code == 200:
    data = response.json()
    with open("animals_data.json", "w") as file:
      json.dump(data, file, indent=4)

    animals_template = read_animals_template("animals_template.html")

    if not data:
      output = f"<h2>The animal '{user_input}' doesn't exist.</h2>"
      print(f"Error: The animal '{user_input}' cannot be found on the website.")
    else:
      output = "".join(serialize_animal(animal) for animal in data)
      print("Website was successfully generated to the file animals.html.")
    write_animals_html(animals_template, output, user_input)
  else:
    print(f"Error: API request failed with status code {response.status_code}")

if __name__ == "__main__":
  main()

