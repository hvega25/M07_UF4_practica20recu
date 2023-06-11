from django.shortcuts import render


#importación librerias rest_framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q

#importacion del modelo de la aplicacion
from .models import Orden

#importacion del serializador
from .serializers import ordenSerializer

#lista los elementos de la tabla que esten completados
@api_view(['GET'])
def completados(request):
    listar_todo = Orden.objects.filter(Q(estado__in=['completada', 'Completada']))
    '''
    importante el many=True elimina un error de que un objecto no se 
    serializar
    '''
    serializer = ordenSerializer(listar_todo, many=True)
    return Response(serializer.data)

#lista los elementos de la tabla que esten completados
@api_view(['GET'])
def sin_completar(request):
    listar_todo = Orden.objects.filter(~Q(estado__in=['completada', 'Completada']))
    '''
    importante el many=True elimina un error de que un objecto no se 
    serializar
    '''
    serializer = ordenSerializer(listar_todo, many=True)
    return Response(serializer.data)