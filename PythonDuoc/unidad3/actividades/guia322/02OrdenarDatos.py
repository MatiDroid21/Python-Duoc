import os

os.system("cls")

nombres = []
apellidos = []

for i in range(3):
    nombre = input("Ingrese un nombre >> ")
    apellido = input("Ingrese un apellido >> ")
    nombres.append(nombre)
    apellidos.append(apellido)

nombres.sort()
apellidos.sort()

print("Nombres ordenados: ",nombres)

print("Apellidos ordenados: ",apellidos)

