#Escribir un programa que solicite una frase o palabra al usuario.
#Si el string ingresado termina con vocal, añadir un signo de exclamación al final
#e imprimir el string resultante por pantalla; en caso contrario,
#dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

frase_palabra = input("Ingrese una frase o palabra: ");
if frase_palabra[-1] in "aeiou" or "AEIOU":
    print(f"{frase_palabra}!")
else:
    print(f"{frase_palabra}")