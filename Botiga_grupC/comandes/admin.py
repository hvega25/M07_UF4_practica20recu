from django.contrib import admin


#modelo importado de la aplicación carreto
from . import models

#El admin.py lo uso para poder usar los modelos de la aplicación.
admin.site.register(models.Orden)
