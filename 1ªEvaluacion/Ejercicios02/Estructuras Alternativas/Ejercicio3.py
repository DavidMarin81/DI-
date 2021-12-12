#Algoritmo que pida tres números y los muestre ordenados (de mayor a menor)
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
numero3 = int(input("Introduce el tercer número: "))

numeros = [numero1, numero2, numero3]
numeros.sort()
for i in range (len(numeros)):
    print(numeros[len(numeros) - i - 1])