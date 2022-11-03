# Zona de imports

from ejemplo.models import Familiar
from ejemplo.models import Propiedades
from ejemplo.models import Libros


# Zona de datos

# Datos de Familiar
Familiar(nombre="Rosario", direccion="Rio Parana 745", numero_pasaporte=123123).save()
Familiar(nombre="Alberto", direccion="Rio Parana 745", numero_pasaporte=890890).save()
Familiar(nombre="Samuel", direccion="Rio Parana 745", numero_pasaporte=345345).save()
Familiar(nombre="Florencia", direccion="Rio Parana 745", numero_pasaporte=567567).save()   # Datos creados en clase

Familiar(nombre="Carlos", direccion="Lanus 2170", numero_pasaporte=318624).save()   # Datos creados a mano
Familiar(nombre="Marta", direccion="Rio piedras 1760", numero_pasaporte=347892).save()
Familiar(nombre="Omar", direccion="Ecuador 890", numero_pasaporte=784532).save()

print("Se cargo con éxito los usuarios de pruebas")



# Datos de Propiedades
Propiedades(direccion = "Rio piedras 480", municipio = "Quilmes", USD = "USD $:", valor = f"{USD}87000").save()
Propiedades(direccion = "Marcos Peña 790", municipio = "Berazategui", USD = "USD $:", valor = f"{USD}120000").save()
Propiedades(direccion = "Anunciación 240", municipio = "Merlo", USD = "USD $:", valor = f"{USD}68000").save()
Propiedades(direccion = "San Martín 1260", municipio = "Moreno", USD = "USD $:", valor = f"{USD}135000").save()
Propiedades(direccion = "Juan José Paso 890", municipio = "Ciudad Evita", USD = "USD $:", valor = f"{USD}76000").save()

print("Se cargaron con éxito las propiedades de pruebas")



# Datos de Libros
Libros(nombre = "El Club de las 5AM", autor = "Robin Sharma", genero = "Desarrollo personal").save()    # Podemos estar horas hablando de libros jajaja
Libros(nombre = "El monje que vendió su ferrari", autor = "Robin Sharma", genero = "Desarrollo personal").save()
Libros(nombre = "Descubre tu destino con el monje que vendió su ferrari", autor = "Robin Sharma", genero = "Desarrollo personal").save()
Libros(nombre = "Piense y hágase rico", autor = "Napoleon Hill", genero = "Desarrollo personal").save()
Libros(nombre = "La inteligencia emocional", autor = "Daniel Goleman", genero = "Desarrollo personal").save()

