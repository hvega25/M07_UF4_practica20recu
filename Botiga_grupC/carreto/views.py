from django.shortcuts import render

#importación librerias rest_framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

#importación de model de la app
from .models import CarritoCompra

#importación de el serializers
from .serializers import carretoSerializer

#lista los elementos de la tabla
@api_view(['GET'])
def listar(request):
    listar_todo = CarritoCompra.objects.all()
    '''
    importante el many=True elimina un error de que un objecto no se 
    serializar
    '''
    serializer = carretoSerializer(listar_todo, many=True)
    return Response(serializer.data)

#metodo para crear nuevo elemento
@api_view(['GET', 'POST'])
def agregar_carrito(request):
    data  = request.data
    serializer = carretoSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Con exito" : "Fue agregado con exito"}, status=200)
    else:
        return Response(serializer.errors , status=400)
    
#método delete un elemento
@api_view(['DELETE'])
def eliminar_un_producto(request):
    prod_id  = request.data.get('id')
    try:
        carr = CarritoCompra.objects.get(id = prod_id)
        carr.delete()
        return Response({"Con exito" : "El producto fue eliminado con exito"} ,status=200)
    except CarritoCompra.DoesNotExist:
        return Response({"ERROR" : "El producto no existe"} ,status=404)
    
#método delete un elemento
@api_view(['DELETE'])
def eliminar_todo(request):
    carr  = CarritoCompra.objects.all()
    carr.delete()
    return Response({"Con exito" : "El carrito fue eliminado con exito"} ,status=200)
    