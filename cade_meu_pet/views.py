from django.shortcuts import render, redirect
from .models import AnimalEncontrado, AnimalPerdido
from .forms import AnimalEncontradoForm, AnimalPerdidoForm


def index(request):
    animais_perdidos = AnimalPerdido.objects.all()
    animais_encontrados = AnimalEncontrado.objects.all()
    context = {
        'animais_perdidos': animais_perdidos,
        'animais_encontrados': animais_encontrados
    }
    return render(request, 'index.html', context)

def perdidos(request):
    if request.method == 'POST':
        form = AnimalPerdidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            context = {'form': form}
            return render(request, 'perdidos.html', context)
    else:
        form = AnimalPerdidoForm()
        context = {'form': form}
        return render(request, 'perdidos.html', context)

def encontrados(request):
    if request.method == 'POST':
        form = AnimalEncontradoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            context = {'form': form}
            return render(request, 'encontrados.html', context)
    else:
        form = AnimalEncontradoForm()
        context = {'form': form}
        return render(request, 'encontrados.html', context)

