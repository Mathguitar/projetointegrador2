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
        form = AnimalPerdidoForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                animal_perdido = form.save(commit=False)
                # Verifica se o campo "foto" foi preenchido
                if 'foto' in request.FILES:
                    animal_perdido.foto = request.FILES['foto']
                animal_perdido.save()
                return redirect('envio_sucesso')
            except Exception as e:
                print(form.errors)  # Imprime os erros do formulário para depuração
                return redirect('form_error')  # Redireciona para a página de erro
        else:
            print(form.errors)  # Imprime os erros do formulário para depuração
            return redirect('form_error')  # Redireciona para a página de erro
    else:
        form = AnimalPerdidoForm()
    context = {'form': form}
    return render(request, 'perdidos.html', context)

def encontrados(request):
    if request.method == 'POST':
        form = AnimalEncontradoForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                animal_encontrado = form.save(commit=False)
                # Verifica se o campo "foto" foi preenchido
                if 'foto' in request.FILES:
                    animal_encontrado.foto = request.FILES['foto']
                animal_encontrado.save()
                return redirect('envio_sucesso')
            except Exception as e:
                print(form.errors)  # Imprime os erros do formulário para depuração
                return redirect('form_error')  # Redireciona para a página de erro
        else:
            print(form.errors)  # Imprime os erros do formulário para depuração
            return redirect('form_error')  # Redireciona para a página de erro
    else:
        form = AnimalEncontradoForm()
    context = {'form': form}
    return render(request, 'encontrados.html', context)

def envio_sucesso(request):
    return render(request, 'envio_sucesso.html')

def form_error(request):
    return render(request, 'form_error.html')
