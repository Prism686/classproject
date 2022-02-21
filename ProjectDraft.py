#Class Project 
#Alexander Clifton
# Creation Date: 2/18/2022

import math
from urllib import response
import requests

API_KEY = '699c000917627a01c89ebd34ff280d3d'  
    

print("Welcome to Alex's Weather App\n")

city_name = input("Please enter your Zipcode or City name\n")


def get_weather(API_KEY, city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'   ###Built-in API request by city name vs Built-in API request by city ID vs Built-in API request by ZIP code

    response = requests.get(url).json()

    temp = response['main']['temp']
    temp = math.floor((temp - 273.15) * 1.8 + 32)   # Unit conversion to F

    feels_like = response['main']['feels_like']
    feels_like = math.floor((feels_like * 1.8) - 459.67)   # Unit conversion to F

    humidity = response['main']['humidity']
    
    return {
        'temp' : temp,
        'feels_like' : feels_like,
        'humidity' : humidity
    }




    
weather = get_weather(API_KEY, city_name)

print(weather['temp'])
print(weather['feels_like'])
print(weather['humidity'])













