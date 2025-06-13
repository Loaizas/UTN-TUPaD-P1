def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
# Pedimos al usuario un número
limite = int(input("Ingresá un número entero positivo: "))

# Mostramos los factoriales del 1 al número ingresado
print(f"Factoriales del 1 al {limite}:")
for i in range(1, limite + 1):
    print(f"{i}! = {factorial(i)}")