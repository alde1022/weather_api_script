import requests
import json

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'  # For temperature in Celsius change 'metric' to 'imperial' for Fahrenheit
    }

    response = requests.get(base_url, params=params)
    weather_data = response.json()
    
    if response.status_code == 200:
        main_weather = weather_data['weather'][0]['main']
        description = weather_data['weather'][0]['description']
        temp = weather_data['main']['temp']

        print(f"Weather in {location}:\n{main_weather} ({description}), Temperature: {temp}°C")
    else:
        print(f"Error getting weather data: {weather_data['message']}")

if __name__ == "__main__":
    api_key = 'your_api_key' # replace with your OpenWeatherMap API Key
    location = input("Enter the city name: ")
    get_weather(api_key, location)
