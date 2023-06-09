from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from menu.models import Usuario
from .serializers import UsuarioSerializers
from menu.models import Venta
from .serializers import VentaSerializers


# Create your views here.
@csrf_exempt
@api_view(['GET', 'POST'])
def lista_usuario(request):
    if request.method == 'GET':
        usu = Usuario.objects.all()
        serializer = UsuarioSerializers(usu,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UsuarioSerializers(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET', 'POST'])
def lista_venta(request):
    if request.method == 'GET':
        ven = Venta.objects.all()
        serializer = VentaSerializers(ven,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VentaSerializers(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'DELETE'])  
def lista_u(request, id):
    """
    Get, update, o delete de un usuario en particular
    """
    try:
        usu = Usuario.objects.get(id_usuario=id)     
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)     
    if request.method == 'GET':
        serializer = UsuarioSerializers(usu)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UsuarioSerializers(usu, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        usu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'PUT', 'DELETE'])  
def lista_v(request, id):
    """
    Get, update, o delete de un usuario en particular
    """
    try:
        ven = Venta.objects.get(id_venta=id)     
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)     
    if request.method == 'GET':
        serializer = VentaSerializers(ven)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = VentaSerializers(ven, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        ven.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        

