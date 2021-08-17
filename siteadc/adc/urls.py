from django.urls import path
from adc import views


urlpatterns = [
    path('', views.home, name='home'),
    path('sala/', views.sala, name='sala'),
    path('perfil/', views.perfil, name='perfil'),
    path('repositorio/', views.repositorio, name='repositorio'),
]
