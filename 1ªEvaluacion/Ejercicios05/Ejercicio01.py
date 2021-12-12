'''Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de
apariciones de cada carácter en la cadena.'''

diccionario = {}
cadena = input("Escribe una cadena:")
#Se recorre la cadena caracter a caracter
for i in cadena:
	#Si el caracter ya apareció:
    if i in diccionario:
		#Se incrementa el valor
        diccionario[i] += 1
    else:
		#Si aun no apareció, se incrementa en 1
        diccionario[i] = 1	

#Se usa items() para devolver la clave y el valor de cada elemento del diccionario
for clave,valor in diccionario.items():
	print ("Veces que aparece", clave, "=",valor)
