'''Vamos a declarar un diccionario para guardar los precios de las distintas frutas. El programa
pedirá el nombre de la fruta y la cantidad que se ha vendido y nos mostrará el precio final de la
fruta a partir de los datos guardados en el diccionario. Si la fruta no existe nos dará un error.
Tras cada consulta el programa nos preguntará si queremos hacer otra consulta.'''
#Se incluyen las frutas y sus precios en un diccionario
preciosFrutas = {"naranja": 1.20, 
                "platano": 1.10, 
                "fresa": 1.40, 
                "melocoton": 0.85,
                "melon": 1.45,
                "sandia": 1.80,
                "manzana": 2.45,
                "kiwi": 3.45,
                "uva": 2.35,
                 }

#Mientras comprueba sea verdadero, se pedirá la fruta y su precio
comprueba = True
while comprueba:
    fruta = input("Introduce la fruta: ")
    if fruta.lower() not in preciosFrutas:
        print("La fruta introducida no esta registrada")
    else:
        cantidad = int(input("Frutas vendidas: "))
        precio = preciosFrutas[fruta] * cantidad
        #Se redondea el precio para que tenga 2 decimales como máximo
        print("Precio:", round(precio, 2)) 
    operacion = input("Si quiere comprobar otro precio, pulse una tecla\nPara salir, pulse (n)")
    if operacion.lower() == "n":
        comprueba = False
        print("Gracias por usar nuestro programa")




