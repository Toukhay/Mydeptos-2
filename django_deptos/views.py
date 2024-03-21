from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib import messages
from django.shortcuts import redirect

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