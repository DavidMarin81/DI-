'''Realizar un programa que comprueba si una cadena leída por teclado comienza por una
subcadena introducida por teclado. '''

cadena = input("Introduce una cadena: ")
subcadena = input("Introduce una subcadena: ")

if (cadena.startswith(subcadena)):
    print("La palabra empieza por la subcadena")
else:
    print("La palabra no empieza por la subcadena")