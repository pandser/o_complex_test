from django.conf import settings


def shake(hourly: dict[str: str|int]) -> list:
    data = []
    for i in range(23):
        hour = {}
        for k, v  in hourly.items():
            if k == 'time':
                hour[k] = v[i].split('T')
            elif k == 'weather_code':
                hour[k] = settings.WEATHER_CODE[v[i]]
            else:
                hour[k] = v[i]
        data.append(hour)
    return data
