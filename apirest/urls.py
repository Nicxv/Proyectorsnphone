from django.contrib import admin
from django.urls import path, include
from .views import lista_usuario, lista_venta

urlpatterns = [
    path('lista_usuario/',lista_usuario,name="lista_usuario"),
    path('lista_venta/',lista_venta,name="lista_venta")
]