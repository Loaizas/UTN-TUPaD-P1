#ejercicio 5
frase = input("ingresa una frase: ")

#separar la frase en palabras
palabras = frase.split()

#obtener palabras unicas usando un set
palabras_unicas = set(palabras)

contar_palabras = {}
for palabra in palabras:
    if palabra in contar_palabras:
        contar_palabras[palabras] += 1
    else:
        contar_palabras[palabra] = 1

print(palabras_unicas)
print(contar_palabras)