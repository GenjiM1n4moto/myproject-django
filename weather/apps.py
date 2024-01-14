from django.apps import AppConfig
from .utils.secret import get_api_key

class WeatherConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'weather'
    api_key = None

    def ready(self):
        WeatherConfig.api_key = get_api_key("api_keys/WEATHER_API_KEY")
