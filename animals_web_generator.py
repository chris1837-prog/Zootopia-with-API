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
