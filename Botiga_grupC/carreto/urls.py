from django.urls import path

#importación de la views de la app
from . import views

urlpatterns = [
    #ruta para listar 
    path('listar/', views.listar, name='listar-carreto'),
     #ruta para agregar
    path('agregar/', views.agregar_carrito, name='add-carreto'),
    #ruta para eliminar 
    path('eliminar-producto/' , views.eliminar_un_producto, name='delete_prod'),
    #ruta para eliminar todo el carrito
    path('eliminar-todo/' , views.eliminar_todo, name='delete_all'),
    #ruta para obtener el elemento a editar
    path('editar/' , views.obtener_articulo, name='obtener'),
    path('update-articulo/' , views.UpdateArticulo, name='update-art'),
]