''' 
Clase que permite convertir objetos complejos de Python, como modelos de Django, 
en tipos de datos nativos de Python y viceversa.  
'''

#libreria rest framework
from rest_framework.serializers import ModelSerializer 

#libreria que llama a la aplicación
from .models import CarritoCompra


class carretoSerializer(ModelSerializer):
    class Meta:
        model = CarritoCompra
        fields = '__all__'
    


   