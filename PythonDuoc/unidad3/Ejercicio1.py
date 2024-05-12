import os
import time
os.system("cls")

nombres = []
nombre = ""

for i in range(3):
    nombre = input("Ingrese un nombre >> ") 
    nombres.append(nombre)
    print(f"Nombres en el listado: {nombres}")

#ordena de menor a mayor alfabeticamente o numericamente
nombres.sort()

#ordena de mayor a menor
nombres.sort(reverse=True)


#test
nombres.sort(key=len)

print(f"El nombre más largo es: {nombres[-1]} con cantidad de caracteres {len(nombres[-1])}")
