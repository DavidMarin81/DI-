'''Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve el
valor máximo y el mínimo. Crea un programa que pida números por teclado y muestre el
máximo y el mínimo, utilizando la función anterior'''

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

#Método que ordena una lista y muestra el valor máximo y el mínimo
def calcularMaxMin(lista):
    lista.sort()
    print("El valor máximo es", lista[len(lista) - 1])
    print("El valor mínimo es", lista[0])

#Se crea una lista y un boolean iniciándolo a False
lista = []
salir = False

#Se pide un número y se introduce en una lista. Se da la opción de seguir introduciendo números
while salir == False:
    numero = input("Introduce un número: ")
    comprobarNumero(numero)
    lista.append(int(numero))
    opcion = input("¿Quieres introducir otro número?\nSI -> pulse una tecla\nNO -> pulse 'n'\n")
    if opcion == 'n':
        salir = True

#Al decidir no introducir más números, se muestra el valor máximo y el mínimo
calcularMaxMin(lista)
