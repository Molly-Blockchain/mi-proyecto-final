# Zona de imports

from django import forms


# Zona de clases

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100)