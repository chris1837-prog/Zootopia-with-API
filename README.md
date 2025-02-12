# Animals Web Generator 

This Python program gets animal information from an API and creates an HTML file to display the data.

## How it works

1. User Input: The user enters an animal name.
2. Get Data from API: The program sends a request to the API Ninjas (Animals API) to get information about the animal.
3. Process Data:
   - If the API response is 200 (OK), the program saves the data.
   - If the animal exists, it converts the data into HTML.
   - If the animal does not exist, it shows an error message.
4. Generate HTML: The program adds the animal data to an HTML template and saves it as animals.html.

## Files and their functions

animals_web_generator.py

    functions:
    def load_data(file_path): Loads a JSON File "animals_data.json"
    print_animals(animals_data): Prints animal details (name, diet,location,type)
    read_animals_template(file_path): Reads the HTML template file "animals_template.html"
    write_animals_html(animals_template, output, user_input): Creates the HTML file "animals.html" 
    serialize_animal(animal_obj): Converts the animal data into HTML-List-Item-String
    def main(): Starts the program, fetches and print data

data_fetcher.py
    
    function:
            fetch_data(animal_name): sends a request to the API, 
            if the response it's OK (200) save the data in 
            the file "animals_data.json" else gets an error message

load_env.py

    Loads and gets the API_KEY from .env

request_fox.py
        
    Create the JSON file animal_fox_data.json

API Information

    URL: https://api.api-ninjas.com/v1/animals
    Authentication: Requires an API key (X-Api-Key)

    
## Installation 

    To install this project, simply clone the repository wiht the 
    url: https://github.com/chris1837-prog/Zootopia-with-API.git
    and install the dependencies in requirements.txt using `pip`

## Usage

    To use this project, run the following command - 
    `python 3 animals_web_generator.py`
    and open 'animals.html' in your browser to see the animal information.

## Example

    Input: 
    Enter a name of an animal: pig

    Output:
    Website was successfully generated to the file animals.html.
    Name:  Guinea Pig
    Diet:  Herbivore
    Location:  South-America
    
    Name:  Nicobar pigeon
    Diet:  Omnivore
    Location:  Asia
    Type:  Bird
    
    Name:  Pig
    Diet:  Omnivore
    Location:  Asia
    Type:  Mammal
    
    Name:  Pigeon
    Diet:  Omnivore
    Location:  Africa
    Type:  Bird

    -> The file 'animals.html' will show in browser details about pigs :-)

    If the animal 'xyz' is not found, it will display:
    "The animal 'xyz' doesn't exist."

## Contributing

We welcome contributions! If you'd like to contribute to this project, please follow these steps:

1. **Fork the repository** – Create your own copy of this project.
2. **Make changes** – Edit the code or add new features.
3. **Test your changes** – Make sure everything works correctly.
4. **Create a pull request** – Submit your changes for review.

If you find a bug or have an idea for improvement, feel free to open an issue. 

Thank you for your support!
