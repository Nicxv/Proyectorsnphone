from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate,login, logout
from django.views.decorators.csrf import csrf_exempt

from menu.forms import ProductoForm

from .models import Usuario, Rol, Venta, Detalle_venta, Producto, Marca, Sucursal, Direccion, Comuna, Region

# Create your views here.
def principal(request):
    return render(request,'menu/principal.html')
   
def iniciar_sesion(request):
        nombre = request.POST['nombre']
        clave = request.POST['clave']
        nombre = authenticate(request, username=nombre, password=clave)

        if nombre is not None:
            # Iniciar sesión
            login(request, nombre)
            mensaje_exito = "Usuario Autenticado"
            return redirect('principal')  # Redirigir a la página de inicio después del inicio de sesión
        else:
            # Las credenciales son incorrectas, mostrar un mensaje de error
            mensaje_error = "Nombre o contraseña incorrectos"
            return render(request,'menu/micuenta.html')   
    
def micuenta(request):
    return render(request,'menu/micuenta.html')


def cambiarcontra(request):
    return render(request,'menu/cambiarcontra.html')

def registro(request):
    return render(request,'menu/registro.html')

@csrf_exempt
def guardar_registro(request):
    if request.method == 'POST':
        rut = request.POST.get('rut')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        direccion = request.POST.get('direccion')
        clave = request.POST.get('clave')
        
        registro = Usuario(rut=rut, nombre=nombre, apellido=apellido, correo=correo, direccion=direccion, clave=clave)
        registro.save()

        
        return render(request, 'menu/exito.html')

def exito(request):
    return render(request,'menu/exito.html')  

#modificar producto
def actualizar_producto(request):
    id_productoM = request.POST['id_producto']
    nombreM = request.POST['nombre']
    descripcionM = request.POST['descripcion']
    precioM = request.POST['precio']
    stockM = request.POST['stock']

    producto = Producto.objects.get(id_producto = id_productoM)
    producto.nombre = nombreM
    producto.descripcion = descripcionM
    producto.precio = precioM
    producto.stock = stockM

    producto.save()
    return redirect('listacelular')

def modificar_producto(request, id_producto): 
    
    producto = Producto.objects.get(id_producto = id_producto)

    contexto = {
        "datos": producto 
    }
    return render(request,'menu/modificar_producto.html',contexto) 

def eliminar_producto(request, id_producto):
    producto = Producto.objects.get(id_producto=id_producto)
    producto.delete()
    return redirect("listacelular") 


def registrarse(request):
    return render(request,'menu/registrarse.html')  

def carrito(request):
    return render(request,'menu/carrito.html') 

def pago2(request):
    return render(request,'menu/pago2.html') 


# listas 
def lista_usuario(request):

    usuarios = Usuario.objects.all()

    listaU = {
        'usuarios': usuarios
    }
    return render(request,'menu/lista_usuario.html', listaU)



def listacelular(request):

    celulares = Producto.objects.all()

    datos = {
        'celulares': celulares
    }
    return render(request,'menu/listacelular.html', datos)

@csrf_exempt
def registrar_celular(request):

    if request.method == 'POST':
        id_producto = request.POST.get('id_producto')
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
        
        registrar = Producto(id_producto, nombre=nombre, descripcion=descripcion, precio=precio, stock=stock)
        registrar.save()
        
        return redirect('listacelular')
        
    
def form_celular(request):
    return render(request, 'menu/form_celular.html')    

# Celulares samsung
def samsung(request):
    arregloProductos = Producto.objects.all()
    contexto = {
        "productos": arregloProductos
    }

    return render(request,'menu/samsung.html')

    
def Samsung_galaxy_s10(request):
    return render(request,'menu/Samsung_galaxy_s10.html')

def Samsung_galaxy_a03(request):
    return render(request,'menu/Samsung_galaxy_a03.html')

def Samsung_galaxy_a22(request):
    return render(request,'menu/Samsung_galaxy_a22.html')

def Samsung_galaxy_a53(request):
    return render(request,'menu/Samsung_galaxy_a53.html')

def Samsung_galaxy_a54(request):
    return render(request,'menu/Samsung_galaxy_a54.html')

def Samsung_galaxy_a73(request):
    return render(request,'menu/Samsung_galaxy_a73.html')

def Samsung_galaxy_s23s(request):
    return render(request,'menu/Samsung_galaxy_s23s.html')

def Samsung_galaxy_z_flip4(request):
    return render(request,'menu/Samsung_galaxy_z_flip4.html')

# Vistas de celulares xiaomi

def xiaomi(request):
    return render(request,'menu/xiaomi.html')

def Xiaomi_redmi_note_12(request):
    return render(request,'menu/Xiaomi_redmi_note_12.html')  

def Xiaomi_mi_8_lite(request):
    return render(request,'menu/Xiaomi_mi_8_lite.html')  

def Xiaomi_poco_mxi5(request):
    return render(request,'menu/Xiaomi_poco_mxi5.html')  

def Xiaomi_redmi_10_5g(request):
    return render(request,'menu/Xiaomi_redmi_10_5g.html')  

def Xiaomi_redmi_10_2022(request):
    return render(request,'menu/Xiaomi_redmi_10_2022.html')  

def Xiaomi_redmi_10(request):
    return render(request,'menu/Xiaomi_redmi_10.html')  

def Xiaomi_redmi_note_10s(request):
    return render(request,'menu/Xiaomi_redmi_note_10s.html')  

def Xiaomi_redmi_note_11(request):
    return render(request,'menu/Xiaomi_redmi_note_11.html')   

def PantallaAdmin2(request):
    return render(request, 'menu/PantallaAdmin2.html')

def boleta(request):
    return render(request, 'menu/boleta.html')

def carrito2(request):
    return render(request, 'menu/carrito2.html')






