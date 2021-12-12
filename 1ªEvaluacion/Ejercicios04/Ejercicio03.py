'''Queremos guardar los nombres y las edades de los alumnos de un curso. Realiza un programa
que introduzca el nombre y la edad de cada alumno. El proceso de lectura de datos terminará
cuando se introduzca como nombre un asterisco (*) Al finalizar se mostrará los siguientes
datos:
- Todos los alumnos mayores de edad.
- Los alumnos mayores (los que tienen más edad)'''

#Se declaran dos listas, una con nombres y otra con edades de los alumnos
nombres = []
edades = []

#Metodo que comprueba que solo se introduzcan letras
#Si se introduce un * se finaliza el programa
def comprobarNombre(nombre):
    correcto = False
    if nombre == "*":
        correcto = True
    elif nombre.isalpha():
        correcto = True
    else:
        print("Un nombre solo puede contener letras")
    return correcto

#Metodo que comprueba que la edad sea de 1 a 120 años
def comprobarEdad(edad):
    correcto = True
    if edad < 1 or edad > 120:
        correcto = False
        print("La edad no puede ser mayor que 120 ni menor que 1")
    return correcto

#Metodo que pide el nombre del alumno, si es correcto, lo añade a la lista de nombres
def introducirNombre():
    nombre = input("Introduce un nombre: ")
    while comprobarNombre(nombre) == False:
        nombre = input("Introduce un nombre: ")
    nombres.append(nombre)
    return nombre

#Metodo que pida la edad del alumno, si es correcta, la añade a la lista de edades
#Se envuelve en un try/except por si el usuario no introduce un int
def introducirEdad():
    try:
        edad = int(input("Introduce una edad: "))
        while comprobarEdad(edad) == False:
            edad = int(input("Introduce una edad: "))
        edades.append(edad)
    except ValueError:
        print("Solo se permiten datos numericos")
        introducirEdad()
        
#Metodo que imprime los alumnos mayor de edad y los alumnos mas mayores
def imprimirDatos():
    edadMasAlta = 0
    print("Alumno/s mayor/es de edad:")
    for i in range (len(nombres)):
        if edadMasAlta < edades[i]:
            edadMasAlta = edades[i]
        if (edades[i] >= 18):
            print(nombres[i])

    print("Alumno/s mas mayor/es: ")
    for i in range (len(nombres)):
        if edadMasAlta == edades[i]:
            print(nombres[i])

#Se pide el nombre y la edad de los alumnos. Si se introduce un * se finaliza el programa
while introducirNombre() != '*':
    introducirEdad()
nombres.pop() #para eliminar el último elemento (*)
imprimirDatos()


