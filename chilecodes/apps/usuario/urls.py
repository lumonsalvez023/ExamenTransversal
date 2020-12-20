from django.urls import path
from .views import iniciarSesion, perfil, registro, loginSocial, perfilAdmi, iniciarSesionAdmi

urlpatterns = [
    path('iniciarSesion/',iniciarSesion,name='iniciarSesion'),
    path('registro/',registro,name='registro'),
    path('perfil/',perfil,name='perfil'),
    path('loginSocial/', loginSocial,name='loginSocial'),
    path('perfilAdmi/', perfilAdmi,name='perfilAdmi'),
    path('iniciarSesionAdmi/', iniciarSesionAdmi,name='iniciarSesionAdmi')
]