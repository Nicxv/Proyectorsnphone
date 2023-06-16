from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate,login, logout

from menu.forms import ProductoForm

from .models import Usuario, Rol, Venta, Detalle_venta, Producto, Marca, Sucursal, Direccion, Comuna, Region

# Create your views here.
def principal(request):
    return render(request,'menu/principal.html')


def inicio_sesion(request):
    return render(request,'menu/micuenta.html')    

def micuenta(request):

    usuario1 = request.post['usuario']
    contra1 = request.post['contra']
    try:
        user1 = User.objects.get(username = usuario1)
    except User.DoesNotExist:
        messages.error(request,'El usuario o la contraseña son incorrectos')
        return redirect('iniciar')  

    pass_valida = check_password(contra1, user1.password)
    if not pass_valida:
        messages.error(request,'El usuario o la contraseña son incorrectos')
        return redirect ('iniciar')
    usuario2 = Usuario.objects.get(correo = usuario1,psw = contra1)
    user = authenticate(username=usuario1, password=contra1)
    if user is not None:
        login(request, user)
        if(usuario2.tipousuario.idTipoUsuario ==1):
            return redirect ('menu_admin')
        else:
            contexto = {"usuario":usuario2}             

    return render(request,'menu/micuenta.html', contexto)


def cambiarcontra(request):
    return render(request,'menu/cambiarcontra.html')

def registro(request):
    return render(request,'menu/registro.html')

def registrarse(request):
    return render(request,'menu/registrarse.html')  

def carrito(request):
    return render(request,'menu/carrito.html') 

def pago2(request):
    return render(request,'menu/pago2.html') 


# listas de celulares samsung
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


def form_celular(request):

    datos = {
        'form': ProductoForm()

    }
    if request.method== 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardados correctamente"

    return render(request,'menu/form_celular.html', datos)


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






