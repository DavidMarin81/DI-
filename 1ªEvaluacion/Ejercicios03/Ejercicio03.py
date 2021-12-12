'''Suponiendo que hemos introducido una cadena por teclado que representa una frase
(palabras separadas por espacios), realiza un programa que cuente cuantas palabras tiene.'''

def comprobarEspacios():
    espacio = False
    for i in range(len(cadena)):
        if(cadena[i] == " "):
            espacio = True
    return espacio
    
cadena = input("Introduce una cadena: ")
while (comprobarEspacios() == False):
    print("Debe introducir más de una palabra")
    cadena = input("Introduce una cadena: ")
palabras = cadena.split()
print("La frase tiene", len(palabras), "palabras")
