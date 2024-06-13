## registro de personas
import os
import time

os.system("cls")
listado_personas = []

cant_personas = 0

try:
    cant_personas = int(input("Ingrese la cantidad de personas: "))
except:
    print("Debe ser numero")
    time.sleep(1)
    os.system("cls")

for i in range(cant_personas):
    print(f"Se registra a la persona N° {i+1}")
    nombre = input("Ingrese el nombre de la persona >>> ")
    apellido = input("Ingrese el apellido de la persona >>> ")
    edad = int(input("Ingrese la edad de la persona >>> "))
    peso = float(input("Ingrese el peso de la persona >>> "))
    estatura = float(input("Ingrese la estatura de la persona >>> "))
    os.system("cls")
    personas = [nombre,apellido,edad,peso,estatura]
    listado_personas.append(personas)

print(listado_personas)

