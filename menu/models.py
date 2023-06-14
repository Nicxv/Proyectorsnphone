from django.db import models

# Create your models here.

class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    correo = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)
    clave = models.CharField(max_length=20)
    

    def __str__(self) -> str:
        return self.nombre

class Rol(models.Model): 
    id_rol = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)

class Venta(models.Model):
    id_venta = models.IntegerField(primary_key=True)
    fecha_venta = models.DateField()
    total = models.IntegerField()
    estado = models.CharField(max_length=20)
    carrito = models.IntegerField()

class Detalle_venta(models.Model):  
    id_detalle = models.IntegerField(primary_key=True)   
    cantidad = models.IntegerField()
    subtotal = models.IntegerField()

class Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True)   
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=300)
    precio = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self) -> str:
        return self.nombre

class Marca(models.Model):
    id_marca = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.nombre

class Sucursal(models.Model):
    id_sucursal = models.IntegerField(primary_key=True) 
    nombre = models.CharField(max_length=30)

class Direccion(models.Model):
    id_direccion = models.IntegerField(primary_key=True)
    calle = models.CharField(max_length=30) 
    numero_c = models.IntegerField()

class Comuna(models.Model):  
    id_comuna = models.IntegerField(primary_key=True)   
    nombre = models.CharField(max_length=30) 

class Region(models.Model):
    id_region = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)  



    
