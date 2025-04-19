#Escribir un programa que solicite al usuario que ingrese su nombre y el número 1,
#2 o 3 dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.

Nombre = input("Ingrese su nombre: ");
numero_nombre = int(input("Ingrese un numero segun corresponda: (1-si queres tu nombre en mayuscula, " \
"2-si queres tu nombre en minuscula, 3-si solo queres en mayuscula la primera letra): "))
if numero_nombre == 1:
    print(Nombre.upper());
elif numero_nombre == 2:
    print(Nombre.lower());
elif numero_nombre == 3:
    print(Nombre.title())
