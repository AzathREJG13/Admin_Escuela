from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)  
            return redirect('home')   
        else:
            messages.error(request, 'Credenciales inválidas')  

    return render(request, 'login.html')

@login_required
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.success(request, 'Cuenta creada con éxito. Por favor, inicia sesión.') 
            return redirect('login')  
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/registro.html', {'form': form})

def inicio(request):
    return render(request, 'inicio.html')