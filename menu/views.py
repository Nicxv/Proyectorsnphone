from django.shortcuts import render

# Create your views here.
def principal(request):
    return render(request,'menu/principal.html')
    
def micuenta(request):
    return render(request,'menu/micuenta.html')

def cambiarcontra(request):
    return render(request,'menu/cambiarcontra.html')

def registro(request):
    return render(request,'menu/registro.html') 


# Vistas de celulares samsung
def samsung(request):
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








def index(request):
    return render(request,'menu/index.html')

def home(request):
    return render(request,'menu/home.html')

def contacto(request):
    return render(request,'menu/contacto.html')

def borgona(request):
    nombreMascota= "Copito de Nieve"
    edadMascota = 4
    razaMascota = "Pitbull"

    contexto = {
        "datito1": nombreMascota,
        "datito2": edadMascota,
        "datito3": razaMascota
    }

    return render(request,'menu/borgona.html',contexto)


def borgona2(request):
    lista = ["Borgoña","Copito de Nieve","Joselito"]

    contexto = {
        "nombres": lista
    }
    return render(request,'menu/borgona2.html',contexto)