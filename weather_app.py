

import datetime as dt

import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

API_KEY = "" #OPENWEATHER API KEY GOES HERE. GO TO OPENWEATHER WEBSITE TO GET ONE. ITS FREE.

CITY = "San Lorenzo, US"

def kelvin_to_farenheit(kelvin):
    farenheit = (((kelvin - 273.15) * (9/5)) + 32)
    
    return farenheit

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()

#print(response)

temp_kelvin = response['main']['temp']
temp_farenheit = kelvin_to_farenheit(temp_kelvin)

message = f"Temperature in {CITY} is {temp_farenheit:.2f}°F"
print(message)