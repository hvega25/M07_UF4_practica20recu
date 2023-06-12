from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import  Response
from .models import Producto
from .serializer import ProductoSerializer

# Create your views here.

@api_view(['POST'])
def add_product(request):
    serializer = ProductoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return  Response(serializer.errors, status=400)
