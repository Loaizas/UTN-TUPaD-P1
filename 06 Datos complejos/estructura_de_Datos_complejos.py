#ejercicio1 añadiendo nuevos valores
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melon': 3000, 'Uva':
1450}

precios_frutas ["Naranja"] = 1200
precios_frutas ["Manzana"] = 1500
precios_frutas ["Pera"] = 2300

print(f"el precio de las frutas es {precios_frutas}")

#ejercicio2 cambiar el precio de banana, manzana y melon
precios_frutas ["Manzana"] = 1700
precios_frutas ["Banana"] = 1330
precios_frutas ["Melon"] = 2800
print(f"Se actualizo el precio de las frutas, ahora quedo {precios_frutas}")


#ejercicio 3 creando una lista  keys
print(precios_frutas.keys())