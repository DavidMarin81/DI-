'''Escribe un programa que pida un nombre de usuario y una contraseña
y si se ha introducido "pepe" y "asdasd" se indica 
"Has entrado al sistema", sino se da un error'''

nombre = input("Introduce el nombre de usuario: ")
contraseña = input("Introduce la contraseña: ")
while nombre != "pepe" or contraseña != "asdasd":
    print("Usuario o contraseña incorrectos.")
    nombre = input("Introduce el nombre de usuario: ")
    contraseña = input("Introduce la contraseña: ")

print("Has entrado al sistema")