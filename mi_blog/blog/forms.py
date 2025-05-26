from django import forms
from .models import Autor, TipoComida, Receta

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

class TipoComidaForm(forms.ModelForm):
    class Meta:
        model = TipoComida
        fields = '__all__'

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = '__all__'

class BuscarRecetaForm(forms.Form):
    consulta = forms.CharField(label='Buscar por título', max_length=100)
