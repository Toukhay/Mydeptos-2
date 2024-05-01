from django.shortcuts import render
from .models import Listing

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def listings(request):
    return render(request, 'listings.html')


def search(request):
    return render(request, 'search.html')

def view_property(request):
    return render(request, 'view_property.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def user_panel(request):
    return render(request, 'user_panel.html')

def post_property(request):
    return render(request, 'post_property.html')

def view_property(request):
    return render(request, 'view_property.html')

def favorites(request):
    return render(request, 'favorite.html')