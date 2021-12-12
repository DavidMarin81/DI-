'''Realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas
entre 0 y 10). A continuación, debe mostrar: todas las notas, la nota media, la nota más alta
que ha sacado y la menor.'''

numNotas = 5
notas = []
notaMedia = 0

#Metodo que pide la nota al usuario. 
#En caso de no introducir un int, se lanza una excepcion
def introducirNota():
    try:
        nota = int(input("Introduce una nota: ")) 
        while comprobarNota(nota) == False:
            nota = int(input("Introduce una nota: "))
        notas.append(nota)
    except ValueError:
        print("Solo se permiten datos numericos")
        introducirNota()

#Metodo que comprueba que la nota introducida este entre el 0 y el 10
def comprobarNota(nota):
    correcto = True
    if nota < 0 or nota > 10:
        correcto = False
        print("La nota no puede ser mayor que 10 ni menor que 0")
    return correcto

#Se usa un bucle for para introducir las 5 notas
for i in range(numNotas):
    introducirNota()

#Se muestran las notas y se aprovecha el bucle for para saber la nota media
print("Las notas son:")
for i in range(5):
    notaMedia += notas[i]
    print(notas[i])
print("La nota media es:", notaMedia / 5)

#Se ordena la lista para saber la nota mas alta y la mas baja
notas.sort()

#Se muestran la nota mas alta y la nota mas baja
print("La nota mas alta es:", notas[4])
print("La nota mas baja es:", notas[0])