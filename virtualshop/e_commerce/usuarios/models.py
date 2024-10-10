from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nome = models.CharField(max_length = 100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length = 100)