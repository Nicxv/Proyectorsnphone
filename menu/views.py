from django.shortcuts import render

# Create your views here.
def principal(request):
    return render(request,'menu/principal.html')

def samsung(request):
    return render(request,'menu/samsung.html')

def xiaomi(request):
    return render(request,'menu/xiaomi.html')    

def micuenta(request):
    return render(request,'menu/micuenta.html')

def Samsung_galaxy_s10(request):
    return render(request,'menu/Samsung_galaxy_s10.html')

def Xiaomi_redmi_note_12(request):
    return render(request,'menu/Xiaomi_redmi_note_12.html')   

def cambiarcontra(request):
    return render(request,'menu/cambiarcontra.html')

def registro(request):
    return render(request,'menu/registro.html')    
