'''Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir
 la suma y la media de todos los números introducidos.'''

numero = 1
suma = 0
media = 0
contador = 0

while numero != 0:
    numero = int(input("Introduce un número\n(Para salir, pulse 0): "))
    if numero != 0:
        suma += numero
        contador += 1
        media = suma / contador
print("La suma de los números introducidos es", suma)
print("La medida de los números introducidos es", media)