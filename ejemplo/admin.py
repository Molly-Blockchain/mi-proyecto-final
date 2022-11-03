# Zona de imports

from django.contrib import admin
from ejemplo.models import Familiar
from ejemplo.models import Propiedades # Si no lo importo no funciona
from ejemplo.models import Libros



# Register your models here.

admin.site.register(Familiar)
admin.site.register(Propiedades)    # Para poder modificar datos desde el admin de Django en caso de ser necesario
admin.site.register(Libros)