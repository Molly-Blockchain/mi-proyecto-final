# Zona de imports

# Debemos importar los modelos que creamos
from django import forms
from ejemplo.models import Familiar
from ejemplo.models import Propiedades
from ejemplo.models import Libros

# Zona de clases

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100)

class FamiliarForm(forms.ModelForm):
    class Meta:
        model = Familiar
        fields = ['nombre', 'direccion', 'numero_pasaporte']

class PropiedadesForm(forms.ModelForm):
    class Meta:
        model = Propiedades
        fields = ['direccion', 'municipio', 'valor']

class LibrosForm(forms.ModelForm):
    class Meta:
        model = Libros
        fields = ['nombre', 'autor', 'genero']

