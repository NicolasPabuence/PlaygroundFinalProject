from django import forms
from .models import CategoriaZapatos, Zapato, ComentarioZapato

class CategoriaZapatosForm(forms.ModelForm):
    class Meta:
        model = CategoriaZapatos
        fields = ['nombre']

class ZapatoForm(forms.ModelForm):
    class Meta:
        model = Zapato
        fields = ['nombre', 'descripcion', 'precio', 'categoria', 'imagen']

class ComentarioZapatoForm(forms.ModelForm):
    class Meta:
        model = ComentarioZapato
        fields = ['contenido']
      