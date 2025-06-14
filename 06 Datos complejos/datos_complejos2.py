#ejercicio 6, notas y promedios de 3 alumnos
nota_alumnos= {}

for i in range(3):
    nombre = input("Ingresa el nombre del alumno: ")
    
    print(f"ingresa las 3 notas de {nombre}")
    nota1 = float(input("Ingresa la nota 1: "))
    nota2 = float(input("ingresa la nota 2: "))
    nota3 = float(input("ingresa la nota 3: "))

#guardar las notas como tuplas en el diccionario
    nota_alumnos[nombre] = (nota1, nota2, nota3)

print("\n--- Promedio de los alumnos ---")

for nombre, notas in nota_alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"el promedio de {nombre} es {promedio:.2f}")