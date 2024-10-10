from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
# Create your views here.

def usuarios(request):
    if request.method == 'POST':
        data = request.POST
        nome = data.get('nome')
        email = data.get('email')
        senha = data.get('senha')

        Usuarios.objects.create(
            nome=nome,
            email=email,
            senha=senha
        )

        return redirect('/')
    
    # Renderiza o template correto
    return render(request, 'cadastro_usuarios.html')