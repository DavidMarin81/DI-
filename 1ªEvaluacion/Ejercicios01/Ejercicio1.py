#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa

import math

cateto1 = float(input("Introduce el cateto 1: "))
cateto2 = float(input("Introduce el cateto 2: "))
print("La hipotenusa es", str(math.hypot(cateto1, cateto2)))