from django.contrib import admin
from django.urls import path, include
from .views import exito, registrar_usuario, inicio_sesion, principal, samsung, xiaomi, pago2, Xiaomi_redmi_note_12, Xiaomi_mi_8_lite,Xiaomi_poco_mxi5,Xiaomi_redmi_10_5g,Xiaomi_redmi_10_2022,Xiaomi_redmi_10,Xiaomi_redmi_note_10s,Xiaomi_redmi_note_11, Samsung_galaxy_s10,Samsung_galaxy_a03,Samsung_galaxy_a22,Samsung_galaxy_a53,Samsung_galaxy_a54,Samsung_galaxy_a73,Samsung_galaxy_s23s,Samsung_galaxy_z_flip4, registro, cambiarcontra, micuenta, carrito

urlpatterns = [
    path('',principal,name="principal"),
    path('samsung',samsung,name="samsung"),
    # Urls de xiaomi
    path('xiaomi',xiaomi,name="xiaomi"),
    path('Xiaomi_redmi_note_12',Xiaomi_redmi_note_12,name="Xiaomi_redmi_note_12"),
    path('Xiaomi_mi_8_lite',Xiaomi_mi_8_lite,name="Xiaomi_mi_8_lite"),
    path('Xiaomi_poco_mxi5',Xiaomi_poco_mxi5,name="Xiaomi_poco_mxi5"),
    path('Xiaomi_redmi_10_5g',Xiaomi_redmi_10_5g,name="Xiaomi_redmi_10_5g"),
    path('Xiaomi_redmi_10_2022',Xiaomi_redmi_10_2022,name="Xiaomi_redmi_10_2022"),
    path('Xiaomi_redmi_10',Xiaomi_redmi_10,name="Xiaomi_redmi_10"),
    path('Xiaomi_redmi_note_10s',Xiaomi_redmi_note_10s,name="Xiaomi_redmi_note_10s"),
    path('Xiaomi_redmi_note_11',Xiaomi_redmi_note_11,name="Xiaomi_redmi_note_11"),
    # Urls de samsung
    path('Samsung_galaxy_s10',Samsung_galaxy_s10,name="Samsung_galaxy_s10"),
    path('Samsung_galaxy_a03',Samsung_galaxy_a03,name="Samsung_galaxy_a03"),
    path('Samsung_galaxy_a22',Samsung_galaxy_a22,name="Samsung_galaxy_a22"),
    path('Samsung_galaxy_a53',Samsung_galaxy_a53,name="Samsung_galaxy_a53"),
    path('Samsung_galaxy_a54',Samsung_galaxy_a54 ,name="Samsung_galaxy_a54"),
    path('Samsung_galaxy_a73',Samsung_galaxy_a73,name="Samsung_galaxy_a73"),
    path('Samsung_galaxy_s23s',Samsung_galaxy_s23s,name="Samsung_galaxy_s23s"),
    path('Samsung_galaxy_z_flip4',Samsung_galaxy_z_flip4,name="Samsung_galaxy_z_flip4"),

    path('cambiarcontra',cambiarcontra,name="cambiarcontra"),
    path('registro',registro,name="registro"),
    path('micuenta',micuenta,name="micuenta"),
    path('carrito',carrito,name="carrito"),
    path('pago2',pago2,name="pago2"),
    path('inicio_sesion',inicio_sesion,name="inicio_sesion"),
    path('registrar_usuario',registrar_usuario, name='registrar_usuario'),
    path('exito/', exito, name='exito') 


 
 
]