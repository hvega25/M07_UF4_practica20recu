from django.urls import path

#importación de la views de la app
from . import views

urlpatterns = [
    path('listar/', views.listar, name='listar-carreto'),
    path('agregar/', views.agregar_carrito, name='add-carreto'),
]