from django.shortcuts import render
from .weather import get_weather

weather_template = 'weather/weather.html'

def weather_view(request):
    if request.method == 'POST':
        city = request.POST.get('city_name')
        print(city)
        weather = get_weather(city)
        if weather:
            context = {'weather': weather}
            return render(request, weather_template, context)
        else:
            return render(request, weather_template, {'error': 'City not found'})
    elif request.method == 'GET':
        return render(request, weather_template)
    return render(request, weather_template, {'error': 'Not Get or Post'})