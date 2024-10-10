from django.shortcuts import render, redirect
from django.http import HttpResponse
from models import *

def produtos(request):
    #pegando dados do html form
    if request.method == 'POST':
        data = request.POST
        produto_nome = data.get('produto_nome') 
        produto_descricao = data.get('produto_descricao')
        produto_imagem = request.FILES.get('produto_imagem')
        
        Produtos.objects.create(
            produto_nome = produto_nome,
            produto_descricao = produto_descricao,
            produto_imagem = produto_imagem
        )
    return redirect('/')

def deletar_produtos(request, id):
    query = Produtos.objects.get(id = id)
    query.delete()
    return redirect('/')

