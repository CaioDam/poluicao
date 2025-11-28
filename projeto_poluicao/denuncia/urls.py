from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_admin, name='login'),
    
    path('denunciar/', views.enviar_denuncia, name='enviar_denuncia'),
    
    path('sucesso/', views.sucesso_denuncia, name='sucesso_denuncia'),
    path('quem-somos/', views.quem_somos, name='quem_somos'),
    path('faq/', views.faq, name='faq'),
    path('mapa/', views.mapa, name='mapa'),
    path('denuncias/', views.denuncias_lista, name='denuncias_lista'),
    path('contato/', views.contato, name='contato'),
    path('guia-de-denuncia/', views.guia_denuncia, name='guia_denuncia'),
    path('estatisticas/', views.estatisticas, name='estatisticas'),
    
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_admin, name='login_admin'),
    path('logout/', views.logout_admin, name='logout'),
    
    path('painel/', views.admin_home, name='admin_home'),
    path('painel/relatorios/', views.relatorios, name='relatorios'),
]