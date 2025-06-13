def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + suma_digitos(n // 10)
    
numero = input("Ingresa un numero: ")
print(f"{suma_digitos(numero)}")