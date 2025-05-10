#ejercicio1
lista_multiplos_4 = list(range(4, 101, 4))
print(lista_multiplos_4)

#ejercicio2

lista_5_elementos = ["michi", "compu", "celular", "mate", "manzanas"]
penultimo_elemento = lista_5_elementos[3]
print(penultimo_elemento)

#ejercicio3
lista_vacia = []
lista_vacia.append("alfajores")
lista_vacia.append("mate")
lista_vacia.append("ya tengo mi merienda")
print(lista_vacia)

#ejercicio4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[3] = "oso"
print(animales)

#ejercicio5
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)
#elimina solo el numero mayor del listado de numeros ingresados.

#ejercicio6
listado_5_en_5 = list(range(10, 31, 5))
print(listado_5_en_5[0:2])

#ejercicio7
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "bicicleta"
autos[2] = "monopatin electrico"
print(autos)

#ejercicio8
lista_dobles = []
lista_dobles.append(5*2)
lista_dobles.append(10*2)
lista_dobles.append(15*2)
print(lista_dobles)

#ejercicio9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]
compras.append("jugo")
compras[1][1] = "tallarines"
for sublista in compras:
    if "pan" in sublista:
        sublista.remove("pan")            
        break
print(compras)

#ejercicio10
lista_anidada = [[15], True, [25.5, 57.9, 30.6], [False]]
print(lista_anidada)