from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

TIPO_POLUICAO_CHOICES = [
    ('AR', 'Poluição do Ar'),
    ('AGUA', 'Poluição da Água'),
    ('SOLO', 'Poluição do Solo'),
    ('SONORA', 'Poluição Sonora'),
    ('VISUAL', 'Poluição Visual'),
    ('OUTRO', 'Outro Tipo'),
]

class UsuarioCadastroForm(UserCreationForm):
    email = forms.EmailField(
        required=True, 
        label="E-mail",
        widget=forms.EmailInput(attrs={'placeholder': 'seu.email@exemplo.com'})
    )
    
    first_name = forms.CharField(
        required=True,
        label="Primeiro Nome",
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Seu primeiro nome'})
    )
    
    last_name = forms.CharField(
        required=True,
        label="Sobrenome",
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Seu sobrenome'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Escolha um nome de usuário'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(
        label="Usuário", 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'input-minimal', 'placeholder': 'Nome de usuário'})
    )
    password = forms.CharField(
        label="Senha", 
        widget=forms.PasswordInput(attrs={'class': 'input-minimal', 'placeholder': 'Senha'})
    )

class DenunciaForm(forms.Form): 
    tipo = forms.ChoiceField(
        label="Tipo de Poluição", 
        choices=TIPO_POLUICAO_CHOICES,
        widget=forms.Select(attrs={'class': 'input-minimal'})
    )
    descricao = forms.CharField(
        label="Descreva a Denúncia", 
        widget=forms.Textarea(attrs={'class': 'input-minimal', 'rows': 4, 'placeholder': 'Detalhes sobre a poluição, localização, etc.'})
    )
    imagem = forms.FileField(
        label="Anexar Imagem (Opcional)", 
        required=False
    )