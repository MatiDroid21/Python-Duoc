import os
os.system("cls")

nombres = []
apellidos = []

for nom in range(3):
    nombre = input("Ingrese nombre >> ")
    nombres.append(nombre)

for ape in range(3):
    apellido = input("Ingrese apellido >> ")
    apellidos.append(apellido)

os.system("cls")
print("Nombres:",nombres)
print("Apellidos:",apellidos)

