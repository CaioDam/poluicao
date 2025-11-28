from django.contrib import admin
from .models import Denuncia

@admin.register(Denuncia)
class DenunciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo', 'data_criacao', 'resolvida') 
    list_filter = ('tipo', 'resolvida', 'data_criacao')
    search_fields = ('descricao', 'id') 
    fields = ('tipo', 'descricao', 'imagem', 'resolvida')