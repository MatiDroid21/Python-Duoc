import os
import time

os.system("cls")

nombres = []  # array vacio que luego llenaremos con nombres
nombre = ""

for i in range(3):
    while True:
        nombre = input("Ingrese un nombre >> ")
        if nombre == "":
            print("No se ingreso un nombre o ingresaste algo nada que ver")
        else:
            nombres.append(nombre)
            print(f"Nombres en el listado: {nombres}")
            break

os.system("cls")

print("validando...")

os.system("cls")
print("Espere un momento...")
time.sleep(1)

if nombres:  # Verificar si el array no está vacío
    print(f"El nombre más largo es: {max(nombres, key=len)} con cantidad de caracteres {len(max(nombres, key=len))}")
else:
    print("No se ingresaron nombres")