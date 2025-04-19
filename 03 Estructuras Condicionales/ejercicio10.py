#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S),
#qué mes del año es y qué día es. El programa deberá utilizar esa información
#para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

Hemisferio = input("Ingrese el hemisferio donde se encuentra, N (norte) o S (sur): ");
Mes = int(input("Ingrese el mes en que esta, en numero(1 a 12): "));
dia = int(input("Ingrese el dia, en numero (1 a 30 o 31): "));
if (Mes == 12 or Mes == 1 or Mes == 2 or Mes == 3 and dia >= 21 or dia <= 20 and Hemisferio == "N"):
    print("La estación es Invierno");
else:
    Hemisferio == "S"
    print("La estación es Verano");
if (Mes == 3 or Mes == 4 or Mes == 5 or Mes == 6 and dia >= 21 or dia <= 20 and Hemisferio == "N"):
    print("La estación es Primavera");
else:
    Hemisferio == "S"
    print("La estación es Otoño");
if (Mes == 6 or Mes == 7 or Mes == 8 or Mes == 9 and dia >= 21 or dia <= 20 and Hemisferio == "N"):
    print("La estación es Verano");
else:
    Hemisferio == "S"
    print("La estación es Invierno");
if (Mes == 9 or Mes == 10 or Mes == 11 or Mes == 12 and dia >= 21 or dia <= 20 and Hemisferio == "N"):
    print("La estación es Otoño");
else:
    Hemisferio == "S"
    print("La estación es Primavera")