import json

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
  with open(file_path, "r", encoding="utf-8") as file:
    return file.read()


def write_animals_html(animals_template, output):
  """Replaces a placeholder in the HTML template
  with formatted animal data and writes it to 'animals.html'."""
  with open("animals.html", "w", encoding="utf-8") as file:
    my_html = animals_template.replace("__REPLACE_ANIMALS_INFO__", output)
    return file.write(my_html)


def serialize_animal(animal_obj):
  """Formats an animal object's details into an HTML list item string."""
  output = "" # define an empty string
  output += '<li class="cards__item">'
  output += f'<div class="card__title"> {animal_obj['name']}</div><br/>'
  output += f'<p class="card__text"> <strong> Diet: </strong> {animal_obj['characteristics']['diet']}<br/></p>'
  output += f'<p class="card__text"> <strong> Location: </strong>{animal_obj['locations'][0] if animal_obj['locations'] else ' '}<br/></p>'

  if "type" in animal_obj["characteristics"]:
    output += f'<p class="card__text"> <strong> Type: </strong> {animal_obj['characteristics']['type'] if 'type' in animal_obj['characteristics'] else ''}<br/></p>'
  output += '</li>'
  return output

def main():
  """Main function to load data, print it, format it as HTML, and write to a file."""
  animals_data = load_data('animals_data.json')
  animals_template = read_animals_template("animals_template.html")
  print_animals(animals_data)

  output = ""
  for animal_obj in animals_data:
    output += serialize_animal(animal_obj)

  write_animals_html(animals_template, output)

if __name__ == "__main__":
  main()

