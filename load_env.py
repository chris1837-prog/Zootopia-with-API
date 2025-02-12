from dotenv import load_dotenv
import os

load_dotenv()  # load the .env file

API_KEY = os.getenv('API_KEY')  # Gets the API key from .env
print("API_KEY:", API_KEY)