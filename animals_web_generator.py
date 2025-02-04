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
animals_string = ""
for animal in animals_data:
  animals_string += f"Name: {animal['name']}\n"
  animals_string += f"Diet: {animal['characteristics']['diet']}\n"
  animals_string += f"Location: {animal['locations'][0] if animal['locations'] else ' '}\n"
  animals_string += f"Type:  {animal['characteristics']['type'] if 'type' in animal['characteristics'] else ''}\n"

my_html = animals_template.replace("__REPLACE_ANIMALS_INFO__", animals_string)

with open("animals.html", "w", encoding="utf-8") as file:
  file.write(my_html)
