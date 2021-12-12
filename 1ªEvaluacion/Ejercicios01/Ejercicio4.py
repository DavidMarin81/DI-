'''Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS
segundos. El tiempo de viaje hasta llegar a otra ciudad B es de T segundos.
Escribir un algoritmo que determine la hora de llegada a la ciudad B'''

horaSalida = int(input("Introduce la hora de la salida:"))
while horaSalida < 0 or horaSalida > 23:
    print("\tHora incorrecta.")
    print("\tValores entre 0 y 23")
    horaSalida = int(input("Introduce la hora de la salida:"))

minutosSalida = int(input("Introduce los minutos de la salida:"))
while minutosSalida < 0 or minutosSalida > 59:
    print("\tMinutos incorrectos.")
    print("\tValores entre 0 y 59")
    minutosSalida = int(input("Introduce los minutos de la salida:"))

segundosSalida = int(input("Introduce los segundos de la salida:"))
while segundosSalida < 0 or segundosSalida > 59:
    print("\tSegundos incorrectos.")
    print("\tValores entre 0 y 59")
    segundosSalida = int(input("Introduce los segundos de la salida:"))

print("==========================================")
segundosTrayecto = int(input("Introduce los segundos que tarda:"))
while segundosTrayecto < 1:
    print("\tDatos negativos o valor 0 no permitidos.")
    segundosTrayecto = int(input("Introduce los segundos que tarda:"))
print("==========================================")
totalSegundos = horaSalida * 3600 + minutosSalida * 60 + segundosSalida + segundosTrayecto
horasLlegada = (totalSegundos // 3600) % 24
minutosLlegada = int((totalSegundos / 60) % 60)
segundosLlegada = (totalSegundos % 3600) % 60
print("El ciclista llegará a las", "{:0>2d}:".format(horasLlegada) + "{:0>2d}:".format(minutosLlegada) 
        + "{:0>2d}".format(segundosLlegada))
