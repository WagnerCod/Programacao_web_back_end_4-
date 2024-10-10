from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length = 200)
    slug = models.SlugField(max_length = 200, unique = True)
    
    class Meta:
        ordering = ['nome']
        indexes = [
            models.Index(fields = ['nome']),
        ]
        verbose_name = 'categoria'
        verbose_name_plural  =  'categorias'
        
    def _str_(self):
        return self.name

class Produto(models.Model):
    categoria  =  models.ForeignKey(
        Categoria,
        related_name = 'produtos',
        on_delete = models.CASCADE
    ) 
    nome = models.CharField(max_length = 200)
    slug = models.SlugField(max_length = 200)
    imagem = models.ImageField(
        upload_to = 'produtos/%Y/%m/%d',
        blank = True
    )
    descricao = models.TextField(blank = True)
    preco  =  models.DecimalField(max_digits = 10, decimal_places = 2)
    disponivel = models.BooleanField(default = True)
    criado = models.TimeField(auto_now_add = True)
    atualizado = models.DateTimeField(auto_now = True)  

class Meta:
    ordering = ['nome']
    indexes = [
        models.Index(fields = ['id','slug']),
        models.Index(fields = ['nome']),
        models.Index(fields = ['-criado']),
    ]
    
    def _str_(self):
        return self.nome    