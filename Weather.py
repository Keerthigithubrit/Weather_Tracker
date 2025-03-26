import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_current_weather():
    print("***Get Current Weather***")

    city = input("Enter Your CityName:")

    requests_url = f"https://api.openweathermap.org/data/2.5/weather?&appid={os.getenv('API_KEY')}&q={city}&units=metric"

    print(requests_url)
    weather_data = requests.get(requests_url).json()
    # pprint(weather_data)

    print(f"Current weather for {weather_data['name']}:")
    print(f"The temperature is {weather_data['main']['temp']:.1f}celcius")
    print(f"Wind Speed is {weather_data['wind']['speed']:}")

get_current_weather()