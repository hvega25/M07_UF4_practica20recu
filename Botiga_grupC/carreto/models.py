from django.db import models


class CarritoCompra(models.Model):
    #producto = models.ForeignKey(Catalogo, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    metodo_envio = models.CharField(max_length=100)

   
    #Función para calcular el subtotal 
    ''' def subtotal(self):
        return self.producto.precio * self.cantidad
    '''