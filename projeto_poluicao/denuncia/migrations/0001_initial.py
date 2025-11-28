from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Denuncia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('AR', 'Poluição do Ar'), ('AGUA', 'Poluição da Água'), ('SOLO', 'Poluição do Solo'), ('SONORA', 'Poluição Sonora'), ('VISUAL', 'Poluição Visual'), ('OUTRO', 'Outro Tipo')], max_length=10, verbose_name='Tipo de Poluição')),
                ('descricao', models.TextField(verbose_name='Descreva a Denúncia')),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='denuncias_imgs/', verbose_name='Anexar Imagem (Opcional)')),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('resolvida', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Denúncia de Poluição',
                'verbose_name_plural': 'Denúncias de Poluição',
            },
        ),
    ]
