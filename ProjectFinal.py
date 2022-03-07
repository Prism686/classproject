#Class Project 
#Alexander Clifton
# Creation Date: 2/18/2022


#Allow the user to run the program multiple times.
# Validate whether the user entered valid data. If valid data isn’t presented notify the user.   


import math
from urllib import response
import requests

API_KEY = '699c000917627a01c89ebd34ff280d3d'  
    

print("Welcome to Alex's Weather App\n")

city_name = input("Please enter your Zipcode or City name\n")


def get_weather(API_KEY, city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'   ###Built-in API request by city name vs Built-in API request by city ID vs Built-in API request by ZIP code

    response = requests.get(url).json()

    #if response.status_code == 404:
     #   print(f"City not located, Please try again.\n")

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

print(f"The Current tempature in {city_name} is {weather['temp']} degrees fairenheit.\n")
print(f"The tempature should feel like {weather['feels_like']} degrees fairenheit.\n")
print(f"The humidity is at {weather['humidity']}%.\n")













