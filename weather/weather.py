import requests
from .apps import WeatherConfig

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WeatherConfig.api_key}&units=metric"
    print(url)
    response = requests.get(url)
    print(response.status_code)
    if response.status_code == 200:
        data = response.json()
        print(data)
        weather = {
            'city': city,
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }
        return weather
    else:
        return None