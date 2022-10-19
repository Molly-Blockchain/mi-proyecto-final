from ejemplo.models import Familiar

Familiar(nombre="Rosario", direccion="Rio Parana 745", numero_pasaporte=123123).save()
Familiar(nombre="Alberto", direccion="Rio Parana 745", numero_pasaporte=890890).save()
Familiar(nombre="Samuel", direccion="Rio Parana 745", numero_pasaporte=345345).save()
Familiar(nombre="Florencia", direccion="Rio Parana 745", numero_pasaporte=567567).save()

Familiar(nombre="Carlos", direccion="Lanus 2170", numero_pasaporte=318624).save()
Familiar(nombre="Marta", direccion="Rio piedras 1760", numero_pasaporte=347892).save()
Familiar(nombre="Omar", direccion="Ecuador 890", numero_pasaporte=784532).save()

print("Se cargo con éxito los usuarios de pruebas")

