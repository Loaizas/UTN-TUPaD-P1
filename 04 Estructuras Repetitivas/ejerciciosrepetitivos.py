#ejercicio1 numeros del 0 al 100
for i in range(101):
    print(i)

#ejercicio2 Desarrolla un programa que solicite al usuario un 
# número entero y determine la cantidad de dígitos que contiene
numero = int(input("Ingrese un numero entero: "))
cantidad_digitos = len(str(numero))
if numero < 0:
    print("Ingrese un numero positivo")
else:
    print(f"la cantidad de digitos del numero ingresado es {cantidad_digitos}")


#ejercicio3 Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))

suma = 0

for i in range (num1 +1, num2):
    suma += i
print(f"el resultado de sumar los numeros entre {num1} y {num2} es {suma}")



#ejercicio4 Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0

sumatoria = 0
numero = int(input("Ingresa un numero (0 para terminar): "))
while numero != 0:
    sumatoria += numero
    numero = int(input("Ingresa otro numero (0 para terminar): "))

print("La suma total es:", sumatoria)


#ejercicio5 programa de adivinanza

import random

numero_secreto = random.randint(0, 9)
intentos = 0
adivinanza = -1

print("Encontra el numero secreto, entre 0 y 9!")
while adivinanza != numero_secreto:
    adivinanza = int(input("Ingresa tu numero: "))
    intentos += 1

    if adivinanza < numero_secreto:
        print("El numero secreto es mas grande")
    elif adivinanza > numero_secreto:
        print("El numero secreto es menor")
print(f"Muy bien, encontraste el numero en {intentos} intentos")



#ejercicio6 numeros decrececientes pares

for i in range(101, 0, -1):
    if i%2 == 0:
     print(i)



#ejercicio7 Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.
numero_positivo = int(input("Ingrese un numero entero positivo: "))
suma = 0
if numero_positivo < 0:
    print("El numero debia ser positivo")
else:
    for i in range(0, numero_positivo+1):
        suma += i
    print("La suma total es:", suma)


#ejercicio8 calculo de los 100 numeros

cantidad_numeros = 10

pares = 0
impares = 0
positivos = 0
negativos = 0

print(f"Escriba los {cantidad_numeros} numeros enteros a analizar: ")
for _ in range(cantidad_numeros):
    numero = int(input("numero: "))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero > 0:
        positivos += 1
    else:
        negativos += 1

print("La cantidad de numeros pares son:", pares)
print("La cantidad de numeros impares son: ", impares)
print("Los cantidad de numeros positivos son: ", positivos)
print("La cantidad de numeros negativos son: ", negativos)


#ejercicio9 calculando la media de los valores ingresados

valores_ingresados = 10
suma_total = 0

print(f"ingrese los {valores_ingresados} de numeros enteros: ")

for i in range(valores_ingresados):
    numero = int(input("ingrese el valor: "))
    suma_total += numero

media = suma_total / valores_ingresados
print("La media de los valores ingresados es:", media)


#ejercicio10 cambiando el orden de los numeros ingresados

tu_numero = int(input("Ingresa tu numero: "))
numero_invertido = str(tu_numero)[::-1]

print(f"Tu número invertido es: {numero_invertido}")