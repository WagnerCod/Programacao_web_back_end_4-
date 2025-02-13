from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Postagem(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    foto = models.ImageField(upload_to='postagens/', null=True, blank=True)
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)  # Permite valores nulos
    nome = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='usuarios/', null=True, blank=True)

    def __str__(self):
        return self.nome
    
class Comentario(models.Model):
    postagem = models.ForeignKey('Postagem', on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentário de {self.usuario.username} em {self.postagem.titulo}'