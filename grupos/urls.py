from django.contrib import admin
from django.urls import path, include
from .views import home, salvar, editar, atualizar, deletar, home_psicologo

urlpatterns = [
    #Cadastro Policiais
    path('', home),
    path('salvar/',             salvar,     name="salvar"),
    path('editar/<int:id>',     editar,     name="editar"),
    path('atualizar/<int:id>',  atualizar,  name="atualizar"),
    path('deletar/<int:id>',    deletar,    name="deletar"),

    #Cadastro Psicologo
    path('home_psicologo', home_psicologo, name="home_psicologo")
]