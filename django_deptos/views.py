from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import logout
from .forms import RegisterForm

from django.contrib.auth.models import User

def login_view(request):

    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username= username, password = password)
        if user:
            login(request, user)
            messages.success(request,'Ha iniciado sesion')
            print('loggeado')
            return redirect('home')
        else:
            print('no logg')
            messages.error(request, 'Acesso denegado')

    return render(request,"usuarios/login.html")

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada correctamente')
    return redirect('login')

def registro(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        phone = form.cleaned_data.get('phone')
        localidad = form.cleaned_data.get('localidad')

        user = User.objects.create_user(username=username,email=email,password=password)
        user.phone = phone
        user.localidad = localidad
        
        if user:
            login(request,user)
            messages.success(request,'Usuario creado existosamente')

            if request.GET.get('next'):
                 return HttpResponseRedirect(request.GET['next'])

            return redirect('home')

    return render(request, 'usuarios/register.html',{
        'form':form
    })