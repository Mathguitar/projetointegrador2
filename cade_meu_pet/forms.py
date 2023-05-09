from django import forms
from .models import AnimalPerdido, AnimalEncontrado

class AnimalPerdidoForm(forms.ModelForm):
    class Meta:
        model = AnimalPerdido
        fields = ('nome', 'especie', 'raca', 'cor', 'descricao', 'data_perdido', 'local_perdido', 'usuario')

class AnimalEncontradoForm(forms.ModelForm):
    class Meta:
        model = AnimalEncontrado
        fields = ('nome', 'especie', 'raca', 'cor', 'descricao', 'data_encontrado', 'local_encontrado', 'usuario')

