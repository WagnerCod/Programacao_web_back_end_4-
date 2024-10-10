from django.urls import path
from . import views 

urlpatterns = [
    path('cadastro_usuarios/', views.usuarios, name='cadastro_usuarios'),  # URL da rota
]