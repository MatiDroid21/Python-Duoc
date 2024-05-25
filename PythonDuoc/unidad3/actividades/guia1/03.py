import os
import time

nombres = []
confirmacion = ""
indice = 1
os.system("cls")
registro = True
while registro:
    print(f"Ingresando a la persona {indice}")
    nombre = input("Ingrese un nombre ")
    nombres.append(nombre)
    indice +=1
    confirmacion = input("¿Desea agregar otro nombre? si/no ").lower()
    if confirmacion == "no":
        registro = False
    else:
        os.system("cls")

print(nombres)