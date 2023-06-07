from django.contrib import admin
from django.urls import path, include
from .views import lista_usuario,lista_venta,lista_u,lista_v


urlpatterns = [
    path('lista_usuario',lista_usuario,name="lista_usuario"),
    path('lista_venta/',lista_venta,name="lista_venta"),
    path('lista_u/<id>',lista_u,name="lista_u"),
    path('lista_v/<id>',lista_v,name="lista_v"),
       
    ]