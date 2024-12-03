from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def registro(request):
    return render(request, '/home/rafael1302/Escritorio/Login/apps/App1/templates/registration/registro.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)  # Inicia sesión
            return redirect('home')   # Redirige al home si las credenciales son válidas
        else:
            messages.error(request, 'Credenciales inválidas')  # Muestra un mensaje de error

    return render(request, 'login.html')

@login_required
def home(request):
    return render(request, 'home.html')
