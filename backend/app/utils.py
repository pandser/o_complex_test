WEATHER_CODE = {
    0: 'Ясно',
    1: 'Малооблачно',
    2: 'Переменная облачность',
    3: 'Пасмурно',
    45: 'Туман',
    48: 'Иней',
    51: 'Слабый дождь', 
    53: 'Слабый дождь', 
    55: 'Слабый дождь',
    56: 'Ледяная морозь',
    57: 'Ледяная морозь',
    61: 'Дождь',
    63: 'Дождь',
    65: 'Дождь',
    66: 'Ледяной дождь',
    67: 'Ледяной дождь',
    71: 'Снег',
    73: 'Снег',
    75: 'Снег',
    77: 'Снежная крупа',
    80: 'Ливень',
    81: 'Ливень',
    82: 'Ливень',
    85: 'Снегопад',
    86: 'Снегопад',
    96: 'Гроза',
    95: 'Гроза с градом',
    99: 'Гроза с градом',
}


def shake(hourly: dict[str: str|int]) -> list:
    data = []
    for i in range(23):
        hour = {}
        for k, v  in hourly.items():
            if k == 'time':
                hour[k] = v[i].split('T')
            elif k == 'weather_code':
                hour[k] = WEATHER_CODE[v[i]]
            else:
                hour[k] = v[i]
        data.append(hour)
    return data


if __name__ == '__main__':
    import requests


    params = {
        'latitude': 45.0428,
        'longitude': 41.9734,
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
    
    s = shake(response.json()['hourly'])
    for _ in s:
        print(_)
