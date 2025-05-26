from django.shortcuts import render, redirect
from .forms import AutorForm, TipoComidaForm, RecetaForm, BuscarRecetaForm
from .models import Receta

def home(request):
    return render(request, 'blog/home.html')

def crear_autor(request):
    form = AutorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Nuevo Autor de Receta'})

def crear_tipo(request):
    form = TipoComidaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Nuevo Tipo de Comida'})

def crear_receta(request):
    form = RecetaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Nueva Receta'})

def buscar_receta(request):
    resultados = []
    form = BuscarRecetaForm(request.GET or None)
    if form.is_valid():
        consulta = form.cleaned_data['consulta']
        resultados = Receta.objects.filter(titulo__icontains=consulta)
    return render(request, 'blog/buscar.html', {
        'form': form,
        'resultados': resultados,
        'titulo': 'Buscar Recetas'})

def listar_recetas(request):
    posts = Receta.objects.all()
    return render(request, 'blog/listar_recetas.html', {
        'posts': posts,
        'titulo': 'Listado de Recetas'})