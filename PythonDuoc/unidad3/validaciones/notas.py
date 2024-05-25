import os
import time #libreria para esperar x tiempo
os.system("cls")

try:
    cantidad_notas = int(input("Ingrese la cantidad de notas > "))
except:
    print("Debe ser numero")

suma_notas = 0

for i in range(cantidad_notas):
    notas = int(input(f"Ingrese la nota numero {i+1} > "))
    suma_notas = suma_notas + 1

print(f"El promedio es {suma_notas/cantidad_notas}")