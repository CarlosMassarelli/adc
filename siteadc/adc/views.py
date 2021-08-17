from django.shortcuts import render
from adc.models import Info, Perfil


def home(request):
    """Função de visualização para a pagina principal do site"""

    # Inserir aqui todas as partes dinâmicas do site, que acessarão o banco de dados buscando informações.

    nome = Info.objects.count()

    context = {
        'nome': nome,
    }

    # Renderizar o template home com as informações trazidas do banco de dados
    return render(request, 'home.html', context=context)


def sala(request):

    return render(request, 'sala.html')


def perfil(request):

    return render(request, 'perfil.html')


def repositorio(request):

    return render(request, 'repositorio.html')
