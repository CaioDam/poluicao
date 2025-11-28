from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import DenunciaForm, LoginForm, UsuarioCadastroForm 
from .models import Denuncia

@login_required(login_url='login')
def enviar_denuncia(request):
    if request.method == 'POST':
        form = DenunciaForm(request.POST, request.FILES)
        if form.is_valid():
            denuncia = form.save(commit=False)
            denuncia.usuario = request.user
            denuncia.save()
            return redirect('sucesso_denuncia')
    else:
        form = DenunciaForm()
        
    return render(request, 'index.html', {'form': form})

def sucesso_denuncia(request):
    return render(request, 'sucesso.html')

def quem_somos(request):
    return render(request, 'quem_somos.html')

def faq(request):
    return render(request, 'faq.html')

def mapa(request):
    return render(request, 'mapa.html')

def denuncias_lista(request):
    denuncias_resolvidas = Denuncia.objects.filter(resolvida=True).order_by('-data_criacao')
    context = {'denuncias': denuncias_resolvidas}
    return render(request, 'denuncias_lista.html', context)

def contato(request):
    return render(request, 'contato.html')

def guia_denuncia(request):
    return render(request, 'guia_denuncia.html')

def estatisticas(request):
    total_denuncias = Denuncia.objects.count()
    denuncias_resolvidas = Denuncia.objects.filter(resolvida=True).count()
    
    context = {
        'total_denuncias': total_denuncias,
        'denuncias_resolvidas': denuncias_resolvidas
    }
    return render(request, 'estatisticas.html', context)

def login_admin(request):
    if request.user.is_authenticated:
        return redirect('enviar_denuncia')
        
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None and user.is_staff:
                login(request, user)
                return redirect('admin_home') 
            elif user is not None:
                login(request, user)
                return redirect('enviar_denuncia')
            else:
                messages.error(request, 'Credenciais inválidas ou usuário não autorizado.')
    else:
        form = LoginForm()
        
    return render(request, 'login_admin.html', {'form': form})

def logout_admin(request):
    logout(request)
    messages.info(request, "Você foi desconectado.")
    return redirect('login')

def cadastro(request):
    if request.method == 'POST':
        form = UsuarioCadastroForm(request.POST) 
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Conta criada com sucesso! Faça login para continuar.')
            return redirect('login')
    else:
        form = UsuarioCadastroForm()
        
    return render(request, 'cadastro.html', {'form': form})

@login_required(login_url='login')
def admin_home(request):
    if not request.user.is_staff:
        return redirect('enviar_denuncia') 

    total_denuncias = Denuncia.objects.count()
    denuncias_pendentes = Denuncia.objects.filter(resolvida=False).count()

    context = {
        'total_denuncias': total_denuncias,
        'denuncias_pendentes': denuncias_pendentes,
    }
    
    return render(request, 'admin_home.html', context)

@login_required(login_url='login') 
def relatorios(request):
    if not request.user.is_staff:
        return redirect('login')
    
    return render(request, 'relatorios.html')

def handler404(request, exception):
    return render(request, 'not_found.html', {}, status=404)