def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)
    
    # Pedimos datos al usuario
base = int(input("Ingresá la base: "))
exponente = int(input("Ingresá el exponente: "))

# Calculamos la potencia
resultado = potencia(base, exponente)

# Mostramos el resultado
print(f"{base}^{exponente} = {resultado}")