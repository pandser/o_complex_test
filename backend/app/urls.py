from django.urls import include, path

from app import views


app_name = 'app'

urlpatterns = [
    path('search/', views.city, name='search'),
    path('weather/', views.weather, name='weather'),
]
