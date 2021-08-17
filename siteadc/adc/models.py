from django.contrib.auth.forms import UserCreationForm
from django.db import models


class Perfil(models.Model):
    """Modelo para o perfil"""
    # Nome de preferência, como deseja ser chamado
    nome_social = models.CharField(max_length=200, help_text='Nome de Preferência')

    # Faculdade ou concursos
    faculdade = models.CharField(max_length=150, blank=True, help_text='Faculdade / Concursos')

    # Objetivo
    objetivo = models.TextField(max_length=500, blank=True, help_text='Objetivos')

    def __str__(self):
        """String representando o campo"""
        return self.nome_social


class Info(models.Model):
    """Modelo para campos dos usuários"""
    # Nome completo
    nome_completo = models.CharField(max_length=200, help_text='Nome Completo')

    # Email
    email = models.EmailField(max_length=150, help_text='Email')

    # Cpf
    cpf = models.CharField(max_length=11, help_text='CPF (somente números)')

    # Telefone
    telefone = models.CharField(max_length=30, help_text='Numero de telefone')

    # CEP
    cep = models.CharField(max_length=8, help_text='CEP (somente números)')

    # Referência
    referencia = models.CharField(max_length=50, blank=True, help_text='Referência')

    # Endereço
    endereco = models.CharField(max_length=50, help_text='Endereço')

    # Numero Casa
    numero_casa = models.CharField(max_length=10, help_text='Numero da casa')

    # Complemento
    complemento = models.CharField(max_length=50, blank=True, help_text='Complemento')

    # Bairro
    bairro = models.CharField(max_length=30, help_text='Bairro')

    # Cidade
    cidade = models.CharField(max_length=30, help_text='Cidade')

    # Estado
    estado = models.CharField(max_length=30, help_text='Estado')

    # País
    pais = models.CharField(max_length=30, help_text='Referência')

    # Chave um para um, relacionada ao Perfil
    perfil = models.OneToOneField(Perfil, help_text='Perfil Vinculado', on_delete=models.CASCADE)

    def __str__(self):
        """String representando o campo"""
        return self.nome_completo



