#libreria rest framework
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

#libreria que llama a la aplicación
from .models import Orden




class ordenSerializer(ModelSerializer):
    carrito = serializers.StringRelatedField()
    class Meta:
        model = Orden
        fields = '__all__'
    

    
