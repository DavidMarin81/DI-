#Algoritmo que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.

def tablaMultiplicar(numero):
    for i in range(1, 11):
        print(numero, "x", i, "=", numero*i)

for i in range(5):
    tablaMultiplicar(i+1)
    print("=================")
