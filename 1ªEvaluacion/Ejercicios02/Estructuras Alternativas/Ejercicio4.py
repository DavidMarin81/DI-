#Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta. 
dia = int(input("Introduce el día: "))
mes = int(input("Introduce el mes: "))
anho = int(input("Introduce el año: "))
correcto = True

if  dia < 1 or dia > 31:
    correcto = False
if correcto:
    if mes < 1 or mes > 12:
        correcto = False
if correcto:
    if anho == 0:
        correcto = False

if correcto:
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia > 30:
            correcto = False
    elif mes == 2:
        if anho % 4 == 0 and (anho % 100 != 0 or anho % 400 == 0):
            if dia > 29:
                correcto = False
        else:
            if dia > 28:
                correcto = False

if correcto:
    print("La fecha es correcta")
else:
    print("La fecha es incorrecta")

