from rest_framework import serializers
from menu.models import Usuario, Venta
class UsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id_usuario', 'rut', 'nombre', 'apellido', 'correo', 'direccion', 'clave']

class VentaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = ['id_venta', 'fecha_venta', 'total', 'estado', 'carrito']

