from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    if request.method=='POST':
        nombreUsuario = request.POST.get('nombreUsuario') #Capturamos el usuario y password ingresado en el HTML
        contraUsuario = request.POST.get('contraUsuario')
        usuarioInfo = authenticate(request,username=nombreUsuario,password=contraUsuario) #valida si usuario y password existen
        if usuarioInfo is not None:  #existe
            login(request,usuarioInfo) # indica que hay un usuario que accede al sistema
            return HttpResponseRedirect(reverse('gestion_tienda:consolaAdministrador')) #Redireccionamos a la consola de adminstración de usuarios
        else:
            return HttpResponseRedirect(reverse('gestion_tienda:index')) #Nos lleva a la ruta index de la aplicación gestion_tienda
    return render(request,'ingresoUsuario.html')                         #Ya no hace request, renderiza la vista de login   

@login_required(login_url='http://127.0.0.1:8000')      # En caso usuario no haya sido autenticado se va la ruta vacía
def consolaAdministrador(request):
    return render(request,'consolaAdministrador.html')
