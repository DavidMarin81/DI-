
'''Crea un programa que pida dos números enteros al usuario y diga si alguno de ellos es
múltiplo del otro. Crea una función EsMultiplo que reciba los dos números, y devuelve si el
primero es múltiplo del segundo'''

#Método que comprueba que el dato introducido sea un número
#En caso de no serlo, se volverá a pedir el dato hasta que éste sea un valor numérico
def comprobarNumero(numero):
    correcto = False
    while correcto == False:
        if numero.isdigit():
            correcto = True
        else:
            print("ERROR -> Solo se permiten números enteros")
            numero = input("Introduce un numero: ")

#Método que pide dos datos por parámetros y comprueba si el primero es múltiplo del segundo
def esMultiplo(num1, num2):
    if num1 % num2 == 0:
        print("El número", num1, "es múltiplo de", num2)
    else:
        print("El número", num1, "no es múltiplo de", num2)

#Se pide al usuario dos números y se comprueba que sea un dato numérico
numero1 = input("Introduce un numero: ")
comprobarNumero(numero1)
numero2 = input("introduce otro número: ")
comprobarNumero(numero2)

#Se comprueba si el primer dato es múltiplo del segundo
esMultiplo(int(numero1), int(numero2))