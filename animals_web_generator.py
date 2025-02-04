import json

def load_data(file_path):
  """Loads a JSON file"""
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

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
  with open(file_path, "r", encoding="utf-8") as file:
    return file.read()

animals_template = read_animals_template("animals_template.html")
animals_string = "" # define an empty string
for animal in animals_data:
  #append information to each string
  animals_string += '<li class="cards__item">'
  animals_string += f"Name: {animal['name']}<br/>\n"
  animals_string += f"Diet: {animal['characteristics']['diet']}<br/>\n"
  animals_string += f"Location: {animal['locations'][0] if animal['locations'] else ' '}<br/>\n"

  if "type" in animal["characteristics"]:
    animals_string += f"Type:  {animal['characteristics']['type'] if 'type' in animal['characteristics'] else ''}<br/>\n"
  animals_string += '</li>'
print(animals_string)


my_html = animals_template.replace("__REPLACE_ANIMALS_INFO__", animals_string)
with open("animals.html", "w", encoding="utf-8") as file:
  file.write(my_html)
