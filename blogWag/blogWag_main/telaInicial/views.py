from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .models import Postagem, Usuario, Comentario
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    postagens = Postagem.objects.all().order_by('-data_hora')
    usuario = None
    admin = False
    if request.user.is_authenticated:
        usuario = request.user
        admin = usuario.is_superuser
        print(usuario)
    return render(request, 'telaInicial/home.html', {'postagens': postagens, 'usuario': usuario, 'admin': admin})


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = authenticate(request, username=email, password=senha)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'telaInicial/login.html', {'erro': 'Email ou senha incorretos'})
    return render(request, 'telaInicial/login.html')

def logout(request):
    auth_logout(request)
    return redirect('home')

def createUser(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        senha2 = request.POST.get('senha2')
        foto = request.FILES.get('foto')

        if User.objects.filter(email=email).exists():
            return render(request, 'telaInicial/cadastroUsuario.html', {'erro': 'Email já cadastrado'})


        if senha != senha2:
            return render(request, 'telaInicial/cadastroUsuario.html', {'erro': 'As senhas não coincidem'})

        user = User.objects.create_user(username=email, email=email, password=senha)
        user.save()

        # Criar usuário na tabela Usuario com vínculo ao User
        usuario = Usuario.objects.create(user=user, nome=nome, foto=foto)
        usuario.save()

        return redirect('login')  

    return render(request, 'telaInicial/cadastroUsuario.html')

def createPost(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        foto = request.FILES.get('foto')

        postagem = Postagem(titulo=titulo, descricao=descricao, foto=foto)
        postagem.save()

        return redirect('home')
    return render(request, 'telaInicial/postar.html')

def deletePost(request, id):
    postagem = get_object_or_404(Postagem, id=id)
    postagem.delete()
    return redirect('home')

@login_required
def comentar(request, id):
    postagem = get_object_or_404(Postagem, id=id)

    if request.method == 'POST':
        texto = request.POST.get('texto')
        if texto.strip():
            Comentario.objects.create(
                postagem=postagem,
                usuario=request.user,
                texto=texto
            )
    
    return redirect('home')