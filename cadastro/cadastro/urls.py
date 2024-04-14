from django.urls import path
from sitecadastro import views

urlpatterns = [
    path('', views.index, name='index'),  
    path('criar_cadastro.html/', views.criar_cadastro, name='criar_cadastro'),  
    path('atualizar/<int:usuario_id>/', views.atualizar_cadastro, name='atualizar_cadastro'),
    path('deletar/<int:usuario_id>/', views.deletar_cadastro, name='deletar_cadastro'),
    path('pesquisar_cadastro.html/', views.pesquisar_cadastros, name='pesquisar_cadastros'),
]