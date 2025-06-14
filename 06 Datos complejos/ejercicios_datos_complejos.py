#ejercicio 4, una agenda de 5 contactos
agenda = {}
for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input(f"ingresa el numero de {nombre}: ")
    agenda[nombre] = numero

buscar = input("ingresa el contacto a buscar: ")

if buscar in agenda:
    print(f"el numero de {buscar} es {agenda[buscar]}")
else:
    print(f"no existe {buscar} en agenda")