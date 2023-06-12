from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField("nombre",max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    fabricante = models.CharField("fabricante",max_length=100)
    pais = models.CharField("pais",max_length=50)
    categoria = models.CharField(max_length=255)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre