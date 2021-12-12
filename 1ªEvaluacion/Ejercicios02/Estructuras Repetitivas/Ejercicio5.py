'''Escribe un programa que diga si un número introducido por teclado es o no primo. Un número 
primo es aquel que sólo es divisible entre él mismo y la unidad. Nota: Es suficiente probar hasta la 
raíz cuadrada del número para ver si es divisible por algún otro número'''

numero = int(input("Introduce un número: "))
correcto = True
if numero < 1:
        correcto = False
elif numero == 2:
        correcto = True
else:
    for i in range(2, numero):
        if numero % i == 0:
            correcto = False    

if correcto:
    print("El número es primo")
else:
    print("El número no es primo")