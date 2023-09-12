from django.shortcuts import render, get_object_or_404
from .models import Zapato, CategoriaZapatos

def lista_zapatos(request):
    zapatos = Zapato.objects.all()
    return render(request, 'mi_app/lista_zapatos.html', {'zapatos': zapatos})

def detalle_zapato(request, zapato_id):
    zapato = get_object_or_404(Zapato, pk=zapato_id)
    return render(request, 'mi_app/detalle_zapato.html', {'zapato': zapato})

def categorias(request):
    categorias = CategoriaZapatos.objects.all()
    return render(request, 'mi_app/categorias.html', {'categorias': categorias})

def zapatos_por_categoria(request, categoria_id):
    categoria = get_object_or_404(CategoriaZapatos, pk=categoria_id)
    zapatos = Zapato.objects.filter(categoria=categoria)
    return render(request, 'mi_app/zapatos_por_categoria.html', {'categoria': categoria, 'zapatos': zapatos})

def inicio(request):
    return render(request, 'mi_app/inicio.html')

def ofertas(request):
    return render(request, 'mi_app/ofertas.html')

def contacto(request):
    return render(request, 'mi_app/contacto.html')