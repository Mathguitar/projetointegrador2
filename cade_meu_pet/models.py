from django.db import models
# Create your models here.

class User(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    
class AnimalPerdido(models.Model):
    nome = models.CharField(max_length=100)
    especie = models.CharField(max_length=100)
    raca = models.CharField(max_length=100)
    cor = models.CharField(max_length=100)
    descricao = models.TextField()
    foto = models.ImageField(upload_to='animais')
    data_perdido = models.DateField()
    local_perdido = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

class AnimalEncontrado(models.Model):
    nome = models.CharField(max_length=100)
    especie = models.CharField(max_length=100)
    raca = models.CharField(max_length=100)
    cor = models.CharField(max_length=100)
    descricao = models.TextField()
    foto = models.ImageField(upload_to='animais')
    data_encontrado = models.DateField()
    local_encontrado = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
