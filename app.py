# For calling the api
import requests
# For loading .env
from dotenv import load_dotenv 
import os 
# To play with json
import json
# We get all the env variables
load_dotenv()  
api_key = os.getenv("WEATHER_API") 

# Get city from user
city_name = input("Enter a city: ")
# api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

# Get coordinates from api
geo_api = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={1}&appid={api_key}"
response = requests.get(geo_api)
# Try-catch, if success we print coordinates
if response.status_code == 200:
    data = response.json()
    print(len(data))
    lat = data[0]['lat']
    lon = data[0]['lon']
    print(f"Coordinates: Latitude {lat} Longitude {lon}")
else:
    print("Error in the api: " + str(response.status_code))

# Get weather
weather_api = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
response = requests.get(weather_api)

# Try-catch, if success we print Weather response
if response.status_code == 200:
    data = response.json()
    print(len(data))
    # Pretty json print
    print(json.dumps(data, indent=4))
else:
    print("Error in the api: " + str(response.status_code))

