from django.db import models

class Orden(models.Model):
    ESTADOS_ORDEN = [
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En proceso'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada'),
    ]
    '''
        Importante al momento de importar se hace directamente en la variable y no
        se escribe en la parte superior como normalmente se hace
    '''
    carrito = models.ForeignKey('carreto.CarritoCompra', on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS_ORDEN, default='pendiente')
  

   