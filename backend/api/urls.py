from django.urls import include, path
from rest_framework import routers

from api.views import CityViewSet


app_name = 'api'

router = routers.DefaultRouter()

router.register(
    'stat',
    CityViewSet,
    basename='stat',
)

urlpatterns = [
    path('', include(router.urls)),
]
