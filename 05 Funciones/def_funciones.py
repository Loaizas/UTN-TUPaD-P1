#ejercicio1
def imprimir_hola_mundo():
    return "Hola Mundo"

print( imprimir_hola_mundo() )

#ejercicio2
saludar_nombre = input("Ingresa tu nombre: ")
print(f"Hola {saludar_nombre}!")


#ejercicio3
def informacion_personal(nombre, apellido, edad, residencia):
    return print(f"Soy {nombre} {apellido}, tengo {edad} años y resido en {residencia}")

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("¿cuantos años tenes?: ")
residencia = input("¿Cual es tu lugar de residencia?:")

informacion_personal(nombre, apellido, edad, residencia)

#ejercicio4
from math import pi
def calcular_area_circulo(radio):
    return pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * pi * radio

radio = float(input("Ingrese el radio del circulo: "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"el area del circulo es: {area}")
print(f"el perimetro del circulo es: {perimetro}")


#ejercicio5
def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingrese los segundos: "))
horas = segundos_a_horas(segundos)
print(f"Los segundos ingresados equivalen a {horas} horas")


#ejercicio6
def tabla_de_multiplicar(numero):
   for i in range(1, 11):
       resultado = numero * i
       print(f"{numero} x {i} = {resultado}")

num = int(input("Ingrese un numero para ver su tabla de multiplicar: "))
tabla_de_multiplicar(num)

#ejercicio7
def operaciones_basicas(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2 if num2 !=0 else "no se puede dividir por 0"
    return(suma, resta, multiplicacion, division)

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

resultados = operaciones_basicas(num1, num2)

print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicacion: {resultados[2]}")
print(f"division: {resultados[3]}")


#ejercicio8
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = calcular_imc(peso, altura)
print(f"Su IMC es: {imc:.2f}")

