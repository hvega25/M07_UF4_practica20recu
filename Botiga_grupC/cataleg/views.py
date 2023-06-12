from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import  Response
from .models import Producto
from .serializer import ProductoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


# Create your views here.

@api_view(['POST'])
def add_product(request):
    serializer = ProductoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return  Response(serializer.errors, status=400)

@api_view(['GET','PUT'])
def update_product(request, pk):
    try:
        product = Producto.objects.get(pk=pk)
    except Producto.DoesNotExist:
        return Response({'error':'Producto no encontrado'}, status=404)
    if request.method == 'PUT':
        serializer = ProductoSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'GET':
        serializer = ProductoSerializer(product)
        return Response(serializer.data)

@api_view(['DELETE'])
def delete_product(request, pk):
    try:
        product = Producto.objects.get(pk=pk)
    except Producto.DoesNotExist:
        return Response({'error':'Producto no encontrado'}, status=404)
    product.delete()
    return Response(status=204)

@api_view(['GET'])
def view_product(request,pk):
    try:
        product = Producto.objects.get(pk=pk)
    except Producto.DoesNotExist:
        return Response({'error':'Producto no encontrado'}, status=404)
    serializer = ProductoSerializer(product)
    return Response(serializer.data)