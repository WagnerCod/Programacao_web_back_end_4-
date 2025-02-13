from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('cadastroUsuario/', views.createUser, name='create_user'),
    path('logout/', views.logout, name='logout'),
    path('createPost/', views.createPost, name='createPost'),
    path('deletePost/<int:id>/', views.deletePost, name='deletePost'),
    path('comentar/<int:id>/', views.comentar, name='comentar'),
]