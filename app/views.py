from django.shortcuts import render
from .models import Localidad, Agente, Departamento, Foto, Usuario, Listing #importamos los modelos que creamos en models.py para poder usarlos en las vistas y poder mostrar la informacion en el html

def home(request):
    listings = Listing.objects.all()
    context = {
        'listings': listings,
    }
    return render(request, 'home.html', context)#esto hace que se renderice el archivo home.html que esta en la carpeta templates de la app

def about(request):
    return render(request, 'about.html') #esto hace que se renderice el archivo about.html que esta en la carpeta templates de la app

def contact(request):
    return render(request, 'contact.html')

def listings(request):
    return render(request, 'listings.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def search(request):
    return render(request, 'search.html')

def view_property(request):
    return render(request, 'view_property.html')

def PanelUsuario(request):
    return render(request, 'user_panel.html')






