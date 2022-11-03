"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Zona de imports

from django.contrib import admin
from django.urls import path
from ejemplo.views import imc
from ejemplo.views import index_tres
from ejemplo.views import index_dos
from ejemplo.views import index
from ejemplo.views import monstrar_familiares # Se usa snake_case porque es una función
from ejemplo.views import BuscarFamiliar # Se usa Camel Case porque es una clase
from ejemplo.views import AltaFamiliar # Agregado en clase 21
from blog.views import index as blog_index

# Modelo Propiedades
from ejemplo.views import monstrar_propiedades # Claro, si no lo importo no funciona jajaja
from ejemplo.views import BuscarPropiedades
from ejemplo.views import AltaPropiedades

# Modelo Libros
from ejemplo.views import monstrar_libros
from ejemplo.views import BuscarLibros
from ejemplo.views import AltaLibros



# Zona de URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', index),
    path('saludar/<nombre>/<apellido>/', index_dos),
    path('mostrar-notas/', index_tres),
    path('imc/<peso>/<altura>/', imc),
    path('mi-familia/', monstrar_familiares),
    path('blog/', blog_index),
    path('mi-familia/buscar', BuscarFamiliar.as_view()),
    path('mi-familia/alta', AltaFamiliar.as_view()),
    
    path('propiedades.html', lista_propiedades),    # Mostrar propiedades (seed_data.py)
    path('propiedades/buscar_propiedades.html', BuscarPropiedades.as_view()),   # Pruebo buscar propiedades dentro de la "categoría" propiedades
    path('propiedades/alta_propiedades.html', AltaPropiedades.as_view()),

    path('libros.html', monstrar_libros),   # Mostrar libros (seed_data.py)
    path('libros/buscar_libros.html', BuscarLibros.as_view()),   # Buscar libros
    path('libros/alta_libros.html', AltaLibros.as_view()),   # Cargar datos de libros
]
