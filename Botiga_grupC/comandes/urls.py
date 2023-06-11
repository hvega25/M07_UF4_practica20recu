from django.urls import path

#importación de la views de la app
from . import views


urlpatterns = [
    #ruta para listar 
    path('completados/', views.completados, name='completados'),
    path('sin-completar/', views.sin_completar, name='sinCompletar'),
]