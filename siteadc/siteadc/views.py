from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.decorators.http import require_POST


@require_POST
def cadastro(request):

    nome = request.POST['nome']
    cpf = request.POST['cpf']
    email = request.POST['email']
    senha = request.POST['senha']
    confirmar_senha = request.POST['confirmar_senha']

    novo_usuario = User.objects.create_user(username=nome, email=email, password=senha)
    novo_usuario.save()

    return render(request, 'cadastro.html')
