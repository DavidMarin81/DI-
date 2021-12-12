'''Realizar un programa que compruebe si una cadena contiene una subcadena. Las dos cadenas
se introducen por teclado'''

cadena = input("Introduce una cadena: ")
subcadena = input("Introduce una subcadena: ")

if (subcadena in cadena):
    print("La palabra contiene la subcadena")
else:
    print("La palabra no contiene la subcadena")