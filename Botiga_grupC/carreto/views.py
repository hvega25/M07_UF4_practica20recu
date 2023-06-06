from django.shortcuts import render

#importación librerias rest_framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

#importación de model de la app
from .models import CarritoCompra

#importación de el serializers
from .serializers import carretoSerializer

@api_view(['GET'])
def listar(request):
    listar_todo = CarritoCompra.objects.all()
    '''
    importante el many=True elimina un error de que un objecto no se 
    serializar
    '''
    serializer = carretoSerializer(listar_todo, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def agregar_carrito(request):
    data  = request.data
    serializer = carretoSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Con exito" : "Fue agregado con exito"})
    else:
        return Response(serializer.errors , status=400)
    
