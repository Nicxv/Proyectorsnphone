from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate,login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from .models import Usuario, Rol, Venta, Detalle_venta, Producto, Marca, Sucursal, Direccion, Comuna, Region

# Create your views here.
def principal(request):
    return render(request,'menu/principal.html')

def verperfil(request):

    verUsuario = Usuario.objects.all()

    contexto = {
        "vUsuario": verUsuario
    }
    return render(request,'menu/verperfil.html', contexto)

def actualizar_usuario(request):
    rutM = request.POST['rut']
    nombreM = request.POST['nombre']
    apellidoM = request.POST['apellido']
    direccionM = request.POST['direccion']

    usuario = Usuario.objects.get(rut = rutM)
    if rutM !='':
        usuario.rut=rutM

    if nombreM !='':
        usuario.nombre=nombreM

    if apellidoM !='':
        usuario.apellido=apellidoM

    if direccionM !='':
        usuario.direccion=direccionM

    usuario.save()

    contexto = {
        "modificarU": usuario
    }
    
    return render(request, 'menu/micuenta.html',contexto)

def modificar_usuario(request, id):

    usuarioM = Usuario.objects.get(id_usuario = id)

    contexto = {
        "modU": usuarioM 
    }
    return render(request,'menu/modificar_usuario.html',contexto)
   
def iniciar_sesion(request):
        vCorreo = request.POST['correo']
        vClave = request.POST['clave']
        registro = Usuario.objects.all()
        correo = authenticate(request, username=vCorreo, password=vClave)

        if correo is not None:
            # Iniciar sesión
            login(request, correo)
            mensaje_exito = "Usuario Autenticado"
            return redirect('principal2')  # Redirigir a la página de inicio después del inicio de sesión
        else:
            # Las credenciales son incorrectas, mostrar un mensaje de error
            mensaje_error = "Nombre o contraseña incorrectos"
            return render(request,'menu/micuenta.html')   
    
def micuenta(request):
    logout(request)
    return render(request,'menu/micuenta.html')


def cambiarcontra(request):
    return render(request,'menu/cambiarcontra.html')

def registro(request):
    return render(request,'menu/registro.html')


def guardar_registro(request):
        contexto = {} 

        vRutU = request.POST['rut']
        contexto["rut"]=vRutU

        vNombreU = request.POST['nombre']
        contexto["nombre"]=vNombreU

        vApellidoU = request.POST['apellido']
        contexto["apellido"]=vApellidoU

        vCorreoU = request.POST['correo']
        contexto["correo"]=vCorreoU

        vDireccionU = request.POST['direccion']
        contexto["direccion"]=vDireccionU

        vClaveU = request.POST['clave']
        contexto["clave"]=vClaveU

        valida = Usuario.objects.all()

        for forcorreo in valida:
            if forcorreo.correo == vCorreoU:
                messages.error(request,"El correo ya existe")
                return render(request,'menu/registrarse.html',contexto)
            
        Usuario.objects.create(rut=vRutU, nombre=vNombreU, apellido=vApellidoU, correo=vCorreoU,
                               direccion=vDireccionU, clave=vClaveU)    
        
        user = User.objects.create_user(vCorreoU,vCorreoU, vClaveU)

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


def registrar_celular(request):
    contexto = {} 

    pid_producto = request.POST['id_producto']
    contexto["id_producto"]=pid_producto

    pnombre = request.POST['nombre']
    contexto["nombre"]=pnombre

    pdescripcion = request.POST['descripcion']
    contexto["descripcion"]=pdescripcion

    pprecio = request.POST['precio']
    contexto["precio"]=pprecio

    pstock = request.POST['stock']
    contexto["stock"]=pstock

    pfoto = request.FILES['foto']


    Producto.objects.create(id_producto=pid_producto, nombre=pnombre, descripcion=pdescripcion,
                            precio=pprecio, stock=pstock, foto=pfoto)



    valida = Usuario.objects.all()

       
   
        
    return redirect('form_celular')

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

def principal2(request):
    return render(request, 'menu/principal2.html')





