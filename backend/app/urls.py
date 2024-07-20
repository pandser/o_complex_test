from django.urls import path

from app import views


app_name = 'app'

urlpatterns = [
    path('search/', views.search, name='search'),
    path('weather/', views.weather, name='weather'),
]
