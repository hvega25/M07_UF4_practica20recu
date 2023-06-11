from django.urls import path

#importación de la views de la app
from . import views


urlpatterns = [
    #ruta para listar 
    path('listar/', views.listar, name='listar-comanda'),
]