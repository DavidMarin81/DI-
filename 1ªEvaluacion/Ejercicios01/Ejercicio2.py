'''Un alumno desea saber cual será su calificación final en la materia de
Matemáticas. Dicha calificación se compone de los siguientes porcentajes:
    55% del promedio de sus tres calificaciones parciales
    30% de la calificación del examen final
    15% de la calificación de un trabajo final'''

parcial1 = float(input("Introduce la nota del primer parcial:"))
while parcial1 < 1 or parcial1 > 10:
    print("Nota incorrecta. Los valores tienen que estar entre el 1 y el 10")
    parcial1 = float(input("Introduce la nota del primer parcial:"))

parcial2 = float(input("Introduce la nota del segundo parcial:"))
while parcial2 < 1 or parcial2 > 10:
    print("Nota incorrecta. Los valores tienen que estar entre el 1 y el 10")
    parcial2 = float(input("Introduce la nota del segundo parcial:"))

parcial3 = float(input("Introduce la nota del tercer parcial:"))
while parcial3 < 1 or parcial3 > 10:
    print("Nota incorrecta. Los valores tienen que estar entre el 1 y el 10")
    parcial3 = float(input("Introduce la nota del tercer parcial:"))

examenFinal = float(input("Introduce la nota del examen final:"))
while examenFinal < 1 or examenFinal > 10:
    print("Nota incorrecta. Los valores tienen que estar entre el 1 y el 10")
    examenFinal = float(input("Introduce la nota del examen final:"))

trabajoFinal = float(input("Introduce la nota del trabajo final:"))
while trabajoFinal < 1 or trabajoFinal > 10:
    print("Nota incorrecta. Los valores tienen que estar entre el 1 y el 10")
    trabajoFinal = float(input("Introduce la nota del trabajo final:"))

print("La nota final es", str(round((((parcial1 + parcial2 + parcial3) / 3) * 0.55) +
         (examenFinal * 0.3) + (trabajoFinal * 0.15))))