from django.shortcuts import render
from .models import Livro

def home(request):
    return render(request,'livros/home.html')

def livros(request):
    # Salvar dados da tela para o banco de dados
    novo_livro = Livro()
    novo_livro.nome = request.POST.get('st_nome')
    novo_livro.idade = request.POST.get('nu_idade')
    novo_livro.save()
    # Exibir todos os livros cadastrados em nova página
    livros = {
        'livros': Livro.objects.all()
    }
    # Retornar dados para página com os livros
    return render(request, 'livros/livros.html', livros)