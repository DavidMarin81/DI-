'''Diseñar el algoritmo correspondiente a un programa, que:
- Crea una tabla (lista con dos dimensiones) de 5x5 enteros.
- Carga la tabla con valores numéricos enteros.
- Suma todos los elementos de cada fila y todos los elementos de cada columna 
visualizando los resultados en pantalla'''

import random

filas = 5
contador = 0
tabla = []
#Se crea una tabla bidimensional de 5x5 con numeros aleatorios
for i in range(filas):
    tabla.append([random.randint(1, 9), random.randint(1, 9), random.randint(1, 9), 
            random.randint(1, 9), random.randint(1, 9)])

#Se imprime la tabla
for i in range(filas):
    print(tabla[i])

#Se suman las filas
for i in range(filas):
    for j in range(filas):
        contador += tabla[i][j]
    print("La suma de la fila", i + 1, "es", contador)
    contador = 0

#Se suman las columnas
for i in range(filas):
    for j in range(filas):
        contador += tabla[j][i]
    print("La suma de la columna", i + 1, "es", contador)
    contador = 0
