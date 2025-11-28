from django.db import models

class Denuncia(models.Model):
    TIPOS_POLUICAO = [
        ('AR', 'Poluição do Ar'),
        ('AGUA', 'Poluição da Água'),
        ('SOLO', 'Poluição do Solo'),
        ('SONORA', 'Poluição Sonora'),
        ('VISUAL', 'Poluição Visual'),
        ('OUTRO', 'Outro Tipo')
    ]
    
    tipo = models.CharField(max_length=10, choices=TIPOS_POLUICAO, verbose_name='Tipo de Poluição')
    descricao = models.TextField(verbose_name='Descreva a Denúncia')
    imagem = models.ImageField(upload_to='denuncias_imgs/', null=True, blank=True, verbose_name='Anexar Imagem (Opcional)')
    data_criacao = models.DateTimeField(auto_now_add=True)
    resolvida = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "Denúncia de Poluição"
        verbose_name_plural = "Denúncias de Poluição"
        
    def __str__(self):
        return f"Denúncia ({self.id}) - {self.get_tipo_display()}"