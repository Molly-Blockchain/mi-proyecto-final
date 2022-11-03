from django.shortcuts import render
from ejemplo.models import Familiar
from ejemplo.forms import Buscar
from ejemplo.forms import FamiliarForm # Nuevo import, clase 21
from ejemplo.forms import PropiedadesForm # import primera entrega TP final
from ejemplo.forms import LibrosForm # import primera entrega TP final
from django.views import View

# Create your views here.

def index(request):
    suma = 1 + 1
    return render(request, "ejemplo/saludar.html", {
        "nombre":"Juan",
        "apellido":"García",
        "resultado": suma
        })

def index_dos(request, nombre, apellido):
    return render(request, "ejemplo/saludar.html",
    {
        "nombre" : nombre,
        "apellido" : apellido,
        
    })

def index_tres(request):
    return render(request, "ejemplo/saludar.html", {"notas" : [1,2,3,4,5,6,7,8]})


def imc(request, peso, altura):
    imc = peso / (altura * altura) 
    return render(request, "ejemplo/imc.html", {"IMC" : imc})


# Modelo "Familiar"

def monstrar_familiares(request):
    lista_familiares = Familiar.objects.all()
    return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})

class BuscarFamiliar(View):

    form_class = Buscar
    template_name = 'ejemplo/buscar.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
            'lista_familiares':lista_familiares})
        return render(request, self.template_name, {"form": form})

class AltaFamiliar(View):

    form_class = FamiliarForm
    template_name = 'ejemplo/alta_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})



# Modelo "Propiedades"

def monstrar_propiedades(request):
    lista_propiedades = Propiedades.objects.all()
    return render(request, "ejemplo/propiedades.html", {"lista_propiedades": lista_propiedades})

class BuscarPropiedades(View):

    form_class = Buscar
    template_name = 'ejemplo/propiedades/buscar_propiedades.html'
    initial = {"direccion":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            direccion = form.cleaned_data.get("direccion")
            lista_propiedades = Propiedades.objects.filter(direccion__icontains = direccion).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
            'lista_propiedades' : lista_propiedades})
        return render(request, self.template_name, {"form": form})

class AltaPropiedades(View):

    form_class = PropiedadesForm
    template_name = 'ejemplo/propiedades/alta_propiedades.html'
    initial = {"direccion":"", "municipio":"", "valor":""} # Reemplazar con los nombres de ejemplo.models (en la clase Propiedades)

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito la propiedad {form.cleaned_data.get('direccion')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})



# Modelo "Libros"

def monstrar_libros(request):
    lista_libros = Libros.objects.all()
    return render(request, "ejemplo/libros.html", {"lista_libros": lista_libros})

class BuscarLibros(View):

    form_class = Buscar
    template_name = 'ejemplo/libros/buscar_libros.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_libros = Libros.objects.filter(nombre__icontains = nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
            'lista_libros' : lista_libros})
        return render(request, self.template_name, {"form": form})

class AltaLibros(View):

    form_class = LibrosForm
    template_name = 'ejemplo/libros/alta_libros.html'
    initial = {"nombre":"", "autor":"", "genero":""} # Reemplazar con los nombres de ejemplo.models (en la clase Libros)

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el libro {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})