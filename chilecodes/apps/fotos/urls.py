from django.urls import path
from .views import agregarFoto
urlpatterns = [
    path('agregarFoto/',agregarFoto, name='agregarFoto')
]