from django.db import models


class CarritoCompra(models.Model):
     cantidad = models.PositiveIntegerField()
     metodo_envio = models.CharField(max_length=100)
   

     def __str__(self):
        campos = []
        for field in self._meta.fields:
            field_value = getattr(self, field.name)
            campos.append(f"{field.name}: {field_value}")
        return ', '.join(campos)