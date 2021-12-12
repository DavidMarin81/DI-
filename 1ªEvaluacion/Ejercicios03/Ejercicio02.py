'''Pide una cadena y un carácter por teclado (valida que sea un carácter) y muestra cuantas veces
aparece el carácter en la cadena.'''

def comprobarCaracter(caracter):
    estado = True
    if (len(caracter) > 1):
        estado = False
    return estado

def comprobarCoincidencias():
    contador = 0
    for i in range(len(cadena)):
        if (cadena[i] == caracter):
            contador += 1
    if(contador == 1):
        print("El caracter '" + caracter + "' aparece 1 vez")
    elif(contador > 1):
        print("El caracter '" + caracter + "' aparece", contador, "veces")
    else:
        print("El caracter '" + caracter + "' no aparece en la cadena")

cadena = input("Introduce una cadena: ")
caracter = input("Introduce un caracter: ")
while (comprobarCaracter(caracter) == False):
    print("Debe introducir un solo caracter")
    caracter = input("Introduce un caracter: ")

comprobarCoincidencias()





