#Algoritmo que pida un número y diga si es positivo, negativo o 0

numero = int(input("Introduce un número: "))

if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es cero")