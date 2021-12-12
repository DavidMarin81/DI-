'''El día juliano correspondiente a una fecha es un número entero que indica los días que han
transcurrido desde el 1 de enero del año indicado. Queremos crear un programa principal que
al introducir una fecha nos diga el día juliano que corresponde. Para ello podemos hacer las
siguientes subrutinas:
- LeerFecha: Nos permite leer por teclado una fecha (día, mes y año).
- DiasDelMes: Recibe un mes y un año y nos dice los días de ese mes en ese año.
- EsBisiesto: Recibe un año y nos dice si es bisiesto.
- Calcular_Dia_Juliano: recibe una fecha y nos devuelve el día juliano.'''

#Método que comprueba que los datos introducidos sean númericos
#En caso de no ser, se volverá a pedir que se introduzcan los datos
def comprobarDato(numero):
    correcto = False
    while correcto == False:
        if numero.isdigit():
            correcto = True
        else:
            print("ERROR -> Solo se permiten números enteros")
            numero = input("Introduce un dato correcto: ")
    return numero

#Método que comprueba si el año es bisiesto
def esBisiesto(year):
    if ((year % 4 == 0 and not (year % 100 == 0)) or year % 400 == 0) == 0:
        return False
    else:
        return True

#Método que comprueba los días del mes
def diasDelMes(mes, year):
    if mes == 1:
        return 0
    elif mes == 2:
        return 31
    elif mes == 3:
        if esBisiesto(year):
            return 60
        else:
            return 59
    elif mes == 4:
        if esBisiesto(year):
            return 91
        else:
            return 90
    elif mes == 5:
        if esBisiesto(year):
            return 121
        else:
            return 120
    elif mes == 6:
        if esBisiesto(year):
            return 152
        else:
            return 151
    elif mes == 7:
        if esBisiesto(year):
            return 182
        else:
            return 181
    elif mes == 8:
        if esBisiesto(year):
            return 213
        else:
            return 212
    elif mes == 9:
        if esBisiesto(year):
            return 244
        else:
            return 243
    elif mes == 10:
        if esBisiesto(year):
            return 274
        else:
            return 273
    elif mes == 11:
        if esBisiesto(year):
            return 305
        else:
            return 304
    elif mes == 12:
        if esBisiesto(year):
            return 335
        else:
            return 334
    
#Método que muestra el día Juliano
def Calcular_Dia_Juliano(dia, mes, year):
        print("Para la fecha", str(dia), "/", str(mes), "/", str(year), ", el día juliano es", diasTotales + diaIntroducido)

#Se piden los datos al usuario
diaIntroducido = int(comprobarDato(input("Introduce un día: ")))
mesIntroducido = int(comprobarDato(input("Introduce un mes (en dígito): ")))
yearIntroducido = int(comprobarDato(input("Introduce un año: ")))
if yearIntroducido == 0:
    yearIntroducido = 1
#Se guardan los días que se llevan del año
diasTotales = int(diasDelMes(mesIntroducido, yearIntroducido))
#Se calcula el día Juliano
Calcular_Dia_Juliano(diaIntroducido, mesIntroducido, yearIntroducido)


