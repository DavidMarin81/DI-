''' Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y
posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su
cubo '''

import random

numeros = []

#Se inicializa la lista con valores aleatorios
for i in range(10):
    numeros.append(random.randint(1, 10))

#Se muestra el cuadrado y el cubo de cada elemento de la lista
for i in range(10):
    print("===========================================")
    print("El cuadrado de", str(numeros[i]), "es", str(numeros[i]*2))
    print("El cubo de", str(numeros[i]), "es", str(pow(numeros[i],3)))