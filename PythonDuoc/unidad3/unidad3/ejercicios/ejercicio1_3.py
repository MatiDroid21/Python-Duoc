import os
import time

nombres = []
confirmacion = ""
os.system("cls")
registro = True
while registro:
    nombre = input("Ingrese un nombre ")
    nombres.append(nombre)
    
    confirmacion = input("¿Desea agregar otro nombre? si/no ").lower()
    if confirmacion == "no":
        registro = False
    else:
        os.system("cls")

print(nombres)