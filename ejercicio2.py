def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
# Pedimos al usuario la posición hasta donde quiere la serie
posicion = int(input("Ingresá la posición hasta donde querés ver la serie de Fibonacci: "))

# Mostramos la serie completa
print(f"Serie de Fibonacci hasta la posición {posicion}:")
for i in range(posicion + 1):
    print(f"F({i}) = {fibonacci(i)}")