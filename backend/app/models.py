from django.db import models
from django.contrib.sessions.models import Session


class City(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()


class CityInSession(models.Model):
    session_id = models.ForeignKey(
        Session,
        on_delete=models.CASCADE,
        related_name='session_id',
    )
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name='city',
    )
