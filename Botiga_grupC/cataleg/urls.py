from django.urls import path
from . import views

urlpatterns = [
    path('products/add/', views.add_product, name="Añadir Producto"),
    path('products/update/<int:pk>', views.update_product, name = "Actualizar Producto"),
    path('products/delete/<int:pk>/', views.delete_product, name="Borrar Producto")
]