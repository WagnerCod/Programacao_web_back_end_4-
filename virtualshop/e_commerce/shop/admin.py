from django.contrib import admin
from .models import Produto, Categoria

# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug']
    prepopulated_fields = {'slug': ('nome',)}
    
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug', 'preco', 'categoria', 'disponivel']
    list_filter = ['disponivel', 'criado', 'atualizado']
    list_editable = ['preco', 'disponivel']
    prepopulated_fields = {'slug':('nome',)}

