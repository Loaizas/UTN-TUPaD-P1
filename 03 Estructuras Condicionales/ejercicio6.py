#escribir un programa que tome la lista numeros_aleatorios,
#calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
#Sesgo positivo o a la derecha: cuando la media
#es mayor que la mediana y, a su vez, la mediana es mayor que la moda.
#Sesgo negativo o a la izquierda: cuando
#la media es menor que la mediana y, a su vez, la mediana es menor que la moda.
#Sin sesgo: cuando la media, la mediana y la moda son iguales.

from statistics import mode, median, mean
import random 
numeros_aleatorios = [random.randint(1, 100) for i in range(50)];
el_modo = mode(numeros_aleatorios);
la_mediana = median(numeros_aleatorios);
la_media = mean(numeros_aleatorios);
if el_modo > la_mediana and la_mediana > el_modo:
    print("Existe sesgo positivo o a la derecha");
elif la_media < la_mediana and la_mediana < el_modo:
    print("Existe sesgo negativo o a la izquierda");
else:
    la_media == la_mediana == el_modo
    print("No existe sesgo");