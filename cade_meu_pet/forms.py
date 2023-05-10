from django import forms
from .models import AnimalPerdido, AnimalEncontrado

class AnimalPerdidoForm(forms.ModelForm):
    class Meta:
        model = AnimalPerdido
        fields = ('nome', 'especie', 'raca', 'cor', 'descricao', 'foto', 'data_perdido', 'local_perdido', 'nome_perdeu', 'tel_perdeu')

class AnimalEncontradoForm(forms.ModelForm):
    class Meta:
        model = AnimalEncontrado
        fields = ('nome', 'especie', 'raca', 'cor', 'descricao','foto', 'data_encontrado', 'local_encontrado', 'nome_encontrou', 'tel_encontrou')
