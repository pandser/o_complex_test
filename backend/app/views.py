from django.shortcuts import render
from django.template.response import TemplateResponse
import requests

from app.utils import shake


def weather(request):
    request.session['last_city'] = {
        'name': request.GET.get('name'),
        'latitude': request.GET.get('latitude'),
        'longitude': request.GET.get('longitude'),
    }
    params = {
        'latitude': request.GET.get('latitude'),
        'longitude': request.GET.get('longitude'),
        'hourly': [
            'temperature_2m', 
            'weather_code',
            'wind_speed_10m',
            'wind_direction_10m',
        ],
        'wind_speed_unit': 'ms',
        'forecast_days': 1,
    }
    response = requests.get(
        url='https://api.open-meteo.com/v1/forecast',
        params=params
        )
    data = shake(response.json()['hourly'])
    context = {
        'data': data,
    }
    return render(
        request,
        'weather.html',
        context,
        )


def city(request):
    if not request.GET.get('city'):
        return render(
        request=request,
        template_name='search.html',
        )
    params = {
        'name': request.GET.get('city'),
        'count': 10,
        'language': 'ru',
        'format': 'json',
    }
    response = requests.get(
        url='https://geocoding-api.open-meteo.com/v1/search',
        params=params,
    )
    print(request.session.get('last_city'))
    return render(
        request=request,
        template_name='search.html',
        context=response.json(),
        )
