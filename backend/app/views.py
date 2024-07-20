import requests
from django.conf import settings
from django.contrib.sessions.models import Session
from django.shortcuts import render

from app.utils import shake
from app.models import City, CityInSession


def weather(request):
    request.session['last_city'] = {
        'name': request.GET.get('name'),
        'latitude': request.GET.get('latitude'),
        'longitude': request.GET.get('longitude'),
    }
    request.session.save()
    session_obj = Session.objects.get(
        session_key=request.session.session_key,
    )
    city_obj = City.objects.get_or_create(
        name=request.GET.get('name'),
        latitude=request.GET.get('latitude'),
        longitude=request.GET.get('longitude'),
    )
    CityInSession.objects.create(
        session_id=session_obj,
        city=city_obj[0],
    )
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
    try:
        response = requests.get(
            url=settings.URL_WEATHER_API,
            params=params
            )
    except requests.exceptions.ConnectionError as error:
        return render(
            request=request,
            template_name='weather.html',
            context={
                'error': 'Не удалось запросить данные, попробуйте позже!'
            },
        )
    data = shake(response.json()['hourly'])
    return render(
        request=request,
        template_name='weather.html',
        context={
        'data': data,
        },
        )


def search(request):
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
    try:
        response = requests.get(
            url=settings.URL_GEOCODING_API,
            params=params,
        )
    except requests.exceptions.ConnectionError as error:
        return render(
            request=request,
            template_name='search.html',
            context={
                'error': 'Не удалось запросить данные, попробуйте позже!'
            },
        )
    return render(
        request=request,
        template_name='search.html',
        context=response.json(),
        )
